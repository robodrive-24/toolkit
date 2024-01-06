# Data Preparation

- [Overall Structure](#overall-structure)
- [Training Data](#training-data)
- [Evaluation Data](#evaluation-data)
- [References](#references)


## Overall Structure
```
└── data 
    └── sets
        │── nuscenes
        └── nuscenes-c        
```



## Training Data
In this competition, all participants are expected to adopt the [nuScenes](https://www.nuscenes.org/nuscenes) dataset for model training.

To install the [nuScenes](https://www.nuscenes.org/nuscenes) dataset, download the data, annotations, and other files from https://www.nuscenes.org/download. Unpack the compressed file(s) into `/data/sets/nuscenes` and your folder structure should end up looking like this:

```
└── nuscenes  
    ├── Usual nuscenes folders (i.e. samples, sweep)
    │
    ├── lidarseg
    │   └── v1.0-{mini, test, trainval} <- contains the .bin files; a .bin file 
    │                                      contains the labels of the points in a 
    │                                      point cloud (note that v1.0-test does not 
    │                                      have any .bin files associated with it)
    │
    └── v1.0-{mini, test, trainval}
        ├── Usual files (e.g. attribute.json, calibrated_sensor.json etc.)
        ├── lidarseg.json  <- contains the mapping of each .bin file to the token   
        └── category.json  <- contains the categories of the labels (note that the 
                              category.json from nuScenes v1.0 is overwritten)
```

It is recommended to use the **absolute dataset path** when generating the `.pkl` annotation files.


## Evaluation Data
To be updated.



## References
Please note that you should cite the corresponding papers once you use these datasets.

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


