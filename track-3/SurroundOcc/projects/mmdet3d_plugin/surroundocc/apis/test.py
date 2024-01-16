# ---------------------------------------------
# Copyright (c) OpenMMLab. All rights reserved.
# ---------------------------------------------
#  Modified by Zhiqi Li
# ---------------------------------------------
import os.path as osp
import os
import pickle
import shutil
import tempfile
import time

import mmcv
import torch
import torch.distributed as dist
from mmcv.image import tensor2imgs
from mmcv.runner import get_dist_info

from mmdet.core import encode_mask_results


import mmcv
import numpy as np
import pycocotools.mask as mask_util
#import open3d as o3d
import pdb

def custom_encode_mask_results(mask_results):
    """Encode bitmap mask to RLE code. Semantic Masks only
    Args:
        mask_results (list | tuple[list]): bitmap mask results.
            In mask scoring rcnn, mask_results is a tuple of (segm_results,
            segm_cls_score).
    Returns:
        list | tuple: RLE encoded mask.
    """
    cls_segms = mask_results
    num_classes = len(cls_segms)
    encoded_mask_results = []
    for i in range(len(cls_segms)):
        encoded_mask_results.append(
            mask_util.encode(
                np.array(
                    cls_segms[i][:, :, np.newaxis], order='F',
                        dtype='uint8'))[0])  # encoded with RLE
    return [encoded_mask_results]

def custom_multi_gpu_test(model, data_loader, tmpdir=None, gpu_collect=False, is_vis=False):
    """Test model with multiple gpus.
    This method tests model with multiple gpus and collects the results
    under two different modes: gpu and cpu modes. By setting 'gpu_collect=True'
    it encodes results to gpu tensors and use gpu communication for results
    collection. On cpu mode it saves the results on different gpus to 'tmpdir'
    and collects them by the rank 0 worker.
    Args:
        model (nn.Module): Model to be tested.
        data_loader (nn.Dataloader): Pytorch data loader.
        tmpdir (str): Path of directory to save the temporary results from
            different gpus under cpu mode.
        gpu_collect (bool): Option to use either gpu or cpu to collect results.
    Returns:
        list: The prediction results.
    """

    model.eval()
    occ_results = []
    occ_preds = []

    dataset = data_loader.dataset
    rank, world_size = get_dist_info()
    if rank == 0:
        prog_bar = mmcv.ProgressBar(len(dataset))
    time.sleep(2)  # This line can prevent deadlock problem in some cases.

    for i, data in enumerate(data_loader):
        with torch.no_grad():

            result = model(return_loss=False, rescale=True, **data)
            # encode mask results
            if isinstance(result, dict):
                if 'evaluation' in result.keys():
                    occ_results.extend(result['evaluation'])
                    occ_preds.extend(result['prediction'])
                    batch_size = len(result['evaluation'])
            
            if is_vis:
                batch_size = result

        if rank == 0:
            
            for _ in range(batch_size * world_size):
                prog_bar.update()
    
    if is_vis:
        return 
    
    # collect results from all ranks
    if gpu_collect:
        occ_results = collect_results_gpu(occ_results, len(dataset))
        occ_preds = collect_results_gpu(occ_preds, len(dataset))
    else:
        tmpdir = tmpdir+'_mask' if tmpdir is not None else None
        occ_results = collect_results_cpu(occ_results, len(dataset), tmpdir)
        occ_preds = collect_results_cpu(occ_preds, len(dataset), tmpdir)
    
    if rank == 0:
        return {'occ_pred': [occ_pred.cpu().numpy() for occ_pred in occ_preds], 'occ_results': occ_results}


