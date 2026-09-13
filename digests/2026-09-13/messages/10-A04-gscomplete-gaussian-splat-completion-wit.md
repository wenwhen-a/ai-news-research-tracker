**[A04] GSComplete: Gaussian Splat Completion with 2D Diffusion Priors**
- **arXiv:** 2609.08449 · https://arxiv.org/abs/2609.08449
- **Submitted:** 2026-09-08
- **Authors:** Elias Brugger, Philipp Erler, Stefan Ohrhallinger, Paul Guerrero
- **Qualifying affiliation(s):** Adobe — Paul Guerrero (Adobe Research, United Kingdom)
- **Categories:** cs.CV
- **Open release:** none (paper states code/dataset "will be made available upon acceptance")
- **Shipped counterpart:** none found

**Summary:** GSComplete completes partial 3D Gaussian-splat objects and scenes by adding new Gaussians in missing regions, guided by 2D diffusion priors through score distillation sampling (SDS) and a text prompt.
**Purpose:** It targets incomplete Gaussian-splat reconstructions (limited viewpoints, occlusions, single-view captures, LiDAR) that leave geometric holes, aiming for a complete representation while keeping the originally observed content unchanged.
**Breakthrough:** The authors report an "input preservation loss" that keeps original splats visible from designated viewpoints while about 5,000 new splats fill gaps, and report better input preservation than MVDream, Trellis, InstantMesh and TripoSG with competitive CLIP-based plausibility scores. They introduce the SplatComplete benchmark of 39 partial Gaussian-splat objects.
**Tools & method:** SDS with 2D diffusion priors over 6,000 optimisation steps; 5,000 new splats initialised spherically around the bounding box with a warm-up phase; evaluated on SplatComplete (multi-view captures, single-view reconstructions, LiDAR scans, synthetic meshes).
**Limitation:** Code and dataset are not yet public (observed, not stated); the paper's own limitations section was not captured by the fetch.
