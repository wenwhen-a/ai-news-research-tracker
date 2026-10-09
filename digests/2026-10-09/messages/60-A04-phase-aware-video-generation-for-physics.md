**[A04] Phase-aware video generation for physics-grounded dynamics and interactions (PAVG)**
- **arXiv:** 2610.11791 · <https://arxiv.org/abs/2610.11791>
- **Submitted:** 2026-10-08 (v1)
- **Authors:** Jingfeng Ou, Kun Wang, Rui Zhao, Jingwei Guan, Limin Wang, Chao Dong, Xingyu Zeng
- **Qualifying affiliation(s):** SenseTime — Kun Wang, Rui Zhao (flag: SenseTime is not on the default list but is a large, publicly listed Chinese AI company comparable to the tracked tier; kept and flagged). Other authors: Nanjing University, Shenzhen University of Advanced Technology (academic).
- **Categories:** cs.CV
- **Open release:** none stated in the abstract
- **Shipped counterpart:** none found

**Summary:** The paper targets physically plausible video generation for scenes where solids and gases behave differently but interact (e.g., smoke, fire, water with solid objects). The authors propose PAVG, a phase-aware generator with a dual-branch architecture that models solid and gas dynamics separately.
**Purpose:** To overcome the limits of single-branch video generators that cannot represent the distinct dynamics of solids versus gases within one interacting scene.
**Breakthrough (≤3 sentences, attributed):** The authors report that PAVG improves motion adherence, physical plausibility, and visual quality over existing approaches, trained on a purpose-built simulation corpus of over 700K physical trajectories covering solid, gas, and solid-gas interaction scenarios.
**Tools & method:** Dual-branch architecture modeling solid and gas dynamics separately, with spatiotemporal cross-attention to capture their interaction; trained on the authors' 700K+-trajectory simulation dataset.
**Limitation:** Not stated in the available abstract text; not independently verified beyond the abstract.
