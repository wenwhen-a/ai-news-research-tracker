**[A03] Seeing Both the Forest and the Trees: Reusing Holistic 3D Priors for Part-Decomposed Generation**
- **arXiv:** 2610.21850 · <https://arxiv.org/abs/2610.21850>
- **Submitted:** 2026-10-15 (v1, 13:27:34 UTC)
- **Authors:** Yiqun Zhao et al.
- **Qualifying affiliation(s):** Tencent — Zibo Zhao (other co-authors at The University of Hong Kong, Transengram, and Shenzhen Loop Area Institute). Not borderline. Note: Alibaba, also flagged by screening, is **not** an author affiliation — it appears only in a Figure 1 citation ("Z-Image Team, Alibaba Group (2025)") referring to an image generator used to create input images.
- **Categories:** cs.CV (primary), cs.GR
- **Open release:** demo/project page only (<https://zhao-yiqun.github.io/structparts/>); no code repository found
- **Shipped counterpart:** none found

**Summary:** The paper introduces STRUCTPARTS, a method for part-decomposed 3D generation from a single image that aims to preserve both fine intra-part geometric detail and structural coherence across an object's parts.
**Purpose:** Existing image-conditioned 3D generators capture both detail and coherence but output a single fused mesh, while part-decomposed methods that adapt holistic 3D priors tend to disrupt those priors.
**Breakthrough:** On PartObjaverse-Tiny part-level metrics the authors report CD 0.107 / F@0.05 0.67 / F@0.10 0.77 for StructParts, versus 0.114/0.63/0.75 for a released X-Part baseline and 0.169/0.55/0.69 for an X-Part variant retrained at matched compute budget.
