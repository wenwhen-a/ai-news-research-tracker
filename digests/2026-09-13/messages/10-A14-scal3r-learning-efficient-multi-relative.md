**[A14] Scal3R: Learning Efficient Multi-Relative Pose Query for Scalable Online 3D Reconstruction**
- **arXiv:** 2609.04201 · https://arxiv.org/abs/2609.04201
- **Submitted:** 2026-09-03
- **Authors:** Chin-Yang Lin et al.
- **Qualifying affiliation(s):** NVIDIA — Cheng Sun, Fu-En Yang, Min-Hung Chen (Chin-Yang Lin dual-affiliated NVIDIA / NYCU)
- **Categories:** cs.CV
- **Open release:** none stated (project page https://linjohnss.github.io/scal3r/)
- **Shipped counterpart:** none found

**Summary:** Scal3R reformulates online 3D reconstruction as multi-reference relative pose querying: lightweight learnable tokens (about 1% of parameters) are injected into a frozen CUT3R or STream3R backbone via asymmetric attention to query poses relative to several past keyframes, with an online pose-graph optimiser and loop closure.
**Purpose:** The authors observe that online reconstruction models collapse on long videos because regressing poses against a fixed first-frame anchor extrapolates beyond the training distribution, while per-frame depth stays stable.
**Breakthrough:** The authors report over 60% lower average ATE on KITTI than the online baseline, state-of-the-art results across Virtual KITTI, Sintel, TUM-Dynamic, ScanNet and 7-Scenes, low drift on kilometre-scale sequences, and convergence in 8 hours on a single NVIDIA A100 using only 4-view training samples.
**Tools & method:** Frozen 24-layer CUT3R/STream3R backbones with DINOv2 encoders; visual-prompt tokens; iSAM2 pose-graph optimisation with loop closure; trained on TartanAir (K=3 references in training, 12 at inference; 40 epochs, AdamW, lr 1e-4).
**Limitation:** The authors state performance is bounded by the frozen backbone under occlusion or textureless regions, appearance-based loop closure can miss revisits under extreme viewpoint or illumination change, and keyframe selection and loop detection rely on hand-set thresholds.
