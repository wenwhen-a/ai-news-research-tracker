**[A07] FILIGREE3D: Scaling Sparse Latent Flow Matching for Ultra-High-Resolution Image-to-3D Generation**
- **arXiv:** 2609.34900 · <https://arxiv.org/abs/2609.34900>
- **Submitted:** 2026-09-28
- **Authors:** Hongjie Li, Xinran Yang, Xiuchao Wu, Jiangjing Lyu, Chengfei Lv
- **Qualifying affiliation(s):** Alibaba Group — all authors
- **Categories:** cs.CV
- **Open release:** none found (no GitHub, weights, or demo mentioned)
- **Shipped counterpart:** none found

**Summary:** FILIGREE3D generates 3D geometry from a single image at very high voxel resolution (up to 4096^3, evaluated at 2048^3) using sparse latent flow matching with a technique the authors call "Structure-Aware Sparse Scaling." It reports large accuracy gains over Hunyuan3D 2.1 on the Toys4K benchmark.
**Purpose:** The paper targets the computational cost of scaling image-to-3D generation to ultra-high voxel resolutions while retaining fine geometric detail.
**Breakthrough:** The authors report a Chamfer Distance of 0.0055 versus 0.0233 for Hunyuan3D 2.1, and F1-0.002 of 0.5202 versus 0.1011, on Toys4K (537 objects); inference at 2048^3 resolution takes about 84 seconds on an H20 GPU with a 2.2B-parameter, 50,000-token-budget model.
**Tools & method:** Conditioning uses multi-level DINOv2 features from layers 5, 7, 11, and 23, with visibility-aware voxel regularization to differentiate visible from occluded regions during training.
**Limitation:** The paper does not state an explicit limitations section in the fetched content, but notes that single-view reconstruction faces inherent ambiguity for occluded regions, requiring learned shape priors.
