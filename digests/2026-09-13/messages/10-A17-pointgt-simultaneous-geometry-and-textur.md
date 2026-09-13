**[A17] PointGT: Simultaneous Geometry and Texture Editing for Point-Based Representations**
- **arXiv:** 2609.03341 · https://arxiv.org/abs/2609.03341
- **Submitted:** 2026-09-03
- **Authors:** Yanshu Zhang, George Shramko, Pratul P. Srinivasan, Ke Li
- **Qualifying affiliation(s):** Google DeepMind — Pratul P. Srinivasan
- **Categories:** cs.CV, cs.GR
- **Open release:** none stated (project page https://zvict.github.io/pointgt/)
- **Shipped counterpart:** none found

**Summary:** PointGT is a point-based 3D representation that supports simultaneous editing of geometry and appearance: it extends PAPR with a learned UV mapping from 3D points to a 2D texture atlas, so textures are edited in 2D while non-rigid geometry edits displace points.
**Purpose:** The authors state that recent texture-editing methods for 3D Gaussian Splatting "are not compatible with geometry edits and deformations."
**Breakthrough:** The authors report novel-view PSNR 33.48 (DTU) and 33.57 (Blender) at 30k points, and on VBench editing metrics subject consistency 0.844 versus 0.827 for GSTex and imaging quality 0.585 (a reported 12.48% improvement over GSTex). Accepted to ECCV 2026.
**Tools & method:** Unstructured point cloud with learned features rendered by cross-attention (PAPR); two geometry regularisers (close-to-ray, close-to-surface); deformation-aware correspondence via attention-weighted displacement fusion; evaluated on DTU, Blender synthetic and Mip-NeRF 360 with Objaverse assets.
**Limitation:** The authors state the method relies on an optimisation-based UV parameterisation that "can struggle to produce clean and low-distortion charts for objects with complex topology."
