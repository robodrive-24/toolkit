# Copyright Niantic 2019. Patent Pending. All rights reserved.
#
# This software is licensed under the terms of the Monodepth2 licence
# which allows for non-commercial use only, the full terms of which are made
# available in the LICENSE file.

from __future__ import absolute_import, division, print_function

import os
import skimage.transform
import numpy as np
import PIL.Image as pil
import sys
import pickle
import pdb
import cv2

from .mono_dataset import MonoDataset

from nuscenes.nuscenes import NuScenes
from pyquaternion import Quaternion

class CorruptionDataset(MonoDataset):
    """Superclass for different types of KITTI dataset loaders
    """
    
    CORRUPTIONS = [
        'brightness', 'dark', 'fog', 'frost', 'snow', 'contrast',
        'defocus_blur', 'glass_blur', 'motion_blur', 'zoom_blur', 'elastic_transform', 'color_quant',
        'gaussian_noise', 'impulse_noise', 'shot_noise', 'iso_noise', 'pixelate', 'jpeg_compression'
    ]
    
    def __init__(self, 
                 *args, 
                 **kwargs):
        super(CorruptionDataset, self).__init__(*args, **kwargs)

        self.corruption_root = self.opt.corruption_root
        self.corruption = self.opt.corruption
        
        assert self.corruption in self.CORRUPTIONS, 'Corruption {} not supported'.format(self.corruption)
        
        self.data_path = 'data/nuscenes/raw_data'
        version = 'robodrive-v1.0-test'
        self.nusc = NuScenes(version=version,
                            dataroot=self.data_path, verbose=False)

        self.depth_path = 'data/nuscenes/depth'
        self.match_path = 'data/nuscenes/match'


        if not self.opt.phase2:
            with open('datasets/robodrive/{}.txt'.format(self.corruption), 'r') as f:
            # for debug usage
            # with open('datasets/robodrive/test.txt', 'r') as f:
                self.filenames = f.readlines()
        else:
            with open('datasets/robodrive-phase2/{}.txt'.format(self.corruption), 'r') as f:
                self.filenames = f.readlines()

        self.camera_ids = ['front', 'front_left', 'back_left', 'back', 'back_right', 'front_right']
        self.camera_names = ['CAM_FRONT', 'CAM_FRONT_LEFT', 'CAM_BACK_LEFT', 'CAM_BACK', 'CAM_BACK_RIGHT', 'CAM_FRONT_RIGHT']

    
    def get_info(self, inputs, index_temporal, do_flip):
        inputs[("color", 0, -1)] = []
        inputs[('K_ori', 0)] = [] 


        inputs['width_ori'], inputs['height_ori'], inputs['id'] = [], [], []

        rec = self.nusc.get('sample', index_temporal)
        inputs['sample_token'] = rec['token']

        for index_spatial in range(6):
            cam_sample = self.nusc.get(
                'sample_data', rec['data'][self.camera_names[index_spatial]])
            inputs['id'].append(self.camera_ids[index_spatial])
            color = self.loader(os.path.join(self.corruption_root, self.corruption, cam_sample['filename']))
            inputs['width_ori'].append(color.size[0])
            inputs['height_ori'].append(color.size[1])
            
            if do_flip:
                color = color.transpose(pil.FLIP_LEFT_RIGHT)
            inputs[("color", 0, -1)].append(color)

            ego_spatial = self.nusc.get(
                    'calibrated_sensor', cam_sample['calibrated_sensor_token'])
    
            K = np.eye(4).astype(np.float32)
            K[:3, :3] = ego_spatial['camera_intrinsic']
            inputs[('K_ori', 0)].append(K)


        inputs[('K_ori', 0)] = np.stack(inputs[('K_ori', 0)], axis=0) 

        for key in ['width_ori', 'height_ori']:
            inputs[key] = np.stack(inputs[key], axis=0)   








