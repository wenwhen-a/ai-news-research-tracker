**[A03] Efficient Confidence-Aware Densification for 3DGS**
- **arXiv:** 2610.13541 · <https://arxiv.org/abs/2610.13541>
- **Submitted:** 2026-10-09 (v1)
- **Authors:** Manuel Hofer et al.
- **Qualifying affiliation(s):** Huawei Technologies (Austria) — Markus Steinberger; FLAG: borderline (Huawei is not on the primary qualified list but is treated as a comparable top-tier industry lab per tracking rules)
- **Categories:** cs.CV (primary), cs.GR
- **Open release:** none found (no code/weights link located in the visible paper text, which was partially truncated)
- **Shipped counterpart:** none found

**Summary:** The paper proposes a confidence-aware densification strategy for fixed-budget 3D Gaussian Splatting, operating within the 3DGS-MCMC framework.
**Purpose:** The authors aim to improve 3DGS reconstruction quality under a fixed primitive budget by making densification decisions more informed than opacity-based heuristics, while remaining compatible with different initialization strategies.
**Breakthrough:** The authors report better PSNR, SSIM, and LPIPS than 3DGS-MCMC averaged over 24 scenes at every tested budget from 100k to 2M primitives, and the highest PSNR and SSIM among fixed-budget methods compared at 500k primitives and above; they also show it can exploit ConeGS or EDGS initializations.
**Tools & method:** Built on the 3DGS codebase with the Faster-GS rasterizer and fused Adam optimizer, evaluated on Mip-NeRF 360, Tanks & Temples, Deep Blending, and DL3DV (24 scenes total), using COLMAP for camera/depth alignment, Depth Anything V2 for background masks, and a VGG backbone for LPIPS; runtime and memory were measured on a single NVIDIA RTX 5090.
