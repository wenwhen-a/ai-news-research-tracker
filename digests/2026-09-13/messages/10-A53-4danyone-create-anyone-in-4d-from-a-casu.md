**[A53] 4DAnyone: Create Anyone in 4D from a Casual Monocular Video**
- **arXiv:** 2608.20335 · https://arxiv.org/abs/2608.20335
- **Submitted:** 2026-08-20
- **Authors:** Yudong Jin, Tao Xie, Qihang Zhang, Zehong Shen, Zhen Xu, Yujun Shen, Hujun Bao, Xiaowei Zhou, Yinghao Xu
- **Qualifying affiliation(s):** Ant Group — Zehong Shen; FLAG: borderline
- **Categories:** cs.CV
- **Open release:** code (project page https://4danyone.github.io)
- **Shipped counterpart:** none found

**Summary:** Reconstructs 4D humans from uncalibrated casual monocular video by generating multi-view-consistent videos and lifting them into 4D Gaussian Splatting.
**Purpose:** Reconstruction-grade 4D human capture from a single handheld camera, addressing context-length and viewpoint-count limits of prior multi-view generation.
**Breakthrough:** The authors report PSNR 24.15 on DNA-Rendering (versus 20.55 for ReCamMaster and 20.38 for MV-Performer), SSIM 0.863, LPIPS 0.159, and PSNR 23.28 / SSIM 0.846 / LPIPS 0.117 on DyMVHumans.
**Tools & method:** Reference Context Packing compresses context from O(N) to O(1) and Target Context Routing shares context across groups during denoising; trained on MVGameHuman (38k videos, 24 cameras, 318 actors), DNA-Rendering (51k videos) and monocular data on 128 H20-3E GPUs.
**Limitation:** The authors state the model struggles with loose garments far from the body and inherits skeleton-estimation errors.
