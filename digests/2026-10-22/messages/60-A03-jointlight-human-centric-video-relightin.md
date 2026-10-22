**[A03] JointLight: Human-Centric Video Relighting with Asynchronous RGB-Irradiance Joint Modeling**
- **arXiv:** 2610.29780 · <https://arxiv.org/abs/2610.29780>
- **Submitted:** 2026-10-21 (v1)
- **Authors:** Henglei Lv et al.
- **Qualifying affiliation(s):** Kuaishou Technology — Xiaoqiang Liu, Haoxian Zhang, Pengfei Wan
- **Categories:** cs.CV; accepted to SIGGRAPH Asia 2026 Conference Papers (DOI 10.1145/3829340.3842252)
- **Open release:** code and dataset stated as "will be publicly released" (not yet released as of this version)
- **Shipped counterpart:** none found

**Summary:** The paper addresses precise illumination control in human-centric video relighting, noting that diffusion-based relighting methods either model light transport implicitly (hurting controllability) or use path-traced irradiance cues directly as control signals (introducing artifacts).
**Purpose:** The authors state existing video relighting approaches lack fine-grained illumination control due to scarce precisely-labeled relighting video datasets and the implicit nature of neural light-transport modeling.
**Breakthrough:** The authors report their model, trained exclusively on their synthetic dataset, generalizes robustly to real-world scenes and outperforms prior approaches in both lighting fidelity and generative quality (per their evaluation against prior methods and HumanOLAT ground-truth comparisons).
**Tools & method:** The method uses asynchronous denoising timestep schedules for RGB vs. irradiance frames, a domain-matching training stage, and an "asynchronous hijacked generation pipeline" at inference; training data is a multi-illumination synthetic video dataset with paired irradiance maps generated via a game engine, evaluated in part against HumanOLAT one-light-at-a-time captures.
