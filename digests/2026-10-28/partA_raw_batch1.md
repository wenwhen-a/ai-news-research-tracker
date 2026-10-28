## Hy-Nomas: Towards Free-form Interactive World Generation
- **arXiv:** 2610.36729 · https://arxiv.org/abs/2610.36729
- **Submitted:** 2026-10-27
- **Authors:** Qiaoling Chen, Jiaxiang Cheng, Xueqing Deng, Tiankai Hang, Ji Hou, Jiaqi Li, Yifan Liu, Tao Lu, Junshu Tang, Yu Tang, Yao Teng, Yu Tian, Heng Wang, Weizhi Wang, Xiyao Wang, Xilun Wu, Mingyu Yang, Yangbin Yu, Rui Zhao, Longjun Cao, Linghao Chen, Haoyi Duan, Jiaming Han, Mingji Han, Enhua Jiang, Shunkai Li, Yanzhe Liang, Qinwei Ma, Cong Wang, Lei Wang, Bing Wu, Ke Xing, Ray Ying, Zhentao Yu, Key Zhang, Yuan Zhou, Zhengguang Zhou, Kai Zou (38 authors, credited collectively as "Tencent Hy Visual Generation Team")
- **Qualifying affiliation(s):** Tencent — all listed authors (Tencent Hy Visual Generation Team)
- **Categories:** cs.CV
- **Open release:** weights + code — the abstract states "We release model weights, code and benchmarks, together with a lightweight adaptation workflow"; no direct link found on the abstract page (comment field just says "Technical Report")
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** Hy-Nomas is an 8B-parameter diffusion-based video world model that follows free-form text instructions and continuous camera control across multiple interaction turns, generating variable-length video segments from current inputs and cached history. Its central design aligns structured video captions with action-aware causal attention so descriptive context persists across segments while action instructions apply only within their intended time window. A vision-language Prompt Enhancer translates user requests and interaction history into structured conditions for each new segment.
**Purpose (≤3 sentences):** The authors target interactive world generation, where a model must follow successive user commands while preserving relevant history and the consequences of prior actions. They aim to let a single world model handle open-ended text instructions and camera control together, rather than only one or the other.
**Breakthrough (≤3 sentences):** The authors report that in human evaluation, Hy-Nomas shows superior performance over existing world models. The reported mechanism is the combination of action-aware causal attention (so captions persist but actions stay temporally scoped) with a multi-stage training curriculum that ends in diffusion distillation for faster generation.
**Tools & method (≤3 sentences):** The model uses an 8B diffusion backbone, a vision-language Prompt Enhancer module, and a multi-stage curriculum that progressively introduces causal generation, text interaction, camera control, and training on model-generated histories, followed by diffusion distillation. The authors release weights, code, and benchmarks plus a lightweight adaptation workflow.
**Limitation (≤3 sentences):** The paper is described as a technical report rather than a peer-reviewed publication, and the evaluation relies on human preference judgments rather than only automated metrics (as stated). No quantitative benchmark numbers beyond "superior" human-evaluation performance are given in the abstract.

---