def robodrive_multi_gpu_test(model, data_loader, corruption, tmpdir=None, gpu_collect=False, is_vis=False):
    """Test model with multiple gpus.
    This method tests model with multiple gpus and collects the results
    under two different modes: gpu and cpu modes. By setting 'gpu_collect=True'
    it encodes results to gpu tensors and use gpu communication for results
    collection. On cpu mode it saves the results on different gpus to 'tmpdir'
    and collects them by the rank 0 worker.
    Args:
        model (nn.Module): Model to be tested.
        data_loader (nn.Dataloader): Pytorch data loader.
        tmpdir (str): Path of directory to save the temporary results from
            different gpus under cpu mode.
        gpu_collect (bool): Option to use either gpu or cpu to collect results.
    Returns:
        list: The prediction results.
    """

    model.eval()
    occ_preds = {}

    dataset = data_loader.dataset
    rank, world_size = get_dist_info()
    if rank == 0:
        prog_bar = mmcv.ProgressBar(len(dataset))
    time.sleep(2)  # This line can prevent deadlock problem in some cases.

    for i, data in enumerate(data_loader):
        with torch.no_grad():

            result = model(return_loss=False, rescale=True, **data)
            # encode mask results
            assert isinstance(result, dict), f'{result} is not a dict'
            assert 'prediction' in result.keys(), f'{result} does not have prediction key'
            
            sample_token = data['img_metas'].data[0][0]['sample_idx']
            assert sample_token not in occ_preds.keys(), f'{sample_token} already exists'
            occ_preds[sample_token] = result['prediction']
            batch_size = len(result['prediction'])
            
            if is_vis:
                batch_size = result

        if rank == 0:
            
            for _ in range(batch_size * world_size):
                prog_bar.update()
    
    # collect results from all ranks
    if gpu_collect:
        occ_preds_list = list(occ_preds.items())
        occ_preds_list = collect_results_gpu(occ_preds_list, len(dataset))
        
    else:
        tmpdir = tmpdir+'_mask' if tmpdir is not None else None
        occ_preds_list = list(occ_preds.items())
        occ_preds_list = collect_results_cpu(occ_preds_list, len(dataset), tmpdir)
    
    if rank == 0:
        
        occ_preds_collect = dict()
        
        for sublist in occ_preds_list:
            occ_preds_collect[sublist[0]] = sublist[1].cpu().numpy().astype(np.uint8)
        
        assert len(dataset) == len(occ_preds_collect), f'{len(dataset)} != {len(occ_preds_collect)}'
        
        print(f'\n===\nNot support evaluate locally, please upload all the results files to the server, saving {corruption}/results.pkl')
        if not osp.exists(osp.join('./test', corruption)):
            os.makedirs(osp.join('./test', corruption))
        with open(osp.join('./test', corruption, f'results.pkl'), 'wb') as f:
            pickle.dump(occ_preds_collect, f)

        return None


def collect_results_cpu(result_part, size, tmpdir=None):
    rank, world_size = get_dist_info()
    # create a tmp dir if it is not specified
    if tmpdir is None:
        MAX_LEN = 512
        # 32 is whitespace
        dir_tensor = torch.full((MAX_LEN, ),
                                32,
                                dtype=torch.uint8,
                                device='cuda')
        if rank == 0:
            mmcv.mkdir_or_exist('.dist_test')
            tmpdir = tempfile.mkdtemp(dir='.dist_test')
            tmpdir = torch.tensor(
                bytearray(tmpdir.encode()), dtype=torch.uint8, device='cuda')
            dir_tensor[:len(tmpdir)] = tmpdir
        dist.broadcast(dir_tensor, 0)
        tmpdir = dir_tensor.cpu().numpy().tobytes().decode().rstrip()
    else:
        mmcv.mkdir_or_exist(tmpdir)
    # dump the part result to the dir
    mmcv.dump(result_part, osp.join(tmpdir, f'part_{rank}.pkl'))
    dist.barrier()
    # collect all parts
    if rank != 0:
        return None
    else:
        # load results of all parts from tmp dir
        part_list = []
        for i in range(world_size):
            part_file = osp.join(tmpdir, f'part_{i}.pkl')
            part_list.append(mmcv.load(part_file))
        # sort the results
        ordered_results = []
        '''
        bacause we change the sample of the evaluation stage to make sure that each gpu will handle continuous sample,
        '''
        #for res in zip(*part_list):
        for res in part_list:  
            ordered_results.extend(list(res))
        # the dataloader may pad some samples
        ordered_results = ordered_results[:size]
        # remove tmp dir
        shutil.rmtree(tmpdir)
        return ordered_results


def collect_results_gpu(result_part, size):
    collect_results_cpu(result_part, size)

