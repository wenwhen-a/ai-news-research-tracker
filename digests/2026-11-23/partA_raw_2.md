## Coda-DaVinci: Reimagining Video Generation with Code2Video
- **arXiv:** 2611.26595 · https://arxiv.org/abs/2611.26595
- **Submitted:** 2026-11-19
- **Authors:** Yiyan Ji, Qixun Wang, Yang Shi, Zhuoran Zhang, Yifan Xu, Tengfei Liu, Yuqi Tang, Xiaohan Zhang, Shujie Li, Jiafu Tang, Xuanyu Zhu, Xinyu Liu, Yan He, Yushuo Guan, Zihao Wang, Xianghua Ying, Shixuan Liu, Haotian Wang, Wenjing Yang, Zhaoxiang Zhang, Yuanxing Zhang, Pengfei Wan, Jiaheng Liu
- **Qualifying affiliation(s):** Kuaishou — KlingAI Research (Qixun Wang, Yang Shi, Yushuo Guan, Zihao Wang, Yuanxing Zhang, Pengfei Wan); KlingAI Research is Kuaishou's generative-video research group. Remaining authors are at Nanjing University, Peking University, HKUST, University of Hong Kong, Tsinghua University.
- **Categories:** cs.CV
- **Open release:** none

**Summary (≤3 sentences):** Code2Video uses agent-authored 3D proxies to guide video generation; this paper studies how proxy granularity, physics simulation, and prompting affect downstream quality via controlled experiments and blinded human evaluation, then introduces Coda-DaVinci, a task-adaptive agentic framework that selects between proxy-guided and direct generation. A multi-agent harness preserves scene assets and guides repairs through visual inspection and independent review.
**Purpose (≤3 sentences):** To understand how 3D-proxy construction and prompting choices affect downstream video-generation quality in the Code2Video paradigm, and to build a framework that adapts proxy granularity and generation strategy per entity.
**Breakthrough (≤3 sentences):** The authors report leading instruction-following on VTR and scene consistency on R2M, improved physical plausibility over direct generation, and higher visual realism than the compared Code2Video baselines; long-video evaluations show gains in event structure and consistency across successive interactions.
**Tools & method (≤3 sentences):** The framework selects between proxy-guided and direct generation, adapts modeling granularity per entity, and coordinates physics simulation with proxy-grounded prompting; a multi-agent harness handles repairs via visual inspection and independent review, evaluated on VTR, R2M, and long-video benchmarks.
**Limitation (≤3 sentences):** The authors state the long-video, multi-turn evaluations reveal limitations in transition stability and adherence to scene settings.

---

