**[A62] SplatGuide: Geometric Priors from 3D Gaussians for Pose-Free Novel View Synthesis**
- **arXiv:** 2608.16863 · https://arxiv.org/abs/2608.16863
- **Submitted:** 2026-08-17
- **Authors:** Yejun Zhang, Zihan Wang, Xu Ji, Yihao Wang, Yuxin Hou, Junyuan Fang, Juho-Matti Kilpeläinen, Arno Solin, Hamed Rezazadegan Tavakoli, Esa Rahtu, Juho Kannala
- **Qualifying affiliation(s):** Nokia Technologies — Hamed Rezazadegan Tavakoli; FLAG: borderline
- **Categories:** cs.CV
- **Open release:** none
- **Shipped counterpart:** none found

**Summary:** SplatGuide reuses one feed-forward 3DGS reconstruction for three roles in pose-free novel view synthesis: pixel-aligned geometric conditioning, occlusion-aware reference-view selection, and feature-level diffusion guidance.
**Purpose:** Prior pose-free NVS pipelines extract only one signal (depth or a single reference image) from reconstruction.
**Breakthrough:** On RealEstate10K (9-view) the authors report 30.00 PSNR / 0.88 SSIM / 0.04 LPIPS, above the ground-truth-pose baseline SEVA (29.63 PSNR); their visibility-aware selector reaches 28.25 PSNR versus 26.93 for the best baseline selector; out of domain on Mip-NeRF 360 (9-view) it reaches 16.01 PSNR.
**Tools & method:** A per-Gaussian visibility view selector and reconstruction-token feature guidance on a 3DGS backbone; trained on DL3DV (10,510 scenes) and RealEstate10K (67,477 videos) on 8 NVIDIA H200 GPUs.
**Limitation:** The authors state failure modes are correlated because renderings, tokens and view indices share one reconstruction, so textureless surfaces, wide baselines, repetitive structure and dynamic content hurt all three signals; dynamic scenes are called the most significant limitation.
