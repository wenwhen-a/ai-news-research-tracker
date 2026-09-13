**[A07] PASTEL: Panoramic Alignment for Monocular 4D Scene Reconstruction**
- **arXiv:** 2609.06099 · https://arxiv.org/abs/2609.06099
- **Submitted:** 2026-09-05
- **Authors:** Yuankun Yang, Yi Wei, Bo Bai, Wenyang Zhou, Li Zhang
- **Qualifying affiliation(s):** Huawei (Central Media Technology Institute) — Yi Wei, Bo Bai, Wenyang Zhou; FLAG: borderline
- **Categories:** cs.CV
- **Open release:** none
- **Shipped counterpart:** none found

**Summary:** PASTEL reconstructs 4D scenes from casually captured monocular video by reconstructing visible regions and generatively completing regions outside the camera's view. Its "panoramic scene alignment" reformulates exploration of invisible regions as a 2D directional trajectory problem instead of a 3D search.
**Purpose:** Monocular 4D reconstruction leaves large unseen regions unfilled, which limits VR and embodied-AI uses that need full scene coverage.
**Breakthrough:** The authors report reducing the search from 6-DoF to a 2D problem with explicit visibility boundaries, and a 0.9 dB PSNR improvement over the prior state of the art on the DyCheck iPhone dataset.
**Tools & method:** Monocular depth, pose and flow estimation combined with camera-controlled video-generation priors; evaluated on DyCheck iPhone.
**Limitation:** The authors state the method depends on accurate depth/pose/flow estimates and stable video-generation priors, degrades under very large camera motion, and that generated content is sometimes blurrier than covisible regions.
