**[A01] TriFold: Folding irregular 3D Gaussians into structured latents for 3D Scene Generation**
- **arXiv:** 2610.23050 · <https://arxiv.org/abs/2610.23050>
- **Submitted:** 2026-10-16 (v1)
- **Authors:** Yun Wang et al.
- **Qualifying affiliation(s):** Alibaba Group (AMAP) — Chiyu Wang, Fan Jiang, Ziyu Zhu, Zhaoxu Sun, Mu Xu (Yun Wang interned at AMAP; Wang and Wu are City University of Hong Kong)
- **Categories:** cs.CV
- **Open release:** none (project page only, <https://fantasy-amap.github.io/TriFold>; no code/weights release stated)
- **Shipped counterpart:** none found

**Summary:** TriFold is a variational autoencoder that folds the irregular, variable-count primitives of a 3D Gaussian Splatting scene into a fixed-size triplane latent, enabling standard latent generative modeling over 3DGS scenes.
**Purpose:** It addresses the mismatch between 3DGS scenes' irregular, variable-length Gaussian sets and the fixed-shape tensors latent generative models require, where prior fixed-budget, voxel, or field-based approaches struggle with density variation or high-frequency attributes.
**Breakthrough:** The authors report a 5.15 dB PSNR gain in reconstruction over the GaussianGPT baseline (26.55 vs 21.40 dB, with lower LPIPS and Chamfer Distance) on InteriorGS and the Aria Synthetic Environments subset of SceneSplat-49K, and demonstrate point-cloud-conditioned and single-image amodal scene generation via a trained latent flow-matching model.
**Tools & method:** A modified Point Transformer V3 encoder with learned per-cell queries projects Gaussians onto three planes with sparse cross-plane attention and a variational bottleneck; a DETR-style set decoder with optimal-transport matching reconstructs variable Gaussian counts per voxel, trained on AMD MI308X GPUs with occupancy, OT-center, rendering, and phantom-voxel losses.
