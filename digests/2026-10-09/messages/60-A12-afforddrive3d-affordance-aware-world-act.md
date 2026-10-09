**[A12] AffordDrive3D: Affordance-Aware World-Action Modeling with Spatial Understanding**
- **arXiv:** 2610.11060 · <https://arxiv.org/abs/2610.11060>
- **Submitted:** 2026-10-08 (v1)
- **Authors:** Tianhui Cai, Xinglong Sun, Chao Fang, Zhenxin Li, Rui Song, Jose M. Alvarez, Yunxiang Mao, Jiaqi Ma, Langechuan Liu
- **Qualifying affiliation(s):** NVIDIA — listed among the paper's affiliations, with a footnote noting "work done during an internship at NVIDIA" and co-author Jose M. Alvarez (a known NVIDIA research manager); the HTML extraction could not confirm the exact superscript-to-author mapping. Also 42dot by Hyundai — Hyundai's autonomous-driving subsidiary (flag: not on the default list but comparable to a top-tier industry lab; kept and flagged). Other authors: UCLA, Fudan University (academic).
- **Categories:** cs.CV (primary); cs.AI (cross-listed)
- **Open release:** none stated in the abstract
- **Shipped counterpart:** none found

**Summary:** The paper addresses world-action models for autonomous driving that jointly predict future scenes and generate trajectories. It argues dense-geometry prediction alone shows scene layout but not which regions matter for the ego vehicle's actions.
**Purpose:** To jointly model future action-relevant regions (e.g., drivable areas, collision-critical zones) together with spatial geometry, rather than relying on appearance or geometry alone.
**Breakthrough (≤3 sentences, attributed):** The authors report state-of-the-art results on the NAVSIM benchmark of 91.3 PDMS and 89.9 EPDMS.
**Tools & method:** AffordDrive3D uses a VLM backbone for scene semantics and driving context, predicts future geometry from RGB world-model latents, and jointly learns action-relevant affordance regions.
**Limitation:** Not stated in the available abstract text.