## SWIM: Learning What Matters from Behaviors for JEPA World Models
- **arXiv:** 2610.36662 · https://arxiv.org/abs/2610.36662
- **Submitted:** 2026-10-27
- **Authors:** Jiaming Hu, Shi Bo, Yan Zheng, Tian Wang, Florian Dubost, Alejandro Mottini, Junze Liu, Arvind Srinivasan, Kai Zhong, Kun Qian, Sharon Gao, Vianne Gao, Houyu Zhang, Qingjun Cui
- **Qualifying affiliation(s):** Unity Technologies — Yan Zheng, Tian Wang, Florian Dubost, Alejandro Mottini, Junze Liu, Arvind Srinivasan, Kai Zhong, Kun Qian, Sharon Gao, Vianne Gao, Houyu Zhang, Qingjun Cui; Jiaming Hu and Shi Bo are listed with dual affiliation (Boston University and Unity Technologies). Verified from the HTML author block ("Unity Technologies" stated explicitly, not the generic word "unity").
- **Categories:** cs.RO (primary), cs.CV
- **Open release:** none found (comment field only says "25 pages, 1 figure"; no code/weights link found)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** SWIM is a method for training JEPA (joint-embedding predictive architecture) world models so that their learned state representation better reflects physical task progress rather than only visual similarity. It learns per-feature weights on simulator state, via an inverse-dynamics model that predicts recorded actions from current states and observed future displacements, instead of hand-picking or uniformly weighting state features. The learned weighted state metric is then used to supervise the world model's latent space.
**Purpose (≤3 sentences):** The authors address a known gap in JEPA world models: their visual prediction objective may not capture the physical state that actually determines task progress, and naive state supervision (hand-picked or uniform feature weights) lets redundant features overcount and irrelevant ones obscure meaningful differences. SWIM aims to fix this weighting problem directly from offline trajectory data.
**Breakthrough (≤3 sentences):** The authors report that across five simulated robotic manipulation tasks, SWIM's learned state weighting improves planning success over uniform weighting of state features, and that the inverse-dynamics model is used only during training so it adds no computation at planning time.
**Tools & method (≤3 sentences):** SWIM uses an inverse-dynamics model trained on offline trajectories to learn feature weights, which define a weighted state metric used to align latent and state distances during world-model training. Evaluation is done across five simulated robotic manipulation tasks with planning-based control from images.
**Limitation (≤3 sentences):** The evaluation is confined to simulated robotic manipulation tasks (observed, not stated as a broader limitation); the abstract does not report results on real robots or non-manipulation domains.

---

## BoxWorld: Let World Engines Control and Video Generators Render
- **arXiv:** 2610.36371 · https://arxiv.org/abs/2610.36371
- **Submitted:** 2026-10-26
- **Authors:** Zike Wu, Ahmed Hatem, Chintan Trivedi, Wallace Michel Pinto Lira, Xuebin Qin, Lele Wang, Renjie Liao
- **Qualifying affiliation(s):** Huawei Canada — Ahmed Hatem, Chintan Trivedi, Wallace Michel Pinto Lira, Xuebin Qin; FLAG: borderline (Huawei is a comparable top-tier industry lab not on the illustrative list, per tracker rules)
- **Categories:** cs.CV
- **Open release:** demo/project page only — project page at https://boxworld-web.github.io; no code or weights release stated in the abstract
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** BoxWorld builds real-time interactive video worlds with user-defined rules by separating interaction logic from video rendering. A coding agent constructs a "Box World Engine" that tracks object states and interaction outcomes, exposing them as layout boxes, persistent attributes, and status variables; a "Box-State Generative Renderer" then renders this evolving state stream into video autoregressively. The authors introduce PairedStateBench, a benchmark for fine-grained interaction control.
**Purpose (≤3 sentences):** The authors target a limitation of end-to-end video world models: learning interaction dynamics purely inside the video generator makes it hard to specify object-level rules or reason about their consequences. BoxWorld aims to let users define rules explicitly while still rendering results through a generative video model.
**Breakthrough (≤3 sentences):** The authors report that BoxWorld substantially outperforms end-to-end world models and remains competitive across multiple public benchmarks. They attribute this to decoupling rule-based interaction reasoning (the Box World Engine) from appearance/physical-effect rendering (the generative renderer).
**Tools & method (≤3 sentences):** The system uses a coding agent to build the rule-based Box World Engine, and a three-stage training strategy for the renderer: object grounding from open-domain videos, state-transition learning from automatically annotated gameplay videos, and rollout distillation on self-generated histories. PairedStateBench is introduced as a paired benchmark for fine-grained interaction control.
**Limitation (≤3 sentences):** The authors note that rendering the evolving state stream is "non-trivial" because the renderer must respond to object-level state updates in real time while staying coherent with generated history (stated as a design challenge, not fully resolved). No quantitative benchmark numbers are given in the abstract beyond "substantially outperforms" and "competitive."

---

