**[A07] Decoding Without a Decoder: Direct Pixel Prediction from Diffusion Transformers**
- **arXiv:** 2611.22287 · <https://arxiv.org/abs/2611.22287>
- **Submitted:** 2026-11-17
- **Authors:** Hansheng Chen, Shengqu Cai, Jan Ackermann, Rayhan Zirvi, Gordon Wetzstein, Xinchen Yan, Leonidas Guibas
- **Qualifying affiliation(s):** FLAG: borderline — Luma AI (Hansheng Chen and Xinchen Yan are listed with "Affiliation: Luma AI" in the HTML author block; other authors are listed with Stanford University / Caltech)
- **Categories:** cs.CV
- **Open release:** project page — <https://hanshengchen.com/dwd> (no code/weights listed)
- **Shipped counterpart:** none found

**Summary:** Latent diffusion models normally need a separate decoder to turn denoised latents into pixels, adding complexity and inference cost.
**Purpose:** To remove the standalone pixel decoder from latent/pixel diffusion pipelines in order to cut inference cost and architectural complexity, without sacrificing (and ideally improving) output pixel quality.
**Breakthrough:** On Wan video generation, the authors report a 23% reduction in warping error along with reduced detail distortion and flickering.
**Tools & method:** Finetune only the last few blocks of a pretrained diffusion transformer; add a linear DWD head trained with pixel-quality losses to directly output pixels, while anchoring the existing denoising head close to its pretrained behavior to preserve the sampling trajectory.
**Limitation:** Neither the abstract nor the comments state explicit limitations; code and weights are not released, only a project page.
