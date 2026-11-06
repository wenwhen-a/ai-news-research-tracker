**[A03] EgoGeneralist: Unifying Egocentric Action-Video Tasks through Video-Native Modeling**
- **arXiv:** 2611.08477 · <https://arxiv.org/abs/2611.08477>
- **Submitted:** 2026-11-05
- **Authors:** Yanlin Jin et al.
- **Qualifying affiliation(s):** Ant Group (Ant Digital Technologies) — among Yanlin Jin / Bowen Yang / Cheng Zhang / Yifan Yang (other affiliations: Monash University, Institute of Automation, Chinese Academy of Sciences); **FLAG: borderline** — Ant Group is a separate entity from Alibaba Group and is treated here as a comparable top-tier industry lab per the tracker's borderline rule, not as "Alibaba" itself
- **Categories:** cs.CV
- **Open release:** none (project page only, no code/weights stated) — <https://www.neiljin.site/egogeneralist_page/>
- **Shipped counterpart:** none found

**Summary:** EgoGeneralist adapts pretrained video generators to jointly handle action-conditioned egocentric video generation, 3D hand/body pose estimation, and joint action-video generation, using a "role-adaptive action renderer" that represents metric 3D motion as both a controllable signal and a recoverable generation target.
**Purpose:** The paper targets the gap between video generators' strong visual priors and their lack of a native, metric 3D representation of human action, aiming for a single framework spanning five action-video tasks instead of separate task-specific models.
**Breakthrough:** On EgoDex, the authors report hand pose estimation Abs-MPJPE of 27.73mm versus 111.98mm for the HaWoR baseline, and text-to-video PCK of 67.91% versus 35.41% for Wan2.2 Fun-Control; on the HOT3D world-action policy benchmark, mean minimum target distance is 3.81cm versus 6.32cm for VITRA, with 58.59% of trials reaching within 2cm.
