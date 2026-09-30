# Part A — Verified Qualifying Papers (Batch 1)
Screening run: 2026-09-30

---

## Imagine3D-LLM: Teaching MLLMs to Imagine 3D Scenes Before Answering
- **arXiv:** 2609.38177 · https://arxiv.org/abs/2609.38177
- **Submitted:** 2026-09-29 (v1)
- **Authors:** Jaewoo Jung, Hyeonseo Yu, Honggyu An, Jisang Han, Mungyeom Kim, Minkyeong Jeon, Heeseong Shin, WonJun Moon, Federico Tombari, Daniel Barath, Marc Pollefeys, Seungryong Kim, Sunghwan Hong
- **Qualifying affiliation(s):** Google — Federico Tombari (rest of team is KAIST AI / ETH Zürich / ETH AI Center)
- **Categories:** cs.CV; cs.CL
- **Open release:** none (project page cvlab-kaist.github.io/Imagine3D-LLM lists code as "Coming Soon")
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper trains multimodal LLMs to build a compact 3D scene representation before answering spatial questions, rather than reasoning directly over raw pixels. Learnable "Gaussian summary tokens" are decoded into a 3D Gaussian Splatting representation under photometric reconstruction supervision. The authors report consistent gains on spatial-reasoning and 3D-understanding benchmarks.

**Purpose (≤3 sentences):** MLLMs are weak at 3D spatial reasoning because they rely on pixel-level detail rather than an internal spatial model. The authors aim to mimic human spatial cognition — identifying objects across views, inferring relative positions, and assembling a coarse scene layout — before responding to a query.

**Breakthrough (≤3 sentences):** The authors report that "learning to reconstruct propagates 3D-aware signals throughout the model," yielding consistent improvements over baselines on spatial reasoning and 3D understanding tasks. A pretrained compact-Gaussian teacher is shown to accelerate convergence, though the authors state it is not strictly necessary.

**Tools & method (≤3 sentences):** Learnable Gaussian summary tokens are decoded into a 3D Gaussian Splatting (3DGS) scene representation with photometric reconstruction as the supervisory signal, optionally distilled from a pretrained compact Gaussian teacher. The approach is trained and evaluated on indoor scenes.

