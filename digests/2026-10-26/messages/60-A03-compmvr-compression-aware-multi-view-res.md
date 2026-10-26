**[A03] CompMVR: Compression-Aware Multi-View Restoration Using Diffusion Models for Geometrically Consistent 3D Reconstruction**
- **arXiv:** 2610.32800 · <https://arxiv.org/abs/2610.32800>
- **Submitted:** 2026-10-23
- **Authors:** Dong-hwi Kim, Chaewon Moon, Hojun Song, Dongbeom Kim, Junyeong Jang, Aro Kim, Gahyeon Kim, Heejung Choi, Jehee Kim, Gianella Cravioto, Sohyun Lee, Gyeongjin Choi, EunHye Jeong, Soo Ye Kim, Jaehyup Lee, Sang-hyo Park
- **Qualifying affiliation(s):** Adobe — Soo Ye Kim (Adobe Research, USA; corresponding author). Remaining authors are affiliated with Kyungpook National University, Republic of Korea.
- **Categories:** cs.CV
- **Open release:** code (project page states code and data are available: <https://mchaewon.github.io/CompMVR-project-page/>)
- **Shipped counterpart:** none found

**Summary:** The paper identifies compression-induced cross-view geometric inconsistency as a failure mode in multi-view 3D reconstruction, where lossy compression disrupts feature matching and correspondence across views.
**Purpose:** Lossy compression of multi-view imagery introduces view-dependent artifacts that break geometric consistency across views, degrading downstream 3D tasks such as camera pose estimation and novel view synthesis.
**Breakthrough:** The authors report consistent gains in restoration quality and downstream 3D reconstruction performance across multiple datasets, codecs, and compression levels compared to baseline restoration approaches.
**Tools & method:** The method is a diffusion-based multi-view restoration framework combining learned compression priors with cross-view correspondence; the authors built new compressed-view datasets to evaluate it.
**Limitation:** Not stated by the authors (not surfaced in the available abstract/summary text).
