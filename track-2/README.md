# Track 2 - Robust Map Segmentation

## About

We implement [BEVerse](https://arxiv.org/abs/2205.09743) as the baseline model for Track 2. The baseline model is trained on the nuScenes dataset and evaluated on the nuScenes dataset with different corruptions. This codebase provides instructions to test the baseline model on the RoboDrive Challenge.

## Preparation

### Installation

Kindly refer to the [installation.md](BEVerse/docs/installation.md) to set up environments and download the checkpoints.

### Dataset

We use nuScenes train split as the training data and use RoboDrive dataset as the evaluation data. For training data preparation, please refer to [prepare_dataset.md](BEVerse/docs/data_preparation.md). 

For evaluation data preparation, please first download the dataset from [robodrive-release](https://drive.google.com/file/d/1FEiBlX9SV69DEaHVfpKcWjkTZQAVSfvw/view?usp=drive_link), then run the following command to generate the evaluation `.pkl` file. You can also download the generated `robodrive_infos_test.pkl` file in [Google Drive](https://drive.google.com/drive/folders/1fd1SCkS2uB1l4PS8S5Le1i4q32X2u8PQ?usp=drive_link). The final folder structure like this:

```bash
bash tools/create_data.sh
```

Finally, please organize the folder structure like this:

```bash
.
├── ckpt
│   └── beverse_small.pth
├── data
│   ├── nuscenes
│   ├── robodrive-release
│   └── nuscenes_infos
│       ├── nuscenes_infos_train_mono3d.coco.json
│       ├── nuscenes_infos_train.pkl
│       ├── nuscenes_infos_trainval.pkl
│       ├── nuscenes_infos_val.pkl
│       └── robodrive_infos_test.pkl
...
```

## Getting Started

### Train

We use nuScenes train split as the training dataset. Please refer to [getting_started.md](BEVerse/docs/getting_started.md) for more details on the usage of the baseline model.

### Eval

Simply run the following command to evaluate the baseline model on the corruption dataset.

```bash
cd BEVerse
bash tools/dist_test_corruption.sh
```

The generated results are in the following folder, Each `results.pkl` is a dictionary, the key is `sample_idx` and the value is `np.ndarray`.

```bash
.
├── brightness
│   └── results.pkl
├── color_quant
│   └── results.pkl
├── contrast
│   └── results.pkl
...
├── snow
└── zoom_blur
```

Finally, convert all the results into one `pred.pkl` file by runing the following script. Compress the file into a `.zip` file and upload to the [server](https://codalab.lisn.upsaclay.fr/competitions/17062) for evaluation. 
> Note: the result file should be named as `pred.pkl` and the `.zip` file can be named as you like.
```bash
python ./tools/convert_submit.py
``` 

We also provide the baseline submission file demo [here](https://drive.google.com/drive/folders/1fd1SCkS2uB1l4PS8S5Le1i4q32X2u8PQ?usp=drive_link). Feel free to download for reference and learn how to submit the results.

### Customized Dataset

To customize your own dataset, just simply build your dataset based on [`NuScenesCorruptionDataset`](./BEVerse/projects/mmdet3d_plugin/datasets/corruption_dataset.py#18). We mainly modify the data loading part: we only consider the subset of scenes for each corruption type, below is an example. For more information, please refer to [robodrive_dataset.py](BEVerse/projects/mmdet3d_plugin/datasets/robodrive_dataset.py). Below is an example showing loading the subset of scenes for each corruption type:

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

and change the data path [here](BEVerse/projects/mmdet3d_plugin/datasets/robodrive_dataset.py#L405):

```python
if self.corruption is not None:
    for img_info in img_infos:
        for cam_name, cam_info in img_info.items():
            cur_path = cam_info['data_path']
            img_info[cam_name]['data_path'] = cur_path.replace('./data/nuscenes', osp.join(self.corruption_root, self.corruption))
```


## Baseline Model

| Corruption        | mIoU  |
| ----------------- | ----- |
| Bright            | 0.234 |
| Dark              | 0.135 |
| Fog               | 0.398 |
| Frost             | 0.037 |
| Snow              | 0.072 |
| Contrast          | 0.057 |
| Defocus Blur      | 0.194 |
| Glass Blur        | 0.296 |
| Motion Blur       | 0.212 |
| Zoom Blur         | 0.105 |
| Elastic Transform | 0.406 |
| Color Quant       | 0.140 |
| Gaussian Noise    | 0.033 |
| Impluse Noise     | 0.018 |
| Shot Noise        | 0.028 |
| ISO Noise         | 0.032 |
| Pixelate          | 0.403 |
| JPEG              | 0.319 |

## References

Please note that you should cite the corresponding papers once you use the baseline model.
```bibtex
@article{zhang2022beverse,
  title={Beverse: Unified perception and prediction in birds-eye-view for vision-centric autonomous driving},
  author={Zhang, Yunpeng and Zhu, Zheng and Zheng, Wenzhao and Huang, Junjie and Huang, Guan and Zhou, Jie and Lu, Jiwen},
  journal={arXiv preprint arXiv:2205.09743},
  year={2022}
}
```
