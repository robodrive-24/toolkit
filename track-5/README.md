# Track 5 - Robust Multi-Modal BEV Detection

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

We implemented [BEVFusion](https://ieeexplore.ieee.org/abstract/document/10160968) as the baseline model for Track `5`. The baseline model was trained on the official `train` split of the nuScenes dataset and evaluated on our robustness probing sets under sensor failure scenarios.

This codebase provides basic instructions for the reproduction of the baseline model in the RoboDrive Challenge.


## :gear: Installation

Kindly refer to [GET_STARTED.md](BEVFusion/README.md) to set up environments and download necessary checkpoints. 

## :hotsprings: Datasets

We use data under the nuScenes `train` split as the training set and the RoboDrive robustness probing data as the evaluation sets. For training data preparation, kindly refer to [NUSCENES_DET.md](https://github.com/open-mmlab/mmdetection3d/blob/master/docs/en/datasets/nuscenes_det.md). 

For evaluation data preparation, kindly download the dataset from [this](https://drive.google.com/file/d/1Hw59VToELsB_bJ9qTGuyn9zdDzaZSnT4/view?usp=sharing) Google Drive link and organize the folder structure as follows:

```bash
.
├── data
│   ├── nuscenes
│   └── robodrive-sensor
├── configs
├── mmdet3d
└── tools
```

Next, run the following command to generate the `.pkl` file for the evaluation sets:

```bash
bash tools/create_data.sh
```

> **:blue_car: Hint:** You can download our generated `.pkl` file from [this](https://drive.google.com/drive/folders/1IAGH-io2wR3YjhNTMPc5Vp7kIRwa5Vdw?usp=sharing) Google Drive link.


The `nuscenes` folder should end up looking like this:nes folder should be like this:

```bash
.
├── basemap
├── can_bus
├── can_bus.zip
├── expansion
├── lidarseg
├── maps
├── nuscenes_infos_train.pkl
├── nuscenes_infos_val.pkl
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

Kindly refer to [GET_STARTED.md](BEVFusion/README.md) for the details regarding model training.

## :bar_chart: Evaluation

Simply run the following command to evaluate the trained baseline model on the RoboDrive robustness probing sets:

```bash
cd BEVFusion
bash tools/test_corruption.sh
```

Please rename the generated `results_nusc.json` file to `pred.json` and compress it into a `.zip` file.


Finally, upload the compressed file to Track `5`'s [evaluation server](https://codalab.lisn.upsaclay.fr/competitions/17137) for model evaluation.

> **:blue_car: Hint:** We provided the baseline submission file at [this](https://drive.google.com/drive/folders/1IAGH-io2wR3YjhNTMPc5Vp7kIRwa5Vdw?usp=drive_link) Google Drive link. Feel free to download and check it for reference and learn how to correctly submit the prediction files to the server.



# Customized Dataset

To customize your own dataset, simply build your dataset based on `RoboDriveDataset` from [this](BEVFusion/mmdet3d/datasets/robodrive_dataset.py#L19) line. We simply modified the data path to load image and LiDAR data.


## Baseline Results

| Model             | NDS    | mAP    | mATE   | mASE   | mAOE   | mAVE   | mAAE   |
| ----------------- | ------ | ------ | ------ | ------ | ------ | ------ | ------ |
| BEVFusion         | 0.4285 | 0.2448 | 0.4012 | 0.2910 | 0.4928 | 0.5289 | 0.2251 |


# References

Kindly cite the corresponding paper(s) once you use the baseline model in this track.
```bibtex
@inproceedings{liu2023bevfusion,
    title = {BEVFusion: Multi-Task Multi-Sensor Fusion with Unified Bird's Eye View Representation},
    author = {Liu, Zhijian and Tang, Haotian and Amini, Alexander and Yang, Xinyu and Mao, Huizi and Rus, Daniela L and Han, Song},
    booktitle = {IEEE International Conference on Robotics and Automation (ICRA)},
    pages = {2774-2781},
    year = {2023}
}
```
