## State World Models: Execute the Rules, Generate the Pixels
- **arXiv:** 2610.26811 · https://arxiv.org/abs/2610.26811
- **Submitted:** 2026-10-19
- **Authors:** Chan Yan Ki, Yanran Zhang, Wenzhao Zheng, Xiaofeng Wang, Zheng Zhu, Lei Chen, Jie Zhou, Jiwen Lu
- **Qualifying affiliation(s):** GigaAI (co-affiliation alongside Dept. of Automation, Tsinghua University); FLAG: borderline
- **Categories:** cs.CV
- **Open release:** none
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper introduces a "Stateful Harness" that separates world-state evolution from video rendering so that identical visible actions produce outcomes consistent with hidden state and explicit rules, plus WorldState-Bench, a set of 50 counterfactual pairs sharing a first frame and action but differing in hidden state (49 hidden variables, 21 themes). On WorldState-Bench, the best unwrapped video backend reaches 32% PairFollow under rule-only prompting, while the same frozen video weights (MiniMax-H3) reach 92% inside the full harness.
**Purpose (≤3 sentences):** To test and support "state world models," where the same visible action should yield different outcomes depending on hidden state, evaluated against rules specified up front rather than left to the video model to infer.
**Breakthrough (≤3 sentences):** The authors report that wrapping a frozen, unmodified video model in their rule-resolution runtime raises PairFollow from 32% to 92%, i.e. no engine integration or model fine-tuning is required to make video generation obey hidden-state rules. They also report human blind-preference tests and an external comparison against "WBench" supporting the harness's gains.
**Tools & method (≤3 sentences):** The runtime resolves each user action against a semantic ledger and an editable 3D scene using fixed rules, compiles the resolved event into a text instruction plus a 3D-scene preview clip for spatial guidance, and has a frozen video model render it while a VLM (Qwen3.8-27B-VL) updates state for the next turn. First frames were generated with FLUX.2; eleven existing video backends were evaluated; generation/judging ran on eight A800 80GB GPUs.
**Limitation (≤3 sentences):** The authors state that rendering remains stochastic and zone-triggered state cases are the most demanding for the harness. Judging relies on a VLM judge, validated only against a human-audited subset, and unclear clips receive no credit.

---

## Mise-en-Video: Fine-Grained 3D Control for Multi-Shot Video Generation
- **arXiv:** 2610.26801 · https://arxiv.org/abs/2610.26801
- **Submitted:** 2026-10-19
- **Authors:** Yingshuang Zou, Xiaoyu Shi, Yawen Luo, Ziang Li, Qinghe Wang, Mengfei Li, Chengfeng Zhao, Xintao Wang, Pengfei Wan, Kun Gai, Yuan Liu
- **Qualifying affiliation(s):** Kuaishou — KlingAI Research (Xintao Wang, Pengfei Wan, Kun Gai)
- **Categories:** cs.CV, cs.AI
- **Open release:** none (a 160K-video dataset is described but no release link was found on the abstract page)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** Mise-en-Video (MeV) is a framework for multi-shot video generation in which creators stage each shot in 3D before generation, combining hierarchical attention for cross-shot narrative consistency with 3D-aware layout guidance for per-shot spatial control. The authors also built a 160K-video dataset (2–6 shots, up to 250 frames each) with hierarchical captions and oriented 3D bounding boxes.
**Purpose (≤3 sentences):** To give creators fine-grained control over subject placement, orientation, and motion within and across shots of a multi-shot video while preserving consistency across shots.
**Breakthrough (≤3 sentences):** The authors report better video quality, inter-shot consistency, and subject-level control than baselines including MultiShotMaster and EchoShot, evaluated on 100 multi-shot prompts generated with Gemini 2.5.
**Tools & method (≤3 sentences):** Subject Layout Guidance encodes subjects as oriented 3D boxes with a NOCS-based color scheme, projects them into per-frame 2D layout maps, and injects them via a ControlNet-style branch; Hierarchical Context Attention splits text into global/shot/subject levels with masked attention. The data pipeline detects shots in web videos, tracks/reconstructs subjects in 3D, and captions with Gemini; training used a roughly 1B-parameter backbone on 32 GPUs.
**Limitation (≤3 sentences):** The authors state that overall generation quality is capped by the pretrained backbone's relatively small parameter count, limiting performance on high-quality dynamic videos, and they plan to use larger backbones and/or larger controllable modules.

---

