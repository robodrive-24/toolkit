# RoboDrive Toolkit
<a href="https://robodrive-24.github.io/" target='_blank'><img src="https://img.shields.io/badge/Website-%F0%9F%94%97-lightblue"></a>
<img src="https://visitor-badge.laobi.icu/badge?page_id=robodrive-24.toolkit&left_color=gray&right_color=blue">

<p align="center">
  <img src="docs/figs/cover.png" align="center" width="100%">
</p>

Welcome to [The RoboDrive Challenge](https://robodrive-24.github.io/)! :wave:


## About

- `RoboDrive` is one of the first competitions that targeted probing the Out-of-Distribution (OoD) robustness of state-of-the-art autonomous driving perception models, centered around two mainstream topics: **common corruptions** and **sensor failures**.
- This year's `RoboDrive` challenge is associated with the 41st IEEE Conference on Robotics and Automation ([ICRA 2024](https://2024.ieee-icra.org/)).
- There are eighteen real-world corruption types in total, ranging from three perspectives:
    - Weather and lighting conditions, such as bright, low-light, foggy, and snowy conditions.
    - Movement and acquisition failures, such as potential blurs caused by vehicle motions.
    - Data processing issues, such as noises and quantizations happen due to hardware malfunctions.
- Additionally, we aim to probe the 3D scene perception robustness under camera and LiDAR sensor failures:
    - Loss of certain camera frames during the driving system sensing process.
    - Loss of one or more camera views during the driving system sensing process.
    - Loss of the roof-top LiDAR view during the driving system sensing process.
- Kindly visit the `RoboDrive` [webpage](https://robodrive-24.github.io/) to explore more details and instructions of this challenge. :blue_car:


## Outline
- [Changelog](#changelog)
- [Useful Info](#useful-info)
- [Timeline](#clock1-timeline)
- [Challenge Tracks](#challenge-tracks)
- [Data Preparation](#data-preparation)
- [Getting Started](#getting-started)
- [Citation](#citation)
- [License](#license)
- [Sponsor](#sponsor)
- [Terms & Conditions](#balance_scale-terms--conditions)
- [Acknowledgements](#acknowledgements)


## Changelog
- `Jan 06 '24` - Instructions, baseline models, and results of Tracks `1` to `3` have been released.
- `Jan 05 '24` - Training and evaluation data of Tracks `1` to `4` have been released.
- `Dec 25 '23` - Register for your team by filling in [this](https://forms.gle/hnaezVhEycPAjUD78) Google Form.
- `Dec 01 '23` - Launch of [The RoboDrive Challenge](https://robodrive-24.github.io/) at [ICRA 2024](https://2024.ieee-icra.org/). More info coming soon!


## Useful Info
| \# | Item | Link |
|:-:|:-|:-|
| :globe_with_meridians: | Competition Webpage | https://robodrive-24.github.io |
| :wrench: | Competition Toolkit | https://github.com/robodrive-24/toolkit |
| :octocat: | Official GitHub Account | https://github.com/robodrive-24 |
| :mailbox: | Contact | robodrive.2024@gmail.com |


## :clock1: Timeline
> **Note:** All timestamps are in the `AoE` (Anywhere on Earth) format.
- `Dec 25 '23` - Team Up; Register for your team by filling in [this](https://forms.gle/hnaezVhEycPAjUD78) Google Form. 
- `Jan 05 '24` - Release of training and evaluation data.
- `Jan 10 '24` - Competition servers online @ [EvalAI](https://eval.ai/).
- `Mar 31 '24` - Phase `One` deadline.
- `Apr 30 '24` - Phase `Two` deadline.
- `May 17 '24` - Award decision announcement @ [ICRA 2024](https://2024.ieee-icra.org/).


## Challenge Tracks
There are **five** tracks in this `RoboDrive` challenge, with emphasis on the following 3D scene perception tasks:

| \# | Task | Description | Doc | Server |
|:-:|:-|:-|:-:|:-:|
| Track `1` | Robust BEV Detection | Evaluating the resilience of detection algorithms against diverse environmental and sensor-based corruptions | [`[Link]`](https://github.com/robodrive-24/toolkit/blob/main/track-1/README.md) | [Link] |
| Track `2` | Robust Map Segmentation | Focusing on the segmentation of complex driving scene elements in BEV maps under varied driving conditions | [`[Link]`](https://github.com/robodrive-24/toolkit/blob/main/track-2/README.md) | [Link] |
| Track `3` | Robust Occupancy Prediction | Testing the accuracy of occupancy grid predictions in dynamic and unpredictable real-world driving environments | [`[Link]`](https://github.com/robodrive-24/toolkit/blob/main/track-3/README.md) | [Link] |
| Track `4` | Robust Depth Estimation | Assessing the depth estimation robustness from multiple perspectives for comprehensive 3D scene perception | [`[Link]`](https://github.com/robodrive-24/toolkit/blob/main/track-4/README.md) | [Link] |
| Track `5` | Robust Multi-Modal BEV Detection | Tailored for evaluating the reliability of advanced driving perception systems equipped with multiple types of sensors | [`[Link]`](https://github.com/robodrive-24/toolkit/blob/main/track-5/README.md) | [Link] |


## Data Preparation
Kindly refer to [DATA_PREPARE.md](docs/DATA_PREPARE.md) for the details to prepare the training and evaluation data.


## Getting Started
Kindly refer to [GET_STARTED.md](docs/GET_STARTED.md) to learn more usage of this toolkit.


## Citation
If you find this competition helpful for your research, please kindly consider citing our papers:

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

```bibtex
@inproceedings{kong2023robo3d,
    title = {Robo3D: Towards Robust and Reliable 3D Perception against Corruptions},
    author = {Lingdong Kong and Youquan Liu and Xin Li and Runnan Chen and Wenwei Zhang and Jiawei Ren and Liang Pan and Kai Chen and Ziwei Liu},
    booktitle = {Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV)},
    pages = {19994--20006},
    year = {2023},
}
```


## License
<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/80x15.png" /></a>
<br />
This competition is under the <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.


## Sponsor
To be updated.


## :balance_scale: Terms & Conditions
This competition is made freely available to academic and non-academic entities for non-commercial purposes such as academic research, teaching, scientific publications, or personal experimentation. Permission is granted to use the data given that you agree:
1. That the data in this competition comes “AS IS”, without express or implied warranty. Although every effort has been made to ensure accuracy, we do not accept any responsibility for errors or omissions.
2. That you may not use the data in this competition or any derivative work for commercial purposes such as, for example, licensing or selling the data, or using the data with a purpose of procuring a commercial gain.
3. That you include a reference to RoboDrive (including the benchmark data and the specially generated data for academic challenges) in any work that makes use of the benchmark. For research papers, please cite our preferred publications as listed on our webpage.

To ensure a fair comparison among all participants, we require:
1. All participants must follow the exact same data configuration when training and evaluating their algorithms. Please do not use any public or private datasets other than those specified for model training.
2. The theme of this competition is to probe the out-of-distribution robustness of autonomous driving perception models. Therefore, any use of the corruption and sensor failure types designed in this benchmark is strictly prohibited, including any atomic operation that comprises any one of the mentioned corruptions.
3. To ensure the above two rules are followed, each participant is requested to submit the code with reproducible results before the final result is announced; the code is for examination purposes only and we will manually verify the training and evaluation of each participant's model.


## Acknowledgements
This competition is developed based on the [RoboBEV](https://github.com/Daniel-xsy/RoboBEV), [RoboDepth](https://github.com/ldkong1205/RoboDepth), and [Robo3D](https://github.com/ldkong1205/Robo3D) projects.

This competition toolkit is developed based on the [MMDetection3D](https://github.com/open-mmlab/mmdetection3d) codebase.

><img src="https://github.com/open-mmlab/mmdetection3d/blob/main/resources/mmdet3d-logo.png" width="30%"/><br>
> MMDetection3D is an open-source toolbox based on PyTorch, towards the next-generation platform for general 3D perception. It is a part of the OpenMMLab project developed by MMLab.

The evaluation sets of this competition are constructed based on the [nuScenes](https://www.nuscenes.org/nuscenes) dataset from [Motional AD LLC](https://motional.com/).

Part of the content of this toolkit is adopted from [The RoboDepth Challenge](https://robodepth.github.io/) @ [ICRA 2023](https://www.icra2023.org/).
