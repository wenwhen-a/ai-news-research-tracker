**[A06] GeoState: Learning View-Decoupled Geometry States for 3D World Modeling**
- **arXiv:** 2610.22343 · <https://arxiv.org/abs/2610.22343>
- **Submitted:** 2026-10-15 (v1, 17:56:18 UTC)
- **Authors:** Hongchang Liu et al.
- **Qualifying affiliation(s):** Tencent — Liang Peng (co-authors otherwise at Tongji University, Hong Kong Polytechnic University, and Guangdong Laboratory of Artificial Intelligence and Digital Economy). Not borderline. Note: NVIDIA, also flagged by screening, is **not** an author affiliation — it appears only in the reference list as the author of a cited Cosmos world-foundation-model paper.
- **Categories:** cs.CV (primary), cs.AI, cs.LG, cs.RO
- **Open release:** demo/project page only (<https://hongchang-liu.github.io/GeoState-project-page/>); no code repository found
- **Shipped counterpart:** none found

**Summary:** GeoState proposes a view-decoupled scene-state representation for predictive 3D world modeling, built to avoid entangling scene dynamics with camera-motion-induced changes in geometry-foundation-model features.
**Purpose:** Geometry foundation model (GFM) features are organized around the observing viewpoint, so camera motion changes the features even when the underlying scene is static, which the authors say entangles scene dynamics with camera-induced variation and makes forecasting harder.
**Breakthrough:** On Waymo depth forecasting with predicted cameras, the authors report AbsRel/δ1 of 0.065/0.939 at t+0.2s, 0.092/0.902 at t+1.0s, and 0.127/0.848 at t+2.0s for GeoState, versus 0.073/0.931, 0.143/0.826, and 0.213/0.731 for VGGT-World — a reported 40.4% lower AbsRel at t+2.0s.
