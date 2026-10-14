## WorldRecon: Generative Multi-View Mesh Reconstruction for Large-Scale 3D World
- **arXiv:** 2610.18846 · https://arxiv.org/abs/2610.18846
- **Submitted:** 2026-10-13
- **Authors:** Mengchen Zhang, Yang Li, Chunshi Wang, Tong Wu, Chunchao Guo
- **Qualifying affiliation(s):** Tencent (Tencent Hunyuan) — Yang Li, Chunchao Guo (also Mengchen Zhang, Chunshi Wang dual-affiliated with Zhejiang University and Tencent Hunyuan)
- **Categories:** cs.CV
- **Open release:** none (project page only, no code/weights found) — https://kszpxxzmc.github.io/WorldRecon-website/
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** WorldRecon is a generative framework for reconstructing complete, large-scale 3D scene meshes from unposed RGB images. It builds a noisy global point cloud and camera-pose scaffold, splits the scene into overlapping blocks, and extends the TRELLIS.2 generative model to synthesize each block conditioned on local point-cloud crops and relevant image views.
**Purpose (≤3 sentences):** The authors target the problem that existing multi-view reconstruction methods struggle to produce complete, generative (not just depth-fused) meshes across large indoor environments while keeping geometry and materials consistent block-to-block.
**Breakthrough (≤3 sentences):** The authors report that neighbor-aware latent inpainting plus a causal block-generation process let WorldRecon achieve lower Chamfer distance and higher F-score than baselines including VGGT-Ω+TSDF, Murre, MonoSDF, FineRecon, and GenRecon, with claimed generalization from synthetic training to real indoor scenes.
**Tools & method (≤3 sentences):** The model is trained on two synthetic indoor datasets, 3D-FRONT and SAGE-10k (~117k block-level training blocks), using up to 32 NVIDIA GPUs, and evaluated on 30 held-out 3D-FRONT scenes plus 30 real-world ScanNet++ scenes.
**Limitation (≤3 sentences):** The authors state training data covers only indoor scenes, so current applicability "is limited to indoor environments," and the representation uses a single layer of 4m-high blocks, which restricts reconstruction to single-story buildings. They list extending to outdoor and multi-story scenes as future work.

## GAD: Geometry Attention Distillation for Consistent Video Generation
- **arXiv:** 2610.18779 · https://arxiv.org/abs/2610.18779
- **Submitted:** 2026-10-13
- **Authors:** Junfeng Ni, Ziyu Zhu, Fan Jiang, Yu Liu, Chiyu Wang, Jiawei Zhang, Zhaoxu Sun, Mu Xu, Siyuan Huang, Yixin Chen
- **Qualifying affiliation(s):** Alibaba (AMAP, Alibaba Group) — Ziyu Zhu, Fan Jiang, Chiyu Wang, Jiawei Zhang, Zhaoxu Sun, Mu Xu (Junfeng Ni also dual-affiliated, work partly done at AMAP)
- **Categories:** cs.CV
- **Open release:** none (project page only, no code/weights found) — https://fantasy-amap.github.io/GAD/
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** GAD addresses the tendency of video diffusion models to lose stable scene geometry and object structure over time because their video attention fails to find reliable cross-frame correspondences. It distills correspondence patterns from a frozen geometry model's (VGGT-Ω) attention into the video model's attention on clean videos, with the distillation layer chosen adaptively by noise timestep.
**Purpose (≤3 sentences):** The goal is to improve long-range and dynamic temporal consistency in video generation without adding extra inference-time modules or changing model architecture.
**Breakthrough (≤3 sentences):** The authors report that on Wan2.2 5B, GAD raises cross-frame matching accuracy by at least 30% over baseline on two long-range benchmarks (RealEstate10K and DL3DV-10K, 15-second generation) and also improves 5-second dynamic generation on OmniWorld-Game, across three video backbones.
**Tools & method (≤3 sentences):** Training used a 35K-clip corpus with reference correspondences drawn from 50 DL3DV scenes (static) and 30 dynamic scenes from TAPVid-DAVIS, run for 10 epochs on 32 NVIDIA A800 GPUs (inference cost measured on a single A800).
**Limitation (≤3 sentences):** The authors note GAD's training targets come from VGGT-Ω attention, so distillation quality depends on that teacher's own matching ability, especially under occlusion or ambiguous appearance. They also flag that the current noise-timestep-based layer routing is fixed rather than adaptive to training progress, and that extension to autoregressive (causal-attention) video generation is left to future work.

