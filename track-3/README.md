# Track 3 - Robust Occupancy Prediction

## About

We implement [SurroundOcc](https://arxiv.org/abs/2303.09551) as the baseline model for Track 3. The baseline model is trained on the nuScenes dataset and evaluated on the nuScenes dataset with different corruptions. This codebase provides instructions to test the baseline model on the RoboDrive Challenge.

## Preparation

### Installation

Kindly refer to the [install.md](./SurroundOcc/docs/install.md) to set up environments and download the checkpoints. 

### Dataset

We use nuScenes train split as the training data and use robodrive dataset as the evaluation data. For training data preparation, please refer to [data.md](./SurroundOcc/docs/data.md). 

For evaluation data preparetion, please first download the dataset from [robodrive-release]() and then run the following command to generate the evaluation dataset:

```bash
bash tools/create_data.sh
```

You can also download the generated `robodrive_infos_temporal_test.pkl` file in [Google Drive](). The final folder structure like this:

```bash
.
├── ckpts
│   └── surroundocc.pth
├── data
│   ├── nuscenes
│   ├── nuscenes_infos_val.pkl
│   ├── nuscenes_occ
│   ├── robodrive_infos_temporal_test.pkl
│   └── robodrive-release
├── docs
├── extensions
├── projects
...
```

## Getting Started

### Train

We use nuScenes train split as training dataset. Please refer to [run.md](occupancy/SurroundOcc/docs/run.md) for more details on the usage of baseline model.

### Eval

Simply run the following command to evaluate the baseline model on the corruption dataset.

```bash
cd SurroundOcc
bash tools/dist_test_corruption.sh
```

Please upload the generated `results.pkl` to the [server]() for evaluation. Each `results.pkl` is a dictionary, the key is `sample_idx` and the value is `np.ndarray`. The upload folder struction should be like this:

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

 We provide the script to generated results file, please refer to [`robodrive_multi_gpu_test`](./SurroundOcc/projects/mmdet3d_plugin/surroundocc/apis/test.py#L110).


### Customized Dataset

To customize your own dataset, just simply build your dataset based on `NuScenesCorruptionDataset`. We mainly modify the data loading part: we only consider the subset of scenes for each corruption type, below is an example. For more information, please refer to [corruption_dataset.py](./SurroundOcc/projects/mmdet3d_plugin/datasets/corruption_dataset.py).

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


## Baseline Model

| Corruption        | SC IoU | SSC mIoU | barrier | bicycle | car    | const. veh | motorcycle | pedestrain | traffic cone | trailer | trunk | drive. suf | other flat | sidewalk | terrian | manmade | vegetation |
| ----------------- | ------ | -------- | ------- | ------- | ------ | ---------- | ---------- | ---------- | ------------ | ------- | ----- | ---------- | ---------- | -------- | ------- | ------- | ---------- |
| Bright | 0.2923 | 0.1613 | 0.2028 | 0.1209 | 0.2327 | 0.2937 | 0.0096 | 0.1923 | 0.1173 | 0.0766 | 0.0000 | 0.2356 | 0.3451 | 0.0438 | 0.1908 | 0.2145 | 0.1083 |
| Dark | 0.2404 | 0.1232 | 0.1030 | 0.0508 | 0.1821 | 0.2305 | 0.0591 | 0.0843 | 0.0294 | 0.0583 | 0.1201 | 0.1846 | 0.2859 | 0.1057 | 0.1503 | 0.1247 | 0.0802 |
| Fog | 0.2815 | 0.1815 | 0.2795 | 0.1067 | 0.1999 | 0.2944 | 0.0536 | 0.1204 | 0.1478 | 0.0803 | 0.1692 | 0.2228 | 0.3258 | 0.2652 | 0.1817 | 0.1876 | 0.1029 |
| Frost | 0.1417 | 0.0349 | 0.0062 | 0.0041 | 0.0241 | 0.1240 | 0.0002 | 0.0037 | 0.0111 | 0.0196 | 0.0052 | 0.0438 | 0.1365 | 0.0118 | 0.0241 | 0.0314 | 0.0373 |
| Snow | 0.2233 | 0.1085 | 0.1271 | 0.0298 | 0.1902 | 0.2272 | 0.0469 | 0.0149 | 0.0595 | 0.0913 | 0.0233 | 0.1110 | 0.2780 | 0.1520 | 0.1107 | 0.0935 | 0.0606 |
| Contrast | 0.2217 | 0.0768 | 0.0000 | 0.0060 | 0.1457 | 0.2217 | 0.0000 | 0.0237 | 0.0511 | 0.0020 | 0.0000 | 0.1725 | 0.2534 | 0.0174 | 0.1069 | 0.0518 | 0.0650 |
| Defocus Blur | 0.2484 | 0.1067 | 0.0635 | 0.0070 | 0.0871 | 0.2857 | 0.0660 | 0.0307 | 0.0494 | 0.0155 | 0.0279 | 0.1546 | 0.2901 | 0.1083 | 0.1811 | 0.0978 | 0.0994 |
| Glass Blur | 0.2397 | 0.0978 | 0.0685 | 0.0222 | 0.0726 | 0.2577 | 0.0018 | 0.0079 | 0.0477 | 0.0677 | 0.0394 | 0.1171 | 0.2793 | 0.1006 | 0.1704 | 0.1257 | 0.0820 |
| Motion Blur | 0.1675 | 0.1002 | 0.1448 | 0.0549 | 0.2610 | 0.2073 | 0.0092 | 0.0270 | 0.0685 | 0.0541 | 0.0000 | 0.1628 | 0.2161 | 0.1223 | 0.0791 | 0.0706 | 0.0528 |
| Zoom Blur | 0.1775 | 0.0566 | 0.0441 | 0.0000 | 0.1167 | 0.0855 | 0.0085 | 0.0008 | 0.0103 | 0.0043 | 0.0265 | 0.0616 | 0.2267 | 0.0400 | 0.0871 | 0.0702 | 0.0637 |
| Elastic Transform | 0.2890 | 0.1671 | 0.1173 | 0.0660 | 0.1935 | 0.2881 | 0.0601 | 0.0506 | 0.1180 | 0.0913 | 0.1838 | 0.2277 | 0.3395 | 0.2026 | 0.2208 | 0.1694 | 0.1239 |
| Color Quant | 0.2282 | 0.0974 | 0.0274 | 0.0160 | 0.1895 | 0.2417 | 0.0032 | 0.0195 | 0.0481 | 0.0238 | 0.0551 | 0.1456 | 0.2725 | 0.1350 | 0.1460 | 0.0428 | 0.0849 |
| Gaussian Noise | 0.2420 | 0.0875 | 0.0201 | 0.0098 | 0.0692 | 0.2420 | 0.0334 | 0.0448 | 0.0248 | 0.0218 | 0.0267 | 0.1075 | 0.2735 | 0.0344 | 0.1719 | 0.0904 | 0.0987 |
| Impluse Noise | 0.2256 | 0.1000 | 0.0338 | 0.0205 | 0.1510 | 0.2209 | 0.0166 | 0.0350 | 0.0399 | 0.0266 | 0.0838 | 0.1580 | 0.2376 | 0.1008 | 0.1621 | 0.0863 | 0.0897 |
| Shot Noise | 0.2604 | 0.1263 | 0.0746 | 0.0267 | 0.2982 | 0.2810 | 0.0694 | 0.0506 | 0.0400 | 0.0210 | 0.0973 | 0.1150 | 0.3019 | 0.1424 | 0.1828 | 0.0767 | 0.0988 |
| ISO Noise | 0.2334 | 0.1114 | 0.0786 | 0.0076 | 0.2046 | 0.2726 | 0.0891 | 0.0169 | 0.0294 | 0.0223 | 0.0271 | 0.1519 | 0.2580 | 0.1207 | 0.1684 | 0.0865 | 0.0855 |
| Pixelate | 0.3012 | 0.1677 | 0.0777 | 0.0415 | 0.3107 | 0.3057 | 0.0879 | 0.1745 | 0.0428 | 0.0518 | 0.0559 | 0.1871 | 0.3377 | 0.2475 | 0.2573 | 0.1448 | 0.1462 |
| JPEG | 0.2549 | 0.1287 | 0.0781 | 0.0189 | 0.1998 | 0.2455 | 0.0932 | 0.1151 | 0.0686 | 0.0530 | 0.1465 | 0.1369 | 0.2963 | 0.1495 | 0.1814 | 0.1052 | 0.0784 |

## References

Please note that you should cite the corresponding papers once you use the baseline model.
```bibtex
@inproceedings{wei2023surroundocc,
  title={Surroundocc: Multi-camera 3d occupancy prediction for autonomous driving},
  author={Wei, Yi and Zhao, Linqing and Zheng, Wenzhao and Zhu, Zheng and Zhou, Jie and Lu, Jiwen},
  booktitle={Proceedings of the IEEE/CVF International Conference on Computer Vision},
  pages={21729--21740},
  year={2023}
}
```