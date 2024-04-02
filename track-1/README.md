# Track 1 - Robust BEV Detection

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

We implemented [BEVFormer](https://arxiv.org/abs/2203.17270) as the baseline model for Track `1`. The baseline model was trained on the official `train` split of the nuScenes dataset and evaluated on our robustness probing sets under different corruptions.

This codebase provides basic instructions for the reproduction of the baseline model in the RoboDrive Challenge.


## :gear: Installation

Kindly refer to [GET_STARTED.md](./BEVFormer/docs/getting_started.md) to set up environments and download necessary checkpoints. 

## :hotsprings: Datasets

We use data under the nuScenes `train` split as the training set and the RoboDrive robustness probing data as the evaluation sets. For training data preparation, kindly refer to [PREPARE_DATASET.md](./BEVFormer/docs/prepare_dataset.md). 

For evaluation data preparation, kindly download the dataset from the following resources:

| Type | Phase 1 | Phase 2 |
| :-: | :-: | :-: |
| Google Drive | [`link1`](https://drive.google.com/file/d/1FEiBlX9SV69DEaHVfpKcWjkTZQAVSfvw/view?usp=drive_link) or [`link2`](https://drive.google.com/file/d/1V2YTaBgqEEKKFiD7uQ2z3cf7GMHuUYk1/view?usp=sharing) | [`link1`](https://drive.google.com/file/d/1wBg0RhjboUmBs6Ibyq-d8qNzZTgtalwV/view?usp=sharing) or `link2` |

Uncompress the downloaded dataset and organize the folder structure as follows:

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

Next, run the following command to generate the `.pkl` file for the evaluation sets:

```bash
bash tools/create_data.sh
```

> **:blue_car: Hint:** You can download our generated `robodrive_infos_temporal_test.pkl` file from [this](https://drive.google.com/drive/folders/1rbpRKTsFhQc-Una53hixKgZjo0PM0bSL?usp=drive_link) Google Drive link.


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
├── robodrive_infos_temporal_test.pkl
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

Kindly refer to [GET_STARTED.md](./BEVFormer/docs/getting_started.md) for the details regarding model training.

## :bar_chart: Evaluation

Simply run the following command to evaluate the trained baseline model on the RoboDrive robustness probing sets:

```bash
cd BEVFormer
bash tools/dist_test_corruption.sh ./projects/configs/robodrive/bevformer_base.py ./ckpt/bevformer_r101_dcn_24ep.pth 1
```

The generated results will be saved in the folder like this:

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

Next, kindly merge all the `.json` files into a **single** `pred.json` file and zip compress it.

You can merge the results using the following command:

```bash
python ./tools/convert_submit.py
```
> **:warning: Note:** The prediction file **MUST** be named as `pred.json`. The `.zip` file can be named as you like.

Finally, upload the compressed file to Track `1`'s [evaluation server](https://codalab.lisn.upsaclay.fr/competitions/17135) for model evaluation.

> **:blue_car: Hint:** We provided the baseline submission file at [this](https://drive.google.com/drive/folders/1rbpRKTsFhQc-Una53hixKgZjo0PM0bSL?usp=drive_link) Google Drive link. Feel free to download and check it for reference and learn how to correctly submit the prediction files to the server.



# Customized Dataset

To customize your own dataset, simply build your dataset based on `NuScenesCorruptionDataset`.

We mainly modified the data loading part. We only consider the subset of scenes for each corruption type, below is an example.

For more information, kindly refer to [corruption_dataset.py](BEVFormer/projects/mmdet3d_plugin/datasets/corruption_dataset.py).

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


## Baseline Results

### Phase 1

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


### Phase 2

To be updated.



# References

Kindly cite the corresponding paper(s) once you use the baseline model in this track.
```bibtex
@inproceedings{li2022bevformer,
    title = {BEVFormer: Learning Bird’s Eye View Representation from Multi-Camera Images via Spatiotemporal Transformers},
    author = {Li, Zhiqi and Wang, Wenhai and Li, Hongyang and Xie, Enze and Sima, Chonghao and Lu, Tong and Qiao, Yu and Dai, Jifeng},
    booktitle = {European Conference on Computer Vision},
    pages = {1-18},
    year = {2022},
}
```