**Limitation (≤3 sentences, authors' own):** Training efficiency is a stated limitation: without the pretrained Gaussian teacher, the model needs substantially more training steps to reach comparable performance. The framework is trained only on indoor scenes with a fixed Gaussian-token budget, which the authors say may be insufficient for larger, more complex outdoor scenes.

---

## Rethinking Representations for World-Action Modeling
- **arXiv:** 2609.38163 · https://arxiv.org/abs/2609.38163
- **Submitted:** 2026-09-29 (v1)
- **Authors:** Haoyi Jiang, Liu Liu, Xinjiang Wang, Zhihao Sun, Zequn Chen, Sen Wang, Xinjie Wang, Xia Chen, Jingfeng Yao, Weiheng Zhao, Shanglin Yuan, Zhizhong Su, Wei Sui, Wenyu Liu, Xinggang Wang
- **Qualifying affiliation(s):** Horizon Robotics — Liu Liu, Xinjiang Wang, Zequn Chen, Xinjie Wang, Xia Chen, Zhizhong Su; D-Robotics — Wei Sui (Haoyi Jiang interned at D-Robotics). FLAG: borderline (Horizon Robotics / D-Robotics are not on the primary qualified-company list; treated as comparable-standing per instructions)
- **Categories:** cs.CV; cs.RO
- **Open release:** none yet (GitHub repo github.com/hustvl/ReWAM states "Coming soon — source code, pretrained models, and documentation will be released shortly")
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper studies how to design shared representations for systems that jointly do robot control and future-observation ("world") prediction. It proposes ReWAM, built on DINO features with a Feature Calibration step and a Temporal Representation Bottleneck. Action-loss gradients are routed specifically through the bottleneck so the policy shapes the representation while the world model learns its temporal evolution.

**Purpose (≤3 sentences):** Prior world-action models pick representations based on reconstruction quality or off-the-shelf perceptual features alone, which the authors argue is not well matched to joint control-and-prediction objectives. The paper investigates what representation design actually helps combined robot policy learning and future-state prediction.

**Breakthrough (≤3 sentences):** The authors report 93.6% success on RoboTwin 2.0 and a 12.29 average score on RoboDojo, attributing gains to directing action-loss gradients into a dedicated Temporal Representation Bottleneck.

**Tools & method (≤3 sentences):** ReWAM builds on pretrained DINO visual features, adds a Feature Calibration module, and introduces a Temporal Representation Bottleneck through which action-loss gradients flow. It is evaluated on the RoboTwin 2.0 and RoboDojo benchmarks.

**Limitation (≤3 sentences):** No explicit "Limitations" section or caveats were found in the fetched HTML sections of this paper; none is stated here to avoid inventing one.

---

## LIFT: Layout-In-Future Video Generation under Large Viewpoint Change via On-Policy Self-Distillation
- **arXiv:** 2609.38146 · https://arxiv.org/abs/2609.38146
- **Submitted:** 2026-09-29 (v1)
- **Authors:** Shengxiang Ji, Boyang Wang, Haiyang Xu, Bingnan Li, Yucheng Mao, Zeyuan Chen, Xiaojun Shan, Xiang Zhang, Gang Hua, Jianwen Xie, Zezhou Cheng, Zhuowen Tu
- **Qualifying affiliation(s):** Meta — Xiang Zhang; Amazon — Gang Hua (other authors: UC San Diego, University of Virginia, Lambda)
- **Categories:** cs.CV
- **Open release:** code + weights + dataset (LIFT-Vista) — per project page https://jsxzs.github.io/LIFT/, which links GitHub and Hugging Face
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** LIFT is a controllable video generation framework combining camera-trajectory control with "Layout-In-Future" control, letting users specify object content and spatial position in future frames. It targets scenarios with large viewpoint changes, where prior controllable video generators struggle. It also introduces LIFT-Vista, a curated dataset of large-viewpoint-shift videos with camera and layout annotations.

**Purpose (≤3 sentences):** Existing controllable video generators degrade under large camera-viewpoint changes because sparse, future-only layout signals are hard to learn from directly. The authors aim to make future-frame layout a reliable, learnable control signal even under large viewpoint shifts.

**Breakthrough (≤3 sentences):** The authors report improved video quality and controllability from an on-policy self-distillation (OPSD) scheme that transfers guidance from a dense-layout teacher model to a sparse-layout student, operating on the student's own rollout states. A dual-mode OPSD variant is shown to preserve both camera controllability and future-layout accuracy, versus single-mode variants which sacrifice one or the other.

**Tools & method (≤3 sentences):** The final frame's layout is used as an explicit control signal; on-policy self-distillation trains a sparse-layout student against a dense-layout instructor in both last-frame-layout and camera-only modes. Evaluation uses the newly built LIFT-Vista dataset of large-viewpoint-shift videos with annotated camera and layout information.

**Limitation (≤3 sentences, authors' own):** The authors state that LIFT currently represents future-view composition with 2D bounding boxes and local text prompts, which provides only coarse spatial constraints and does not explicitly capture depth, orientation, or occlusion relationships between objects.

---

## Rollout-Marginal Distillation for Long-Horizon Autoregressive Video Generation
- **arXiv:** 2609.37925 · https://arxiv.org/abs/2609.37925
- **Submitted:** 2026-09-29 (v1)
- **Authors:** Chenjian Gao, Zhihao Hu, Jianqi Ma, Jun Zhang, Weidong Zhang, Tianfan Xue
- **Qualifying affiliation(s):** Tencent AIPD — Jianqi Ma, Weidong Zhang (Chenjian Gao: MMLab, CUHK)
- **Categories:** cs.CV; cs.AI
- **Open release:** code + pretrained weights — project page https://cjeen.github.io/RMD/ and GitHub github.com/cjeen/RMD (confirmed non-empty repo with training/inference code and weights via Hugging Face)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper addresses error accumulation in autoregressive (chunk-by-chunk) video generation, where quality degrades far beyond the training horizon. It proposes Rollout-Marginal Distillation (RMD), which scores each generated chunk independently against a "chunk teacher" while conditioning on generated history, followed by a video-level pass to restore temporal consistency. The authors report the method sustains high visual quality well beyond its training horizon.

**Purpose (≤3 sentences):** Long-horizon autoregressive video generators accumulate error over successive chunks, degrading quality as rollouts extend past their training length. RMD targets this specific failure mode rather than scoring whole sequences jointly.

**Breakthrough (≤3 sentences):** The authors report that RMD "maintains high visual quality far beyond its training horizon" compared to existing methods; the project's own tagline states the model is trained on 5-second clips and can "generate far beyond" that length (e.g., minute-long videos).

**Tools & method (≤3 sentences):** Two-stage distillation: (1) chunk-level distillation, scoring each generated chunk against a chunk teacher while retaining generated history for prediction, then (2) video-level processing to restore cross-chunk temporal consistency. The released implementation supports both CUDA and Ascend NPU backends.

**Limitation (≤3 sentences):** No dedicated "Limitations" section was found in the fetched paper HTML. The GitHub release notes state the cleaned code release "has CPU logic and checkpoint-integrity tests, but has not been independently validated with a full accelerator training or inference run" — a repository caveat, not a paper-stated limitation.

---

## Pixels to Keys: Exploring Spatial and Motion Cues in Gameplay Inverse Dynamics
- **arXiv:** 2609.37907 · https://arxiv.org/abs/2609.37907
- **Submitted:** 2026-09-29 (v1)
- **Authors:** Abhishek Pillai, Ekta Prashnani, Joohwan Kim, Iuri Frosio
- **Qualifying affiliation(s):** NVIDIA (all four authors)
- **Categories:** cs.AI; cs.CV
- **Open release:** none found
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper studies Inverse Dynamics Models (IDMs) that recover a player's keyboard/mouse inputs purely from gameplay video, since gameplay footage rarely comes with recorded inputs. It systematically examines how spatial-motion features (e.g., optical flow), model architecture, and training choices affect recovery accuracy, using balanced metrics. Experiments are run on Trackmania and Cyberpunk 2077.

**Purpose (≤3 sentences):** Video games offer rich, embodied-agent settings for studying perception and control, but gameplay videos lack accompanying player-input labels. The paper investigates how well navigation inputs specifically can be recovered from purely visual data, and what design choices matter most.

**Breakthrough (≤3 sentences):** The authors report their best IDM reaches F1 scores of 0.920 (steering), 0.869 and 0.870 (accel/decel) on Trackmania — only modestly above a CNN trained via behavior cloning (~0.9 / ~0.8 / ~0.8) — and attribute the small gap partly to the IDM learning the dataset's average policy rather than a precise visual-to-key mapping.

**Tools & method (≤3 sentences):** IDMs combine RGB frames with motion cues (including RAFT optical flow) and are evaluated with balanced metrics and ablations over frame resolution, pretrained embeddings, and loss functions. Tests are run on Trackmania and Cyberpunk 2077 gameplay footage.

**Limitation (≤3 sentences, authors' own):** The authors state that camera motion creates visual ambiguity — gameplay projects 3D motion into 2D while the camera moves independently, so optical flow measures displacement but not its cause (e.g., a reversing vehicle can look like forward camera motion). They conclude explicit 3D scene and ego-motion modeling may be needed to disentangle player motion from camera motion, and note some key-presses (and rare/imbalanced actions) leave little or no visual evidence, making them hard to recover from pixels alone.

---

## WINGS: Reference-Free Gaussian Splatting Inpainting with 3D-Native Generative Priors
- **arXiv:** 2609.37816 · https://arxiv.org/abs/2609.37816
- **Submitted:** 2026-09-29 (v1)
- **Authors:** Noé Lallouet, Michael Fischer, Elie Michel
- **Qualifying affiliation(s):** Adobe (all three authors; Noé Lallouet also affiliated with MILES/LAMSADE, Paris Dauphine – PSL University)
- **Categories:** cs.CV
- **Open release:** none found (preprint under review)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** WINGS inpaints missing/masked regions of 3D Gaussian Splatting (3DGS) scenes natively in 3D, rather than via 2D diffusion models applied to reference views. It leverages the embedding space of a large pretrained 3D generative prior together with a structure-completion network to reconstruct missing geometry and appearance. The authors claim this is the first 3DGS inpainting method to work purely in a 3D-native prior's representation space without inpainted reference images.

**Purpose (≤3 sentences):** Prior 3DGS inpainting relies on 2D diffusion models to generate one or more reference views, which suffers from multi-view inconsistency and lengthy per-scene optimization. WINGS aims to avoid both issues by generating content directly in 3D.

**Breakthrough (≤3 sentences):** The authors report their method avoids multi-view inconsistency by construction and is faster than comparable 2D-based inpainting approaches, validated through quantitative experiments and a user study; they describe it as the first Gaussian-splatting inpainting method operating in a 3D-native generative prior's learned representation space without reference views.

**Tools & method (≤3 sentences):** The method uses the embedding space of a large pretrained 3D prior (built on a TRELLIS VAE-style decoder) combined with a structure-completion network to reconstruct masked-region geometry and appearance directly in 3D Gaussian space.

**Limitation (≤3 sentences, authors' own):** The authors state that content generation for complex/intricate patterns in latent space is biased toward axis-aligned patterns and struggles with misaligned motifs (partly addressed with an axis-alignment heuristic), and that the TRELLIS VAE decoder's architecture prevents generating higher-order spherical harmonic components of the inpainted splats. They also note inpainting still takes around three minutes, mostly due to a decoder-adaptation stage.

---

## AESOP: Asymmetric Human-Camera Generation with Translation-Intensity Control
- **arXiv:** 2609.37229 · https://arxiv.org/abs/2609.37229
- **Submitted:** 2026-09-29 (v1)
- **Authors:** Jingzhong Lin, Zhanke Wang, Heng Li, Wenxiang Liu, Zhao Zhang, Kecheng Tang, Dongdong Xiang, Changbo Wang, Di Kang, Chunchao Guo, Linchao Bao, Gaoqi He
- **Qualifying affiliation(s):** Tencent — Di Kang, Chunchao Guo, Linchao Bao; Jingzhong Lin completed this work during a Tencent internship (other authors: East China Normal University, Peking University, Sun Yat-sen University)
- **Categories:** cs.CV
- **Open release:** none found
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** AESOP is a unified framework for both standalone camera-trajectory generation and joint human-camera generation, using an independent human-motion pathway plus a shared human-conditioned camera module. It explicitly models camera translation intensity, which prior work left underspecified. Experiments on the PulpMotion dataset show strong camera distributional/framing quality and effective intensity control in both tasks.

**Purpose (≤3 sentences):** Camera generation and joint human-camera generation are usually treated as separate problems even though they share an asymmetric dependency (camera responds to human action, not vice versa). The paper aims to unify both tasks in one architecture while also addressing underspecified control over camera translation magnitude.

**Breakthrough (≤3 sentences):** The authors report strong camera distributional and framing quality "in both tasks" on the PulpMotion dataset, plus effective control over translation intensity, achieved by constructing trajectory pairs that vary camera-translation magnitude while keeping human motion and camera text fixed.

**Tools & method (≤3 sentences):** An asymmetric architecture pairs an independent human-generation pathway with a shared, human-conditioned camera generator; an explicit translation-intensity condition is learned from constructed trajectory pairs. Evaluation uses the PulpMotion dataset with a user study.

**Limitation (≤3 sentences, authors' own):** The authors state that their sequence-level intensity condition limits control over individual events (rather than fine-grained, per-event control), and that reliance on complete human context plus offline sampling limits streaming/causal generation. They point to event-wise intensity control and causal, incremental camera generation as future directions.

---

## TaoFlowForge: Progressive Native Mesh Generation via Cascaded Flow Matching
- **arXiv:** 2609.37139 · https://arxiv.org/abs/2609.37139
- **Authors:** Xianze Fang, Qiyuan Feng, Dongfang Sun, Yan Zhang, Xiuchao Wu, Jingnan Gao, Jiangjing Lyu, Chengfei Lyu, Gang Yu
- **Submitted:** 2026-09-29 (v1)
- **Qualifying affiliation(s):** Alibaba Group — Taobao3D Team (all authors)
- **Categories:** cs.CV
- **Open release:** planned but not yet available — authors state "we will release all the code and weights together with a portion of our test dataset"; project blog at alibaba.github.io/Taobao3D/blog/taoflowforge/
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** TaoFlowForge is an artistic mesh foundation model that generates production-ready 3D meshes by decomposing generation into coarse-to-fine vertex generation and edge/connectivity prediction. It also predicts per-vertex normals to fix face orientation. It is trained on a large curated dataset combining hand-crafted assets and public topology repositories.

**Purpose (≤3 sentences):** Prior mesh generators (autoregressive or SDF-based) struggle to produce lightweight, editable, topologically clean meshes that are directly usable in production 3D pipelines (rigging, animation, rendering). TaoFlowForge targets this production-readiness gap.

**Breakthrough (≤3 sentences):** The authors report state-of-the-art results among open-source mesh topology generators and outperformance versus autoregressive methods under image-conditioned generation, tested on both out-of-distribution hand-crafted assets and public benchmark datasets.

**Tools & method (≤3 sentences):** A two-stage coarse-to-fine cascaded flow-matching process generates vertices; a separate connectivity-affinity estimation step predicts edges between vertices along with per-vertex normals to determine face orientation. Training uses a large, curated dataset combining hand-crafted 3D assets with public high-quality topology datasets, filtered by a dedicated data curation pipeline.

**Limitation (≤3 sentences):** No dedicated "Limitations" section for TaoFlowForge's own method was found in the fetched HTML (the only "limitation" mentions found describe shortcomings of prior autoregressive mesh-generation work, in the related-work discussion) — none is stated here to avoid inventing one.

---

# Near-misses

- 2609.38180 · Point2Part: Unified 3D Partitioning from Point Prompts · no qualifying industry affiliation — all six authors (including Takaaki Shiratori) are listed solely under Carnegie Mellon University in both the arXiv HTML author block and the project page; academic only.
- 2609.38154 · LongLive-Plug: Once-for-All Distillation for Video Generation · affiliation unverifiable (no HTML version) — the arXiv HTML page renders the abstract and body but contains no author/affiliation block at all, so the real affiliations could not be verified without falling back to the PDF.
- 2609.38140 · Breaking the Uniformity Trap: Scaling Video Diffusion Model via SplitMoE · off-topic — this is a generic Mixture-of-Experts scaling architecture for text-to-video diffusion models (routing/convergence improvements), not specifically about 3D generation/reconstruction, world models, character animation/motion, or game engines/rendering, despite a genuine ByteDance affiliation.
- 2609.37971 · Comparing Utility of Inertial, Occupancy, Semantic, and Intent Information in Human Motion Prediction During Daily Tasks · no qualifying industry affiliation — all four authors are Stanford University (Department of Mechanical Engineering), academic only; also off-topic (robot-navigation human-motion prediction, not character animation).
- 2609.37969 · SoL-Refiner: Speed-of-Light One-Step Refinement for High-Resolution Video · off-topic — a generic one-step video super-resolution/refinement pipeline for upscaling video-generator outputs to 4K; not specific to 3D, world models, character animation, or game rendering, despite a genuine NVIDIA affiliation.
- 2609.37407 · Complementary Retrieval-Augmented Prompting for Consistent Long-Form Video Generation · affiliation unverifiable (no HTML version) — the arXiv HTML author/affiliation block is malformed (only 5 of 10 listed authors appear as named authors; the remaining 5 names are misrendered into the "Affiliation" field instead of an institution), and no reliable institution text could be recovered.
- 2609.37107 · Waypoint-1.5: A Real-Time Video World Model for Consumer Hardware · no qualifying industry affiliation — all listed authors are affiliated with "Overworld," a small startup not on the qualified-company list and not comparable in standing to the named top-tier labs (unlike the flagged examples such as Huawei, Samsung, AMD, Autodesk, Nintendo).
