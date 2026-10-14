**[A11] Totem: Object-Centric 3D Memory for World-Consistent Video Generation**
- **arXiv:** 2610.15807 · <https://arxiv.org/abs/2610.15807>
- **Submitted:** 2026-10-11
- **Authors:** Zichen Wan, Tianyu Huang, Fan Li, Kai Wang, Hongzhi Zhang, Wangmeng Zuo
- **Qualifying affiliation(s):** Huawei — Tianyu Huang, Fan Li (Huawei Technologies Ltd.) — FLAG: borderline; remaining authors at Harbin Institute of Technology
- **Categories:** cs.CV
- **Open release:** none found
- **Shipped counterpart:** none found

**Summary:** Totem represents selected objects as persistent 3D memories anchored to a shared world coordinate frame, each with its own state, and combines these object memories with scene geometry in a dual-stream conditioning architecture to synthesize new-viewpoint video.
**Purpose:** Generating video that stays coherent to a single underlying 3D world is difficult under large viewpoint changes, where existing methods struggle to keep individual objects' surfaces and layouts stable.
**Breakthrough:** The authors report Totem scoring highest overall on WorldScore (86.43 vs. 85.53 for the strongest baseline, UniWorld-View) and best on all three metrics of ConsIDVid-Bench (Object Similarity 73.2, Chamfer Distance 0.0976, MEt3R 0.0818 vs. 71.4/0.1053/0.0964 for the best baseline).
**Tools & method:** Trained on ~80K clips (about 40K each) from RealEstate10K and DL3DV, resampled to 15fps, split into 81-frame windows, and center-cropped to 720p.
**Limitation:** The available paper content contains no dedicated limitations section and the authors do not explicitly discuss failure cases beyond qualitative baseline-artifact comparisons (e.g., blurred textures, distorted structures in competing methods).
