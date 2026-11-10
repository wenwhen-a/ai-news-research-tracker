**[A01] Spaghetti Splatting: Differentiating Curvilinear Dirac Masses via Convolution**
- **arXiv:** 2611.12716 · <https://arxiv.org/abs/2611.12716>
- **Submitted:** 2026-11-09
- **Authors:** George Shramko et al.
- **Qualifying affiliation(s):** Wayve Labs — Shrisudhan Govindarajan, Daniel Rebain, Andrea Tagliasacchi (FLAG: borderline — Wayve is a well-funded autonomous-driving AI company, not on the main tracked list)
- **Categories:** cs.CV, cs.GR
- **Open release:** code (authors state they "commit to fully release code" and mention a project webpage, but no URL is given in the paper)
- **Shipped counterpart:** none found

**Summary:** The paper introduces "Spaghetti Splatting," a method for learning curve-like (curvilinear) 3D primitives directly from images via differentiable volume rendering, extending the convolution-based formulation used in EWA splatting and 3D Gaussian Splatting to one-dimensional, infinitely-thin geometry.
**Purpose:** Existing splatting methods struggle to represent curve-like structures (hair, fur, thin strands) because such primitives are infinitely thin and poorly suited to Gaussian "blob" kernels.
**Breakthrough:** The authors report their formulation is a strict superset of 3D Gaussian Splatting (points are zero-length curves), supports kernels beyond Gaussians (e.g., Beta kernels), and yields native anti-aliasing plus long connected strands suitable for physics simulation.
**Tools & method:** Evaluated on Mip-NeRF 360 (standard unbounded-scene benchmark), plus Shelly (synthetic fur/wool/leaves), Fuzzy (captured fibrous objects), and GeomHair (400 strand-level hairstyles from head scans); hair renders use a Yuksel curly-hair model with GeomHair scenes path-traced in Blender.
**Limitation:** The authors state that reproducing fine texture currently requires many short segments, and real hair reconstruction remains challenging.
