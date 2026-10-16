**[A04] SUPRA-TEX: 3D Generation with Super-Aligned Texture**
- **arXiv:** 2610.22352 · <https://arxiv.org/abs/2610.22352>
- **Submitted:** 2026-10-15 (v1, 17:58:02 UTC)
- **Authors:** Chen Yang et al.
- **Qualifying affiliation(s):** Huawei Inc. — Chen Yang, Jiemin Fang, Fanpeng Meng, Zihao Huang, Jichen Pang, Guanjun Wu, Zhikuan Bao, Qi Tian (additional academic affiliations: Shanghai Jiao Tong University, Huazhong University of Science and Technology); **FLAG: borderline** (Huawei). Note: screening had flagged "Tencent Hunyuan3D Team" as a possible co-author affiliation — verified this is **false**; Tencent Hunyuan3D only appears as a cited baseline/related-work comparison (Hunyuan3D 2.1), not as an author affiliation. The real affiliation on this paper is Huawei Inc.
- **Categories:** cs.CV (primary), cs.GR
- **Open release:** weights, code (paper states "Code and checkpoints are released on our project page" at supra-3d.github.io/supratex)
- **Shipped counterpart:** none found

**Summary:** SUPRA-Tex is a single-image 3D texturing method that estimates relightable materials (albedo, metallic-roughness) for the visible surface of a given mesh, aligns them precisely to that surface, and completes unobserved regions.
**Purpose:** The paper targets a failure mode of prior single-image 3D generators: fine reference details such as text, logos, and patterns are not faithfully reproduced at their correct visible-surface locations, and hidden regions are completed inconsistently.
**Breakthrough:** The authors report shaded PSNR of 30.89/30.05 (DTC-Tex/Complex-Tex) for given-geometry texturing versus 29.19/28.84 for the Pixal3D⋆ baseline, and LPIPS of 0.025/0.029 versus 0.071/0.070 for the same baseline in the end-to-end setting.
