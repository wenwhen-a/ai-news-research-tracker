**[A16] Rethinking 3D Noise: Learning 3D-Aware Video Priors via Optimization-Free Morphological Perturbations**
- **arXiv:** 2609.03657 · https://arxiv.org/abs/2609.03657
- **Submitted:** 2026-09-03
- **Authors:** Onat Şahin, Mohammad Altillawi, George Eskandar, Carlos Carbone, Ziyuan Liu
- **Qualifying affiliation(s):** Huawei Heisenberg Research Center — Onat Şahin, Mohammad Altillawi, Carlos Carbone, Ziyuan Liu; FLAG: borderline
- **Categories:** cs.CV
- **Open release:** none
- **Shipped counterpart:** none found

**Summary:** Proposes "3D Morphological Perturbations," an optimisation-free regulariser that perturbs each Gaussian's scale, rotation and pruning in 3DGS scenes to create view-consistent corrupted training data, used to inject 3D-aware priors into video diffusion models.
**Purpose:** Sparse-view NeRF/3DGS artefacts need generative "fixers" trained on paired corrupted/clean renders, which previously required costly per-scene re-optimisation.
**Breakthrough:** The authors report removing per-scene 3DGS optimisation from data curation, and, scaled to a 14B-parameter video model via ControlNet, a 12.5% reduction in mean depth error versus image-to-image 3D artefact refiners and up to 8.0% higher robotics manipulation success on 3 of 4 tasks.
**Tools & method:** Per-Gaussian morphological perturbation; a lightweight video-diffusion sandbox plus a 14B video model with ControlNet; downstream robotics manipulation evaluation.
**Limitation:** Gains apply to 3 of 4 manipulation tasks (observed, not stated); the paper's stated limitations were not captured by the fetch.
