**[A17] Mira-Scene: Pixel-Aligned Layouts for Generative 3D Scene Reconstruction**
- **arXiv:** 2609.23796 · <https://arxiv.org/abs/2609.23796>
- **Submitted:** 2026-09-20
- **Authors:** Yang-Tian Sun et al.
- **Qualifying affiliation(s):** VAST — co-authors (paper's affiliation footnote lists "The University of Hong Kong" and "VAST"; per-author numeric mapping not resolved from the rendered HTML); FLAG: borderline
- **Categories:** cs.CV, cs.GR
- **Open release:** none confirmed (project page <https://sunyangtian.github.io/Mira-Scene-web/> now redirects to <https://vast-ai-research.github.io/eden-page/?p=mira-scene;> no code/weights link found in the paper text itself)
- **Shipped counterpart:** none found

**Summary:** Mira-Scene reconstructs compositional 3D scenes from a single image by replacing sparse object-pose regression with dense, pixel-aligned correspondence recovery via a "Canonical Coordinate Map." A multimodal diffusion transformer jointly generates object geometry and these coordinate maps, which are then used to assemble the full scene.
**Purpose:** Single-image compositional 3D scene reconstruction requires placing high-fidelity 3D objects into a coherent scene layout, but existing sparse-pose-regression approaches to layout are hard to learn and generalize poorly given limited scene-level supervision.
**Breakthrough:** The authors report relative gains of 39.8% in 3D-IoU (0.520 → 0.727) and 16.5% in 2D-IoU (0.672 → 0.783) over SAM3D on the BlendSwap benchmark, while maintaining competitive object geometry (Chamfer Distance 0.021) with substantially less training data.
