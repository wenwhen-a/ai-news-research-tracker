**[A01] Split-and-scale Latent 3D Representations**
- **arXiv:** 2611.16126 · <https://arxiv.org/abs/2611.16126>
- **Submitted:** 2026-11-12
- **Authors:** Dorian Chan, Muhammed Kocabas, Xiaoming Zhao, Oncel Tuzel, Jen-Hao Rick Chang
- **Qualifying affiliation(s):** Apple — all five authors; paper states all funding came from Apple
- **Categories:** cs.CV (accepted to NeurIPS 2026)
- **Open release:** none (mentions a "supplemental website" with additional generation results, but no code/weight link found in the available text)
- **Shipped counterpart:** none found

**Summary:** Apple researchers propose "split-and-scale," a way to boost the effective capacity of latent 3D representations at inference time without retraining a larger tokenizer.
**Purpose:** Latent 3D representations (for compact scene encoding and 3D generative models) are capacity-limited by latent size; increasing capacity during training is expensive and naively adding latent tokens at inference gives limited gains.
**Breakthrough:** The authors report that split-and-scale at 32,768 inference tokens achieves LPIPS 0.091 versus 0.124 for a 8,192-token LiTo baseline and 0.230 for TRELLIS, and lower Chamfer distance than larger-latent baselines that exceed single-GPU memory.
**Tools & method:** The method splits a scene into n³ voxels, renormalizes each to [-1,1]³, and encodes/decodes them independently with a Perceiver-based tokenizer (built on "LiTo," with Gaussian and point-cloud decoders), skipping empty voxels and training on coarse subdivisions/voxel subsets to control memory.
**Limitation:** The authors note independent voxel encoding can cause seam artifacts (especially in view-dependent highlights), uniform voxel subdivision ignores content complexity, and output Gaussian count grows with subdivision level, hurting rendering efficiency.
