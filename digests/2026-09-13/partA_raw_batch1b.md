# Part A verified blocks — batch 1b (world models)

## DUET-DINO: Simultaneous Cross-View World Modeling for Latent Planning in Robot Manipulation
- **arXiv:** 2609.10506 · https://arxiv.org/abs/2609.10506
- **Submitted:** 2026-09-09
- **Authors:** Nisarga Nilavadi, Ralf Römer, Moritz Reuss, Michael Krawez, Tobias Jülg, Angela P. Schoellig, Rudolf Lioutikov, Wolfram Burgard
- **Qualifying affiliation(s):** NVIDIA — Moritz Reuss (also Intuitive Robots Lab, KIT)
- **Categories:** cs.RO, cs.CV
- **Open release:** code planned (the paper states "the code and model checkpoints will be open-sourced"; project page https://utn-air.github.io/DUET-DINO)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** A dual-view latent world model for robot manipulation that fuses side-view and wrist-camera observations through cross-view attention and extends latent planning to a full 7-DoF end-effector action space.
**Purpose (≤3 sentences):** Single-view latent world models struggle to predict the fine translational, rotational and gripper-state changes needed for 7-DoF control.
**Breakthrough (≤3 sentences):** The authors report that DINOv3 captures action-conditioned visual dynamics better than V-JEPA 2, and that their normalised dual-view cost optimisation reaches 92% reach success, 72.5% angled-reach success and 60% lift-to-home success.
**Tools & method (≤3 sentences):** Cross-view conditioned latent prediction with CEM planning; trained on DROID (62,877 trajectories) and RoboArena (5,856 trajectories); evaluated in the RoboLab simulator and on a Franka Research 3 with two ZED cameras.
**Limitation (≤3 sentences):** The authors state CEM planning "limits real-time control" because of its computational cost and suggest vision-language-action models to accelerate planning.

## WorldReward: Reward Modeling for Camera-Conditioned World Models
- **arXiv:** 2609.03952 · https://arxiv.org/abs/2609.03952
- **Submitted:** 2026-09-03
- **Authors:** Yibin Wang, Zehan Wang, Junshu Tang, Zhimin Li, Yujie Zhou, Jiazi Bu, Pengyang Ling, Feng Han, Zhixiong Zhang, Long Xing, Shengyuan Ding, Ziang Li, Cheng Jin, Yuhang Zang, Jiaqi Wang, Tianyu Pang
- **Qualifying affiliation(s):** Tencent Hunyuan — Zehan Wang, Junshu Tang, Zhimin Li, Tianyu Pang
- **Categories:** cs.CV
- **Open release:** none stated (project page https://codegoat24.github.io/WorldReward)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** WorldReward is a VLM-based pairwise reward model for camera-conditioned world models that splits videos into action-aligned chunks, scores each with structured visual evidence, and aggregates separate action-consistency and visual-quality scores.
**Purpose (≤3 sentences):** To supply a reward signal for reinforcement-learning post-training of camera-conditioned video world models that covers action fidelity and visual quality in one evaluator.
**Breakthrough (≤3 sentences):** The authors describe it as the "first VLM-based pairwise reward model that unifies action-consistency and visual-quality evaluation," report that it improves RL post-training of Tencent's HY-WorldPlay 1.5, and release WorldReward-Bench with 760 human-annotated video pairs.
**Tools & method (≤3 sentences):** Trained on 50,000 reasoning-augmented video pairs from eight world models across 224 trajectories, built through frontier-VLM distillation, agent-assisted auditing and human calibration.
**Limitation (≤3 sentences):** The paper discusses trade-offs between action and visual rewards but states no formal limitations in the retrieved content (observed, not stated).

## SV-WAM: An Efficient Surround-View World-Action Model for End-to-End Autonomous Driving
- **arXiv:** 2609.03602 · https://arxiv.org/abs/2609.03602
- **Submitted:** 2026-09-03
- **Authors:** Jinyang Wang, Shiwei Li, Junjian Wang, Zhiqiang Deng, Jianbin Gao, Yihang Zhao, Liu Liu, Yongjia Zhao, Jinlong Chen, Huirui Xu, Yifeng Pan, Kangwei Liu, Fan Ren, Ji Tao, Minghao Yang
- **Qualifying affiliation(s):** Chongqing Changan Technology Co., Ltd. — Junjian Wang, Zhiqiang Deng, Jianbin Gao, Yifeng Pan, Kangwei Liu, Fan Ren, Ji Tao; FLAG: borderline (automaker R&D, comparable to Toyota Research / Wayve)
- **Categories:** cs.CV, cs.RO
- **Open release:** none
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** SV-WAM is a surround-view world-action model for end-to-end driving that keeps six-camera context through an action-centred causal mask, co-trains with future-video prediction, and drops the video branch at inference.
**Purpose (≤3 sentences):** Low-latency closed-loop planning that retains the full surround context that front-view-only planners lack.
**Breakthrough (≤3 sentences):** The authors report 91.0 EPDMS on NAVSIMv2 at 342 ms latency, aided by a differentiable drivable-area compliance regulariser.
**Tools & method (≤3 sentences):** Trained on the NAVSIM trainval split on 16 NVIDIA H800 GPUs (about 24 h per stage); evaluated closed-loop on NAVSIMv2 and zero-shot open-loop on nuScenes; inference on one NVIDIA H20 (341.6 ± 2.1 ms).
**Limitation (≤3 sentences):** The authors state the roughly 5B-parameter backbone "remains relatively large for deployment on resource-constrained on-board platforms" and plan distillation, pruning, quantisation and real-vehicle closed-loop tests.

## Building Pretraining Data for World Models: An Unreal Engine-Based Pipeline for Action-Conditioned Video Generation
- **arXiv:** 2609.03557 · https://arxiv.org/abs/2609.03557
- **Submitted:** 2026-09-03
- **Authors:** Haoyu Wang, Songchun Zhang, Haoran Li, Haoyang Huang, Zeyue Xue, Nan Duan
- **Qualifying affiliation(s):** JD (Joy Future Academy) — Haoyu Wang, Songchun Zhang, Haoyang Huang, Nan Duan; FLAG: borderline (JD.com)
- **Categories:** cs.CV, cs.GR
- **Open release:** none stated (project page https://echo-team-joy-future-academy-jd.github.io/Echo-1.5-Page/wm/)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** A production pipeline on Unreal Engine that generates synthetic, action-conditioned, multi-view video for training interactive world models, combining physics simulation of character trajectories with offline cinematic rendering.
**Purpose (≤3 sentences):** Large-scale, precisely action-aligned pretraining data for action-conditioned video models, given the scarcity of controllable real-world video.
**Breakthrough (≤3 sentences):** The authors report about 2,691 hours of 1080p and 6,076 hours of 720p five-camera video from 429 curated Unreal Engine levels and 40 characters on a 200-GPU farm (25 nodes of 8 NVIDIA RTX 5090), with non-forward actions making up 46.6% of trajectories.
**Tools & method (≤3 sentences):** Stage I physics simulation for trajectories; Stage II offline rendering through Unreal Engine's Movie Render Queue; asset curation and cache-aware scheduling across 2,384 Fab asset packs.
**Limitation (≤3 sentences):** The authors state the system prioritises controllability and scale over cinematic quality, that actions are limited to locomotion (no jumping, climbing or complex interaction), and that it is infrastructure rather than a new world-model architecture.

## VeriPhy: Agentic Physical Reasoning for World Model Evaluation and Refinement
- **arXiv:** 2609.03153 · https://arxiv.org/abs/2609.03153
- **Submitted:** 2026-09-02
- **Authors:** Wenzhuo Xu, Yuchen Zhu, Chongjian Ge, Xuan Shen, Jing Shi, Jason Kuen, Yongxin Chen, Molei Tao, Christopher McComb, Noelia Grande Gutiérrez, Jiuxiang Gu
- **Qualifying affiliation(s):** Adobe Research — Jason Kuen, Jiuxiang Gu
- **Categories:** cs.CV
- **Open release:** none stated (project page https://veriphy-ai.github.io)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** VeriPhy is an agentic physical-verification system that checks generated video against a natural-language prompt: a text-only planner compiles the prompt into typed physical obligations and a statically validated execution plan before any frame is observed.
**Purpose (≤3 sentences):** To evaluate and refine world models by verifying whether generated physics matches what was requested, beyond plausibility scoring.
**Breakthrough (≤3 sentences):** On a 149-clip core with 304 annotated flaws, the authors report VeriPhy identified 228 defects versus 164 for a published question-decomposition evaluator on identical clips and models.
**Tools & method (≤3 sentences):** Qwen3-VL-30B-A3B-Instruct as planner and verifier, SAM 3 for segmentation, TAPNext++ for tracking, FlexSED for audio, Wan 2.2-VACE for generation and MuJoCo for simulation rendered as depth controls; a 1,500-clip benchmark with 2,582 human-annotated flaw records.
**Limitation (≤3 sentences):** The authors state the corpus was labelled by a single annotator without inter-rater metrics, that multi-object interactions such as billiard collisions do not reliably reproduce simulated physics, and that closed-loop refinement is not yet implemented.

## SolarWM: Open Data and Scalable Training for Long-Horizon Video World Models
- **arXiv:** 2609.02886 · https://arxiv.org/abs/2609.02886
- **Submitted:** 2026-09-02
- **Authors:** Junchao Huang, Guian Fang, Shengju Qian, Xianghao Kong, Zhuoran Zhao, Wei Huang, Yihua Du, Zixin Zhang, Justin Cui, Yuchao Gu, Yukang Chen, Xinting Hu, Tianyu He, Shaoshuai Shi, Zhuotao Tian, Xin Wang, Mike Zheng Shou, Li Jiang
- **Qualifying affiliation(s):** NVIDIA — Wei Huang, Yuchao Gu, Yukang Chen; Microsoft Research Asia — Tianyu He
- **Categories:** cs.CV
- **Open release:** weights, code and data (https://github.com/Junchao-cs/SolarWM; https://huggingface.co/datasets/junchaoh-cs/SolarWM-Data)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** SolarWM is an open foundation for interactive video world models: a reconfigurable data engine (1.43M clips from 10 datasets, about 25.85 TB) plus a backbone-native adaptation framework instantiated as four 5B to 33B models built on Wan2.2, LTX-2.5 and MiniMax-H3.
**Purpose (≤3 sentences):** A reproducible open foundation (data, recipe, weights) for long-horizon interactive world models, addressing inconsistent supervision from naive multi-source mixing.
**Breakthrough (≤3 sentences):** The authors report causal models that sustain real-time interaction over rollouts from minutes to hours despite training on 5-second sequences, via bidirectional adaptation, teacher-forced autoregressive initialisation and distribution-matching distillation.
**Tools & method (≤3 sentences):** A frame-aligned data contract covering observations, metric camera geometry, captions and quality metadata; sources include ABOT-World, DL3DV, MiraData, RealCam-Vid, SpatialVID, Sekai-Game, Sekai-Walking, MIND, MultiCamVideo and OmniWorld.
**Limitation (≤3 sentences):** No explicit limitations section was found in the retrieved content (observed, not stated).

## H3-World: Turning Language Understanding into World Control
- **arXiv:** 2609.01560 · https://arxiv.org/abs/2609.01560
- **Submitted:** 2026-09-01
- **Authors:** Danze Chen, Zeqing Wang, Ziyue Lin, Xingyi Yang, Yeying Jin
- **Qualifying affiliation(s):** Tencent — Danze Chen, Zeqing Wang, Yeying Jin (also National University of Singapore)
- **Categories:** cs.CV, cs.AI
- **Open release:** weights and code (https://github.com/Danzer1xxxxChan/H3-World; https://huggingface.co/DANNY621/H3-World)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** H3-World turns the MiniMax-H3 video generator into an interactive world model by using natural language as the control interface for character and camera actions, aligning instructions to video latent intervals with temporal attention routing.
**Purpose (≤3 sentences):** To show that a large pretrained video generator can become a controllable interactive world model without a dedicated action module.
**Breakthrough (≤3 sentences):** The authors report effective character and camera control with only 0.199% trainable parameters (rank-32 LoRA, 10,000 steps).
**Tools & method (≤3 sentences):** 7,872 gameplay clips from ABot-World-Explorer-500h (128 held out), 124 frames per clip at 24 fps and 832x480; LoRA fine-tuning at learning rate 1e-4.
**Limitation (≤3 sentences):** The authors state the work is limited to short-horizon generation, lacks systematic evaluation across action combinations, and does not yet support persistent world state, real-time interaction, planning or policy learning.

## ZimaBlue: Evolving Generalizable World Action Models through Scalable Video Pre-training
- **arXiv:** 2609.00188 · https://arxiv.org/abs/2609.00188
- **Submitted:** 2026-08-31
- **Authors:** Xionghao Wu, Yijun Yang, Shiyang Zhou, Haoze Sun, Jianhui Liu, Songsong Yu, Jiyao Zhang, Wenbo Li, Bo Wang, Guoqing Ma, Lin Song, Renjie Liao, Shenghe Zheng, Wei Tang, Xiaojuan Qi, Yanwei Li, Yuan Zhang, Zhuotao Tian, Haoyang Huang, Nan Duan
- **Qualifying affiliation(s):** JD (Joy Future Academy, collective byline) — FLAG: borderline (JD.com)
- **Categories:** cs.CV
- **Open release:** code (https://github.com/ZimaBlue-WAM/ZimaBlue; project https://zimablue-wam.github.io/)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** ZimaBlue trains World Action Models through a three-stage curriculum: causal video pretraining on egocentric video without action labels, multi-embodiment video-action mid-training with a unified action representation, then target-robot post-training with a Slow-Fast dual-system architecture.
**Purpose (≤3 sentences):** To scale world-action-model pretraining on abundant action-free egocentric video for cross-embodiment manipulation.
**Breakthrough (≤3 sentences):** The authors report that scaling pretraining video from 300 to more than 120,000 hours raises zero-shot task success from 36.1% to 77.8%, and that the Slow-Fast design predicts actions at 30 Hz on an RTX 4090.
**Tools & method (≤3 sentences):** A unified 100-dimensional state-action representation; pretraining data including EPIC-KITCHENS, Egocentric-100K, EgoDex, DROID and RoboCOIN; evaluation on real Franka robots and the LIBERO-Plus, RoboTwin 2.0 and RoboCasa365 simulators.
**Limitation (≤3 sentences):** The authors state remaining failures include difficulty advancing from correct intermediate states and local interaction errors such as target displacement or lost contact.

## CAER: Causal Action Effect Reweighting for World Model Training
- **arXiv:** 2608.30897 · https://arxiv.org/abs/2608.30897
- **Submitted:** 2026-08-31
- **Authors:** Jianjie Fang, Xvyuan Liu, Ziyou Wang, Rongze Tang, Zhaolu Wang, Zhuohang Li, Xin Zhang, Haisheng Su, Chen Gao, Wei Wu, Xinlei Chen, Yong Li
- **Qualifying affiliation(s):** Manifold AI — Xin Zhang, Haisheng Su, Wei Wu; FLAG: borderline (company tier unclear)
- **Categories:** cs.AI
- **Open release:** none
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** CAER reweights the training loss of action-conditioned video world models toward action-responsive tokens, since a uniform space-time MSE lets static background dominate gradients while sparse interaction dynamics stay under-optimised.
**Purpose (≤3 sentences):** To focus supervision on tokens causally affected by actions.
**Breakthrough (≤3 sentences):** The authors report consistent improvements across heterogeneous action-conditioned tasks, an online method to identify action-responsive tokens without external annotation, and a theoretical analysis of when focused reweighting beats uniform averaging.
**Tools & method (≤3 sentences):** Wan 2.2 5B backbone trained on eight NVIDIA H20 GPUs; evaluated on LIBERO, RoboTwin 2.0, RealEstate10K and PoseAnything.
**Limitation (≤3 sentences):** The authors note sensitivity to hyperparameters (about 10% action dropout, fixed noise level 0.50) and open questions about scaling to longer horizons and larger models.

## PAWBench: How Far Are We from Probabilistically Aligned World Modeling?
- **arXiv:** 2608.27345 · https://arxiv.org/abs/2608.27345
- **Submitted:** 2026-08-27
- **Authors:** Yuandong Pu, Le Zhuo, Sayak Paul, Gabriel Jorge Menezes, Avram Đorđević, Shiyang Li, Yifan Zhou, Bin Fu, Wenlong Zhang, Junjun He, Yu Qiao, Yihao Liu, Jinbo Xing, Xi Chen
- **Qualifying affiliation(s):** Alibaba (Tongyi Lab) — Yihao Liu
- **Categories:** cs.CV, cs.AI
- **Open release:** none stated (project page https://pawbench.github.io)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** PAWBench tests whether video generators behave as probabilistically aligned world models: whether repeated rollouts from identical initial conditions and actions recover the correct distribution over futures rather than one plausible video.
**Purpose (≤3 sentences):** To formalise and measure probabilistic alignment as a distributional criterion for world models.
**Breakthrough (≤3 sentences):** The authors report benchmarking 11 video generation systems, including Veo 3.1 Fast, Kling 3 and Seedance 2, and find that none consistently matches reference probabilities while also covering valid futures.
**Tools & method (≤3 sentences):** 50 scenarios in two tracks, PAW-Calibration (analytically specified distributions) and PAW-Coverage (recovery of valid outcomes), with a PAWEval protocol built on Gemini 3.5 Flash to map videos to terminal outcomes.
**Limitation (≤3 sentences):** The authors state the benchmark scores only terminal outcomes rather than full trajectories, that finite rollout budgets limit distribution estimates, and that it covers controlled, visually parseable scenarios rather than interactive settings.

## GameWAM: A World Action Model for Video Games
- **arXiv:** 2608.26200 · https://arxiv.org/abs/2608.26200
- **Submitted:** 2026-08-25
- **Authors:** Yuncheng Guo, Zhanqiu Zhang, Yiwen Guo, Weijia Li
- **Qualifying affiliation(s):** LIGHTSPEED — Zhanqiu Zhang (the paper's affiliation footnote reads only "LIGHTSPEED"; not identified in the paper as Tencent's Lightspeed Studios); FLAG: borderline
- **Categories:** cs.AI, cs.CV, cs.LG
- **Open release:** none stated (project page https://yunncheng.github.io/GameWAM/)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** GameWAM is presented as the first World Action Model for native closed-loop video-game play and GUI control, jointly generating future observations and executable keyboard-mouse action trajectories through parallel visual and action generative processes with block-causal conditioning and flow matching.
**Purpose (≤3 sentences):** To unify game-playing control policies with world-model-style visual prediction, since prior agents map perception to actions without modelling dynamics while interactive world models predict visuals without acting.
**Breakthrough (≤3 sentences):** The authors report competitive task success with fewer executed native actions than compared agents, and identify a failure mode they call "Low-Frequency Action Source Imprinting," where low-frequency components of the sampled action source steer coarse camera motion.
**Tools & method (≤3 sentences):** Block-cycle control coordinating prediction, execution and replanning; mode-specific prediction distributions and continuous-action normalisation; trained on synchronised gameplay and GUI trajectory data the authors constructed.
**Limitation (≤3 sentences):** The authors state GameWAM "is designed as a low-level closed-loop controller rather than a standalone high-level planner," with no symbolic task graph or long-horizon search.

## CaliBench: Are the Stochastic Dynamics of Video World Models Physically Calibrated?
- **arXiv:** 2608.16829 · https://arxiv.org/abs/2608.16829
- **Submitted:** 2026-08-17
- **Authors:** Jonathan Sadeghi, Jenny Seidenschwarz, Jesse Allardice, Sirish Srinivasan, Benjamin Graham, Jeffrey Hawke
- **Qualifying affiliation(s):** Odyssey — all authors; FLAG: borderline (world-model startup, not on the tracked list)
- **Categories:** cs.LG, cs.AI
- **Open release:** code (https://github.com/odysseyml/calibench)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** CaliBench tests whether video world models reproduce the correct statistical distribution of physical outcomes, evaluating six image-to-video models on nine scenes with analytically known outcome distributions (Galton boards, dice, roulette, cards and others).
**Purpose (≤3 sentences):** To measure distributional calibration, split into "scorability" (share of valid generations) and "calibration" (distance from the true outcome distribution).
**Breakthrough (≤3 sentences):** The authors report "severe probability mass over-concentration" in most models despite plausible individual frames, across 1,728 generations and 5,184 VLM queries; models include WAN-2.7, SeeDance-2.0, HappyHorse-1.0, Veo 3.1, Runway Gen-4.5 and Cosmos3-Super.
**Tools & method (≤3 sentences):** A Mean Normalised Total Variation metric over nine discrete-outcome scenes with closed-form references; VLM-based outcome extraction validated at 93.8% agreement.
**Limitation (≤3 sentences):** The authors state the benchmark covers image-to-video pipelines only, that VLM extraction adds noise, that it tests marginal outcome distributions rather than trajectories, and that it cannot audit commercial training corpora.

# Near-misses (batch 1b)
- 2608.12564 · Scaling Automatic Research Agents via World Models · out of window (v1 2026-08-12)
- 2608.01397 · SG-WAM · out of window (v1 2026-08-02)
- 2609.07051 · TrojanWorld · academic-only (SJTU, NTU)
- 2609.06207 · PhysWeep · academic-only (Hamad Bin Khalifa University)
- 2609.02811 · Do Better Imagined Rollouts Mean Better Robot Control? · academic-only (Georgia Tech, Emory)
- 2609.02046 · Modeling What Changes: Sparse, Residual World Models · academic-only
- 2609.03774 · Rethinking World Models for Safety-Critical Embodied Systems · academic-only (KAIST)
- 2608.15156 · Low-Rank Dynamics-Effective Latent Carriers · academic-only (Fudan)
- 2608.16859 · HarnessEval-W · affiliation unverifiable (no institutions listed for 43 authors)