## Simulation Priors for Rapid Adaptation in Model-Based RL for Autonomous Racing
- **arXiv:** 2610.26757 · https://arxiv.org/abs/2610.26757
- **Submitted:** 2026-10-19
- **Authors:** Adrian Remonda, Jiajun Xi, Nicklas Hansen, Marcus Greiff, Thomas Lew, John Talbot, John Subosits, Xiaolong Wang
- **Qualifying affiliation(s):** Toyota Research Institute (Los Altos, CA); FLAG: borderline
- **Categories:** cs.LG, cs.RO, eess.SY
- **Open release:** none (authors state they release code and datasets, but no link was located)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper proposes Prior-Informed Adaptation (PIA), an offline-to-online model-based RL framework for autonomous racing that pretrains a world model on low- and high-fidelity simulated trajectories, then adapts it online with limited real interaction. It is evaluated in high-fidelity simulation and on a full-size autonomous race car.
**Purpose (≤3 sentences):** To address the high cost and risk of RL data collection in settings like racing, enabling quick adaptation to new tracks/surfaces without requiring an exact simulator.
**Breakthrough (≤3 sentences):** The authors report that treating simulated trajectories as biased priors — rather than as an environment for direct policy transfer — combined with a mixed sim/target replay buffer and uncertainty-regularized latent planning (Q-ensemble disagreement) enables adaptation validated on a real full-size race car (the F317).
**Tools & method (≤3 sentences):** Assetto Corsa Gym (ACGym), a high-fidelity racing simulator, plus a lightweight low-fidelity ODE vehicle model sharing ACGym's interface; the authors report a released dataset covering 15 tracks and more than 740 hours of Assetto Corsa driving data, with simulation experiments on 9 tracks.
**Limitation (≤3 sentences):** The authors state PIA requires a model/simulator sharing the target's observation-action interface, making image- or LiDAR-heavy inputs harder to use, and that experiments focus on dynamics mismatch rather than strong exogenous randomness (e.g. opponent vehicles). The real-car study covers only one track/surface, and early deployments can fail when the real-data anchor is too small.

---

## PVBench: Quantifying Physical Plausibility in Video Generation with Object-Level Physical Measurements
- **arXiv:** 2610.26711 · https://arxiv.org/abs/2610.26711
- **Submitted:** 2026-10-19
- **Authors:** Kaiwei Chen, Moran Li, Zhenye Gan, Yabiao Wang, Chengjie Wang, Kexin Zhang, Yong Liu, Jiangning Zhang
- **Qualifying affiliation(s):** Tencent — Tencent Youtu Lab
- **Categories:** cs.CV
- **Open release:** none (authors state intent to release the benchmark, prompts, and calibration protocol, but no link was found)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** PVBench scores the physical plausibility of generated videos across 46 dimensions spanning seven domains, using 600 paired text-to-video/image-to-video prompt groups (30% involving embodied agents such as robot arms and humanoids). Specialized vision models produce measurements such as 6D pose, metric scale, surface normals, kinematics, and conservation-law residuals, mapped to 1–5 scores and validated against human judgments.
**Purpose (≤3 sentences):** To move evaluation of video generation from semantic impressions toward computable physical quantities checked against physical laws, moving video generation from "looking good" to "physically usable" as the authors put it.
**Breakthrough (≤3 sentences):** The authors evaluate six T2V/I2V model configurations (~7,200 videos total), including MiniMax H3, SANA-Video 2.0, Wan2.1, Wan2.2, Seedance 2.5, and LingBot-Video, reporting the protocol's physical scores track human judgment while most benchmark dimensions remain unresolved by current generators.
**Tools & method (≤3 sentences):** Paired T2V/I2V prompt groups were drafted with GPT-5.6 and screened by humans; reference images were made with GPT-image-2; a multimodal LLM scores only dimensions that are hard to quantify numerically (materials, phase change). Evaluation ran on a single H20 GPU with 10 annotators per human-validation sample.
**Limitation (≤3 sentences):** The authors note results depend on specialized vision models and that unobservable cases are skipped; material and phase-change dimensions still rely on MLLM scoring rather than measurement, and most dimensions lack ground-truth references.

---

## PrismWAM: Decoupling State Representations in World Action Models
- **arXiv:** 2610.26564 · https://arxiv.org/abs/2610.26564
- **Submitted:** 2026-10-19
- **Authors:** Tianyu Xin, Wanqi Zhong, Bowen Hu, Zhangchi Guo, Lijie Wang, Yiming Wang, Haoran Liao, Heyang Yu, Xiaoyu Tian, Zhiding Yu, Yiming Li
- **Qualifying affiliation(s):** NVIDIA (co-affiliation alongside Tsinghua University)
- **Categories:** cs.CV
- **Open release:** demo — project page https://prism-wam.github.io/
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** PrismWAM argues that the video latents used by World Action Models (WAMs) conflate appearance (texture, color) with physical configuration (occupancy, pose), which is a poor state representation for action. It splits the task into semantic planning, physical rollout in depth space, and action generation, built on a pretrained video backbone (Wan).
**Purpose (≤3 sentences):** To determine what the internal "state" of a world-action model should be, and to argue it should separate how the world looks from how it physically changes under action.
**Breakthrough (≤3 sentences):** The authors report strong performance in both simulation and the real world without any embodied action pretraining, using sparse RGB goal supervision combined with dense depth supervision and a "chain attention" mask controlling information flow between an RGB planning stream and a depth rollout stream.
**Tools & method (≤3 sentences):** A Mixture-of-Transformers architecture (main model ~6B parameters, PrismWAM* variant 15B) with depth-VAE pretraining on ~2,300 hours of depth data from AgiBotWorld-Beta plus simulated RoboTwin depth; evaluated on RoboTwin 2.0, LIBERO/LIBERO-Plus/LIBERO-Pro, and RoboDojo, and on real single/dual-arm Piper-X robots with Orbbec Gemini 335 RGB-D cameras.
**Limitation (≤3 sentences):** The authors state that large-scale real-world manipulation data with synchronized depth remains limited, constraining how much depth pretraining is currently possible, though they expect this to improve as depth sensing becomes more accessible.

