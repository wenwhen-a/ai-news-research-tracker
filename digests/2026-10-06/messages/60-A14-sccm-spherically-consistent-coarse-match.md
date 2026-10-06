**[A14] SCCM: Spherically Consistent Coarse Matching for ERP Dense Feature Correspondence**
- **arXiv:** 2609.36545 · <https://arxiv.org/abs/2609.36545>
- **Submitted:** 2026-09-29
- **Authors:** Gyeonggwan Lee et al.
- **Qualifying affiliation(s):** Kakao Mobility Corp. — Gyeonggwan Lee, Eunsoo Im, Seunghwan Hong, Junghun Suh (FLAG: borderline)
- **Categories:** cs.CV
- **Open release:** code (<https://github.com/gandanlee/sccm>) | demo/project page (<https://gandanlee.github.io/sccm/>)
- **Shipped counterpart:** none found

**Summary:** The paper addresses dense feature matching between 360° panoramas stored in equirectangular projection (ERP), which introduces three distortions — a longitudinal seam (topology), latitude-dependent stretch (metric), and non-uniform pixel area (area) — not modeled by perspective-trained dense matchers.
**Purpose:** The authors state that dense feature matching between 360° panoramas underpins omnidirectional pose estimation, 3D reconstruction, and SLAM, but that the coarse stage of perspective-trained dense matchers does not model ERP-specific distortions, causing systematic degradation on panoramic imagery.
**Breakthrough:** The authors report that correcting the three distortions at the coarse-stage interfaces improves PCK@1° from 0.230 to 0.275 on Matterport3D under a fixed coarse scaffold with the refiner architecture unchanged, and that instantiated in the RoMa V1 framework, SCCM also outperforms the ERP-native EDM (0.163) and an ERP-retrained RoMa V1 (0.198), while transferring zero-shot to Stanford2D3D and leading on outdoor Holo360D when trained there.
