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

We implemented [SurroundDepth](https://proceedings.mlr.press/v205/wei23a.html) as the baseline model for Track `4`. The baseline model was trained on the official `train` split of the nuScenes dataset and evaluated on our robustness probing sets under different corruptions.

This codebase provides basic instructions for the reproduction of the baseline model in the RoboDrive Challenge.


## :gear: Installation

Kindly refer to [README.md](SurroundDepth/README.md) to set up environments and download necessary checkpoints.

## :hotsprings: Datasets

We use data under the nuScenes `train` split as the training set and the RoboDrive robustness probing data as the evaluation set. For training data preparation, kindly refer to [README.md](SurroundDepth/README.md). 

For evaluation data preparation, kindly download the dataset from [this](https://drive.google.com/file/d/1FEiBlX9SV69DEaHVfpKcWjkTZQAVSfvw/view?usp=drive_link) Google Drive link and organize the folder structure as follows:

```bash
.
├── data
│   ├── nuscenes
│   │   ├── depth
│   │   └── raw_data
│   └── robodrive
├── datasets
│   ├── __init__.py
│   ├── corruption_dataset.py
│   ├── ddad_dataset.py
│   ├── mono_dataset.py
│   ├── nusc_dataset.py
│   ├── nusc
│   ├── ddad
│   └── robodrive
│
...
```

Then copy the `./robodrive/robodrive-v1.0-test` to the nuscenes folder by running:
```bash
cp -r ./data/robodrive/robodrive-v1.0-test ./data/nuscenes/raw_data
```


# Getting Started

The training and evaluation instructions are summarized as follows.

## :rocket: Training

Kindly refer to [README.md](SurroundDepth/README.md) for the details regarding model training.


## :bar_chart: Evaluation

Simply run the following command to evaluate the trained baseline model on the RoboDrive robustness probing sets:

```bash
cd SurroundDepth
bash eval.sh
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

Next, kindly merge all the `.pkl` files into a **single** `pred.npz` file.

You can merge the results using the following command:
```bash
python ./convert_submit.py
```
> **:warning: Note:** The prediction file **MUST** be named as `pred.npz`.

Finally, upload the compressed file to Track `4`'s [evaluation server](https://codalab.lisn.upsaclay.fr/competitions/17226) for model evaluation.

> **:blue_car: Hint:** We provided the baseline submission file at [this](https://drive.google.com/drive/folders/1oEDgaBdmkXN3dv45fbvnzdo9Gw20PXk-?usp=sharing) Google Drive link. Feel free to download and check it for reference and learn how to correctly submit the prediction files to the server.


# Customized Dataset

To customize your own dataset, simply build your dataset based on `CorruptionDataset` from [this](SurroundDepth/datasets/corruption_dataset.py) link.

We mainly modified the data loading part. We only consider the subset of scenes for each corruption type, below is an example showing how to load a subset of scenes under each corruption type.


```python
cam_sample = self.nusc.get(
    'sample_data', rec['data'][self.camera_names[index_spatial]])
inputs['id'].append(self.camera_ids[index_spatial])
# modify the data path to corruption data path here
color = self.loader(os.path.join(self.corruption_root, self.corruption, cam_sample['filename']))
```


# Baseline Results

| Metric            | Results   |
| :---------------: | :----:    |
| Abs Rel           | 0.348     |
| Sq Rel            | 4.336     |
| RMSE              | 7.102     |
| RMSE Log          | 0.396     |
| a1                | 0.623     |
| a2                | 0.819     |
| a3                | 0.899     |


# References

Kindly cite the corresponding paper(s) once you use the baseline model in this track.
```bibtex
@inproceedings{wei2023surrounddepth,
  title={SurroundDepth: Entangling Surrounding Views for Self-Supervised Multi-Camera Depth Estimation},
  author={Wei, Yi and Zhao, Linqing and Zheng, Wenzhao and Zhu, Zheng and Rao, Yongming and Huang, Guan and Lu, Jiwen and Zhou, Jie},
  booktitle={Conference on Robot Learning},
  pages={539-549},
  year={2023},
  organization={PMLR}
}
```
