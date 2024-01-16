# Track 5 - Robust Multi-Modal BEV Detection

## About

We implement [BEVFusion](https://ieeexplore.ieee.org/abstract/document/10160968) as the baseline model for Track 5. The baseline model is trained on the nuScenes dataset using both camera and LiDAR input and evaluated on the RoboDrive dataset with sensor failures. This codebase provide instructions to evaluate the baseline model.

## Preparation

### Installation

Kindly refer to the [README.md](BEVFusion/README.md) to set up environments and download the checkpoints. 

### Dataset

We use nuScenes train split as the training data and use robodrive dataset as the evaluation data. For training data preparation, please refer to [nuscenes_det.md](https://github.com/open-mmlab/mmdetection3d/blob/master/docs/en/datasets/nuscenes_det.md). 

For evaluation data preparetion, please first download the dataset from [RoboDrive](https://drive.google.com/file/d/1Hw59VToELsB_bJ9qTGuyn9zdDzaZSnT4/view?usp=sharing) and organize folder structure like this:

```bash
.
├── data
│   ├── nuscenes
│   └── robodrive-sensor
├── configs
├── mmdet3d
└── tools
```

Then run the following command to generate the evaluation dataset. You can also download the generated `.pkl` file from [Google Drive](https://drive.google.com/drive/folders/1IAGH-io2wR3YjhNTMPc5Vp7kIRwa5Vdw?usp=sharing).

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
├── v1.0-trainval
```

## Getting Started

### Train

Please refer to [README.md](BEVFusion/README.md).

### Eval

Simply run the following command to evaluate the baseline model on the corruption dataset.

```bash
cd BEVFusion
bash tools/test_corruption.sh
```

Please rename the generated `results_nusc.json` to `pred.json` file and compress it into `.zip` file. Then upload to the [server](https://codalab.lisn.upsaclay.fr/competitions/17137) for evaluation.

> Note: the result file should be named as `pred.json` and the `.zip` file can be named as you like.

We also provide the baseline submission file demo [here](https://drive.google.com/drive/folders/1IAGH-io2wR3YjhNTMPc5Vp7kIRwa5Vdw?usp=drive_link). Feel free to download for reference and learn how to submit the results.

## Customized Dataset

To customize your own dataset, just simply build your dataset based on [`RoboDriveDataset`](BEVFusion/mmdet3d/datasets/robodrive_dataset.py#L19). We simply modify the data path to load image and lidar data.


## Baseline Model

| Model             | NDS    | mAP    | mATE   | mASE   | mAOE   | mAVE   | mAAE   |
| ----------------- | ------ | ------ | ------ | ------ | ------ | ------ | ------ |
| BEVFusion         | 0.4285 | 0.2448 | 0.4012 | 0.2910 | 0.4928 | 0.5289 | 0.2251 |


## References

Please note that you should cite the corresponding papers once you use the baseline model.
```bibtex
@inproceedings{liu2023bevfusion,
  title={Bevfusion: Multi-task multi-sensor fusion with unified bird's-eye view representation},
  author={Liu, Zhijian and Tang, Haotian and Amini, Alexander and Yang, Xinyu and Mao, Huizi and Rus, Daniela L and Han, Song},
  booktitle={2023 IEEE international conference on robotics and automation (ICRA)},
  pages={2774--2781},
  year={2023},
  organization={IEEE}
}
```
