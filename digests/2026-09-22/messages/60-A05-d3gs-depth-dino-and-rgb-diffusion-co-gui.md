**[A05] D3GS: Depth, DINO, and RGB Diffusion Co-Guided 3D Gaussian Splatting for Sparse-View Reconstruction**
- **arXiv:** 2609.22941 · <https://arxiv.org/abs/2609.22941>
- **Submitted:** 2026-09-19
- **Authors:** Yunqi Gao, Zhanfeng Liao, Hanzhang Tu, Zhaoqi Su, Guoqing Zheng, Songtao Wang, Hongwen Zhang, Zhou Xue, Leyuan Liu, Yebin Liu
- **Qualifying affiliation(s):** ByteDance Inc. — Zhou Xue
- **Categories:** cs.CV
- **Open release:** none stated
- **Shipped counterpart:** none found

**Summary:** D3GS is a 3D Gaussian Splatting method for reconstructing scenes from only a few input views, combining metric depth estimation, DINO-feature-guided multi-view consistency, and diffusion-based novel-view refinement.
**Purpose:** Sparse-view 3D Gaussian Splatting suffers from ambiguous geometry, cross-view inconsistency, and missing detail in regions under-constrained by the few available views, which degrades reconstruction quality and rendering stability.
**Breakthrough:** The authors report that combining (1) high-resolution metric depth recovered via diffusion-based completion and DPT refinement, (2) DINOv3-feature-based multi-view consistent supervision, and (3) single-step diffusion refinement of rendered novel views fed back into the Gaussians, yields consistent gains over baselines such as CoR-GS, BinocularGS and Difix3D+.
**Tools & method:** The pipeline uses MapAnything and bundle adjustment for sparse metric depth, a denoising U-Net plus DPT decoder for high-resolution metric depth completion, DINOv3 features (top-3 PCA components) attached to each Gaussian for cross-view consistency, and a single-step diffusion model fine-tuned on the SynCamMaster dataset for iterative novel-view refinement.
**Limitation:** The authors acknowledge computational overhead of roughly 25 minutes per scene from depth estimation, feature extraction and diffusion processing combined.
