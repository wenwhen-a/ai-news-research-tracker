**[A61] GS-Voxel: Fitting-Free Structured Latents for Large-Scale 3DGS Generation**
- **arXiv:** 2608.17988 · https://arxiv.org/abs/2608.17988
- **Submitted:** 2026-08-18
- **Authors:** Ming Qian, Zijian Wang, Minchao Sun, Jincheng Xiong, Hang Zhang, Mu Xu, Chi Wang, Baoquan Chen
- **Qualifying affiliation(s):** Alibaba (Amap) — Ming Qian, Zijian Wang, Minchao Sun, Jincheng Xiong, Hang Zhang, Mu Xu
- **Categories:** cs.CV
- **Open release:** none
- **Shipped counterpart:** none found

**Summary:** GS-Voxel converts pre-optimised large-scale aerial 3DGS reconstructions into structured sparse-voxel latents without per-scene refitting, then generates new aerial 3DGS scenes from those latents.
**Purpose:** Million-scale unordered Gaussian primitives create a representation bottleneck for generative modelling of large aerial scenes.
**Breakthrough:** The authors report tile-level FID 28.0 / KID 0.020, geometry-VAE shape IoU 0.99, attribute-VAE PSNR 23.09 / SSIM 0.62 and PSNR 40.04 for direct conversion, and demonstrate generation over 1,400 m x 800 m scenes from 200 m x 200 m training tiles.
**Tools & method:** A factorised two-stage VAE (voxel geometry and local Gaussian attributes) with 0.3B-parameter image-conditioned flow DiTs and overlap-aware tiled inference; about 18,000 training samples from real aerial 3DGS reconstructions.
**Limitation:** The authors state training relies on real reconstructed scenes, that the implementation targets SH0 aerial scenes only, that primitives are discarded in very dense voxels, and that thin structures are hard to preserve.
