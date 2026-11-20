**[A11] Infer3D: Inverse Generative Modeling Enables Robust 3D Reconstruction**
- **arXiv:** 2611.25061 · <https://arxiv.org/abs/2611.25061>
- **Submitted:** 2026-11-18
- **Authors:** Amani Kiruga et al.
- **Qualifying affiliation(s):** Google DeepMind — Mark Hamilton
- **Categories:** cs.CV, cs.LG, cs.RO
- **Open release:** none found (project website listed: amanikiruga.github.io/infer3d-site; no code/weights release statement found)
- **Shipped counterpart:** none found

**Summary:** Infer3D reframes monocular 3D reconstruction as inverse generative modeling: instead of a feedforward network mapping an image directly to 3D, it searches the latent space of a 2D generative prior (StyleGAN2 or a Diffusion Autoencoder) plus camera/sensor parameters.
**Purpose:** The authors motivate the work by noting humans can infer 3D structure even from unfamiliar viewpoints via top-down generative reasoning, whereas state-of-the-art feedforward 3D reconstruction networks degrade on out-of-distribution scenes.
**Breakthrough:** The authors report Infer3D achieves better OOD reconstruction accuracy than feedforward networks trained on equal or larger datasets, with examples including 18.46 dB vs. 15.73 dB PSNR (Splatter Image) on CO3D Hydrants under OOD viewpoint shift, and 20.29 dB vs. 14.30–15.23 dB on ShapeNet Cars under OOD rotation.
**Tools & method:** The method optimizes latents of a frozen 2D generative prior (StyleGAN2/DiffAE) against a frozen 3D lifter and a Gaussian-splatting renderer, and uses initial reconstruction error as an OOD signal to route only suspicious inputs to the costlier optimization loop.
**Limitation:** The authors report that optimization alone is less accurate than the feedforward lifter on in-distribution data (by about 0.9–2.7 dB depending on dataset), and that reconstruction sharpness is capped by the generative prior, with lighter backbones (StyleGAN2, DiffAE) missing high-frequency detail.
