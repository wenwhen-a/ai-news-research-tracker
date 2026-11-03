## Reconstruction as Spatial Evaluation: Diagnosing Cross-View Spatial Intelligence in Large Vision-Language Models
- **arXiv:** 2611.02026 · https://arxiv.org/abs/2611.02026
- **Submitted:** 1 Nov 2026 (v1)
- **Authors:** Junfei Wu, Qiuyue Wang, Xuhong Huang, Qihang Peng, Mingsheng Li, Jian Guan, Qiang Liu, Shu Wu, Liang Wang, Shuai Bai, Tieniu Tan
- **Qualifying affiliation(s):** Alibaba Group (Alibaba Token Hub) — Junfei Wu, Qiuyue Wang, Xuhong Huang, Qihang Peng, Mingsheng Li, Jian Guan, Shuai Bai
- **Categories:** cs.CV (primary), cs.AI
- **Open release:** code — https://github.com/Hyperwjf/ReconSpatial
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper introduces ReconSpatial, a benchmark that diagnoses cross-view spatial intelligence in large vision-language models (LVLMs) by requiring multi-view 3D scene reconstruction in indoor, tabletop, and outdoor settings. Models must predict oriented 3D bounding boxes in a shared metric coordinate frame, scored along structural and metric-accuracy axes. The benchmark also includes nine atomic spatial QA tasks and an offline navigation extension.

**Purpose (≤3 sentences):** The authors aim to diagnose whether LVLMs build coherent, metrically accurate 3D spatial representations across multiple views, rather than only locally plausible single-view outputs. They also test whether such spatial reconstruction ability transfers to downstream spatial QA and navigation tasks.

**Breakthrough (≤3 sentences):** The authors report that across 18 frontier LVLMs, models scored much higher on structural reconstruction than on metric accuracy, with the top model reaching 81.4% on the Structure metric versus 58.7% on the Metric score. They also report that explicit 3D map injection separates scene-construction ability from path-planning ability, and that spatial fine-tuning transfers to other vision-language spatial benchmarks.

**Tools & method (≤3 sentences):** ReconSpatial evaluates models via oriented 3D bounding box prediction in a shared metric coordinate frame across multi-view inputs, nine atomic spatial QA tasks, and an offline open-loop navigation extension. The authors benchmarked 18 frontier LVLMs and released a project repository.

**Limitation (≤3 sentences):** The authors state that objects are modeled only as oriented 3D bounding boxes, omitting fine-grained surface meshes, articulated parts, and continuous free-space occupancy. Navigation evaluation is offline and open-loop within single rooms, leaving closed-loop recovery and multi-room exploration untested. Spatial fine-tuning was evaluated on only one model family.

## Learning-to-Memorize: Dynamic Context Management for Long-Horizon Autoregressive Video Generation
- **arXiv:** 2611.01858 · https://arxiv.org/abs/2611.01858
- **Submitted:** 1 Nov 2026 (v1)
- **Authors:** Haowei Zhu, Qijie Wang, Jia Li, Xing Wang, Tianyu Zhao, Jiexi Wang, Xurui Peng, Xinglong Wu, Junhai Yong, Bin Wang
- **Qualifying affiliation(s):** ByteDance Seed — Haowei Zhu (also Tsinghua University), Jia Li, Xing Wang, Tianyu Zhao, Jiexi Wang, Xurui Peng, Xinglong Wu
- **Categories:** cs.CV
- **Open release:** none found
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper proposes Learning to Memorize (L2M), a learned framework that decides which historical frames to keep, evict, or update during long-horizon autoregressive video generation, operating under a fixed KV-cache budget. It combines an importance-prediction router with degradation-aware training for robustness to noisy context. The work is noted as accepted at NeurIPS 2026.

**Purpose (≤3 sentences):** The authors target the degradation in temporal consistency and quality that long-horizon autoregressive video generation suffers from when context management relies on naive fixed windows or hand-crafted heuristics. L2M aims to replace such heuristics with a learned, importance-based memory policy.

**Breakthrough (≤3 sentences):** The authors report better long-horizon video quality and temporal consistency than existing context-management baselines. This is achieved through a learned importance-prediction router, exponential-moving-average-based memory updates, teacher-student distillation, and sparsity regularization under a fixed cache budget.

