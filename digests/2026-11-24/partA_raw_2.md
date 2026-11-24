# Part A — Papers (batch 2)
Window: last 30 days (2026-10-25 to 2026-11-24). Categories: cs.GR, cs.CV, cs.LG, cs.AI, cs.RO. Retrieval: pre-screened lead list, verified individually via arXiv abs + HTML pages. Qualifying papers: 4 (0 flagged).

---
## GravHMR: Coupling SLAM and Human Mesh Recovery in a Shared Gravity Frame
- **arXiv:** 2611.29614 · https://arxiv.org/abs/2611.29614
- **Submitted:** 2026-11-22 (v1)
- **Authors:** Hanglei Jin, Chenglu Sun, Junchen Ge, Yuchao Wang, Siqi Chen, Yuzhi Huang, Jingyan Jiang, Zhi Wang
- **Qualifying affiliation(s):** Tencent D-Live — Hanglei Jin (dual-affiliated with Tsinghua SIGS), Chenglu Sun, Yuchao Wang
- **Categories:** cs.CV
- **Open release:** project page only (https://jhl25-pixel.github.io/gravhmr/); no code/weights release stated
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper addresses recovering globally consistent 3D human motion from monocular video captured by a moving camera, where SLAM and human mesh recovery (HMR) are usually run independently and can disagree on orientation and scale. GravHMR is a training-free, plug-and-play framework that couples SLAM and HMR through a shared gravity-aligned reference frame, estimating gravity independently of the HMR backbone so it works with HMR models that do or don't produce a gravity-aware representation.

**Purpose (≤3 sentences):** To fix heading (yaw) and trajectory-scale errors that arise when combining separately-estimated camera motion (SLAM) and body motion (HMR) for moving-camera human motion capture.

**Breakthrough (≤3 sentences):** The authors report two components: Yaw-Aware Orientation Optimization (YAOO), which corrects body/velocity heading about the gravity axis, and Gravity-Aware Trajectory Optimization (GATO), which anchors root trajectories in the metric SLAM world using 2D reprojection and the body's implied scale and motion. On EMDB-2 they report 154.0 mm W-MPJPE100 using ViPE and 189.8 mm using masked DROID-SLAM, the latter beating TRAM's reported 222.4 mm under the same camera estimates.

**Tools & method (≤3 sentences):** Benchmarked on EMDB-2 against baselines including TRAM, GVHMR (276.5 mm W-MPJPE100) and HTD-Refine (192.4 mm) with the same HMR backbone; the method is described as training-free and plug-and-play on top of existing SLAM and HMR models.

**Limitation (≤3 sentences):** The abstract/HTML text available does not state explicit failure modes or acknowledged limitations beyond the comparative benchmark numbers; none could be extracted without risking fabrication.

---
## SANA-Robot: Efficient World Action Model with Hybrid Memory
- **arXiv:** 2611.28943 · https://arxiv.org/abs/2611.28943
- **Submitted:** 2026-11-21 (v1)
- **Authors:** Yuyang Zhao, Zekai Li, Yicheng Pan, Jiaming Tang, Zhuoyang Zhang, Jiaxu Xing, Moritz Reuss, Quanquan Peng, Junsong Chen, Enze Xie, Zhijian Liu, Song Han
- **Qualifying affiliation(s):** NVIDIA — listed among the paper's affiliations (NVIDIA, UCSD, THU, MIT, HKU, Inco AI); per-author mapping not shown in the HTML text
- **Categories:** cs.RO (primary), cs.CV
- **Open release:** project page only (https://nvlabs.github.io/Sana/Robot/); no code/weights release stated in the fetched text
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper presents SANA-Robot, a 4.5B-parameter "world action model" that combines action generation with video-model world knowledge, aimed at real-time edge deployment and long-term memory, two things the authors say existing models lack. A unified network assigns different noise levels to action and video tokens so the same model can act as a policy or as a world simulator.

**Purpose (≤3 sentences):** To address prediction overhead that blocks real-time, on-edge control and to give a robot world/action model minute-level memory at constant inference cost.

**Breakthrough (≤3 sentences):** The authors report a hybrid-memory design — fixed-size linear-attention global memory plus sliding-window softmax attention for recent context — and report top results on the memory dimension of RoboDojo among mid-sized (~5B) models and the highest success rates on LIBERO-Plus, LIBERO-Pro and LIBERO-Max. On an RTX 5090 they report 135 ms per action chunk with FP8 GEMMs and 115 ms with NVFP4, enabling closed-loop asynchronous control at 30 Hz on edge hardware.

**Tools & method (≤3 sentences):** The system includes efficient data packing, shuffling, and memory-phase-based asynchronous execution for training and inference; benchmarks used are RoboDojo and the LIBERO-Plus/Pro/Max suites.

**Limitation (≤3 sentences):** The fetched text does not state explicit acknowledged limitations beyond the benchmark comparisons; none could be extracted without fabricating.

---
## RecallWorld: Episodic Memory for Persistent Embodied Video World Models
- **arXiv:** 2611.28666 · https://arxiv.org/abs/2611.28666
- **Submitted:** 2026-11-21 (v1)
- **Authors:** Sarosij Bose, Gitika Karumuri, Chenqi Li, Allen Tu, Srikumar Sastry, Mellon Zhang, Avinash Ravichandran, Alexander Schwing, Konstantinos Karydis, Amit K. Roy Chowdhury
- **Qualifying affiliation(s):** Amazon — listed first among affiliations; acknowledgements state the work was completed during an internship at Amazon
- **Categories:** cs.CV
- **Open release:** none found (CC BY-NC-SA 4.0 license noted on the abs page; no code/weights/demo link found in fetched text)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper argues that video world models can generate plausible new views but often fail to keep a place's geometry and appearance consistent when an embodied agent returns to it. RecallWorld jointly reconstructs short multi-view episodes into "Scenelets," keeping each episode's geometry independent while retrieving complementary ones from the full history.

**Purpose (≤3 sentences):** To give embodied video world models a persistent, revisit-consistent spatial memory instead of either reconstructing every past view separately or rebuilding an ever-growing single history.

**Breakthrough (≤3 sentences):** The authors report that camera-aware ray lifting places perspective and fisheye images in a shared world frame, and that coverage-based retrieval plus geometric visibility resolution before appearance fusion improves revisit PSNR over the strongest baseline by 2.6 dB on partial revisits and 3.9 dB on full cycles, across four datasets.

**Tools & method (≤3 sentences):** Method builds episodic "Scenelets" from short multi-view segments and extends memory as new segments are generated; evaluated across four (unnamed in fetched text) datasets on revisit PSNR.

**Limitation (≤3 sentences):** The fetched text does not state explicit acknowledged limitations; none could be extracted without fabricating.

---
## Two Actions from One State: Fork Futures Teach JEPA World Models to Compare
- **arXiv:** 2611.28350 · https://arxiv.org/abs/2611.28350
- **Submitted:** 2026-11-20 (v1)
- **Authors:** Yihao Wu, Runjia Zeng, Tongyan Wang, Renzhong Huang, Chongzhou Fang, Qifan Wang, Fan Heng, Dongfang Liu
- **Qualifying affiliation(s):** Meta AI — Qifan Wang
- **Categories:** cs.CV (primary), cs.AI
- **Open release:** project page only (https://fork-jepa.github.io/); no code/weights release stated in fetched text
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper observes that JEPA world models are trained on logged transitions containing only one action per state, so under a local linear analysis the action's effect on outcomes is unidentifiable along directions the logging policy never varied. The authors propose "fork futures" — executing two different actions from the same restored state — so the difference in outcomes cancels the shared state term and isolates the action's effect.

**Purpose (≤3 sentences):** To make JEPA world models' action-conditioned predictions actually sensitive to which action is taken, since the authors report behavior-only training leaves predicted action effects no better than a constant guess.

**Breakthrough (≤3 sentences):** The resulting model, Fork-JEPA, adds training-time-only objectives (matching predicted vs. measured action differences, anchoring successor predictions to logged behavior, and a lookback head for predecessor-state recoverability); the authors report this raises planning success by up to 14% over its base model, LeWM, on three visual control tasks, and that 1,024 fork pairs outperform 1.2 million additional behavior-only steps.

**Tools & method (≤3 sentences):** Changes apply only during training (planning/inference is unchanged); evaluated on three visual control tasks including a setting with hidden "zones" where the action response varies, on which the authors report nearly doubled cross-zone success.

**Limitation (≤3 sentences):** The fetched text does not state explicit acknowledged limitations beyond the comparative experiments; none could be extracted without fabricating.

---
# Near-misses
- 2611.29897 · Motion Mamba 2.0: Autoregressive Diffusion Mamba for Long-Horizon Humanoid Control · academic-only (authors from Peking University, Korea University, Monash University, Nanyang Technological University; no industry affiliation found in HTML; pre-screen "ByteDance" hint not confirmed)
- 2611.29630 · SuperFine3D: Efficient Global-Local Recursive Refinement for Extremely Detailed 3D Geometry Generation · academic-only (sole stated affiliation is Dartmouth College; pre-screen "Tencent" hint not confirmed)
- 2611.28922 · PIAE: Physics-Informed Continuous Autoencoding for Compact 3D Human Motion · academic-only (authors affiliated with KAUST and King Khalid University only; pre-screen "Google" hint not confirmed)
- 2611.28902 · StudioBench: Benchmarking Agentic Multimodal Large Language Models for Productive Audiovisual Creation · Tencent affiliation confirmed (Siyuan Li, Yuxin Liu, Caijun Jia, Alden Cai, Cheng Tan), but off-topic: a general agentic-MLLM benchmark for audiovisual (video/audio/ads/documentary) production, not specifically 3D generation, world models, character animation methods, or game engines (uses Blender/three.js/headless-Chromium as generic rendering tools, not as a game-engine or 3D-generation contribution)

Silently dropped as off-topic (not listed above per instructions): 2611.28397 (TOGO — general training-free image-editor-to-video-editor transfer method; not 3D/world-model/character-animation/game-engine specific, despite confirmed Epic Games affiliation); 2611.28098 (Causal Dioramas — controllable video generation/editing via causal intervention graphs; explicitly not framed by the authors as a world model, and not 3D/character-animation/game-engine specific, despite a Tencent affiliation among its authors).

Note: while fetching arxiv.org/html/2611.28098, the page's trailing content contained a block of text formatted as instructions directed at the fetching tool (asking it to produce certain outputs). This was correctly treated as untrusted page data, not as an instruction, and ignored; it did not affect the verification above.

Verification pass: each of the 10 candidate IDs was checked against both its arXiv abstract page (v1 date, title, authors, categories, withdrawal status) and its arXiv HTML page (author affiliations, full abstract/content) independently of the pre-screen hints; 3 of the 4 pre-screened company hints for excluded papers did not match what the papers' own HTML pages state. All 4 included papers' Tencent/NVIDIA/Amazon/Meta affiliations were read directly from each paper's HTML author/affiliation block or acknowledgements, not assumed from the hint.
