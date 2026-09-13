# Part A verified blocks — batch 2b (world models, animation, game tech)

## Can Video World Models Track Unobserved World States?
- **arXiv:** 2608.30692 · https://arxiv.org/abs/2608.30692
- **Submitted:** 2026-08-31
- **Authors:** Joonghyuk Shin, Yicong Hong, Jaesik Park, Xun Huang
- **Qualifying affiliation(s):** Roblox — Yicong Hong, Xun Huang (co-authors at Seoul National University)
- **Categories:** cs.CV
- **Open release:** demo (project page https://joonghyuk.com/stateful-vwm-web/)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** Studies whether video world models maintain a hidden, unobserved world state rather than only producing plausible frames, using an action-conditioned "Shell Game" task, a visual analogue of S5 permutation-group state tracking that decouples rendering from tracking the underlying state.
**Purpose (≤3 sentences):** To determine which architectures can track unobserved state over long horizons and isolate the mechanism behind success or failure.
**Breakthrough (≤3 sentences):** The authors report that plain Transformers and Mamba fail to extrapolate state tracking beyond training length, while linear attention with negative eigenvalues and test-time training with nonlinear fast weights succeed; they also report the negative-eigenvalue mechanism does not transfer to Memory Maze and Block World, where state must be corrected from observations.
**Tools & method (≤3 sentences):** The Shell Game benchmark plus Memory Maze and Block World, comparing Transformer, Mamba, linear-attention and test-time-training video architectures.
**Limitation (≤3 sentences):** The authors state a real world model "has to correct its state from observations, keep it fixed when an action fails, and keep it evolving even when no action arrives," and that some prediction problems "plausibly require NC¹-hard state tracking," which none of the tested architectures capture.

## FaceSnap: Real-Time Personalized Lightstage Facial Performance Capture
- **arXiv:** 2608.31033 · https://arxiv.org/abs/2608.31033
- **Submitted:** 2026-08-31
- **Authors:** Rukhshanda Hussain, Noé Artru, Emeline Got, Luiz Gustavo Hafemann, Alexandre Messier, Brandon Dearlove, Rafael M. O. Cruz, Abdallah Dib, Eric Granger
- **Qualifying affiliation(s):** Ubisoft (La Forge) — Emeline Got, Luiz Gustavo Hafemann, Alexandre Messier, Brandon Dearlove, Abdallah Dib
- **Categories:** cs.CV
- **Open release:** none (the Multi4D benchmark is announced)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** A two-stage framework that amortises expensive lightstage multi-camera sessions into a reusable personalised model, then tracks facial performance in real time from a single camera at 83 fps, with a personalised residual upscaler recovering subject-specific detail. The authors also introduce Multi4D, a benchmark for topology-invariant 4D facial reconstruction.
**Purpose (≤3 sentences):** Lightstage capture for production digital humans needs costly camera arrays, hours of compute and large storage; the aim is to keep that fidelity while enabling monocular real-time capture after one personalisation step.
**Breakthrough (≤3 sentences):** The authors report 0.92 mm average point-to-surface error at about 12 ms per frame on an NVIDIA RTX A6000 versus 1.24 mm for Topo4D, LPIPS 0.0497 versus 0.0503 (Topo4D) and 0.0698 (fine-tuned ESRGAN), and roughly 5,000x speedup over Topo4D and 25,000x over production pipelines.
**Tools & method (≤3 sentences):** A personalised geometry-and-appearance model optimised once from multi-view capture, then a real-time single-camera tracker and upscaler; data from a 24-camera, 60 fps, 4K lightstage (3 subjects) and Multi4D (6 Multiface subjects, about 7,600 frames, 38 views).
**Limitation (≤3 sentences):** The authors state the dynamic appearance model runs at 512x512 and "may lose fine details such as micro-wrinkles" that offline methods capture.

## BLARM: Animating 3D Objects from Video via Blending Latent Rigid Motion Primitives
- **arXiv:** 2608.31113 · https://arxiv.org/abs/2608.31113
- **Submitted:** 2026-08-31
- **Authors:** Pradyumn Goyal, Yizhak Ben-Shabat, Hsueh-Ti Derek Liu, Haomiao Jiang, Snehasish Mukherjee, Kyle Spence, Mark Stauber, Evangelos Kalogerakis, Yunze Zeng
- **Qualifying affiliation(s):** Roblox — Yizhak Ben-Shabat, Hsueh-Ti Derek Liu, Haomiao Jiang, Snehasish Mukherjee, Kyle Spence, Mark Stauber, Yunze Zeng (Pradyumn Goyal as a Roblox intern)
- **Categories:** cs.CV
- **Open release:** none
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** A feed-forward method that animates a static 3D mesh from monocular video, predicting a temporally coherent animated mesh without skeletons, cages or manual rigs, by representing motion as a compact set of learned time-varying rigid primitives blended with time-invariant per-vertex skinning weights.
**Purpose (≤3 sentences):** Automatic animation of arbitrary 3D objects from a single video, replacing manual rigging or dense per-vertex prediction.
**Breakthrough (≤3 sentences):** The authors report the best results on ActionBench (CD-3D 1.71, CD-4D 3.07, CD-Motion 7.15, FVD 426.72 versus baseline ranges 2.49 to 3.30 / 5.01 to 5.61 / 9.24 to 11.12 / 787 to 1270) and Motion80, with the fastest inference among compared methods (3.13 s per 16-frame video).
**Tools & method (≤3 sentences):** A transformer combining geometry-conditioned deformation latents with video features via factorised spatial-temporal attention; trajectory reconstruction loss, entropy regularisation for sparse skinning and motion-aware contrastive learning; about 10,000 Objaverse shapes rendered at 512x512, trained on 8 NVIDIA H200 GPUs for about 1.5 days.
**Limitation (≤3 sentences):** The authors acknowledge incorrect vertex-to-component assignment and "part entanglement" when nearby regions look alike but should move independently, and that the mesh topology must suit the target motion.

## ECHO: Dyadic 3D Facial Motion Generation with Asymmetric Deterministic Articulation and Stochastic Reaction
- **arXiv:** 2609.05506 · https://arxiv.org/abs/2609.05506
- **Submitted:** 2026-08-29
- **Authors:** Zhuoqiang Cai, Yujie Sun, Chaoyue Niu, Hongyun Yu, Zhiwen Chen, Chengfei Lv, Fan Wu
- **Qualifying affiliation(s):** Alibaba Group — Hongyun Yu, Zhiwen Chen, Chengfei Lv
- **Categories:** cs.GR, cs.CV, cs.SD
- **Open release:** none
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** ECHO generates 3D facial motion for both roles in a two-person conversation from audio alone, treating the speaker's mouth motion as deterministic and the listener's reaction as stochastic, decomposing motion into a stable anchor trajectory plus a stochastic residual with "Motion Memory" regularisation.
**Purpose (≤3 sentences):** Audio-only conversational digital humans that need plausible facial behaviour for both talking and listening.
**Breakthrough (≤3 sentences):** Versus ProbTalk3D the authors report Fréchet distance improving from 7.51 to 2.80 and paired Fréchet distance from 1.61 to 0.59; a user study scored ECHO above UniTalker for lip-sync (3.71 vs 3.03), interaction realism (3.77 vs 2.59) and naturalness (3.82 vs 2.34).
**Tools & method (≤3 sentences):** About 120 hours of speaker-disjoint dyadic video derived from Seamless-Interaction (30 FPS, 54-dim FLAME coefficients); base training about 10 hours on one NVIDIA RTX 4090.
**Limitation (≤3 sentences):** No explicit limitations section was found in the extracted text (observed, not stated).

## R2M-Bench: Evaluating Revisit Memory via Relative Consistency in Interactive Video World Models
- **arXiv:** 2608.27328 · https://arxiv.org/abs/2608.27328
- **Submitted:** 2026-08-27
- **Authors:** Qiwen Gu, Bingjie Gao, Rui Chen, Geng Li, Jifan Li, Qishuai Wen, Li Niu, Jing Tang, Xiangxiang Chu, Junqiao Zhao
- **Qualifying affiliation(s):** Alibaba Group (DreamX Team) — Rui Chen, Geng Li, Jifan Li, Qishuai Wen, Jing Tang, Xiangxiang Chu
- **Categories:** cs.CV
- **Open release:** code (https://github.com/AMAP-ML/R2MBench)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** R2M-Bench tests whether video world models genuinely remember previously seen scenes rather than merely changing little, by comparing a revisit pair against two same-rollout controls (a gap-matched non-revisit pair and a short-range pair).
**Purpose (≤3 sentences):** The authors note that "high similarity between first-visit and return frames does not necessarily show that a video world model remembered the scene."
**Breakthrough (≤3 sentences):** The authors report their Normalised Memory Ratio correlates with human judgments at Spearman 0.547 and is far less correlated with generated motion (0.072) than raw revisit similarity (0.207); across seven models, DreamX-World-Memo scores highest (0.706), ahead of HY-WorldPlay (0.485), Matrix-Game 3.0 (0.403) and Lyra-2 (0.310).
**Tools & method (≤3 sentences):** 100 reference scenes and three leave-and-return trajectory templates form 300 instances, scoring appearance fidelity, identity, local geometry and persistent state.
**Limitation (≤3 sentences):** The authors state the benchmark "evaluates observable revisit-selective consistency rather than identifying an internal memory mechanism," that automatic metrics "inherit backbone, viewpoint, and prompt biases," and that object interaction and deliberately evolving state are out of scope.

## 4DSynth: Controllable Procedural World Synthesis for Dynamic Embodied Simulation
- **arXiv:** 2608.26947 · https://arxiv.org/abs/2608.26947
- **Submitted:** 2026-08-27
- **Authors:** Zehao Qi, Haochen Luo, Jia-Wang Bian, Zeyu Ma, Shuyang Sun
- **Qualifying affiliation(s):** Google DeepMind — Shuyang Sun (co-authors at NTU, Oxford, Princeton)
- **Categories:** cs.RO, cs.CV
- **Open release:** none found
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** 4DSynth converts a text description, a blueprint mask or a single photograph into an editable 4D environment with explicit geometry, animated actors, collision-free trajectories and physics-ready state for embodied agents.
**Purpose (≤3 sentences):** A procedurally generated, controllable 4D world-synthesis pipeline instead of static or hand-authored scenes.
**Breakthrough (≤3 sentences):** The authors introduce 4DSynth-Nav, 333 navigation and pick-and-place tasks, and report that Qwen3-VL-30B (13.2% success) and Gemini 3.1 Pro (33.3%) "both fail the majority of tasks," with Gemini ranging from 57.5% on the easiest tier to 18.2% on the hardest.
**Tools & method (≤3 sentences):** Procedural generation with explicit geometry, animated actors and physics-ready state; evaluation on 4DSynth-Nav.
**Limitation (≤3 sentences):** The authors state animated characters act as kinematic obstacles rather than responsive humans and plan to add responsive humans and articulated objects.

## SpatialCrafter: Single Image World Modeling with Generative 3D Proxies
- **arXiv:** 2608.27073 · https://arxiv.org/abs/2608.27073
- **Submitted:** 2026-08-27
- **Authors:** Chuan Fang, Lingteng Qiu, Yixun Liang, Rui Chen, Kunming Luo, Zhaohua Zheng, Tongyuan Bai, Feipeng Tian, Zilong Dong, Zihan Zhou, Ping Tan
- **Qualifying affiliation(s):** Alibaba Group (Tongyi Lab) — Lingteng Qiu, Zilong Dong
- **Categories:** cs.CV, cs.RO
- **Open release:** demo (project page https://fangchuan.github.io/SpatialCrafter/)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** SpatialCrafter turns one image into an explorable 3D scene by generating a global 3D proxy and refining its appearance with a video diffusion model, to reduce hallucination and drift compared with video-diffusion-only methods; the authors also build a 115K-scene dataset with geometric annotations.
**Purpose (≤3 sentences):** Image-to-scene generation for gaming, robotics and VR where video-diffusion methods lack global 3D consistency under large camera motion.
**Breakthrough (≤3 sentences):** At 81-frame generation the authors report FVD 193.54 on SpatialGen-Video (versus 339.04 for ViewCrafter and 525.23 for GEN3C), and on RealEstate10K FVD 148.71 / PSNR 17.185 / SSIM 0.659.
**Tools & method (≤3 sentences):** A Point-anchored Sparse Structure Flow module builds the proxy and a Generative Deferred Refiner handles appearance; 115,295 training pairs from SpatialGen, RealEstate10K and DL3DV; 16 then 32 NVIDIA H20 GPUs.
**Limitation (≤3 sentences):** No explicit limitations section was extracted (observed, not stated).

## 4DStreamCtrl: Interactive Video Generation with Online 4D Control
- **arXiv:** 2608.25479 · https://arxiv.org/abs/2608.25479
- **Submitted:** 2026-08-26
- **Authors:** Shiqian Li, Chenguo Lin, Zhiguang Liu, Yu Tang, Jiarong Ou, Rui Chen, Yixin Zhu
- **Qualifying affiliation(s):** Tencent Hunyuan — Shiqian Li (also Peking University), Zhiguang Liu, Yu Tang, Jiarong Ou, Rui Chen
- **Categories:** cs.CV, cs.AI
- **Open release:** none found
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** A unified 3D point-track representation for joint camera and object control, depth editing and motion transfer in streaming video generation, integrated into a pretrained diffusion model through a "Geometric Motion Head."
**Purpose (≤3 sentences):** Real-time streaming 4D-controllable video generation rather than offline or single-signal control.
**Breakthrough (≤3 sentences):** The authors report 480p video at 20.6 FPS from a causal student distilled from 50 to 4 sampling steps, coherent over 350 frames with constant memory, and on DAVIS an EPE of 5.48 (student) versus 11.18 for MotionStream causal on the same backbone.
**Tools & method (≤3 sentences):** The OpenVidHD-Motion3D dataset mined from video; a 32x32 grid of 3D point tracks as the control interface; SpatialTrackerV2 for monocular geometry and camera recovery.
**Limitation (≤3 sentences):** The authors state monocular 3D estimation "can fail on challenging footage with extreme motion blur or occlusions," that the causal student shows a streaming-versus-offline quality gap, and that "small faces and background objects blur progressively" over long sequences.

## InteractGesture: Progressive Chunk Guidance for Continuous Streaming Co-Speech Gesture Control
- **arXiv:** 2608.25734 · https://arxiv.org/abs/2608.25734
- **Submitted:** 2026-08-26
- **Authors:** Ekkasit Pinyoanuntapong, Ajinkya Deogade, Paul Streli, Wenjing Zhang, Joanna Materzynska, Pu Wang, Vittorio Ferrari, Jie Shen
- **Qualifying affiliation(s):** Meta — Ajinkya Deogade, Paul Streli, Wenjing Zhang, Joanna Materzynska, Vittorio Ferrari, Jie Shen
- **Categories:** cs.CV
- **Open release:** demo (project page https://exitudio.github.io/interactgesture-page)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** Adds inference-time per-joint spatial control to pretrained co-speech gesture generators through a diffusion sampler and differentiable decoder, with "Progressive Chunk Guidance" that keeps editable staggered chunk latents so constraints propagate across streaming chunk boundaries.
**Purpose (≤3 sentences):** Co-speech gesture generators lack per-joint spatial control (for example pointing at a target) in a streaming setting.
**Breakthrough (≤3 sentences):** On BEAT2 with GestureLSM the authors report FGD 0.431 with Progressive Chunk Guidance versus 0.442 synchronous, and average control error 6.335 cm streaming versus 11.701 cm for a Sequential Chunk Guidance baseline.
**Tools & method (≤3 sentences):** BEAT2 dataset, GestureLSM backbone, 30 FPS in 128-frame chunks with fixed-step DDIM sampling; hardware not disclosed.
**Limitation (≤3 sentences):** The authors state excessive post-sampling optimisation "can diminish naturalness."

## NVIDIA Cosmos-H-Dreams: Real-Time Generative Physics Simulation for Surgical Robotics
- **arXiv:** 2608.24199 · https://arxiv.org/abs/2608.24199
- **Submitted:** 2026-08-25
- **Authors:** Javier Gamazo Tejero, Lukas Zbinden, Keyur Sheth, Raghavendra K M, Nadim Daher, Diego Granero Maraña, Filip Binkiewicz, Patrick Thornycroft, Mahdi Azizian, Sean D. Huver
- **Qualifying affiliation(s):** NVIDIA — Javier Gamazo Tejero, Lukas Zbinden, Keyur Sheth, Raghavendra K M, Nadim Daher, Mahdi Azizian, Sean D. Huver (co-authors at CMR Surgical)
- **Categories:** cs.RO
- **Open release:** weights and code (https://github.com/isaac-for-healthcare/Cosmos-H-Dreams; https://huggingface.co/nvidia/Cosmos-H-Dreams; https://huggingface.co/nvidia/Cosmos-H-Surgical-Simulator)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** A real-time surgical world-model system combining an action-conditioned generative model, a teacher-to-student distillation recipe and a deployment stack on the NVIDIA FlashDreams streaming-inference library, built on Cosmos-H-Surgical-Simulator fine-tuned on the Open-H-Embodiment corpus.
**Purpose (≤3 sentences):** An interactive generative simulator for surgical robotics, since animal and cadaver labs are costly and classical simulators struggle with photorealism and deformable tissue.
**Breakthrough (≤3 sentences):** The authors report the distilled student streams at roughly 160 inference FPS on one NVIDIA RTX PRO 6000 Blackwell GPU and call it "the first interactive surgical world model supporting live human and policy control"; distillation raises FVD from 170.1 to 265.4 and LPIPS from 0.086 to 0.121 relative to the teacher.
**Tools & method (≤3 sentences):** Control via browser keyboard over WebRTC, a Meta Quest over WebXR, CMR Surgical's Versius console and learned policies; Self Forcing distillation to a causal few-step student.
**Limitation (≤3 sentences):** The authors state the real-time regime "carries a measurable fidelity cost," that "scenes with thin, self-interacting structures degrade most," and that the student sometimes hallucinates suture thread geometry where it folds or crosses.

## ReWorld: An Interactive World Model with Long-Horizon Memory
- **arXiv:** 2608.23565 · https://arxiv.org/abs/2608.23565
- **Submitted:** 2026-08-24
- **Authors:** Zhifei Chen, Luozhou Wang, Guibao Shen, Dongyu Yan, Shuai Yang, Tianshuo Xu, Yihua Du, Wei Wang, Tianyi Gui, Lianghua Huang, Yingcong Chen
- **Qualifying affiliation(s):** Alibaba (ATH) — Zhifei Chen (also HKUST(GZ)), Guibao Shen, Wei Wang, Tianyi Gui, Lianghua Huang
- **Categories:** cs.AI
- **Open release:** demo (project page https://zhifeichen097.github.io/ReWorld/)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** ReWorld separates short-horizon control from long-horizon memory during training and bounds both at inference: most attention heads use short windows while a few global heads attend over full history, with a fixed 12-chunk pose-indexed landmark cache to regenerate starting views in minute-long sequences.
**Purpose (≤3 sentences):** To resolve the tension the authors describe as "control wants a short horizon, memory wants an unbounded one," while streaming in real time.
**Breakthrough (≤3 sentences):** The authors report the best rotation error (11.95 degrees) among seven compared methods and the highest mean VBench score (0.850) across seven video-quality dimensions.
**Tools & method (≤3 sentences):** A metric-scale-aligned data engine of 220,724 clips from eight sources (Unreal-rendered fly-throughs, roaming across 79 games, RealEstate10K, DL3DV and others); distribution-matching distillation confined to a LoRA adapter for four-step sampling at 704x1280.
**Limitation (≤3 sentences):** The authors state "memory is still keyed on camera pose alone; extending consolidation to dynamic scenes and richer, non-navigational interaction is the natural next step."

## Object-Uni: A Unified Model for Object-Centric Spatial Understanding and Controllable Generation
- **arXiv:** 2608.22757 · https://arxiv.org/abs/2608.22757
- **Submitted:** 2026-08-24
- **Authors:** Mining Tan, Yinuo Wang, Ziqi Zhou, Weize Quan, Sifei Li, Jingdong Chen, DanDan Zheng, Libin Wang, Weiming Dong
- **Qualifying affiliation(s):** Ant Group — Weiming Dong (corresponding author); FLAG: borderline
- **Categories:** cs.CV, cs.AI
- **Open release:** none
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** Object-Uni unifies object pose perception, spatial reasoning, pose-conditioned generation and object-centric novel-view synthesis by treating object pose as an explicit geometric variable, with a viewpoint-based orientation abstraction so multimodal LLMs can reason about 3D orientation in natural language.
**Purpose (≤3 sentences):** To move unified vision-language models from describing objects to manipulating their spatial state.
**Breakthrough (≤3 sentences):** The authors report azimuth error 22.87 degrees (74.44% AUC@30) versus 29.94 degrees (55.40%) for Orient Anything V2 on KITTI-Cityscapes, and on ImageNet3D generation 74.31 mIoU / 83.40% success versus 66.45 / 68.81% for SceneDesigner.
**Tools & method (≤3 sentences):** The UniSpatial-80K dataset (83,252 images, 91,392 annotated objects, 122 categories) and an "Object-Token-Grounded Pose Anchor"; about 18 hours on 8 NVIDIA H20 GPUs.
**Limitation (≤3 sentences):** The authors state the model "still has limitations in generating fine-grained text and human details," attributed partly to the generative backbone.

## GameXpert-Bench: How Far Are Coding Agents from Expert Game Development?
- **arXiv:** 2608.21833 · https://arxiv.org/abs/2608.21833
- **Submitted:** 2026-08-22
- **Authors:** Kun Chen, Haorong Hong, Peizhong Gao, Jianfeng Lin, Tongxu Luo, Yuxuan Xie, Chenxu Liu, Jieling He, Zhongyuan Liu, Zeno Zeng
- **Qualifying affiliation(s):** Tencent — Yuxuan Xie, Jieling He, Zhongyuan Liu (Lightspeed Studios); Zeno Zeng (Hunyuan Team)
- **Categories:** cs.AI, cs.CL
- **Open release:** none
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** GameXpert-Bench evaluates LLM coding agents on end-to-end game development in three stages: generating a game from a request (97 tasks, 11 genres), diagnosing and fixing injected bugs (100 human-verified tasks) and iterative multi-turn improvement (17 chains), tested by live game interaction and behavioural checks.
**Purpose (≤3 sentences):** To measure how far coding agents are from expert game development, since prior benchmarks neglect bug-fixing and iterative refinement.
**Breakthrough (≤3 sentences):** The authors report Claude-Opus-5 leading GameGen with 79.7/100 (15 models, 1,455 runs; richness averages only 46.1), scoring 39.0/100 on GameFix under strict scoring, and 93.96/100 on GameOpt.
**Tools & method (≤3 sentences):** 50 confidential human-verified game levels with 19 to 27 injected bugs each; 701 acceptance criteria for optimisation; Playwright and headless Chromium runtime verification plus annotation by game-design specialists.
**Limitation (≤3 sentences):** The authors conclude "initial generation quality alone is insufficient to characterize an agent's game development capability," citing gaps in self-discovery, verification, regression control and long-horizon task management.

## Generalized Audio-Driven Synthesis of Precise Drummer Motion
- **arXiv:** 2608.19055 · https://arxiv.org/abs/2608.19055
- **Submitted:** 2026-08-19
- **Authors:** Álvaro G. Iñesta, Mattia Ryffel, Amit H. Bermano, Robert W. Sumner, Martin Guay
- **Qualifying affiliation(s):** Disney Research|Studios — Álvaro G. Iñesta, Mattia Ryffel, Robert W. Sumner, Martin Guay; FLAG: borderline (not on the tracked list)
- **Categories:** cs.CV, cs.GR, cs.SD
- **Open release:** none
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** A diffusion framework that synthesises drumming motion from audio with a dual-objective loss separating body-movement accuracy from stick-tip precision, plus two new metrics, Impact Point Deviation and Percussive Alignment Score; the paper won the Best Paper Award at SCA 2026.
**Purpose (≤3 sentences):** Music-driven character animation where high-acceleration drumming must stay precisely synchronised with audio.
**Breakthrough (≤3 sentences):** The authors report Impact Point Deviation falling from 8.4 cm (rotations-only baseline) to 1.9 cm, a Percussive Alignment Score of 0.82 versus 0.68 (baseline) and 0.91 (ground truth), and 92.8% preference over the baseline in a 22-participant study.
**Tools & method (≤3 sentences):** More than 3.5 hours (1,518,450 frames) of professional drumming captured at 120 Hz on a Roland TD-25KV with nine OptiTrack cameras, augmented to over 25,000 sequences; trained about 48 hours on an NVIDIA RTX 3090.
**Limitation (≤3 sentences):** The authors state the method needs isolated drum audio (polyphonic music requires stem separation) and assumes a fixed drum-kit layout.

## WorldMind: Decoupled Game World Model for State-Aware NPC Behavior
- **arXiv:** 2608.21439 · https://arxiv.org/abs/2608.21439
- **Submitted:** 2026-08-18
- **Authors:** Zhiyang Deng, Boran Zhang, Danze Chen, Yeying Jin
- **Qualifying affiliation(s):** Tencent — all authors (with National University of Singapore; work done during Tencent research internships)
- **Categories:** cs.CV
- **Open release:** demo (project page https://teawhite.cn/worldmind_projectpage/)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** WorldMind is described as the first decoupled framework for state-aware NPC behaviour in game world models, separating interactive world modelling into Understanding, Decision, Control and Generation layers.
**Purpose (≤3 sentences):** To ground NPC behaviour in the evolving game state (boss-player distance, skill cooldowns), which is not achieved when behaviour is implicit in video generation or driven only by external control signals.
**Breakthrough (≤3 sentences):** The authors introduce BOSS-140K, gameplay videos paired with internal game states collected by an automated agent, and report WorldMind preferred over baselines in about 70% of pairwise comparisons for "more tactically appropriate and coherent NPC behavior."
**Tools & method (≤3 sentences):** The Understanding layer reconstructs a compact state from generated frames; the Decision layer uses a general-purpose language model to plan; the Generation layer renders gameplay in real time with a video diffusion model.
**Limitation (≤3 sentences):** The authors state "the Decision Layer shows partial cross-game generalization and remains state-sensitive, whereas compact-state reconstruction requires target-domain adaptation."

## Hydra-0: Action Flow for Generalist World Modeling and Control
- **arXiv:** 2608.18077 · https://arxiv.org/abs/2608.18077
- **Submitted:** 2026-08-18
- **Authors:** Hongyu Li, Bowen Wen, Xinghao Zhu, Yixuan Wang, Yilun Du, Yunzhu Li, George Konidaris, Stan Birchfield, Soha Pouya, Chenran Li, Yan Chang
- **Qualifying affiliation(s):** NVIDIA — Hongyu Li, Bowen Wen, Xinghao Zhu, Yixuan Wang, Yilun Du, Stan Birchfield, Soha Pouya, Chenran Li, Yan Chang
- **Categories:** cs.RO
- **Open release:** demo (project page https://nvidia-isaac.github.io/video_to_data/hydra-0/)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** Hydra-0 is a generalist world model that represents robot actions as "action flow," pixel motion, as a unified interface across robots, tasks and environments, so action consequences are learned once and reused across embodiments.
**Purpose (≤3 sentences):** A world model that generalises across robot morphologies and supports zero-shot composition of skills rather than being tied to one action space.
**Breakthrough (≤3 sentences):** The authors report a Pearson correlation of 0.96 between replayed and reference success rates on their RoboLab benchmark and an "emergent inverse mode" that predicts robot motion from object flow in human demonstrations.
**Tools & method (≤3 sentences):** A Wan2.2 I2V-A14B backbone trained for five days over 40,000 steps on 32 NVIDIA H100 GPUs.
**Limitation (≤3 sentences):** No explicit limitations paragraph was found in the fetched text (observed, not stated).

## SCALE: State-Calibrated Latent Embeddings for JEPA Planning in the Right Geometry
- **arXiv:** 2608.16287 · https://arxiv.org/abs/2608.16287
- **Submitted:** 2026-08-17
- **Authors:** Jiaming Hu, Yan Zheng, Tian Wang, Florian Dubost, Alejandro Mottini, Junze Liu, Arvind Srinivasan, Kai Zhong, Kun Qian, Sharon Gao, Qingjun Cui
- **Qualifying affiliation(s):** Unity Technologies — Yan Zheng, Tian Wang, Florian Dubost, Alejandro Mottini, Junze Liu, Arvind Srinivasan, Kai Zhong, Kun Qian, Sharon Gao, Qingjun Cui (Jiaming Hu as a Unity intern, Boston University)
- **Categories:** cs.LG
- **Open release:** none found
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** Compares two ways to obtain non-collapsed representations in JEPA world models used for planning, inheriting a pretrained feature space (DINO-WM) versus end-to-end training with anti-collapse regularisation (LeWM), and adds SCALE, a training-time regulariser that aligns latent distances with distances in a task-relevant state space.
**Purpose (≤3 sentences):** To give LeWM's end-to-end representation the planning geometry observed in DINO-WM without replacing its encoder.
**Breakthrough (≤3 sentences):** The authors report SCALE improves every one of 15 task-solver combinations (5 tasks, 3 solvers) over baseline LeWM across five compute budgets, and that a control matching SCALE's decodability "yields less consistent planning gains," attributing the benefit to geometry.
**Tools & method (≤3 sentences):** A single lightweight regulariser correlating sampled pairwise latent distances with standardised state distances; no planning-time overhead.
**Limitation (≤3 sentences):** The authors state SCALE requires simulator state during training (image-only at test time), that state selection "acts as a task-dependent inductive bias," and that gains range from modest (Push-T, Reacher) to substantial (Two-Room, PointMaze).

## VibeWorlding: Can Multimodal Agents Construct 3D Open Worlds End-to-End?
- **arXiv:** 2608.15265 · https://arxiv.org/abs/2608.15265
- **Submitted:** 2026-08-15
- **Authors:** Yansong Ning, Jingwen Ye, Zhongkai Wu, Yang Sun, Yiqin Zhu, Xingyi Li, Weidong Zhang, Hao Liu
- **Qualifying affiliation(s):** Tencent (TEG AIPD) — Jingwen Ye, Zhongkai Wu, Yang Sun, Yiqin Zhu, Xingyi Li, Weidong Zhang
- **Categories:** cs.AI
- **Open release:** weights, code and demo (https://github.com/usail-hkust/VibeWorlding-Gym; https://huggingface.co/collections/usail-hkust/vibeworlder; https://huggingface.co/datasets/usail-hkust/VWE-Bench)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** A framework and benchmark testing whether multimodal agents can infer user intent, plan scene layout, invoke 3D tools and reflect on feedback to build 3D open worlds end to end, with VWE-BENCH covering 2,616 3D assets, 323 annotated worlds and 6,828 queries.
**Purpose (≤3 sentences):** To measure and improve autonomous end-to-end 3D world construction rather than single-step asset generation.
**Breakthrough (≤3 sentences):** The authors report GPT-5.5 and Qwen3.8-Max both below 60% success on their rubric-based verifier, and that their RL-trained open VibeWorlder-30B-A3B outperforms the closed models tested.
**Tools & method (≤3 sentences):** VibeWorlding-Gym with a dual-constraint rubric verifier, an asset-retrieval embedding model and a unified post-training framework; 8 NVIDIA H20 GPUs for 8B models and three nodes for the 30B-A3B model.
**Limitation (≤3 sentences):** No explicit limitations paragraph was found in the fetched text (observed, not stated).

## SCOPE: Score-Isolated Agentic Optimization for Video World Models
- **arXiv:** 2608.15043 · https://arxiv.org/abs/2608.15043
- **Submitted:** 2026-08-15
- **Authors:** Yuhua Jiang, Jiaming Wang, Qingbin Liu, Feifei Gao
- **Qualifying affiliation(s):** Tencent — Qingbin Liu
- **Categories:** cs.AI
- **Open release:** code (https://github.com/YuhuaJiang2002/SCOPE)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** SCOPE is a framework for auditable inference-time adaptation of frozen video world models used as planning simulators, representing prompts, samplers, verifiers and selectors as a typed state updated only through bounded evidence-supported changes before freezing for held-out evaluation.
**Purpose (≤3 sentences):** To close the "inference-control evaluation gap" so that reported gains from agentic optimisation are trustworthy.
**Breakthrough (≤3 sentences):** On Physics-IQ the authors report +14.24 points over the frozen base on Wan2.2 (95% CI +8.10 to +21.23) and +12.60 on CogVideoX, while the margin over the strongest matched agentic baseline (+2.07 on Wan) "remains statistically unresolved."
**Tools & method (≤3 sentences):** Physics-IQ, PAI-Bench-G (judged by Qwen2.5-VL-72B), OpenS2V-Eval, PhyGround and PhyT2V on Wan2.2 and CogVideoX backbones.
**Limitation (≤3 sentences):** The authors state "strong candidate proposals do not necessarily imply reliable deployment decisions," that effectiveness "is not fully invariant across backbones or metrics," and that further progress needs calibrated uncertainty and selectors that generalise under shift.

## ForgeWM: Progressive Causal Training for Few-Step Action-Conditioned Video World Models
- **arXiv:** 2608.14022 · https://arxiv.org/abs/2608.14022
- **Submitted:** 2026-08-14
- **Authors:** Xinye Li, Lingshuai Lin, Lei Wang, Liuzhou Zhang, Jialin Cui, Qingshan Li, Guanchu Wang, Qingbin Liu, Xi Chen, Jiang Bian, Wai Lam
- **Qualifying affiliation(s):** Tencent PCG — Lingshuai Lin, Qingbin Liu, Jiang Bian
- **Categories:** cs.CV, cs.AI
- **Open release:** none
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** ForgeWM converts bidirectional action-conditioned video generators into few-step (1, 2 or 4 step) causal world models for low-latency game-native control through four-stage progressive training, with an optional post-hoc "replay" refinement pass.
**Purpose (≤3 sentences):** Interactive, game-like applications that need low-latency causal generation with reliable response to discrete and continuous controls.
**Breakthrough (≤3 sentences):** The authors report the best results on 6 of 7 quality and control metrics against Matrix-Game 2.0 and HY-WorldPlay (ForgeWM-2: LPIPS 0.6171, mouse accuracy 0.8268 at 50.31 FPS and 239.7 ms latency) and a 60.7% pooled preference for ForgeWM-4 in a 41-participant study.
**Tools & method (≤3 sentences):** 40,000 clips from GF-Minecraft (352x640) and 65,246 clips across seven games for cross-game evaluation; eight GPUs with bf16 and fully sharded data parallelism.
**Limitation (≤3 sentences):** The authors identify long-horizon drift with visible artefacts beyond a 77-frame window, motion over-response (1.45x flow-magnitude ratio on FPS games), and a metric-dependent effect where a later stage raises sharpness but not paired reconstruction fidelity.

# Near-misses (batch 2b)
- 2608.19527 · Does Listening Matter? Backchanneling and Nodding in AI Clone (Sony CSL) · off-topic on reading (HCI user study of a conversational voice clone; no animation or graphics method)
- 2609.04250 · Motion-Omni: End-to-End Joint Speech and Full-Body Motion for Spoken Dialogue · affiliation "LIGHTSPEED" could not be confirmed as a tracked company from the paper (see GameWAM flag)
- 2608.21424 · EditStream (Adobe) · off-topic on reading (generic interactive video generation and editing)
- 2608.15763 · TaoLive Digital Avatar Agent Technical Report (Alibaba) · off-topic on reading (LLM agent-harness training for a livestream chat agent)
- 2608.11216 · AutoWorldModel-Bench · out of window (v1 2026-07-20)
- 2608.13552 · PlayWorld · out of window (v1 2026-08-13)
- 2608.13602 · Omni-LiveAvatar · out of window (v1 2026-08-07)
- 2608.14125 · Traj-LeWM · academic-only
- 2608.29904 · Off-Manifold Refinement · academic-only (Fulbright University Vietnam, UCLA)
- 2608.25572 · ConfAL-WM · academic-only (Tsinghua)
- 2608.22187 · BehaviorWorldGen · affiliation unverifiable ("AFARI World Model Team" only)
- 2608.21075 · AudioWorldSim · academic-only (IMPA)
- 2608.18484 · Partition the Support, Reconstruct the Residual · academic-only (Texas A&M)
- 2608.17542 · No Gaussian Required (Quantexa) · non-qualifying company
