**[A40] SceneReGen: Generative Reconstruction of 3D Scenes from a Single Image**
- **arXiv:** 2608.23930 · https://arxiv.org/abs/2608.23930
- **Submitted:** 2026-08-25
- **Authors:** Zefan Tian, Yuteng Ye, Yiheng Zhang, Yuhang Yang, Xueqiang Lv, Shizhou Zhang, Le Liu, Di Xu
- **Qualifying affiliation(s):** Huawei — corresponding author Di Xu and co-authors (with Northwestern Polytechnical University); FLAG: borderline
- **Categories:** cs.CV
- **Open release:** none
- **Shipped counterpart:** none found

**Summary:** SceneReGen reconstructs a full 3D scene from one image by treating generated object assets as reconstruction primitives, with "selective pose factorization" that encodes observed orientation in the generated meshes while estimating translation and scale from scene evidence.
**Purpose:** To complete partially observed objects and place them coherently in a shared observation-aligned frame, bridging single-object generation and scene reconstruction.
**Breakthrough:** On 3D-FUTURE the authors report the best scene-level Chamfer distance (89.50), scene-level F-score (0.031) and 3D box IoU (0.009) among evaluated methods, with object-level Chamfer tied for best (68.95).
**Tools & method:** Trained on 3D-FUTURE (14,761 scenes) plus Objaverse and MeshFleet (about 25K objects) on 96 Ascend 910B NPUs for 500k iterations.
**Limitation:** The authors state texture synthesis lacks occlusion awareness, that performance degrades on low-resolution or blurry inputs, and that position estimation lacks collision regularisation, causing interpenetration.