---

## PhysSkin++: Real-Time and Generalizable Physics-Based Animation via Self-Supervised Neural Skinning
- **arXiv:** 2610.26067 · https://arxiv.org/abs/2610.26067
- **Submitted:** 2026-10-19
- **Authors:** Yuanhang Lei, Baofei Liu, Xingxuan Li, Tao Cheng, Zixuan Wang, Boming Zhao, Yujun Shen, Siyuan Huang, Ruizhen Hu, Peter Yichen Chen, Hujun Bao, Zhaopeng Cui
- **Qualifying affiliation(s):** Ant Group — Yujun Shen; FLAG: borderline
- **Categories:** cs.CV (cross-listed cs.GR)
- **Open release:** demo — project page https://zju3dv.github.io/PhysSkin_plus/
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** PhysSkin++ is a physics-informed framework that learns continuous neural skinning fields from static 3D geometry to build compact deformation subspaces for real-time, generalizable physics-based animation, supporting meshes, point clouds, and 3D Gaussians as well as rig-complementary animation. It extends the authors' earlier conference paper, PhysSkin.
**Purpose (≤3 sentences):** To generalize real-time physics-based animation across different 3D shapes and spatial discretizations without relying on simulation trajectories or annotated skinning data.
**Breakthrough (≤3 sentences):** The authors introduce a rig-complementarity loss that lets the model learn physically-grounded elastic responses on top of artist-authored rig animation, and report supporting controllable, collision-aware animation with Dirichlet boundary conditions, user dragging, gravity, floor contact, and rigid/deformable multi-object contact.
**Tools & method (≤3 sentences):** A Neural Skinning Fields Autoencoder (transformer shape encoder + cross-attention decoder) is trained with a self-supervised strategy (PISSL) combining potential-energy, smoothness, and orthogonality losses with conflict-aware gradient correction (ConFIG). Evaluation uses ShapeNet, RigNet, a deformable Lego family from Mani-GS, ShapeSplat (3D Gaussians), and Mixamo sequences retargeted with Auto-Rig Pro, trained on 4 NVIDIA RTX 4090 GPUs.
**Limitation (≤3 sentences):** The authors state the current formulation "does not incorporate semantic priors for modeling complex geometries" and plan to explore such priors in future work.

---

# Near-misses
- 2610.26837 · SpecKCast: Spectral Kalman Forecasting for Diffusion Acceleration · off-topic (generic diffusion-sampling acceleration technique for text-to-image/video generation, not specific to 3D/world-models/character-animation/game-engines) — note: screen matched "Tencent" but the actual, confirmed industry affiliation is Samsung Electronics (AI Center–Toronto), not Tencent
- 2610.26828 · Agent World Model in the Wild: Computer-Use Agent Environment Synthesis · off-topic (GUI/computer-use agent environment synthesis for agent training — matches the explicit off-topic "GUI agents" category despite "World Model" in the title); Microsoft Research co-authorship confirmed but topic disqualifies it
- 2610.26414 · RoboMMT: Learning Stable Tracking of Modulated Expressive and Interactive Robot Motion · no industry co-author (only University of Stuttgart + IMPRS-IS funding acknowledgment; Unitree/ROBOTIS/NVIDIA appear only as hardware used, not affiliations)
- 2610.26262 · Dynamics-Aware Sparse Attention for Efficient Autoregressive Video Diffusion · affiliation unverifiable — no HTML version (arXiv offers only PDF and TeX source for this paper)
- 2610.26179 · Learning Goal-Conditioned Subgoals through Frozen Hierarchical World Models · no industry co-author (sole affiliation found is Hosei University; an NVIDIA L40S GPU is used only as hardware, not an affiliation)
- 2610.26165 · TriTD: Tri-Partite Trajectory-Distribution Distillation for Real-Time Autoregressive Video Generation · affiliation unverifiable — no HTML version (arXiv offers only PDF and TeX source for this paper)

Verification pass: all 12 candidates' arXiv abstract pages were fetched to confirm title, authors, v1 date (all 2026-10-19, within the 30-day window), categories, and non-withdrawn status; HTML pages were fetched where available to read author-affiliation footnotes and abstract/method/limitations text. Two papers (2610.26262, 2610.26165) have no HTML rendering on arXiv (PDF/TeX source only) and were therefore treated as near-misses per the no-PDF-fallback rule rather than guessed at.
