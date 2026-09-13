**[A65] ES3D: Embedding Semantics into 3D Space for Component-Aware Editing**
- **arXiv:** 2608.15749 · https://arxiv.org/abs/2608.15749
- **Submitted:** 2026-08-16
- **Authors:** Xuancheng Jin, Rengan Xie, Jiayuan Lu, Wenting Zheng, Rui Wang, Yuchi Huo, Lincheng Li, Yingfeng Chen
- **Qualifying affiliation(s):** NetEase Fuxi AI Lab — Wenting Zheng, Yingfeng Chen
- **Categories:** cs.CV
- **Open release:** none
- **Shipped counterpart:** none found

**Summary:** ES3D embeds semantics directly into 3D space to enable component-aware retrieval and editing of a 3D asset, conditioned on one or more local reference images and an optional text query.
**Purpose:** Finer component-level control over 3D asset editing than text-only methods, with a local reference image specifying which part to change.
**Breakthrough:** The authors report CLIP score 32.19 (versus 29.02 IP-Adapter, 29.38 TRELLIS, 30.29 Fuse3D), ImageReward 0.5853 and CD_keep 0.91e-3 (versus 13.12 / 11.25 / 9.87), and a user study rating 4.4 to 4.8 out of 5 on quality, accuracy and preservation.
**Tools & method:** 3D semantic embeddings from multi-view feature projection; semantic component retrieval; inpainting-based editing with an "image stacking" strategy bridging local conditioning and global training.
**Limitation:** The authors state voxel-level retrieval produces noisy boundaries that need clustering for stable component identification.