## Urbex: Agentic Spatial Grounding for City-Scale 3D Scenes
- **arXiv:** 2610.18356 · https://arxiv.org/abs/2610.18356
- **Submitted:** 2026-10-13
- **Authors:** Yu Wang, Rui Dai, Wei Chen, Yi Wang, Bo Dang, Kaikui Liu, Xiangxiang Chu, Yansheng Li
- **Qualifying affiliation(s):** Alibaba (DreamX Team, Alibaba Group) — Kaikui Liu, Xiangxiang Chu (also confirmed via code repo under github.com/AMAP-ML)
- **Categories:** cs.CV, cs.AI
- **Open release:** code — https://github.com/AMAP-ML/Urbex
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** Urbex reframes city-scale 3D visual grounding — locating a referred object in a large outdoor scene from language — as an active search problem rather than ranking precomputed candidate boxes. A vision-language agent explores a multi-view scene representation, zooms into regions and renders oblique views, then commits to a bounding box.
**Purpose (≤3 sentences):** The authors target the slowness and scalability limits of candidate-ranking approaches to 3D grounding once scenes grow to city scale.
**Breakthrough (≤3 sentences):** The authors report the best Hit@1 and IoU on the CityRefer benchmark among compared methods, candidate-free grounding (no ground-truth box proposals needed), and substantially faster inference than the strongest ranking baseline; zero-shot tests on STPLS3D-Refer are reported to show improved cross-scene robustness.
**Tools & method (≤3 sentences):** The tool-use policy is trained with reinforcement learning on CityRefer using localization and exploration-shaping rewards, operating over a bird's-eye-view (BEV) rendering and view-to-world calibration pipeline.
**Limitation (≤3 sentences):** The authors state the method depends on reliable BEV rendering and view-to-world calibration, and that calibration or rendering errors can place a plausible 2D box at the wrong world location. They also note missing or ambiguous landmarks push the agent toward costlier visual search, and that the BEV-aligned output leaves room for finer 3D segmentation, which they suggest addressing with added 3D instance-segmentation tools.

## CityCode: Building Agent-Operable 3D Cities from Sparse Aerial Observations
- **arXiv:** 2610.18342 · https://arxiv.org/abs/2610.18342
- **Submitted:** 2026-10-13
- **Authors:** Jiahui Sun, Ran Bi, Yifei Liu, Xiaolong Zhou, Yishuo Xu, Yuanqi Li, Congcong Zhu, Lei Yang, Yanwen Guo, Zhihang Zhong, Hongjie Zhang
- **Qualifying affiliation(s):** SenseTime — Lei Yang; FLAG: borderline
- **Categories:** cs.CV
- **Open release:** none (authors state a "code supplement" accompanies the paper and that runnable code is planned, but no URL is published)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** CityCode defines a new task of building large-scale, agent-operable 3D city models — metrically scaled, instance-level buildings plus explicit road geometry/connectivity — from a single low-altitude aerial RGB image per region with known camera parameters. The authors' Air2Code method combines structure extraction with adapted metric depth estimation and generative completion to fill occluded or unseen areas.
**Purpose (≤3 sentences):** The goal is a persistent, queryable and editable 3D city representation that downstream agents can inspect, modify and roll back, rather than a static mesh.
**Breakthrough (≤3 sentences):** The authors report that CityCode's representation recovers metric structure more accurately and produces higher visual fidelity than the evaluated baselines on CitySample-Aerial and UrbanScene3D, and that across 50 task chains of 50 steps each it supported querying, editing, planning, and historical state restoration.
**Tools & method (≤3 sentences):** Evaluation uses the CitySample-Aerial and UrbanScene3D datasets; the representation assigns persistent entity identities and supports validated, dependency-aware versioned updates.
**Limitation (≤3 sentences):** The paper has no dedicated limitations section; the closest statement, in the Reproducibility Statement, says end-to-end execution "additionally requires external checkpoints, datasets, API services, and integration components."