**Tools & method (≤3 sentences):** L2M uses a lightweight importance-prediction router to score historical frames, degradation-aware training to make the model robust to noisy retained context, and teacher-student distillation with sparsity regularization to fit a fixed KV-cache budget during autoregressive generation.

**Limitation (≤3 sentences):** The authors state the router adds computational overhead during training and inference, though its lightweight design keeps this cost small. The framework currently operates at the frame level rather than token level, which the authors suggest could improve cache efficiency if addressed. The degradation-aware training also depends on hand-crafted degradation operators rather than degradations learned from real generation errors.

## Xiaomi Auto World Model 2.0: Causal World Models for Real-World Driving and Embodied Intelligence
- **arXiv:** 2611.01677 · https://arxiv.org/abs/2611.01677
- **Submitted:** 1 Nov 2026 (v1)
- **Authors:** Zhenxin Zhu, Zhijian Huang, Cheng Chi, Yuru Wang, Jianhua Wu, Jiayi Guan, Yonggang Li, Mingfei Tu, et al. (23 authors total, credited as the "Xiaomi Auto World Model Team")
- **Qualifying affiliation(s):** Xiaomi (paper authored and titled by the Xiaomi Auto World Model Team; Xiaomi logo on title page; model feeds "Xiaomi's autonomous driving stack") — FLAG: borderline (Xiaomi)
- **Categories:** cs.AI (primary), cs.LG
- **Open release:** demo (project page with videos) — https://xiaomiautoworldmodel.github.io/CausalWorldModel/
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper presents Xiaomi Auto World Model 2.0, a unified streaming causal world model for "Physical AI" that models physical scene evolution and unifies heterogeneous conditioning inputs within a shared representation space for view-consistent generation. It targets both autonomous driving and embodied/robotic manipulation. The authors state generated observations are consumed by Xiaomi's autonomous driving stack for closed-loop testing.

**Purpose (≤3 sentences):** The authors aim to build a single world model that can serve as a simulator for both training and evaluation, and as a component of a World Action Model (WAM) for prediction, policy learning, and action generation in driving and embodied-robotics settings.

**Breakthrough (≤3 sentences):** The authors report that the model supports closed-loop simulation, closed-loop training, and World Action Model applications including world-state prediction, policy learning, and action generation. WorldRec 2.0 reconstructs static and dynamic 3D Gaussians in a single forward pass and uses their renderings as explicit scene context to preserve geometry and appearance during long-horizon generation.

**Tools & method (≤3 sentences):** The architecture integrates View-Temporal Attention and multi-view rotary position encoding to capture cross-view and temporal relationships, with Gated Linear Attention in temporal layers to reduce compute and KV-cache memory during streaming inference. Training proceeds in three stages — pre-training on physical-interaction data and large-scale video, mid-training across varied view configurations, and distillation-based post-training — using self-collected "MiData" together with public datasets such as SpatialVID-HQ, Sekai, and nuScenes.

**Limitation (≤3 sentences):** Not stated in the portions of the paper retrieved; a dedicated limitations section was not located in the parts of the HTML version read for this entry.

## GSExplorer: Interactive World Generation with a Persistent 3D Gaussian World State
- **arXiv:** 2611.01543 · https://arxiv.org/abs/2611.01543
- **Submitted:** 1 Nov 2026 (v1)
- **Authors:** Sicheng Yu, Liu Liu, Xinjie Wang, Xinjiang Wang, Taojun Ding, Wenhao Hu, Beizhen Zhao, Puxin Yan, Zhizhong Su, Hao Wang
- **Qualifying affiliation(s):** Horizon Robotics — Puxin Yan (also The University of Hong Kong; listed as Project Leader) — FLAG: borderline (Horizon Robotics)
- **Categories:** cs.CV (primary), cs.AI
- **Open release:** none found
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** GSExplorer is a framework for interactive world generation that pairs a video generator with a persistent 3D Gaussian Splatting scene representation. A SLAM-based reconstruction backend filters inconsistent generated content and applies cross-chunk bundle adjustment to keep the growing scene coherent. The authors also built a 293K-pair training dataset of degraded renderings paired with real videos.

