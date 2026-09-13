**[A46] Photorealistic Novel View Synthesis of Human Faces using Next-Scale Transformers**
- **arXiv:** 2608.23410 · https://arxiv.org/abs/2608.23410
- **Submitted:** 2026-08-24
- **Authors:** Federico Stella, Fei Jiang, Zhongshi Jiang, Zohar Barzelay, Emanuel Garbin, Amin Jourabloo, Liuhao Ge
- **Qualifying affiliation(s):** Meta (Reality Labs) — Fei Jiang, Zhongshi Jiang, Zohar Barzelay, Emanuel Garbin, Amin Jourabloo, Liuhao Ge (Federico Stella, EPFL, as a Meta Reality Labs intern)
- **Categories:** cs.CV, cs.LG
- **Open release:** none
- **Shipped counterpart:** none found

**Summary:** Adapts next-scale autoregressive transformers to synthesise multi-view-consistent novel views of human faces at 512x512 from synthetic training data, coupled with a pixel-aligned 3D Gaussian lifting model for face reconstruction.
**Purpose:** Higher-resolution, cross-view-consistent face renderings without large 2D pretraining sets, usable to drive 3D Gaussian face reconstruction.
**Breakthrough:** On the PSGS dataset (6 canonical views) the authors report their best variant reaching PSNR 23.13, SSIM 0.8816, LPIPS 0.1762 and DreamSim 0.01379, versus PSNR 16.75 / SSIM 0.79 for FaceLift-NVS.
**Tools & method:** Three-stage training for high-resolution convergence; the proprietary SS3D dataset (about 2M textured objects), PSGS (3.2K subjects) and the public Ava-256 dataset (256 subjects, 80 dome cameras); 64 to 128 NVIDIA A100 GPUs.
**Limitation:** The authors state the method struggles with unseen expressions and accessories such as hats because training data is limited to neutral expressions, and that background colour bleeding remains an issue.
