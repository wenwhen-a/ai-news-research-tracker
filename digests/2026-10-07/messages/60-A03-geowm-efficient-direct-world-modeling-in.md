**[A03] GeoWM: Efficient Direct World Modeling in Explicit Geometry**
- **arXiv:** 2610.07381 · <https://arxiv.org/abs/2610.07381>
- **Submitted:** 2026-10-05
- **Authors:** Mehrdad Noori et al.
- **Qualifying affiliation(s):** Huawei Noah's Ark Lab, Canada — all authors; FLAG: borderline (Huawei is on the SKILL.md "genuinely unsure" list, kept per instructions rather than dropped)
- **Categories:** cs.CV
- **Open release:** none
- **Shipped counterpart:** none found

**Summary:** Modeling 3D scene geometry and its evolution over time is central to autonomous driving and robotics, but the common world-model paradigm of predicting future images or latent representations and then recovering geometry does not explicitly model geometric structure and relies on recursive rollouts that accumulate error and cost.
**Purpose:** The paper aims to forecast 3D scene geometry (depth, camera pose, geometric structure) at arbitrary future horizons more accurately and efficiently than recursive, image/latent-based world models.
**Breakthrough:** The authors report that GeoWM outperforms the video- and feature-based world models they evaluated on forecasting depth, camera pose, and 3D scene geometry across four datasets spanning urban driving, aerial flight, and dynamic manipulation, while substantially reducing inference time at longer horizons; they also show a lightweight camera-motion predictor can accurately estimate the future viewpoint to condition this forecast.
**Tools & method:** A geometry foundation model converts observed RGB frames into a geometric history; a flow-matching transformer conditions on this history to predict scene geometry at a specified horizon; a lightweight camera-motion predictor estimates the future viewpoint, and the observed geometry is projected into that predicted viewpoint as a prior for the forecast.
