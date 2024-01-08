# Getting Started

- [Challenge One: Corruptions]()
  - [Track 1: Robust BEV Detection](#red_car-track-1-robust-bev-detection)
  - [Track 2: Robust Map Segmentation](#blue_car-track-2-robust-map-segmentation)
  - [Track 3: Robust Occupancy Prediction](#taxi-track-3-robust-occupancy-prediction)
  - [Track 4: Robust Depth Estimation](#track-4-robust-depth-estimation)
- [Challenge Two: Sensor Failures]()
  - [Track 5: Robust Multi-Modal BEV Detection](#track-5-robust-multi-modal-bev-detection)
- [Rules & Conditions](#rules--conditions)
- [Frequently Asked Questions]()


# Challenge One: Corruptions

The first challenge topic contains **18 real-world corruption types**, ranging from the following **three** perspectives:
  - Weather and lighting conditions, such as bright, low-light, foggy, and snowy conditions.
  - Movement and acquisition failures, such as potential blurs caused by vehicle motions.
  - Data processing issues, such as noises and quantizations happen due to hardware malfunctions.


## :red_car: Track 1: Robust BEV Detection
| \# | Task | Robust BEV Detection |
|:-:|:-|:-|
| :red_car: | **Description** | Evaluating the resilience of detection algorithms against diverse environmental and sensor-based corruptions |
| :page_facing_up: | **Document** | [`track-1/README.md`](https://github.com/robodrive-24/toolkit/blob/main/track-1/README.md)
| :house: | **Server** | To be updated |
| :gear: | **Baseline Model** | [BEVFormer](https://arxiv.org/abs/2203.17270) |
| :octocat: | **Baseline Codebase** | https://github.com/fundamentalvision/BEVFormer |
| :bar_chart: | **Baseline Results** | To be updated |


## :blue_car: Track 2: Robust Map Segmentation

| \# | Task | Robust Map Segmentation |
|:-:|:-|:-|
| :blue_car: | **Description** | Focusing on the segmentation of complex driving scene elements in BEV maps under varied driving conditions |
| :page_facing_up: | **Document** | [`track-2/README.md`](https://github.com/robodrive-24/toolkit/blob/main/track-2/README.md)
| :house: | **Server** | To be updated |
| :gear: | **Baseline** | [BEVerse](https://arxiv.org/abs/2205.09743) |
| :octocat: | **Baseline Codebase** | https://github.com/zhangyp15/BEVerse |
| :bar_chart: | **Baseline Results** | To be updated |


## :taxi: Track 3: Robust Occupancy Prediction

| \# | Task | Robust Occupancy Prediction |
|:-:|:-|:-|
| :taxi: | **Description** | Testing the accuracy of occupancy grid predictions in dynamic and unpredictable real-world driving environments |
| :page_facing_up: | **Document** | [`track-3/README.md`](https://github.com/robodrive-24/toolkit/blob/main/track-3/README.md)
| :house: | **Server** | To be updated |
| :gear: | **Baseline** | [SurroundOcc](https://arxiv.org/abs/2303.09551) |
| :octocat: | **Baseline Codebase** | https://github.com/weiyithu/SurroundOcc |
| :bar_chart: | **Baseline Results** | To be updated |


## Track 4: Robust Depth Estimation
To be updated.


# Challenge Two: Sensor Failures

The second challenge topic aims to probe the 3D scene perception robustness under camera and LiDAR sensor failures:
  - Loss of certain camera frames during the driving system sensing process.
  - Loss of one or more camera views during the driving system sensing process.
  - Loss of the roof-top LiDAR view during the driving system sensing process.

## Track 5: Robust Multi-Modal BEV Detection
To be updated.


# Rules & Conditions
To be updated.


# Frequently Asked Questions
To be updated.


