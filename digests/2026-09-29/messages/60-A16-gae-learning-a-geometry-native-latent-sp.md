**[A16] GAE: Learning a Geometry-Native Latent Space for 3D-Consistent World Generation**
- **arXiv:** 2609.24981 · <https://arxiv.org/abs/2609.24981>
- **Submitted:** 2026-09-21
- **Authors:** Jiahao Lu et al.
- **Qualifying affiliation(s):** Tencent (ARC Lab, Tencent IEG) — Minghao Yin, Wenbo Hu, Wang Zhao, Ying Shan
- **Categories:** cs.CV
- **Open release:** none confirmed (project page only: <https://jiah-cloud.github.io/GAE.github.io/;> no code/weights link stated)
- **Shipped counterpart:** none found

**Summary:** GAE (Geometry-Native Autoencoder) is a latent representation for video/scene generation that is decodable to appearance, depth, cameras, and point maps, aiming to give generative models a geometry-aware latent space instead of a purely appearance-focused one.
**Purpose:** Visual generators often fail to maintain 3D consistency across viewpoints because they operate on appearance-centric latents while perception models use geometry-rich representations; the authors argue "perception and generation should instead share a geometry-native latent space."
**Breakthrough:** The authors report that using GAE latents reduces FVD by 12.7% on RealEstate10K and 23.1% on DL3DV, and roughly halves camera-trajectory error versus the strongest competing latent, while GAE-64 achieves 0.0034 ATE on RealEstate10K (a 52.8% improvement) and a 0.1208 MEt3R score.
**Tools & method:** GAE is trained in two stages: a codec stage that compresses frozen DA3 geometry-foundation-model features (four hierarchical levels, 3,072 raw channels) into a compact 64-128 channel latent decodable to RGB and geometry, followed by a flow-training stage that trains conditional flow matching for generation tasks in that latent space; it is evaluated on RealEstate10K and DL3DV at 256² (held-out 64-scene pool, 9 views/scene) and with 81-view rollouts at 672x378 in qualitative demos.