## LongForcing: Scaling Temporal Manifold Matching for Long-Horizon World Rollout
- **arXiv:** 2610.18289 · https://arxiv.org/abs/2610.18289
- **Submitted:** 2026-10-13
- **Authors:** Ziyu Zhu, Zhaoxu Sun, Fan Jiang, Mengchao Wang, Junfeng Ni, Ting-Bing Xu, Zhicheng Liu, Mu Xu
- **Qualifying affiliation(s):** Alibaba (AMAP, Alibaba Group) — Ziyu Zhu, Zhaoxu Sun, Fan Jiang, Mengchao Wang, Ting-Bing Xu, Zhicheng Liu, Mu Xu
- **Categories:** cs.CV
- **Open release:** code — https://github.com/Fantasy-AMAP/LongForcing
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** LongForcing targets the drift that autoregressive video-diffusion world models exhibit when rolled out well past their training horizon — degrading visual quality, inconsistent motion, and eroding object identity as generated frames re-enter as context. It keeps existing short-horizon distillation stages but, in the final distribution-matching stage, swaps in a bidirectional teacher that supervises much longer student self-rollouts, adding no architecture change or inference cost.
**Purpose (≤3 sentences):** The authors aim to close the gap between short-horizon training supervision and the long-horizon behavior needed for extended world-model rollouts (e.g., minutes to hours of generated video).
**Breakthrough (≤3 sentences):** The authors report a VBench Quality score of 85.52 on text-to-video generation and a 23.9-point gain on the WorldRoamBench 60-second action score in first-person ablations, plus qualitative rollouts shown out to 24 hours — well beyond the training horizon.
**Tools & method (≤3 sentences):** Training ran for 10 epochs on 32 NVIDIA A800 GPUs; evaluation used VBench and WorldRoamBench, with inference cost measured on a single A800.
**Limitation (≤3 sentences):** The authors state the method's guarantees are conditional on teacher quality and student–teacher mismatch, tied to "the specified model, domain, and action protocol," and that determining a sufficient horizon for a new task requires evaluating these dependencies over the intended deployment duration.

## FlowCred: Hierarchical Credit Assignment and Functional Coordination for Joint Text-to-Video Post-Training
- **arXiv:** 2610.18142 · https://arxiv.org/abs/2610.18142
- **Submitted:** 2026-10-13
- **Authors:** Mingxuan Zhu, Yanwei Huang, Shiyuan Liu, Xinzhi Zhang, Shujie Li, Yuanxing Zhang, Lu Chen
- **Qualifying affiliation(s):** Kuaishou (KlingAI) — KlingAI is listed among the paper's institutions and a footnote confirms "this work was conducted during the author's internship at KlingAI"; the arXiv HTML page strips superscripts, so the exact author-to-institution mapping could not be independently confirmed beyond this
- **Categories:** cs.CV
- **Open release:** none found (paper links to external model pages Lightricks/LTX-2.5 and Qwen3.5-9B, but no project code repo)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** FlowCred addresses two problems in jointly training a prompt-rewriting policy and a video generator on the same terminal reward: prompt-quality credit gets entangled with generation randomness, and the two modules can make redundant, overlapping improvements. It separates credit for the prompt from the generator's residual effect using matched prompt-seed rollouts, and reduces generator updates that an already-accounted-for prompt change would duplicate by testing alternative prompts at intermediate generation states.
**Purpose (≤3 sentences):** The goal is more sample-efficient, better-coordinated post-training of text-to-video systems where both a prompt policy and the generator are being optimized together.
**Breakthrough (≤3 sentences):** On LTX-2.5, the authors report FlowCred raises T2V-CompBench from 61.47 to 64.46 and StoryEval from 55.58 to 58.08 versus a matched joint-training control, without increasing decoded-video or reward-model-call budgets.
**Tools & method (≤3 sentences):** Experiments use the LTX-2.5 video backbone and Qwen3.5-9B as the prompt-policy model, evaluated on T2V-CompBench and StoryEval, with some baselines re-implemented in a common LTX-2.5 harness; main variants were trained for two or three independent runs.
**Limitation (≤3 sentences):** The authors state their mechanism analyses are descriptive checks of trained behavior, not proof of exact causal responsibility, and that the functional-coordination term is only a local, first-order approximation (a minimum-overlap regularizer, not an exact gradient-transfer). With K=4, the response span is finite (at most three columns) and depends on the current prompt policy.

# Near-misses
- 2610.17926 · CineMem: Attention-Aligned Fine-grained Memory Retrieval for Multi-Shot Long Video Generation · no qualifying industry affiliation found (authors affiliated with Shanghai Artificial Intelligence Laboratory, Shanghai Jiao Tong University, East China Normal University, and Fudan University — all academic/non-profit research institutions, no tracked company)
- 2610.17705 · A Differentiable 3D Scene Graph Metric via Contextual Hellinger Triplet Geometry · affiliation unverifiable (no HTML version found at arxiv.org/html/2610.17705 or /2610.17705v1)
- 2610.17692 · SWORD: Scene-Grounded Wasserstein Object-Relation Distance for 3D Scene Graph Prediction · affiliation unverifiable (no HTML version found at arxiv.org/html/2610.17692 or /2610.17692v1)
