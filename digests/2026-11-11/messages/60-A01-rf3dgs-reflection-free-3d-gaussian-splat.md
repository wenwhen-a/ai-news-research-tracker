**[A01] RF3DGS: Reflection-Free 3D Gaussian Splatting with Self-Priors**
- **arXiv:** 2611.13772 · <https://arxiv.org/abs/2611.13772>
- **Submitted:** 2026-11-10
- **Authors:** Qiang Wen et al.
- **Qualifying affiliation(s):** Huawei Research — Chenyang Lei (other authors: Hong Kong University of Science and Technology); **FLAG: borderline** (Huawei is not on the core tracked list — per product-criteria.md, kept and flagged as a comparable top-tier lab)
- **Categories:** cs.CV
- **Open release:** none found
- **Shipped counterpart:** none found

**Summary:** RF3DGS removes reflections from 3D Gaussian Splatting reconstructions by exploiting the fact that, across multiple views of the same 3D point, the darkest pixel is usually reflection-free.
**Purpose:** Standard 3D Gaussian Splatting bakes reflections (e.g., off glass) into scene geometry and appearance, producing artifacts; the authors aim to reconstruct clean, reflection-free 3D scenes.
**Breakthrough:** The authors report 31.45 PSNR / 0.150 LPIPS on their new synthetic Unity-based benchmark versus 29.58 PSNR / 0.175 LPIPS for vanilla 3DGS, and 25.04 PSNR / 0.915 SSIM on the real-world TNeRF benchmark versus 22.75 PSNR / 0.841 SSIM for TNeRF itself; they also introduce a new Unity benchmark of 45 reflective-glass test cases varying transparency, glass thickness, and reflection strength.
**Tools & method:** The method fits a vanilla 3DGS model to estimate coarse per-view depth, warps reflection-free content from auxiliary views to build a pseudo-label per reference view, and trains with an "Adaptive Twin Rendering" loss that preserves high-frequency detail; it takes ~60.74 minutes per case on the 88-view benchmark (GPU type not stated in the paper).
