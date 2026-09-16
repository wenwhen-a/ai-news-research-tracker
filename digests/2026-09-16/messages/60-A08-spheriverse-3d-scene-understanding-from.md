**[A08] Spheriverse: 3D Scene Understanding from Spherical Observations in the Wild**
- **arXiv:** 2609.09012 · <https://arxiv.org/abs/2609.09012>
- **Submitted:** 2026-09-08 (v1)
- **Authors:** Fei Teng et al.
- **Qualifying affiliation(s):** FLAG: borderline — Ant Group — Hao Shi (Ant Group is an Alibaba-affiliated fintech spinoff, not Alibaba itself; other co-authors are affiliated with Hunan University and Zhejiang University of Science and Technology/Zhejiang University)
- **Categories:** cs.CV; cs.RO; eess.IV
- **Open release:** code (stated "will be available") — link not yet live per paper text; dataset/benchmark also to be released
- **Shipped counterpart:** none found

**Summary:** The paper introduces Spheriverse, a real-world dataset of 64,400 temporally aligned spherical image–LiDAR pairs across 644 sequences, and SphereOcc, a framework for 3D occupancy prediction, semantic mapping, and object detection from spherical (360°) observations.
**Purpose:** The authors aim to bridge the "cross-space representation gap" between angular spherical imagery and the Cartesian voxel space used for dense 3D scene understanding, which existing perspective-camera-focused methods do not address.
**Breakthrough:** The authors report SphereOcc achieves 13.91% mIoU and 24.65% GeoIoU on occupancy prediction, versus 12.21% mIoU (TPVFormer) and 22.55% GeoIoU (SurroundOcc) from the strongest prior methods — relative gains of 13.9% and 9.3% — and ranks first across all five scene categories in their benchmark.
**Tools & method:** SphereOcc uses Cartesian–Spherical Representation Remodeling (CSRR) to align Cartesian voxel features with spherical range–azimuth geometry, and Spherical Evidence Re-querying (SER) to retrieve semantic evidence via the range–height–azimuth mapping induced by spherical imaging; evaluation uses a 360°-horizontal/136.7°-vertical camera rig with a 128-beam LiDAR.
