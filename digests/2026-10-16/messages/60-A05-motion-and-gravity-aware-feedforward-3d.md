**[A05] Motion- and Gravity-Aware Feedforward 3D Reconstruction**
- **arXiv:** 2610.22177 · <https://arxiv.org/abs/2610.22177>
- **Submitted:** 2026-10-15 (v1, 16:34:04 UTC)
- **Authors:** Shiyao Qian, Yuan Ren, Dongfeng Bai
- **Qualifying affiliation(s):** Huawei Noah's Ark Lab, Markham, Canada — Yuan Ren, Dongfeng Bai (first author Shiyao Qian is University of Toronto, with the work done during an internship at Huawei Noah's Ark Lab); **FLAG: borderline** (Huawei).
- **Categories:** cs.CV (primary), cs.AI
- **Open release:** none found
- **Shipped counterpart:** none found

**Summary:** The paper targets feed-forward multi-view 3D reconstruction transformers (e.g., VGGT, π³), which the authors say rely mainly on appearance-based attention and struggle in dynamic scenes with weak geometric cues.
**Purpose:** Feed-forward reconstruction transformers perform well on static, well-textured scenes but the authors state they struggle when geometric cues are weak or scenes are dynamic.
**Breakthrough:** In the paper's 8-view setting (Table 2), the authors report residual-flow injection improves π³ depth-rel to 0.107 (from 0.116 without injection) and VGGT depth-rel to 0.114 (from 0.121).
**Tools & method:** Residual optical flow is computed by subtracting a global affine motion model from RAFT optical flow; gravity direction is the second privileged signal.
**Limitation:** The authors note that for π³, residual-flow injection actually has a lower Pose AUC (40.94) than no injection (42.14) on the 8-view benchmark, so the gain is not universal across metrics.