## RynnWorld-Latent: A Cross-Embodiment World Model Conditioned on Universal Latent Actions
- **arXiv:** 2610.36791 · https://arxiv.org/abs/2610.36791
- **Submitted:** 2026-10-27
- **Authors:** Haoyu Zhao, Yinzhou Tang, Zixuan Wang, Minghao Zhu, Dongchi Huang, Xingyue Zhao, Qin Zhao, Kehan Li, Siteng Huang, Xin Li, Zhenyu Zeng, Mingxiu Chen, Deli Zhao, Zhongyu Li
- **Qualifying affiliation(s):** Alibaba — DAMO Academy, Alibaba Group / Hupan Lab: Minghao Zhu, Dongchi Huang, Xingyue Zhao, Kehan Li, Xin Li, Zhenyu Zeng, Mingxiu Chen, Deli Zhao
- **Categories:** cs.RO
- **Open release:** code — homepage at https://alibaba-damo-academy.github.io/RynnWorld-Latent.github.io and GitHub repo at https://github.com/alibaba-damo-academy/RynnWorld-Latent
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** RynnWorld-Latent is a video world model that uses latent actions from RynnLAM as a shared conditioning interface, letting it train on human videos, robot demonstrations, and simulation rollouts without needing a common action space. It is built on a pretrained video transformer, pretrained on 23 datasets totaling about 553.5M frames, and then adapted to specific target robots.
**Purpose (≤3 sentences):** The authors address the problem that cross-embodiment world models normally need a shared action representation to learn from heterogeneous data sources (human video, robot demos, simulation), which is hard to define across different embodiments. Universal latent actions are proposed as that shared interface.
**Breakthrough (≤3 sentences):** The authors report better video prediction quality, higher downstream policy success on LIBERO and LIBERO-Plus when using synthetic mid-training, and gains on two real-robot platforms. They state this shows "universal latent actions as a scalable interface for learning controllable visual dynamics across heterogeneous embodiments."
**Tools & method (≤3 sentences):** The method conditions a pretrained video transformer on latent actions extracted by RynnLAM, pretrains on 23 datasets (~553.5M frames) spanning human video, robot demonstrations, and simulation, and then adapts to target robot platforms. Code and a project homepage are publicly released on GitHub.
**Limitation (≤3 sentences):** This is a world model whose downstream evaluation is entirely on robot-manipulation benchmarks (LIBERO, LIBERO-Plus, two real-robot platforms), not on game or general video-generation tasks (observed, not stated). The abstract does not report results outside the embodied-manipulation setting.

---

## GeoGSplat: Geometry-Grounded Non-Pixel-Aligned Gaussian Splatting
- **arXiv:** 2610.36760 · https://arxiv.org/abs/2610.36760
- **Submitted:** 2026-10-27
- **Authors:** Jiale Wang, Chen Zhao, Haoyang Zhang, Yanhao Wu, Fei He, Yanhu Shan, Rui Wu, Wei Ke, Tong Zhang
- **Qualifying affiliation(s):** Horizon Robotics — at least one author (exact name-to-institution mapping not recoverable from the HTML author block, which lists "Xi'an Jiaotong University, EPFL, Horizon Robotics, University of the Chinese Academy of Sciences" as a group without clear per-author linkage); FLAG: borderline (Horizon Robotics is not on the illustrative company list)
- **Categories:** cs.CV
- **Open release:** none found — project page at https://comedy0913.github.io/projects/geogsplat exists but no code/weights release is stated in the abstract
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** GeoGSplat is a feed-forward Gaussian Splatting model for novel view synthesis that adds geometric priors to the non-pixel-aligned framework, which otherwise tends to place Gaussian centers poorly under large viewpoint changes. A dual-branch encoder builds Anchors for coarse 3D structure and a Triplane for fine scene features, and a hierarchical decoder progressively produces dense 3D points and Gaussian primitives.
**Purpose (≤3 sentences):** The authors target a tradeoff in feed-forward Gaussian Splatting: pixel-aligned methods scale primitive count with resolution and view count (costly), while non-pixel-aligned methods fix the primitive count but, without explicit ray/depth constraints, misplace Gaussian centers and cause artifacts under large viewpoint changes. GeoGSplat aims to keep the fixed-count efficiency while fixing the placement problem via geometric grounding.
**Breakthrough (≤3 sentences):** The authors report that GeoGSplat surpasses both state-of-the-art pixel-aligned and non-pixel-aligned Gaussian Splatting baselines on the DTU and NRGBD datasets for novel view synthesis and reconstruction, and that the advantage grows as target viewpoints move farther from the input cameras.
**Tools & method (≤3 sentences):** The model uses a dual-branch encoder (Anchors + Triplane) to capture coarse and fine-grained 3D structure, followed by a hierarchical decoder that outputs dense 3D points and Gaussian primitives. Evaluation is on the DTU and NRGBD benchmarks.
**Limitation (≤3 sentences):** The abstract does not report results outside DTU and NRGBD, and the per-author affiliation mapping could not be confirmed, so the exact author tied to Horizon Robotics could not be isolated (observed, not stated).

