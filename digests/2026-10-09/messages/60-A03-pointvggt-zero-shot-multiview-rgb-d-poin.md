**[A03] PointVGGT: Zero-Shot Multiview RGB-D Point Cloud Registration with Visual Geometry Foundation Priors**
- **arXiv:** 2610.11612 · <https://arxiv.org/abs/2610.11612>
- **Submitted:** 2026-10-08 (v1)
- **Authors:** Haobo Jiang, Liang Yu, Jianmin Zheng
- **Qualifying affiliation(s):** Alibaba Group — Liang Yu. Other authors: Nanyang Technological University, Singapore (academic).
- **Categories:** cs.CV
- **Open release:** none stated in the abstract
- **Shipped counterpart:** none found

**Summary:** The paper addresses registering unordered multiview RGB-D scans into one metrically consistent coordinate frame. It argues the standard pairwise-then-global pipeline suffers from locally optimized matches, error accumulation, and high cost.
**Purpose:** To provide a training-free, zero-shot registration method that avoids per-scene optimization and pairwise pose estimation.
**Breakthrough (≤3 sentences, attributed):** The authors report strong zero-shot accuracy and efficiency on indoor, object-centric, and outdoor datasets using a "foundation-then-refinement" two-stage pipeline built on the VGGT visual-geometry foundation model.
**Tools & method:** Stage 1 anchors VGGT's scale-ambiguous pose predictions to metric depth to recover global poses without pairwise estimation; Stage 2 uses voxelized spatial hashing for near-linear-time dense correspondence, refined by a motion-only bundle adjustment solved with conjugate gradient.
**Limitation:** Not stated in the available abstract text.
