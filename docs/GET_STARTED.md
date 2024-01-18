# Getting Started

- [Challenge One: Corruptions](#challenge-one-corruptions)
  - [Track 1: Robust BEV Detection](#red_car-track-1-robust-bev-detection)
  - [Track 2: Robust Map Segmentation](#blue_car-track-2-robust-map-segmentation)
  - [Track 3: Robust Occupancy Prediction](#taxi-track-3-robust-occupancy-prediction)
  - [Track 4: Robust Depth Estimation](#minibus-track-4-robust-depth-estimation)
- [Challenge Two: Sensor Failures](#challenge-two-sensor-failures)
  - [Track 5: Robust Multi-Modal BEV Detection](#truck-track-5-robust-multi-modal-bev-detection)
- [Rules & Conditions](#rules--conditions)
- [Frequently Asked Questions](#frequently-asked-questions)


# Challenge One: Corruptions

The first challenge topic contains 18 real-world corruption types, ranging from the following three perspectives:
  - Weather and lighting conditions, such as bright, low-light, foggy, and snowy conditions.
  - Movement and acquisition failures, such as potential blurs caused by vehicle motions.
  - Data processing issues, such as noises and quantizations happen due to hardware malfunctions.


## :red_car: Track 1: Robust BEV Detection
| \# | Task | Robust BEV Detection |
|:-:|:-|:-|
| :red_car: | **Description** | Evaluating the resilience of detection algorithms against diverse environmental and sensor-based corruptions |
| :page_facing_up: | **Document & Instruction** | [`track-1/README.md`](https://github.com/robodrive-24/toolkit/blob/main/track-1/README.md)
| :house: | **Evaluation Server** | https://codalab.lisn.upsaclay.fr/competitions/17135 |
| :gear: | **Baseline Model** | [BEVFormer](https://arxiv.org/abs/2203.17270) |
| :octocat: | **Baseline Codebase** | https://github.com/fundamentalvision/BEVFormer |
| :bar_chart: | **Baseline Results** | NDS = 31.24%, mAP = 18.82% |

> **Hint:** Participants of Track `1` can refer to the above resources for more details and instructions.


## :blue_car: Track 2: Robust Map Segmentation

| \# | Task | Robust Map Segmentation |
|:-:|:-|:-|
| :blue_car: | **Description** | Focusing on the segmentation of complex driving scene elements in BEV maps under varied driving conditions |
| :page_facing_up: | **Document & Instruction** | [`track-2/README.md`](https://github.com/robodrive-24/toolkit/blob/main/track-2/README.md)
| :house: | **Evaluation Server** | https://codalab.lisn.upsaclay.fr/competitions/17062 |
| :gear: | **Baseline** | [BEVerse](https://arxiv.org/abs/2205.09743) |
| :octocat: | **Baseline Codebase** | https://github.com/zhangyp15/BEVerse |
| :bar_chart: | **Baseline Results** | mIoU = 17.33% |

> **Hint:** Participants of Track `2` can refer to the above resources for more details and instructions.


## :taxi: Track 3: Robust Occupancy Prediction

| \# | Task | Robust Occupancy Prediction |
|:-:|:-|:-|
| :taxi: | **Description** | Testing the accuracy of occupancy grid predictions in dynamic and unpredictable real-world driving environments |
| :page_facing_up: | **Document & Instruction** | [`track-3/README.md`](https://github.com/robodrive-24/toolkit/blob/main/track-3/README.md)
| :house: | **Evaluation Server** | https://codalab.lisn.upsaclay.fr/competitions/17063 |
| :gear: | **Baseline** | [SurroundOcc](https://arxiv.org/abs/2303.09551) |
| :octocat: | **Baseline Codebase** | https://github.com/weiyithu/SurroundOcc |
| :bar_chart: | **Baseline Results** | mIoU = 11.30% |

> **Hint:** Participants of Track `3` can refer to the above resources for more details and instructions.


## :minibus: Track 4: Robust Depth Estimation

| \# | Task | Robust Depth Estimation |
|:-:|:-|:-|
| :minibus: | **Description** | Assessing the depth estimation robustness from multiple perspectives for comprehensive 3D scene perception |
| :page_facing_up: | **Document & Instruction** | [`track-4/README.md`](https://github.com/robodrive-24/toolkit/blob/main/track-4/README.md)
| :house: | **Evaluation Server** | To be updated |
| :gear: | **Baseline** | [SurroundDepth](https://arxiv.org/abs/2204.03636) |
| :octocat: | **Baseline Codebase** | https://github.com/weiyithu/SurroundDepth |
| :bar_chart: | **Baseline Results** | To be updated |

> **Hint:** Participants of Track `4` can refer to the above resources for more details and instructions.


# Challenge Two: Sensor Failures

The second challenge topic aims to probe the 3D scene perception robustness under camera and LiDAR sensor failures:
  - Loss of certain camera frames during the driving system sensing process.
  - Loss of one or more camera views during the driving system sensing process.
  - Loss of the roof-top LiDAR view during the driving system sensing process.

## :truck: Track 5: Robust Multi-Modal BEV Detection

| \# | Task | Robust Multi-Modal BEV Detection |
|:-:|:-|:-|
| :truck: | **Description** | Tailored for evaluating the reliability of advanced driving perception systems equipped with multiple types of sensors |
| :page_facing_up: | **Document & Instruction** | [`track-5/README.md`](https://github.com/robodrive-24/toolkit/blob/main/track-5/README.md)
| :house: | **Evaluation Server** | https://codalab.lisn.upsaclay.fr/competitions/17137 |
| :gear: | **Baseline** | [BEVFusion](https://arxiv.org/abs/2205.13542) |
| :octocat: | **Baseline Codebase** | https://github.com/mit-han-lab/bevfusion |
| :bar_chart: | **Baseline Results** | NDS = 42.86%, mAP = 24.50% |

> **Hint:** Participants of Track `5` can refer to the above resources for more details and instructions.


# Rules & Conditions

This competition is made freely available to academic and non-academic entities for non-commercial purposes such as academic research, teaching, scientific publications, or personal experimentation. Permission is granted to use the data given that you agree:
1. That the data in this competition comes “AS IS”, without express or implied warranty. Although every effort has been made to ensure accuracy, we do not accept any responsibility for errors or omissions.
2. That you may not use the data in this competition or any derivative work for commercial purposes such as, for example, licensing or selling the data, or using the data with a purpose of procuring a commercial gain.
3. That you include a reference to RoboDrive (including the benchmark data and the specially generated data for academic challenges) in any work that makes use of the benchmark. For research papers, please cite our preferred publications as listed on our webpage.

To ensure a fair comparison among all participants, we require:
1. All participants must follow the exact same data configuration when training and evaluating their algorithms. Please do not use any public or private datasets other than those specified for model training.
2. The theme of this competition is to probe the out-of-distribution robustness of autonomous driving perception models. Therefore, any use of the corruption and sensor failure types designed in this benchmark is strictly prohibited, including any atomic operation that comprises any one of the mentioned corruptions.
3. To ensure the above two rules are followed, each participant is requested to submit the code with reproducible results before the final result is announced; the code is for examination purposes only and we will manually verify the training and evaluation of each participant's model.



# Frequently Asked Questions

| | |
|:-:|:-|
| :thinking: | **Q1:** ***"How can I register a valid team for this competition?"*** |
| :blue_car: | **A1:**  To register a team, kindly fill in [this](https://forms.gle/hnaezVhEycPAjUD78) Google Form. The registration period is from `now` till the deadline of phase one, i.e., `Mar 31 '24`. |
|  |
|  |
| :thinking: | **Q2:** ***"Are there any restrictions for the registration? For example, the number of team members."*** |
| :blue_car: | **A2:**  Each team leader should make a **valid** registration for his/her team. Each participant can only be registered by **one** team. This is no restriction on the number of team members in a team.
|  |
|  |
| :thinking: | **Q3:** ***"Whether team members can be changed during the competition?"*** |
| :blue_car: | **A3:**  No. You **CANNOT** change the list of team members after the registration. You must register again as a **new** team if you need to add or remove any members of your team. |
|  |
|  |
| :thinking: | **Q4:** ***"How many tracks can I participate in?"*** |
| :blue_car: | **A4:**  Each team can participate in **at most two tracks** in this competition. |
|  |
|  |
| :thinking: | **Q5:** ***"What can I expect from this competition?"*** |
| :blue_car: | **A5:**  We provide the winning teams from each track with **cash awards** :moneybag: and **certificates** :1st_place_medal:. The winning solutions will be summarized as a **technical report** :book:. An example of last year's technical report can be found [here](https://arxiv.org/abs/2307.15061).
|  |
|  |
| :thinking: | **Q6:** ***“Can I use additional data resources for model training?"*** |
| :blue_car: | **A6:**  No. All participants must follow the **SAME** data preparation procedures as listed in [DATA_PREPARE.md](https://github.com/robodrive-24/toolkit/blob/main/docs/DATA_PREPARE.md). Additional data sources are **NOT** allowed in this competition.
|  |
|  |
| :thinking: | **Q7:** ***"Can I use corruption augmentations during model training?"*** |
| :blue_car: | **A7:**  No. The theme of this competition is to probe the **out-of-distribution robustness** of autonomous driving perception models. Therefore, all participants must **REFRAIN** from using any corruption simulations as data augmentations during the model training, including any atomic operation that comprises any one of the corruptions in this competition.
|  |
|  |
| :thinking: | **Q8:** ***"How should I configurate the model training? Are there any restrictions on model size, image size, loss function, optimizer, number of epochs, and so on?"***
| :blue_car: | **A8:**  We provide one **baseline model** for each track in [GET_STARTED.md](https://github.com/robodrive-24/toolkit/blob/main/docs/GET_STARTED.md). The participants are recommended to refer to these baselines as the starting point in configuring the model training. There is no restriction on normal model training configurations, including model size, image size, loss function, optimizer, and number of epochs. 
|  |
|  |
| :thinking: | **Q9:** ***"Can I use LiDAR data for Tracks `1` to `4`?"*** |
| :blue_car: | **A9:**  No. Tracks `1` to `4` are **single-modality** tracks that only involve the use of camera data. The goal of these tracks is to probe the robustness of perception models under camera-related corruptions. Participants who are interested in **multi-modal robustness** (camera + LiDAR) can refer to Track `5` in this competition.
|  |
|  |
| :thinking: | **Q10:** ***"Is it permissible to use self-supervised model pre-training (such as MoCo and MAE)?"*** |
| :blue_car: | **A10:**  Yes. The use of **self-supervised** pre-trained models is possible. Such models may include [MoCo](https://arxiv.org/abs/1911.05722), [MoCo v2](https://arxiv.org/abs/2003.04297), [MAE](https://arxiv.org/abs/2111.06377), [DINO](https://github.com/facebookresearch/dino), and many others. Please make sure to acknowledge (in your code and report) if you use any pre-trained models.
|  |
|  |
| :thinking: | **Q11:** ***"Can I use large models (such as SAM) to generate pre-training or auxiliary annotations?"*** |
| :blue_car: | **A11:**  No. The use of large foundation models, such as [CLIP](https://github.com/openai/CLIP), [SAM](https://segment-anything.com/), [SEEM](https://github.com/UX-Decoder/Segment-Everything-Everywhere-All-At-Once), and any other similar models, is **NOT** allowed in this competition. This is to ensure a relatively fair comparing environment among different teams. Any violations of this rule will be regarded as **cheating** and the results will be canceled.
|  |
|  |
| :thinking: | **Q12:** ***"Are there any restrictions on the use of pre-trained weights (such as DD3D, ImageNet, COCO, ADE20K, Object365, and so on)?"*** |
| :blue_car: | **A12:**  Following the most recent BEV perception works, it is possible to use pre-trained weights on **DD3D**, **ImageNet**, and **COCO**. The use of weights pre-trained on other datasets is **NOT** allowed in this competition.
|  |
|  |
| :thinking: | **Q13:** ***"Can I combine the training and validation sets for model training?"*** |
| :blue_car: | **A13:**  It is strictly **NOT** allowed to use the validation data for model training. All participants **MUST** follow the nuScenes official `train` split during model training and **REFRAIN** from involving any samples from the validation set. Any violations of this rule will be regarded as **cheating** and the results will be canceled.
|  |
|  |
| :thinking: | **Q14:** ***"Can I use model ensembling and test-time augmentation (TTA)?"*** |
| :blue_car: | **A14:**  Like many other academic competitions, it is possible to use **model ensembling** and **test-time augmentation (TTA)** to enhance the model when preparing the submissions. The participants **SHOULD** include necessary details for the use of model ensembling and TTA in their code and reports.
|  |
|  |
| :thinking: | **Q15:** ***"How many times can I make submissions to the server?"*** |
| :blue_car: | **A15:**  For phase one (Jan. - Mar.), a team can submit up to **3** times per day and **99** times total. For phase two (Apr.), a team can submit up to **2** times per day and **49** times total. One team is affiliated with one CodaLab account only. Please **REFRAIN** from having multiple accounts for the same team.
|  |
|  |
| :thinking: | ... |
| :blue_car: | ... |


### Contact
:mailbox: Didn't find a related FAQ to your questions? Let us know (robodrive.2024@gmail.com)!


