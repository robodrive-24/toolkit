# Track 1 - Robust BEV Detection

## About

We implement [BEVFormer](https://arxiv.org/abs/2203.17270) as the baseline model for Track 1. The baseline model is trained on the nuScenes dataset and evaluated on the nuScenes dataset with different corruptions. This codebase provides instructions to test the baseline model on the RoboDrive Challenge.

## Preparation

### Installation

Kindly refer to the [GET_STARTED.md](./BEVFormer/docs/getting_started.md) to set up environments and download the checkpoints. 

### Dataset

We use nuScenes train split as the training data and use robodrive dataset as the evaluation data. For training data preparation, please refer to [prepare_dataset.md](./BEVFormer/docs/prepare_dataset.md). 

For evaluation data preparation, please first download the dataset from [robodrive-release]() and organize the folder structure like this:

```bash
.
├── ckpts
│   ├── bevformer_r101_dcn_24ep.pth
│   └── bevformer_small_epoch_24.pth
├── data
│   ├── nuscenes
│   └── robodrive-release
├── projects
└── tools
```

Then run the following command to generate the evaluation dataset. You can also download the `robodrive_infos_temporal_test.pkl` file from [Google Drive]().

```bash
bash tools/create_data.sh
```

The nuscenes folder should be like this:

```bash
.
├── basemap
├── can_bus
├── can_bus.zip
├── expansion
├── lidarseg
├── maps
├── nuscenes_infos_temporal_train.pkl
├── nuscenes_infos_temporal_val.pkl
├── nuScenes-panoptic-v1.0-all
├── prediction
├── robodrive_infos_temporal_test.pkl
├── robodrive-v1.0-test
├── samples
├── sweeps
├── v1.0-mini
├── v1.0-test
├── v1.0-trainval
```

## Getting Started

### Train

Please refer to [getting_started.md](./BEVFormer/docs/getting_started.md).

### Eval

Simply run the following command to evaluate the baseline model on the corruption dataset.

```bash
cd BEVFormer
bash tools/dist_test_corruption.sh ./projects/configs/robodrive/bevformer_base.py ./ckpt/bevformer_r101_dcn_24ep.pth 1
```

## Customized Dataset

To customize your own dataset, just simply build your dataset based on `NuScenesCorruptionDataset`. We mainly modify the data loading part: we only consider the subset of scenes for each corruption type, below is an example. For more information, please refer to [corruption_dataset.py](BEVFormer/projects/mmdet3d_plugin/datasets/corruption_dataset.py).

```python
data = mmcv.load(ann_file)
        
# filter scenes
data_infos = data['infos']
sample_data_infos = []
for data_info in data_infos:
    if self.corruption is not None:
        # only consider the subset of scenes for each corruption type
        if data_info['scene_token'] in self.sample_scenes_dict[self.corruption]:
            sample_data_infos.append(data_info)
        else:
            sample_data_infos.append(data_info)
```

## Evaluation

Please upload the generated `results_nusc.json` to the [server]() for evaluation. The upload folder structure should be like this:

```bash
.
├── brightness
│   └── results_nusc.json
├── color_quant
│   └── results_nusc.json
├── contrast
│   └── results_nusc.json
...
├── snow
└── zoom_blur
```

## Baseline Model

| Corruption        | NDS    | mAP    | mATE   | mASE   | mAOE   | mAVE   | mAAE   |
| ----------------- | ------ | ------ | ------ | ------ | ------ | ------ | ------ |
| Bright            | 0.4132 | 0.3157 | 0.8234 | 0.3738 | 0.5239 | 0.4568 | 0.2691 |
| Dark              | 0.3712 | 0.2285 | 0.7797 | 0.3030 | 0.5334 | 0.4555 | 0.3586 |
| Fog               | 0.5534 | 0.4519 | 0.6770 | 0.2665 | 0.3386 | 0.3069 | 0.1369 |
| Frost             | 0.1718 | 0.0649 | 1.0171 | 0.4675 | 0.6829 | 1.0579 | 0.4562 |
| Snow              | 0.2549 | 0.1402 | 0.8814 | 0.3362 | 0.7076 | 1.0516 | 0.2264 |
| Contrast          | 0.2196 | 0.1216 | 0.9530 | 0.4754 | 1.0561 | 0.7240 | 0.2599 |
| Defocus Blur      | 0.2762 | 0.1608 | 0.7869 | 0.4371 | 0.8307 | 0.6749 | 0.3125 |
| Glass Blur        | 0.3327 | 0.1820 | 0.8334 | 0.3711 | 0.6560 | 0.4098 | 0.3124 |
| Motion Blur       | 0.2760 | 0.1885 | 0.8369 | 0.3567 | 0.8282 | 0.7810 | 0.3798 |
| Zoom Blur         | 0.1193 | 0.0082 | 1.1021 | 0.5698 | 0.8678 | 2.4270 | 0.4104 |
| Elastic Transform | 0.4997 | 0.3694 | 0.6417 | 0.2887 | 0.3154 | 0.4376 | 0.1664 |
| Color Quant       | 0.3088 | 0.1878 | 0.8062 | 0.4045 | 0.9392 | 0.4420 | 0.2589 |
| Gaussian Noise    | 0.2104 | 0.0833 | 0.8578 | 0.4349 | 0.6174 | 0.8689 | 0.5338 |
| Impluse Noise     | 0.2411 | 0.1011 | 0.8660 | 0.4649 | 0.7304 | 0.6126 | 0.4205 |
| Shot Noise        | 0.3441 | 0.1545 | 0.8484 | 0.2969 | 0.4450 | 0.5413 | 0.1995 |
| ISO Noise         | 0.2505 | 0.1076 | 0.9036 | 0.3045 | 0.5644 | 1.5776 | 0.2607 |
| Pixelate          | 0.3499 | 0.2668 | 0.8558 | 0.3047 | 0.4907 | 1.1205 | 0.1831 |
| JPEG              | 0.4304 | 0.2552 | 0.7405 | 0.2798 | 0.2946 | 0.3910 | 0.2666 |


## References

Please note that you should cite the corresponding papers once you use the baseline model.
```bibtex
@inproceedings{li2022bevformer,
  title={Bevformer: Learning bird’s-eye-view representation from multi-camera images via spatiotemporal transformers},
  author={Li, Zhiqi and Wang, Wenhai and Li, Hongyang and Xie, Enze and Sima, Chonghao and Lu, Tong and Qiao, Yu and Dai, Jifeng},
  booktitle={European conference on computer vision},
  pages={1--18},
  year={2022},
  organization={Springer}
}
```