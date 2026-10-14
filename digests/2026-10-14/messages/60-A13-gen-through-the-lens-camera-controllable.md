**[A13] Gen Through the Lens: Camera-Controllable Video Generation via Cross-Coordinate Conditioning Fusion**
- **arXiv:** 2610.15900 · <https://arxiv.org/abs/2610.15900>
- **Submitted:** 2026-10-11
- **Authors:** Shuai Li et al.
- **Qualifying affiliation(s):** Tencent — all authors (affiliation listed as "Tencent Video Solar System")
- **Categories:** cs.CV (primary); cs.AI; cs.GR; cs.LG
- **Open release:** none found
- **Shipped counterpart:** none found

**Summary:** "Gen Through the Lens" (GTL) is a camera-controllable image-to-video generation framework that decomposes and fuses control signals across three coordinate spaces — camera (intrinsics), world (spatial geometry hints), and object (3D bounding boxes) — to drive camera motion, focus/depth-of-field, and framing from a single reference image.
**Purpose:** Prior camera-controllable video generators treat camera motion as abstract conditioning or rely on a single coordinate system, limiting precise, physically consistent control of camera, object motion, and focus together.
**Breakthrough:** On a held-out 1k-clip test set, the authors report their 14B model (GTL 14B) scoring best or near-best across FID (53.71), FVD (86.54), Qwen VQA (0.81), camera translation error (8.59) and bounding-box metrics against baselines including PAC, RC-I2V, and GEN3C.
**Tools & method:** Trained on ~110k clips with camera trajectories and 3D bounding-box annotations from DynPose-100K, MultiCamVideo, BEDLAM2.0 and internal data, plus 8k zoom and 15k bokeh samples, all 81 frames at 480p; ablations use a Wan2.1-1.3B model.
