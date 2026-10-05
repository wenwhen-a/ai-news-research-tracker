## FlowHMR: Physically Plausible Motion Capture from Video
- **arXiv:** 2610.03691 · https://arxiv.org/abs/2610.03691
- **Submitted:** 2026-10-02
- **Authors:** Zhanke Wang, Chengfeng Zhao, Qing Shuai, Jingzhong Lin, Heng Li, Zeyu Ling, Yuxin Wen, Jing Li, Di Kang, Chunchao Guo, Linchao Bao
- **Qualifying affiliation(s):** Tencent — Zhanke Wang, Chengfeng Zhao, Qing Shuai, Yuxin Wen, Jing Li, Di Kang, Chunchao Guo, Linchao Bao (joint Peking University / HKUST / Tencent affiliations)
- **Categories:** cs.CV
- **Open release:** code (https://github.com/flowhmr/flowhmr); demo/project page (https://flowhmr.github.io/)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** FlowHMR reframes monocular video human motion capture as a video-conditioned motion generation task, using flow matching to produce physically plausible 3D human motion from single-camera video. The authors also introduce Wild-4K, a new evaluation dataset of about 4,000 internet videos.
**Purpose (≤3 sentences):** Prior direct-regression HMR methods suffer from depth ambiguity and tend to collapse toward an averaged, physically implausible solution, with no guarantee the recovered motion is dynamically trackable.
**Breakthrough (≤3 sentences):** The authors report a two-stage pipeline: a pretrained flow-matching model generates diverse motion candidates from video, then Group Relative Policy Optimization (GRPO) refines them with dual rewards for video fidelity and physics-simulation trackability. On their new Wild-4K benchmark they report an 82.47% physical tracking success rate versus 62.82% for the prior best baseline (GVHMR).
**Tools & method (≤3 sentences):** The method combines flow matching for motion generation with reinforcement learning (GRPO) using video-alignment and physics-tracking reward signals; evaluation uses the newly introduced Wild-4K dataset of ~4K internet videos.
**Limitation (≤3 sentences):** The paper frames its contribution relative to prior regression-based methods' depth ambiguity and mode-collapse issues; no further limitations beyond this framing were stated in the available abstract/HTML content.

## ProAR: Learning Prospective Reasoning with Autoregressive Video Models
- **arXiv:** 2610.03664 · https://arxiv.org/abs/2610.03664
- **Submitted:** 2026-10-02
- **Authors:** Linghui Shen, Tinghui Zhu, Sheng Zhang, Muhao Chen
- **Qualifying affiliation(s):** Microsoft — Sheng Zhang
- **Categories:** cs.CV
- **Open release:** none confirmed (project page mentioned: https://luka-group.github.io/ProAR/; no explicit code/weights release stated)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** ProAR is a framework for autoregressive video (world) models that adds goal-directed, prospective reasoning on top of standard next-frame prediction. It combines goal-frame prediction with future representation self-alignment to steer generation toward target outcomes rather than just locally plausible frames.
**Purpose (≤3 sentences):** The authors argue that standard autoregressive video models are "short-sighted" and reactive, optimizing for immediate visual plausibility rather than reasoning toward a goal state, which limits their usefulness for reasoning and embodied-agent tasks.
**Breakthrough (≤3 sentences):** The authors report two mechanisms: asymmetric attention masking that lets a predicted goal frame guide intermediate state generation without interference, and a future-representation self-alignment objective (training-time only) that encourages hidden states to anticipate upcoming dynamics. They report consistent gains across visual reasoning benchmarks while using only 25% of the training steps needed by standard autoregressive baselines.
**Tools & method (≤3 sentences):** The method builds on autoregressive video diffusion/generation models, adding goal-frame conditioning via asymmetric attention masks and a lightweight future-state predictor used only during training.
**Limitation (≤3 sentences):** The abstract does not state explicit limitations beyond motivating the short-sightedness problem the method addresses; no code/weights release was confirmed from the available content.

## DuoMatching: Joint-Marginal Distribution Matching for Few-Step Video Generation
- **arXiv:** 2610.03543 · https://arxiv.org/abs/2610.03543
- **Submitted:** 2026-10-02
- **Authors:** Jiahao Zhan, Yan Wang, Yongrui Ma, Qunliang Xing, Ruchang Yao, Runtao Liu, Shijie Zhao, Tianfan Xue
- **Qualifying affiliation(s):** ByteDance — Jiahao Zhan, Yan Wang, Yongrui Ma, Qunliang Xing, Shijie Zhao (joint CUHK MMLab / ByteDance Inc. affiliations; Shijie Zhao is ByteDance-only corresponding author)
- **Categories:** cs.CV
- **Open release:** demo/project page (https://johnzhan2023.github.io/DuoMatching/); no explicit code/weights release confirmed
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** DuoMatching is a distillation framework for few-step video generation that combines joint distribution matching (video-level) with marginal distribution matching (frame-level, supervised by an image generator) to improve visual quality and semantic coherence. It introduces LatentBridge to reconcile latent-space mismatches between video and image models, and Latent Variation Sampling to spread frame-level supervision across temporal segments.
**Purpose (≤3 sentences):** Existing few-step video distillation methods that rely solely on joint (video-level) distribution matching can suffer from limited visual quality and semantic coherence because they lack strong frame-level supervision.
**Breakthrough (≤3 sentences):** The authors report that adding image-generator-supervised marginal matching, via the new LatentBridge and Latent Variation Sampling components, yields human-preference rates above 80% against all evaluated baselines, with gains in visual quality, composition, and semantic alignment while motion dynamics are preserved throughout the sequence.
**Tools & method (≤3 sentences):** The method combines a video distribution-matching distillation objective with frame-level supervision from a separate image generator, bridged via LatentBridge, and samples supervision across time via Latent Variation Sampling.
**Limitation (≤3 sentences):** The abstract does not explicitly state limitations or failure cases.

# Near-misses
- 2610.03632 · World Embedding Benchmark · no industry author (all affiliations academic: University of Manchester, Hong Kong Polytechnic University, Zhejiang University, TU Darmstadt, University of Macau, University of Oxford, Nanyang Technological University, Shanghai University of Finance and Economics)
- 2610.03453 · I2CD: Direct Image-to-Convex Decomposition for Simulation-Ready Collision Geometry · no industry author (all authors affiliated with Yale University; screen's "Google, Tencent" guess not supported by HTML affiliations)
- 2610.03162 · Budgeted-GS: Real-Time Large-Scale Gaussian Splatting via Factoring LOD · no industry author (sole author affiliated with Neusoft, which is not on the qualified-company list; screen's "ByteDance" guess not supported)
- 2610.03154 · Does Physics Live in the Activations? Localizing Physical Quantities in Video Diffusion Models · affiliation unverifiable: no HTML version (arxiv.org/html/2610.03154 and v1 both return 404; no PDF fallback used per instructions)
- 2610.03120 · In-Distribution Forcing for Long Video Generation at Test Time · no industry author (all authors affiliated with Korean/academic institutions: Sungkyunkwan University, Korea University, Georgia Institute of Technology, Seoul National University, KAIST; screen's "Google, Kuaishou" guess not supported by HTML affiliations)
