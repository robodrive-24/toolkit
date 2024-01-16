# Track 2 - Robust Map Segmentation

- [Preparation](#preparation)
  - [Installation](#gear-installation)
  - [Datasets](#hotsprings-datasets)
- [Getting Started](#getting-started)
  - [Training](#rocket-training)
  - [Evaluation](#bar_chart-evaluation)
- [Customized Dataset](#customized-dataset)
- [Baseline Results](#baseline-results)
- [References](#references)


# Preparation

We implemented [BEVerse](https://arxiv.org/abs/2205.09743) as the baseline model for Track `2`. The baseline model was trained on the official `train` split of the nuScenes dataset and evaluated on our robustness probing sets under different corruptions.

This codebase provides basic instructions for the reproduction of the baseline model in the RoboDrive Challenge.


## :gear: Installation

Kindly refer to [INSTALL.md](BEVerse/docs/installation.md) to set up environments and download necessary checkpoints.

## :hotsprings: Datasets

We use data under the nuScenes `train` split as the training set and the RoboDrive robustness probing data as the evaluation set. For training data preparation, kindly refer to [PREPARE_DATASET.md](BEVerse/docs/data_preparation.md). 

For evaluation data preparation, kindly download the dataset from [this](https://drive.google.com/file/d/1FEiBlX9SV69DEaHVfpKcWjkTZQAVSfvw/view?usp=drive_link) Google Drive link and organize the folder structure as follows:

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
├── projects
└── tools
```

Next, run the following command to generate the `.pkl` file for the evaluation sets:

```bash
bash tools/create_data.sh
```

> **:blue_car: Hint:** You can download our generated `rrobodrive_infos_test.pkl` file from [this](https://drive.google.com/drive/u/4/folders/1fd1SCkS2uB1l4PS8S5Le1i4q32X2u8PQ) Google Drive link.


The `nuscenes` folder should end up looking like this:

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
├── robodrive_infos_test.pkl
├── robodrive-v1.0-test
├── samples
├── sweeps
├── v1.0-mini
├── v1.0-test
└── v1.0-trainval
```



# Getting Started

The training and evaluation instructions are summarized as follows.

## :rocket: Training

Kindly refer to [GET_STARTED.md](BEVerse/docs/getting_started.md) for the details regarding model training.


## :bar_chart: Evaluation

Simply run the following command to evaluate the trained baseline model on the RoboDrive robustness probing sets:

```bash
cd BEVerse
bash tools/dist_test_corruption.sh
```

The generated results will be saved in the folder structure as follows. Each `results.pkl` is a dictionary, its key is `sample_idx` and its value is `np.ndarray`.

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

Next, kindly merge all the `.pkl` files into a **single** `pred.pkl` file and zip compress it.

You can merge the results using the following command:
```bash
python ./tools/convert_submit.py
```
> **:warning: Note:** The prediction file **MUST** be named as `pred.pkl`. The `.zip` file can be named as you like.

Finally, upload the compressed file to Track `2`'s [evaluation server](https://codalab.lisn.upsaclay.fr/competitions/17062) for model evaluation.

> **:blue_car: Hint:** We provided the baseline submission file at [this](https://drive.google.com/drive/folders/1fd1SCkS2uB1l4PS8S5Le1i4q32X2u8PQ?usp=drive_link) Google Drive link. Feel free to download and check it for reference and learn how to correctly submit the prediction files to the server.


# Customized Dataset

To customize your own dataset, simply build your dataset based on `NuScenesCorruptionDataset` from [this](./BEVerse/projects/mmdet3d_plugin/datasets/corruption_dataset.py#18) link.

We mainly modified the data loading part. We only consider the subset of scenes for each corruption type, below is an example showing how to load a subset of scenes under each corruption type.

For more information, kindly refer to [corruption_dataset.py](BEVerse/projects/mmdet3d_plugin/datasets/robodrive_dataset.py).


```python
data = mmcv.load(ann_file)
        
data_infos = data['infos']
sample_data_infos = []

for data_info in data_infos:
    if self.corruption is not None:
        if data_info['scene_token'] in self.sample_scenes_dict[self.corruption]:
            sample_data_infos.append(data_info)
        else:
            sample_data_infos.append(data_info)
```

You can modify the data path as follows from [here](BEVerse/projects/mmdet3d_plugin/datasets/robodrive_dataset.py#L405):

```python
if self.corruption is not None:
    for img_info in img_infos:
        for cam_name, cam_info in img_info.items():
            cur_path = cam_info['data_path']
            img_info[cam_name]['data_path'] = cur_path.replace('./data/nuscenes', osp.join(self.corruption_root, self.corruption))
```


# Baseline Results

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


# References

Kindly cite the corresponding paper(s) once you use the baseline model in this track.
```bibtex
@article{zhang2022beverse,
    title = {BEVerse: Unified Perception and Prediction in Bird's Eye View for Vision-Centric Autonomous Driving},
    author = {Zhang, Yunpeng and Zhu, Zheng and Zheng, Wenzhao and Huang, Junjie and Huang, Guan and Zhou, Jie and Lu, Jiwen},
    journal = {arXiv preprint arXiv:2205.09743},
    year = {2022}
}
```