**Purpose (≤3 sentences):** The authors aim to enable interactive, explorable 3D world generation that maintains a persistent, revisitable scene state, rather than regenerating inconsistent content each time the camera returns to a previously seen location.

**Breakthrough (≤3 sentences):** The authors report the best WorldScore results among compared methods, including a Camera Control score of 99.07 in single-step extrapolation, and strong revisit consistency over 481-frame leave-and-return rollouts.

**Tools & method (≤3 sentences):** The method combines a video generation model with SLAM-based 3D Gaussian Splatting reconstruction, filtering inconsistent generated content and applying cross-chunk bundle adjustment to maintain a persistent 3D Gaussian world state. The authors curated a 293K-pair dataset of degraded renderings and real videos for training.

**Limitation (≤3 sentences):** The authors state the method adds additional runtime compared with purely feed-forward video generation. The current formulation is primarily designed for static or predominantly static environments, with dynamic objects left as future work. Repeated generation and reconstruction cycles may soften very fine textures and small indoor details over long rollouts.

## UniCaMo: Unified Camera and Motion Control for Video Diffusion Models
- **arXiv:** 2611.00810 · https://arxiv.org/abs/2611.00810
- **Submitted:** 31 Oct 2026 (v1)
- **Authors:** Long Vu, Tan Ngo, Animesh Karnewar, Amir Habibian, Binh-Son Hua, Hung Bui, Minh Hoai Nguyen, Phong Nguyen-Ha
- **Qualifying affiliation(s):** Qualcomm AI Research — Long Vu, Tan Ngo, Animesh Karnewar, Amir Habibian, Hung Bui, Minh Hoai Nguyen, Phong Nguyen-Ha. Note: Binh-Son Hua is primarily affiliated with Trinity College Dublin; his contribution is noted as "work done under consultancy capacity" for Qualcomm.
- **Categories:** cs.CV (primary), cs.GR
- **Open release:** none found (reproducibility statement says code, model checkpoints, and datasets "will be publicly available upon acceptance"); project page with qualitative videos: https://phongnhhn.info/Unicamo/
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** UniCaMo is a unified framework for jointly controlling camera motion and object motion in image-and-text-to-video diffusion models. It builds motion-consistent input noise from a reference image, text prompt, sparse 3D object trajectories, and a 3D camera trajectory, without architectural modifications to the base model.

**Purpose (≤3 sentences):** The authors aim to provide unified, precise control over both camera and object motion in video diffusion generation, avoiding the need for dedicated control modules or architectural changes to the base model.

**Breakthrough (≤3 sentences):** The authors report state-of-the-art motion controllability and high visual quality with minimal inference overhead. They state the method requires no architectural modifications or dedicated control modules and can be adapted to pretrained models via lightweight LoRA fine-tuning on a low volume of training data.

**Tools & method (≤3 sentences):** The method constructs motion-consistent input noise through a foreground noise propagation stage guided by 3D point tracks and camera poses, and a spherical noise sampling stage using a coarse 3D sphere proxy for background. It is adapted to pretrained image-and-text-to-video diffusion models via lightweight LoRA fine-tuning.

**Limitation (≤3 sentences):** The authors state the foreground noise propagation stage depends heavily on accurate 3D point tracks and camera poses, so tracking or calibration errors can degrade controllability. The spherical noise sampling stage uses a coarse 3D sphere proxy that may not capture dynamic background geometry. The authors suggest better 3D tracking, depth estimation, and noise representations as future improvements.

# Near-misses
- 2611.01162 · SHield: Watermarking 4D Gaussian Splatting via Spherical Harmonic Coefficient Perturbation · No qualifying industry affiliation: authors are affiliated only with IIIT Hyderabad and Tufts University. The "Seed" match from screening was a random-seed hyperparameter/sensitivity-analysis mention (Appendix A/I), not a ByteDance Seed affiliation.
- 2611.00756 · SceneBound: How Much Should a Streaming 3D Reconstruction Model Remember? · No qualifying industry affiliation: all authors are affiliated with academic institutions only (The Hong Kong University of Science and Technology, Sun Yat-sen University, Monash University, Beihang University, Renmin University of China). The "Google" match from screening was only a "Google Scholar" link in the arXiv page's citation-tools chrome, not a real author affiliation.