---

## StereoSplat: Metric-Scale Novel View Synthesis via Stereo-Grounded Gaussian Splatting
- **arXiv:** 2610.35902 · https://arxiv.org/abs/2610.35902
- **Submitted:** 2026-09-29
- **Authors:** Vladimir Yugay, Denis Rozumny, Theo Gevers, Elias Vansteenkiste, Martin R. Oswald, Diogo C. Luvizon
- **Qualifying affiliation(s):** Meta — Denis Rozumny, Elias Vansteenkiste, Diogo C. Luvizon (verified as the company Meta in the HTML author block, not a "meta-learning" text match; Vladimir Yugay is University of Amsterdam with a footnote noting an internship at Meta)
- **Categories:** cs.GR, eess.IV
- **Open release:** none found
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** StereoSplat is a feed-forward 3D Gaussian Splatting architecture built specifically for stereo video, aimed at reliable, metric-scale novel view synthesis. It takes dense multi-scale features and disparity from a foundation stereo backbone and decodes them into per-pixel 3D Gaussians via cross-view feature fusion and gated depth refinement, with a depth-adaptive aggregation step to reduce redundant primitives across overlapping views.
**Purpose (≤3 sentences):** The authors address the fact that monocular feed-forward Gaussian Splatting approaches don't exploit the structure of binocular stereo pairs, and aim for metric-scale (not just relative-scale) novel view synthesis that generalizes from synthetic to real stereo video. They also introduce XRStereo, a large synthetic stereo-video dataset with rig configurations matching real hardware, to support this.
**Breakthrough (≤3 sentences):** The authors report substantial improvements in rendered-novel-view depth accuracy over established baselines while maintaining high-fidelity view synthesis, and state that the model transfers zero-shot to real-world stereo video despite being trained exclusively on synthetic data.
**Tools & method (≤3 sentences):** The architecture uses a foundation stereo backbone, a Gaussian decoder with cross-view feature fusion and gated depth refinement, and a learnable depth-adaptive aggregation mechanism operating in inverse-depth space. Training and evaluation use the newly introduced XRStereo synthetic dataset plus other benchmarks.
**Limitation (≤3 sentences):** The model is trained exclusively on synthetic data (stated), and the authors frame real-world deployment (mixed reality, autonomous driving, robotics) as an application area rather than a setting with reported quantitative results in the abstract.

# Near-misses
- 2610.37381 · PDRVLA: A Vision-Language-Action Model with Physical Dynamics Representations · off-topic: vision-language-action model for robot manipulation; the "world model" is only a frozen auxiliary supervision signal, not the paper's topic. Affiliation is Peking University / JD.com (JD.com is a borderline company but the topic gate fails regardless).
- 2610.36539 · CARD: Contact-Anchored Retargeting for Dexterous Manipulation · off-topic: general dexterous-manipulation retargeting (contact-force-preserving human-to-robot retargeting), no stated 3D/world-model/animation/game-engine relevance, despite a verified Amazon (Amazon Frontier AI & Robotics) co-author affiliation.
- 2610.36462 · ClusterSplat: Semantic Cluster Selection for 3D Visual Grounding in Gaussian Splatting · no qualifying industry author — purely academic (all four authors are affiliated only with KAIST); the "ByteDance" regex hit does not appear anywhere in the author/affiliation block and is a screen artifact.
- 2610.36312 · SG^2SLAM: Spatial Geometry-Informed 3D Gaussian Splatting SLAM for Monocular Outdoor Navigation · no qualifying industry author — purely academic (Skoltech, University of Hong Kong, Tsinghua University's SuZhou Automotive Research Institute, Chinese Academy of Sciences).
- 2610.36022 · Learning and Reasoning with Geometry: How Generation Helps Spatial Understanding · affiliation unverifiable — no HTML version exists (arxiv.org/html/2610.36022 returns 404), so the "Google" hit (likely a Scholar-link or citation artifact) could not be checked against a real affiliation block; no PDF fallback used per instructions.
