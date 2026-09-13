**[A35] CoGeo-GS: Concept-Driven and Geometry-Aware Multi-Object Removal in 3D Scenes**
- **arXiv:** 2608.26656 · https://arxiv.org/abs/2608.26656
- **Submitted:** 2026-08-27
- **Authors:** Yuanxiang Ni, Xianliang Huang, Chenhang Ma, Chen Xiao, Yuewen Ma, Ruxin Wang, Hao Zhang
- **Qualifying affiliation(s):** ByteDance (PICO) — Xianliang Huang, Yuewen Ma
- **Categories:** cs.CV, cs.AI
- **Open release:** none
- **Shipped counterpart:** none found

**Summary:** A framework for removing several objects from a 3D Gaussian Splatting scene in one optimisation stage, using concept-aware semantic tagging of Gaussians and a depth-guided completion pipeline that combines monocular depth priors with diffusion-based refinement.
**Purpose:** Geometrically consistent, multi-view coherent removal of multiple objects, addressing occlusion and semantic-entanglement failures of single-object methods.
**Breakthrough:** For multi-object removal the authors report PSNR 28.9 versus 25.6 for the best baseline, SSIM 0.882 versus 0.821, LPIPS 0.086 (a 56.6% improvement) and FID 11.4 (a 50% improvement); single-object removal reaches PSNR 30.7 / SSIM 0.903 / LPIPS 0.072 / FID 9.8.
**Tools & method:** Evaluated on Mip-NeRF 360 and SPIn-NeRF with 30k iterations on one NVIDIA RTX 4090; accepted at ICME 2026.
**Limitation:** The authors state that reliable multi-object removal remains challenging under occlusion and semantic entanglement; specific failure cases are not detailed.