## Plan4D: Generative Plannable 4D Worlds
- **arXiv:** 2611.26516 · https://arxiv.org/abs/2611.26516
- **Submitted:** 2026-11-19
- **Authors:** Hangwei Zhang, Rujing Dang, Ruimin Lin, Jiahong Wu, Xiangxiang Chu, Chuanxia Zheng
- **Qualifying affiliation(s):** Alibaba — AMAP, Alibaba Group (all six authors, per the paper's author block)
- **Categories:** cs.CV
- **Open release:** none (project page only: https://fogradio.github.io/plan4d-project)

**Summary (≤3 sentences):** Plan4D is a generative plannable 4D world model that predicts future RGB video together with dense 4D geometry (depth, cameras, point clouds, scene flow) from an observed scene and text-specified actions. It uses a model-stitching architecture that couples Depth Anything 3 with LongCat-Video and adds an auxiliary DPT head for scene-flow prediction.
**Purpose (≤3 sentences):** To add explicit 4D modeling to video-based world models, which the authors say otherwise offer weak physical grounding and limited geometric consistency, given that training data with paired actions and dense 4D annotations is scarce.
**Breakthrough (≤3 sentences):** The authors report state-of-the-art performance in generative 4D modeling of environmental reactions on both synthetic and real-world datasets, with improved visual fidelity and geometric accuracy for long-horizon, fine-grained action planning in dynamic 3D scenes.
**Tools & method (≤3 sentences):** Plan4D stitches a pretrained 3D reconstructor (Depth Anything 3) with a pretrained video generator (LongCat-Video) and augments it with an auxiliary DPT head for scene-flow prediction, leveraging each model's priors rather than training from scratch on scarce paired data.
**Limitation (≤3 sentences):** (observed, not stated) The abstract does not describe specific failure modes beyond motivating the data-scarcity problem that the model-stitching design addresses.

---

## ViDecide: Teaching Video Diffusion Models to Reason and Plan Step by Step
- **arXiv:** 2611.26389 · https://arxiv.org/abs/2611.26389
- **Submitted:** 2026-11-19
- **Authors:** Kaiwen Zhang, Yiming Gao, Zeqi Xiao, Xintao Wang, Pengfei Wan, Kun Gai, Xingang Pan
- **Qualifying affiliation(s):** Kuaishou — KlingAI Research (Yiming Gao, Pengfei Wan, Kun Gai). Remaining authors are at NTU S-Lab and CUHK.
- **Categories:** cs.CV
- **Open release:** none (project page only: https://kevin-thu.github.io/ViDecide)

**Summary (≤3 sentences):** ViDecide is a decision-centric framework that trains video diffusion models to predict state transitions causally and decide when to stop, using a decision-focused training schedule instead of treating a generation as one fixed-length clip. It adds Corrective Fine-tuning (CFT), which corrects failed decisions by mapping their noise to the model's own successful continuations.
**Purpose (≤3 sentences):** To address current video generation models' frequent violation of physical and logical constraints in multi-step reasoning and planning, which the authors say persists even after large-scale reasoning-data training or existing diffusion RL methods.
**Breakthrough (≤3 sentences):** The authors report an average strict success rate of 83.8% across abstract games, planning tasks, and a new multi-step robot-planning benchmark, versus 23.3% for standard fine-tuning and 67.8% for the strongest prior method, with generalization to larger puzzles and unseen layouts.
**Tools & method (≤3 sentences):** CFT achieves stable improvement without policy-gradient optimization by mapping noise from failed decisions to the model's own successful continuations; evaluated on abstract games, planning tasks, and a new multi-step robot-planning benchmark.
**Limitation (≤3 sentences):** (observed, not stated) The abstract does not state explicit failure modes beyond framing the work against prior fixed-length-clip training and RL baselines.

---

## SpecWM: Turning Verification into Refinement for Streaming World Models
- **arXiv:** 2611.26211 · https://arxiv.org/abs/2611.26211
- **Submitted:** 2026-11-19
- **Authors:** Jiaming Li, Lingzhen Li, Xiaze Yang, Chenyu Zhu, Kaiqi Liu, Xiaotong Zhao, Songlian Li, Toyota Li, Alan Zhao, Haobin Zhong, Yue Ma, Zhiyuan Ma
- **Qualifying affiliation(s):** Tencent (Xiaotong Zhao, Songlian Li, Toyota Li, Alan Zhao, Haobin Zhong; Jiaming Li also lists Tencent alongside Huazhong University of Science and Technology). Other authors are at HUST, Peking University, and HKUST.
- **Categories:** cs.CV
- **Open release:** none

**Summary (≤3 sentences):** SpecWM (Speculative World Model) is a training-free inference framework for streaming world models that verifies draft chunks from a fast model against the target model's latent velocity field, then applies two thresholds to Accept, Refine, or Reject each draft. The verification signal is itself reused as a correction rather than requiring costly target regeneration.
**Purpose (≤3 sentences):** To overcome limits of existing speculative streaming-world-model methods, whose verification covers only an external scorer's evaluation dimensions, adds decoding/scoring cost, and provides no correction for rejected drafts.
**Breakthrough (≤3 sentences):** On WBench Navigation, the authors report SpecWM improves visual quality at a 1.63× speedup over the target model and raises NavScore from the draft's 75.99 to 85.63, achieving the best quality–speed–control trade-off they measured; a new LongSpecBench shows sustained quality and control over long, multi-turn rollouts.
**Tools & method (≤3 sentences):** One-step refinement reuses the verification signal to improve perceptual quality, while three-step refinement strengthens camera following and trajectory consistency; evaluated on WBench Navigation, the new LongSpecBench, and Hy-Nomas across backbones and denoising budgets.
**Limitation (≤3 sentences):** (observed, not stated) The abstract does not state explicit limitations beyond motivating transition-aware refinement as a response to prior methods' shortcomings.

---

## Streaming-AAA: Streaming AAA Game Video Generation at High Resolution, High Frame Rate, and Low Latency
- **arXiv:** 2611.26040 · https://arxiv.org/abs/2611.26040
- **Submitted:** 2026-11-19
- **Authors:** Zhihao Hu, Jianqi Ma, Jun Zhang, Jiayang Bai, Haifeng Shi, Yanxiang Zhuang, Zhongqian Sun, Weidong Zhang, Wei Yang
- **Qualifying affiliation(s):** Tencent — Tencent AIPD (listed as the affiliation for the full author group on the paper). Note: "NVIDIA" in the lead's company-match is a false positive — it refers only to the NVIDIA A800 GPUs used as hardware, not an author affiliation.
- **Categories:** cs.CV
- **Open release:** none

**Summary (≤3 sentences):** Streaming-AAA is a paradigm for controllable, infinite generation of AAA-quality game video, built on a redesigned VAE for efficient high-resolution decoding, diffusion-forcing pretraining with an extended temporal training horizon, and post-training distillation plus memory compression for inference efficiency. The authors report the system generates 1080p gameplay video at 43 FPS with 198 ms end-to-end interaction latency.
**Purpose (≤3 sentences):** To close the gap between existing controllable streaming video-generation methods and practical gameplay, which the authors say have failed to jointly achieve high visual fidelity, high frame rate, and low interaction latency.
**Breakthrough (≤3 sentences):** The authors report 1080p gameplay generation at 43 FPS with 198 ms end-to-end latency on NVIDIA A800 GPUs, supporting long-horizon play without severe temporal degradation or collapse, and substantial improvements in visual fidelity, frame rate, latency, and long-term stability over prior controllable video-generation approaches.
**Tools & method (≤3 sentences):** A redesigned VAE architecture enables real-time 1080p decoding; the diffusion model is pretrained with diffusion forcing over a significantly extended temporal horizon for long-term dependencies and persistent memory; post-training distillation and memory compression improve inference efficiency. Hardware: NVIDIA A800 GPUs.
**Limitation (≤3 sentences):** (observed, not stated) The abstract does not detail specific failure cases beyond the temporal-degradation/collapse risk in long-horizon play that the method is designed to mitigate.

---

## PRIO: Pre-trained Representation for Interactive Objects in 4D Worlds
- **arXiv:** 2611.25500 · https://arxiv.org/abs/2611.25500
- **Submitted:** 2026-11-19
- **Authors:** Shixun Huang, Lifu Wei, Yue Chang, Chen Geng, Heng Zhang, Jinhyung Ahn, Caoliwen Wang, Siyuan Chen, Donglai Xiang, Jiajun Wu, Peter Yichen Chen
- **Qualifying affiliation(s):** NVIDIA — Donglai Xiang. Remaining authors are at University of British Columbia, University of Toronto, Stanford University, and Yonsei University.
- **Categories:** cs.CV
- **Open release:** none

**Summary (≤3 sentences):** PRIO is a pre-trained representation for interactive objects that, given static geometry, predicts an object-specific configuration space in a single forward pass, providing generalized coordinates for Lagrangian mechanics so physical laws and user actions govern motion. Because configurations are linear in these coordinates, the quantities needed for dynamics are precomputed and run at interactive rates without further network inference.
**Purpose (≤3 sentences):** To let objects in reconstructed or generated 3D/4D scenes move, deform, and respond physically to user actions in real time, which the authors say static captured or generated geometry currently cannot do.
**Breakthrough (≤3 sentences):** The authors report that, pre-trained on diverse 4D trajectories, PRIO generalizes to unseen shapes and, compared with existing 4D generation methods, generates dynamics faster and follows user actions more faithfully; they demonstrate its use in real-to-sim workflows and robot manipulation.
**Tools & method (≤3 sentences):** PRIO supports meshes, point clouds, and 3D Gaussians as input geometry; dynamics quantities are precomputed from the predicted linear configuration space and run at interactive rates without further network inference at runtime.
**Limitation (≤3 sentences):** (observed, not stated) The abstract does not state explicit failure modes or scope limits beyond its general generalization claim.

---

## SceneAnything: Agentic Reconstruction of Large-Scale Mesh Scenes from a Single Video
- **arXiv:** 2611.25340 · https://arxiv.org/abs/2611.25340
- **Submitted:** 2026-11-19
- **Authors:** Bowen Xue, Saeed Hadadan, Fabrice Rousselle, Zahra Montazeri, Ravi Ramamoorthi, Milos Hasan
- **Qualifying affiliation(s):** NVIDIA — Bowen Xue, Saeed Hadadan, Fabrice Rousselle, Ravi Ramamoorthi (also University of California, San Diego), Milos Hasan. Zahra Montazeri is at University of Manchester.
- **Categories:** cs.CV, cs.GR
- **Open release:** code (the authors state: "We will release the harness, agent instructions, reusable libraries, and scenes.")

**Summary (≤3 sentences):** SceneAnything is an automated system that reconstructs editable mesh scenes from real and generated video, coordinating agents, pretrained vision models, and graphics tools through an explicit reconstruction protocol; a scene-owner agent plans the environment and briefs author agents who write parameterized Blender programs. Shared camera, depth, and segmentation estimates ground component construction, and a visibility/fit-based level-of-detail rule selects construction level while unseen regions are completed and marked as inferred.
**Purpose (≤3 sentences):** To reconstruct editable 3D scenes from video that both match visible structure and plausibly complete unseen surfaces — including text-to-scene construction when paired with video generation — addressing the layout, scale, and lighting errors the authors say direct agent-reconstruction attempts produce.
**Breakthrough (≤3 sentences):** The authors report, from an evaluation on 100 scenes, improved original-view fidelity over direct-agent reconstruction and higher novel-view content similarity than the compared video-to-3D methods.
**Tools & method (≤3 sentences):** A software harness coordinates agents that write parameterized Blender programs using shared camera/depth/segmentation estimates; assembled scenes use fitted lighting and supported motion, with revisions undergoing programmatic checks and independent visual comparisons, and accepted programs/lessons reused across scenes.
**Limitation (≤3 sentences):** (observed, not stated) The abstract does not state explicit failure modes beyond noting that unseen regions must be completed and are marked as inferred rather than observed.

---

## VideoRNG: Relightable Neural Gaussians from Generative Video Models
- **arXiv:** 2611.25338 · https://arxiv.org/abs/2611.25338
- **Submitted:** 2026-11-19
- **Authors:** Bowen Xue, Saeed Hadadan, Fabrice Rousselle, Ravi Ramamoorthi, Zahra Montazeri, Miloš Hašan
- **Qualifying affiliation(s):** NVIDIA — Bowen Xue, Saeed Hadadan, Fabrice Rousselle, Miloš Hašan. Ravi Ramamoorthi is also at University of California, San Diego; Zahra Montazeri is also at University of Manchester.
- **Categories:** cs.CV, cs.GR
- **Open release:** none

**Summary (≤3 sentences):** VideoRNG generates complete, relightable 3D assets from a text prompt or single image, without prescribing a mesh or analytic material model, using a video generator (fine-tuned from a pretrained video-diffusion backbone) that produces a structured RGBA turntable sequence, followed by a feed-forward reconstruction model mapping selected turntable frames to millions of anisotropic Gaussians with learned neural appearance features. A shared directional decoder and stochastic Gaussian ray tracer turn this "ray-traced Relightable Neural Gaussians" (rtRNG) representation into radiance under novel viewpoints and illumination.
**Purpose (≤3 sentences):** To overcome limits of classical 3D-asset representations (surface meshes, compact PBR materials) and existing Gaussian-splatting generators that bake fixed illumination into appearance, for objects whose look arises from fine geometry or complex light transport.
**Breakthrough (≤3 sentences):** The authors report that VideoRNG generates complex assets such as fur, feathers, and spider webs — appearance categories classical representations struggle to express — that can be interactively rendered, relit, and integrated into scenes.
**Tools & method (≤3 sentences):** Depth-anchored appearance training preserves high-frequency appearance while learning geometry; foreground token selection and cost-aware distributed sampling make million-Gaussian reconstruction practical; both stages initialize from a pretrained video-diffusion backbone.
**Limitation (≤3 sentences):** (observed, not stated) The abstract does not state explicit failure modes or acknowledged limitations.

---

## WEVO: World Model-Enabled VLA Optimization for Whole-Body Loco-Manipulation
- **arXiv:** 2611.25251 · https://arxiv.org/abs/2611.25251
- **Submitted:** 2026-11-18
- **Authors:** Qianzhong Chen, Muyuan Lin, Yuyin Sun, Mac Schwager, Cheng-Hao Kuo, Roberto Martín-Martín
- **Qualifying affiliation(s):** Amazon — listed in the paper's affiliation block alongside Stanford University and University of Texas at Austin; the HTML does not map individual authors to institutions, but a footnote confirms "work done during an internship at Amazon."
- **Categories:** cs.RO
- **Open release:** none (project website only: https://qianzhong-chen.github.io/wevo.github.io/)

**Summary (≤3 sentences):** WEVO is a teleoperation-free framework for post-training a whole-body humanoid VLA policy inside an action-conditioned video world model. Simulated manipulation/locomotion play data first improves the world model's contact-dynamics and viewpoint-change prediction; a VLA trained on synthetic demonstrations then collects 20 autonomous real-robot rollouts per task to align the world model with deployment observations, after which the VLA, a whole-body controller, and the video world model form a closed-loop RL environment with dense progress rewards.
**Purpose (≤3 sentences):** To improve humanoid VLA policies beyond imitation learning via reinforcement learning, without the safety risks of real-world humanoid exploration or the sim-to-real exploitation risk of simulator-only RL.
**Breakthrough (≤3 sentences):** Across three real robot tasks, the authors report that play data improves every evaluated world-model metric and downstream policy success, and that video-world-model RL raises mean success from 23.3% to 75.0%, compared with 48.3% for real-robot RL.
**Tools & method (≤3 sentences):** The closed-loop RL environment combines a VLA, a whole-body controller (WBC), and a video world model with dense progress rewards; the world model is aligned to deployment observations using 20 autonomous real-robot rollouts per task, collected by a VLA trained on synthetic demonstrations.
**Limitation (≤3 sentences):** (observed, not stated) The abstract does not state explicit limitations beyond motivating the approach against unsafe humanoid exploration and sim-to-real gaps.

# Near-misses
- 2611.26493 · SGAR: Feed-Forward 3D Reconstruction via Sparse Geometry-Guided Attention · academic only (all five authors at CVLab, EPFL, Switzerland), no industry co-author despite the "NVIDIA" company-match lead.
- 2611.26334 · Online Temporal Rotations for 2 Bit KV-Cache Quantization in Video Diffusion Transformers · academic only (all three authors at the MIT Operations Research Center), no industry co-author despite the "Tencent" company-match lead (likely triggered because the paper benchmarks against Tencent-associated models such as HY-WorldPlay-8B, not by an author affiliation).
- 2611.25847 · TrajCal: Trajectory-Calibrated Time Schedules for Few-Step Flow Sampling · off-topic on closer read: a generic sampling-schedule calibration method for flow-matching image/video generation, with no 3D, world-model, character-animation, or game-engine content (Alibaba Group affiliation is confirmed for at least two authors, but the topic gate fails independent of the company gate).
