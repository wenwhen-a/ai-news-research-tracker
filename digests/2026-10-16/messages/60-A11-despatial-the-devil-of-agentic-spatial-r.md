**[A11] DeSpatial: The devil of Agentic Spatial Reasoning Lies in 3D Itself**
- **arXiv:** 2610.20990 · <https://arxiv.org/abs/2610.20990>
- **Submitted:** 2026-10-14 (v1, 22:05:23 UTC)
- **Authors:** Yifei Liu et al.
- **Qualifying affiliation(s):** Tencent — co-author(s) within the group of Yuning Gong, Yuchen Yang, Hongjie Zhang, Xue Yang, Xiao Sun, Zhihang Zhong (HTML affiliation block lists "Shanghai Jiaotong University / HKUST / Tencent / Fudan University" jointly for this author group; exact per-author mapping not resolvable from the page). Other authors: Shanghai Artificial Intelligence Laboratory, Beihang University.
- **Categories:** cs.CV
- **Open release:** none found
- **Shipped counterpart:** none found

**Summary:** DeSpatial splits agentic spatial reasoning into a shared 3D perception stage — building one unified, metric, gravity-aligned scene with consistent object identities — and a separate reasoning stage that operates on that scene.
**Purpose:** The paper addresses the problem that spatial agents combine independently predicted tools (segmentation, depth, detection) whose outputs disagree with each other, producing fragmented or duplicated object identities that corrupt downstream spatial answers.
**Breakthrough:** In an oracle test, the authors report that swapping ground-truth 3D bounding boxes into the agent raises accuracy on five object-centric VSI-Bench tasks from 50.38% (raw perception pipeline) to 98.23%.
**Tools & method:** A joint segmentation-depth co-refinement module merges same-object masks across a frame and removes projection artifacts, and a cross-view instance fusion module links overlapping instances of the same object across different views (not within one frame) using 3D structure and mask-appearance checks.
