**[A09] ProDyGS: Dynamic Gaussian Splatting from a Single Static Monocular Camera**
- **arXiv:** 2609.32711 · <https://arxiv.org/abs/2609.32711>
- **Submitted:** 2026-09-26
- **Authors:** Ugo Leone Cavalcanti et al.
- **Qualifying affiliation(s):** Sony (Sony Depthsensing Solutions, Brussels) — Andrea Conti, Vladimir Zlokolica, Valerio Cambareri
- **Categories:** cs.CV
- **Open release:** none confirmed (project page only: <https://prodygs.github.io;> no code/weights link stated)
- **Shipped counterpart:** none found

**Summary:** ProDyGS reconstructs dynamic 3D Gaussian Splatting scenes from video captured by a single static (non-moving) monocular camera, a setting where prior dynamic-view-synthesis methods fail due to a complete absence of multi-view geometric cues.
**Purpose:** Dynamic view synthesis normally needs multi-camera rigs or significant camera motion to supply the geometric constraints needed for reconstruction.
**Breakthrough:** The authors report state-of-the-art results on the DyNeRF benchmark using only monocular depth as external supervision, with reported average metrics of PSNR 26.64 / SSIM 0.8806 / LPIPS 0.1110 versus the prior best (MoDGS) at PSNR 22.64 / SSIM 0.8042 / LPIPS 0.1545.
**Tools & method:** The pipeline uses Depth Pro for initial depth estimation plus neural refinement and optical-flow-based temporal consistency, generates synthetic proxy viewpoints via lightweight 3D Gaussian Splatting, and trains a spatio-temporal HexPlane deformation network to warp canonical Gaussians; it is trained and evaluated on the DyNeRF dataset (6 scenes, 18-20 synchronized cameras) plus the Light Field Video dataset, on a single NVIDIA RTX 5090 GPU (~3 hours, 40k steps).
**Limitation:** The paper does not explicitly enumerate limitations in the fetched text; the evaluation protocol depends on COLMAP pose alignment for benchmarking, and overall quality is tied to the reliability of the monocular depth estimator used.
