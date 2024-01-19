# Data Preparation

- [Overall Structure](#overall-structure)
- [Training Data](#red_car-training-data)
    - [Download](#download)
    - [Prepare for Training](#prepare-for-training)
- [Evaluation Data](#blue_car-evaluation-data)
    - [Download](#download)
        - [Tracks 1 to 3](#hotsprings-tracks-1-to-3)
        - [Track 4](#hotsprings-track-4)
        - [Track 5](#hotsprings-track-5)
    - [Prepare for Evaluation](#prepare-for-evaluation)
- [References](#references)


## Overall Structure
```shell
└── data 
    └── sets
        │
        ├── nuscenes
        │   ├── maps
        │   ├── samples
        │   ├── sweeps
        │   ├── lidarseg
        │   ├── v1.0-{mini, test, trainval}
        │   ├── ...
        │   ├── nuscenes_infos_train.pkl
        │   └── nuscenes_infos_val.pkl
        │
        │── robodrive-release
        │   ├── brightness
        │   ├── color_quant
        │   ├── contrast
        │   ├── ...
        │   ├── zoom_blur
        │   ├── ...
        │   ├── robodrive-v1.0-test
        │   └── sample_scenes.pkl
        │
        │── robodrive-depth
        │   ├── brightness
        │   ├── color_quant
        │   ├── contrast
        │   ├── ...
        │   ├── zoom_blur
        │   ├── ...
        │   ├── robodrive-v1.0-test
        │   └── sample_scenes.pkl
        │
        └── robodrive-sensor
            ├── samples
            ├── robodrive-v1.0-test
            └── sweeps
```



# :red_car: Training Data
In this competition, all participants are expected to adopt the **official** [nuScenes](https://www.nuscenes.org/nuscenes) dataset from [Motional](https://motional.com/) for model training.

:warning: **Note:** Additional data sources are NOT allowed in this competition.

## Download

To install the [nuScenes](https://www.nuscenes.org/nuscenes) dataset, download the data, annotations, and other files from https://www.nuscenes.org/download. 

Alternatively, you can download the [nuScenes](https://www.nuscenes.org/nuscenes) dataset from [OpenDataLab](https://opendatalab.com/) using MIM. The downloading and unzipping command scripts are the following scripts:

```shell
# install OpenDataLab CLI tools
pip install -U opendatalab
```
```shell
# log in OpenDataLab
# note that you should register an account on [OpenDataLab](https://opendatalab.com).
pip install odl
odl login
```
```shell
# download and preprocess by MIM
mim download mmdet3d --dataset nuscenes
```

Unpack the compressed file(s) into `/data/sets/nuscenes` and your folder structure should end up looking like this:

```shell
└── nuscenes
    │ 
    ├── maps
    │ 
    ├── samples  <- contains the image, point cloud, and other data.
    │   ├── CAM_BACK
    │   ├── CAM_BACK_LEFT
    │   ├── CAM_BACK_RIGHT
    │   ├── CAM_FRONT
    │   ├── CAM_FRONT_LEFT
    │   ├── CAM_FRONT_RIGHT
    │   ├── ...
    │   ├── LIDAR_TOP
    │   └── ...
    │
    ├── sweeps
    │
    ├── lidarseg
    │   └── v1.0-{mini, test, trainval}  <- contains the .bin files; a .bin file 
    │                                       contains the labels of the points in a 
    │                                       point cloud (note that v1.0-test does not 
    │                                       have any .bin files associated with it)
    │
    │── v1.0-{mini, test, trainval}
    │   ├── Usual files (e.g. attribute.json, calibrated_sensor.json etc.)
    │   ├── lidarseg.json  <- contains the mapping of each .bin file to the token   
    │   └── category.json  <- contains the categories of the labels (note that the 
    │                         category.json from nuScenes v1.0 is overwritten)
    │
    ├── nuscenes_infos_train.pkl
    └── nuscenes_infos_val.pkl
```

## Prepare for Training

Prepare the `.pkl` files for [nuScenes](https://www.nuscenes.org/nuscenes) training by running the following script:

```shell
python tools/create_data.py nuscenes --root-path ./data/sets/nuscenes --out-dir ./data/sets/nuscenes --extra-tag nuscenes
```

:warning: **Note:** It is recommended to use the **absolute dataset path** when generating these `.pkl` files.

Alternatively, we have provided offline generated `.pkl` files at [this](https://mmdetection3d.readthedocs.io/en/latest/user_guides/dataset_prepare.html#summary-of-annotation-files) link. You can download these files and place them under `data/sets/nuscenes/`. 


# :blue_car: Evaluation Data

In this competition, all participants are expected to adopt our **robustness probing sets** for model evaluation.

## Download

### :hotsprings: Tracks `1` to `3`:

For participants in Track `1` (Robust BEV Detection), Track `2` (Robust Map Segmentation), or Track `3` (Robust Occupancy Prediction), kindly download the RoboDrive **camera-corruption sets** from either one of the following sources:

| Type | Phase 1 | Phase 2 |
| :-: | :-: | :-: |
| Google Drive | [`link1`](https://drive.google.com/file/d/1FEiBlX9SV69DEaHVfpKcWjkTZQAVSfvw/view?usp=drive_link) or [`link2`](https://drive.google.com/file/d/1V2YTaBgqEEKKFiD7uQ2z3cf7GMHuUYk1/view?usp=sharing) | `link1` or `link2` |
| OpenDataLab | `link1` or `link2` | `link1` or `link2` |
| Baidu Disk | `link1` or `link2` | `link1` or `link2` |

Unpack the compressed file(s) into `/data/sets/robodrive-release` and your folder structure should end up looking like this:

```shell
└── robodrive-release
    │
    ├── brightness
    │   └── samples  <- contains the .jpg files from surrounding cameras 
    │       ├── CAM_BACK
    │       ├── CAM_BACK_LEFT
    │       ├── CAM_BACK_RIGHT
    │       ├── CAM_FRONT
    │       ├── CAM_FRONT_LEFT
    │       └── CAM_FRONT_RIGHT
    │
    ├── color_quant
    ├── contrast
    ├── dark
    ├── defocus_blur
    ├── elastic_transform
    ├── fog
    ├── frost
    ├── gaussian_noise
    ├── glass_blur
    ├── impulse_noise
    ├── iso_noise
    ├── jpeg_compression
    ├── motion_blur
    ├── pixelate
    ├── shot_noise
    ├── snow
    ├── zoom_blur
    │
    ├── robodrive-v1.0-test
    │   ├── Usual files (e.g. attribute.json, calibrated_sensor.json etc.)
    │   ├── lidarseg.json  <- contains the mapping of each .bin file to the token   
    │   └── category.json  <- contains the categories of the labels (note that the 
    │                         category.json from nuScenes v1.0 is overwritten)
    │
    └── sample_scenes.pkl
```

> **Hints:** There are **18 corruption types** in total, therefore, you should find the same number of folders that contain the camera-corruption data.



### :hotsprings: Track `4`

For participants in Track `4` (Robust Depth Estimation), kindly download the RoboDrive **depth-corruption sets** from either one of the following sources:

| Type | Phase 1 | Phase 2 |
| :-: | :-: | :-: |
| Google Drive | `link1` or `link2` | `link1` or `link2` |
| OpenDataLab | `link1` or `link2` | `link1` or `link2` |
| Baidu Disk | `link1` or `link2` | `link1` or `link2` |

Unpack the compressed file(s) into `/data/sets/robodrive-depth` and your folder structure should end up looking like this:

```shell
└── robodrive-depth
    │
    ├── brightness
    │   └── samples  <- contains the .jpg files from surrounding cameras 
    │       ├── CAM_BACK
    │       ├── CAM_BACK_LEFT
    │       ├── CAM_BACK_RIGHT
    │       ├── CAM_FRONT
    │       ├── CAM_FRONT_LEFT
    │       └── CAM_FRONT_RIGHT
    │
    ├── color_quant
    ├── contrast
    ├── dark
    ├── defocus_blur
    ├── elastic_transform
    ├── fog
    ├── frost
    ├── gaussian_noise
    ├── glass_blur
    ├── impulse_noise
    ├── iso_noise
    ├── jpeg_compression
    ├── motion_blur
    ├── pixelate
    ├── shot_noise
    ├── snow
    ├── zoom_blur
    │
    ├── robodrive-v1.0-test
    │   ├── Usual files (e.g. attribute.json, calibrated_sensor.json etc.)
    │   ├── lidarseg.json  <- contains the mapping of each .bin file to the token   
    │   └── category.json  <- contains the categories of the labels (note that the 
    │                         category.json from nuScenes v1.0 is overwritten)
    │
    └── sample_scenes.pkl
```

> **Hints:** There are **18 corruption types** in total, therefore, you should find the same number of folders that contain the camera-corruption data.




### :hotsprings: Track `5`

For participants in Track `5` (Robust Multi-Modal BEV Detection), kindly download the RoboDrive **sensor-corruption sets** from either one of the following sources:

| Type | Phase 1 | Phase 2 |
| :-: | :-: | :-: |
| Google Drive | [`link1`](https://drive.google.com/file/d/1Hw59VToELsB_bJ9qTGuyn9zdDzaZSnT4/view?usp=sharing) or [`link2`](https://drive.google.com/file/d/1wksmgzokYB-c9xGw8Ex6qN8R5mld-C_Q/view?usp=sharing) | `link1` or `link2`
| OpenDataLab | `link1` or `link2` | `link1` or `link2` |
| Baidu Disk | `link1` or `link2` | `link1` or `link2` |

Unpack the compressed file(s) into `/data/sets/robodrive-sensor` and your folder structure should end up looking like this:

```shell
└── robodrive-sensor
    │
    ├── samples  <- contains the .jpg files from surrounding cameras 
    │   ├── CAM_BACK
    │   ├── CAM_BACK_LEFT
    │   ├── CAM_BACK_RIGHT
    │   ├── CAM_FRONT
    │   ├── CAM_FRONT_LEFT
    │   ├── CAM_FRONT_RIGHT
    │   └── LIDAR_TOP
    │
    ├── robodrive-v1.0-test
    │   ├── Usual files (e.g. attribute.json, calibrated_sensor.json etc.)
    │   ├── lidarseg.json  <- contains the mapping of each .bin file to the token   
    │   └── category.json  <- contains the categories of the labels (note that the 
    │                         category.json from nuScenes v1.0 is overwritten)
    └── sweeps
```



## Prepare for Evaluation

We have prepared the `sample_scenes.pkl` file for model evaluation. Kindly refer to your `/data/sets/robodrive-release` folder.


# References
Kindly cite the corresponding papers once you use these datasets.

```bibtex
@inproceedings{caesar2020nuscenes,
    title={nuScenes: A Multimodal Dataset for Autonomous Driving},
    author={Holger Caesar and Varun Bankiti and Alex H. Lang and Sourabh Vora and Venice Erin Liong and Qiang Xu and Anush Krishnan and Yu Pan and Giancarlo Baldan and Oscar Beijbom},
    booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
    pages = {11621--11631},
    year={2020}
}
```

```bibtex
@article{fong2021panoptic,
    title={Panoptic nuScenes: A Large-Scale Benchmark for LiDAR Panoptic Segmentation and Tracking},
    author={Whye Kit Fong and Rohit Mohan and Juana Valeria Hurtado and Lubing Zhou and Holger Caesar and Oscar Beijbom and Abhinav Valada},
    journal = {IEEE Robotics and Automation Letters},
    volume = {7},
    number = {2},
    pages = {3795--3802},
    year={2021}
}
```

```bibtex
@article{xie2023robobev,
    title = {RoboBEV: Towards Robust Bird's Eye View Perception under Corruptions},
    author = {Shaoyuan Xie and Lingdong Kong and Wenwei Zhang and Jiawei Ren and Liang Pan and Kai Chen and Ziwei Liu},
    journal = {arXiv preprint arXiv:2304.06719}, 
    year = {2023}
}
```

```bibtex
@inproceedings{kong2023robodepth,
    title = {RoboDepth: Robust Out-of-Distribution Depth Estimation under Corruptions},
    author = {Lingdong Kong and Shaoyuan Xie and Hanjiang Hu and Lai Xing Ng and Benoit R. Cottereau and Wei Tsang Ooi},
    booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
    year = {2023},
}
```


