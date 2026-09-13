**[A52] MultiCube: Compositional 3D Generation With Part-Level Semantic and Spatial Control**
- **arXiv:** 2608.20448 · https://arxiv.org/abs/2608.20448
- **Submitted:** 2026-08-20
- **Authors:** Ava Pun, Kangle Deng, Yiheng Zhu, Jun-Yan Zhu, Maneesh Agrawala, Tinghui Zhou
- **Qualifying affiliation(s):** Roblox — Ava Pun, Kangle Deng, Yiheng Zhu, Maneesh Agrawala, Tinghui Zhou
- **Categories:** cs.GR, cs.CV
- **Open release:** none
- **Shipped counterpart:** none found

**Summary:** MultiCube generates 3D objects composed of semantically meaningful parts, with explicit control over part semantics (a schema) and spatial layout (bounding boxes) from a text prompt.
**Purpose:** Professional asset workflows need controllable, editable, part-decomposed objects rather than monolithic text-to-3D outputs.
**Breakthrough:** The authors report part-level Chamfer distance 0.040 versus 0.183 for CubePart, F-score 0.948 versus 0.787 and box IoU 0.847 versus 0.580, plus win rates of 82.9% over FullPart on semantic alignment and 82.2% over OmniPart on geometric quality.
**Tools & method:** A two-stage diffusion pipeline generates a monolithic mesh aligned to the layout, then decomposes it via a Part Layout Adapter; 510k assets (2.96M parts) for training; a 1.9B-parameter DiT plus a 22M-parameter adapter on 24 NVIDIA H200 GPUs; evaluated on PartObjaverse-Tiny.
**Limitation:** The authors acknowledge failures with badly mis-specified bounding boxes, occasional colliding parts, and no per-part iterative editing without full regeneration.
