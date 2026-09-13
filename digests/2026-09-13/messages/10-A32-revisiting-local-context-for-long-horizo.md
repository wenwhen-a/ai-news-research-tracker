**[A32] Revisiting Local Context for Long-Horizon Streaming 3D Reconstruction**
- **arXiv:** 2608.27529 · https://arxiv.org/abs/2608.27529
- **Submitted:** 2026-08-27
- **Authors:** Jiarong Han, Jincheng Xiong, Yuzhou Liu, Linzhe Shi, Changjie Wu, Ning Guo, Mu Xu, Hang Zhang, Ming Qian
- **Qualifying affiliation(s):** Alibaba Group (AMAP CV Lab) — all authors
- **Categories:** cs.CV
- **Open release:** code (https://github.com/amap-cvlab/ABot-Recon; project page https://amap-cvlab.github.io/ABot-Recon-html)
- **Shipped counterpart:** none found

**Summary:** ABot-Recon is a streaming 3D reconstruction method that keeps only a 12-frame local temporal window, predicts point maps in the current camera frame plus adjacent-frame relative poses, and recovers global geometry and trajectory by sequential composition.
**Purpose:** Camera-motion and geometry estimation from very long video streams under bounded memory and compute, without persistent learned long-range memory.
**Breakthrough:** The authors report a 40% reduction in RPE-R and 4.35 m ATE on Oxford Spires (4.02 m with loop closure), the lowest average ATE among streaming methods on KITTI, and dense-reconstruction results of 1.37 m Chamfer / 91.81% F1 on Oxford Spires, 0.06 m / 94.88% on 7Scenes and 0.11 m / 92.19% on TUM-Dynamic, at 24.45 FPS with 6.71 GB GPU memory on an H100.
**Tools & method:** A lightweight rotation refiner and composition-aware pose loss; trained on 30 synthetic and real datasets (BlendedMVS, TartanAir, OmniWorld-Game, DL3DV, HyperSim, ScanNet++, ARKitScenes and others) on NVIDIA H20 and AMD MI308 GPUs.
**Limitation:** The authors state gains are "less pronounced" on compact indoor benchmarks where persistent context from frequent revisits helps, and leave dynamic scenes and external memory to future work.
