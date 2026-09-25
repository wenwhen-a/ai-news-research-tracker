**[A04] M-plicits: Neural Implicit Surfaces via Nested Multiscale Residuals**
- **arXiv:** 2609.28684 · <https://arxiv.org/abs/2609.28684>
- **Submitted:** 2026-09-23
- **Authors:** Vinícius da Silva et al.
- **Qualifying affiliation(s):** Google — Matheus Bessa and André Araújo listed at Google DeepMind (other authors at PUC-Rio, IMPA, University of Coimbra, Universidade Federal de Santa Maria)
- **Categories:** cs.CV, cs.GR, cs.LG
- **Open release:** none stated
- **Shipped counterpart:** none found

**Summary:** The paper targets a tradeoff in neural implicit surface representations for 3D reconstruction from point clouds: single-MLP methods are accurate but slow at inference, while grid-based methods are fast but can overfit noise and limit surface smoothness.
**Purpose:** The authors aim for a representation that keeps single-MLP-style smoothness and noise robustness while approaching grid-based methods' rendering and mesh-extraction speed, without the large parameter counts of grid representations.
**Breakthrough:** On the Stanford and Thingi32 benchmarks, their fine configuration reports the best median Chamfer Distance (1.87E-05) and best IoU (0.867) at 246,627 parameters, versus a coarse configuration's 17,153 parameters; real-time rendering reaches 180 FPS (coarse) and 35–43 FPS (fine) at 512² resolution, with up to 5× faster mesh extraction than a SIREN baseline.
**Tools & method:** The SDF is expressed as a base network plus successively finer residuals (f₃ = f₁ + r₁ + r₂) at increasing SIREN frequencies (ω₀ = 30/45/100), where each residual is trained only within a narrow, adaptively sized band around the previous level's zero-set — "each residual mᵢ is supervised only within this δᵢ-neighborhood" — rather than over the full domain.
