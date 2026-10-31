**[A04] LucidLyra: Feed-Forward Generative 3D Scene Reconstruction and Joint Understanding via Multi-Task Distillation**
- **arXiv:** 2610.40495 · <https://arxiv.org/abs/2610.40495>
- **Submitted:** 2026-10-29
- **Authors:** Oliver Hahn, Rodrigo Marcuzzi, Sangeetha Grama Srinivasan, Alessandro Burzio, Sherwin Bahmani, Jiahui Huang, Stefan Roth, Shengyu Huang, Qunjie Zhou, Laura Leal-Taixé
- **Qualifying affiliation(s):** NVIDIA — Oliver Hahn, Stefan Roth (also Sherwin Bahmani, work done while at NVIDIA)
- **Categories:** cs.CV
- **Open release:** none (project page only: <https://research.nvidia.com/labs/sil/projects/lucidlyra>)
- **Shipped counterpart:** none found

**Summary:** LucidLyra is a feed-forward model that reconstructs a 3D scene as Gaussians while jointly predicting open-vocabulary semantics and class-agnostic instance groupings, all in a single pass from video-diffusion latents.
**Purpose:** The goal is to make generatively reconstructed 3D scenes directly queryable for semantics and object instances, rather than requiring a separate per-scene 3DGS segmentation step bolted onto generative reconstruction.
**Breakthrough:** The authors report that LucidLyra outperforms baselines that combine existing 3DGS segmentation methods with generative reconstruction, while preserving the base reconstruction quality of the underlying "Lyra" system.
**Tools & method:** The method distills knowledge from a camera-controlled video diffusion model (which supplies both latents and training data) and frozen 2D vision foundation models into a single feed-forward Gaussian decoder that jointly predicts geometry, appearance, semantics, and instance cues.
**Limitation:** The authors do not name a specific limitation explicitly; instead they frame remaining work as scaling the approach with accelerated video generation and larger-scale joint training for generation and scene understanding.
