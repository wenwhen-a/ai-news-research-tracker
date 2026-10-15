**[A04] Holi-Spatial 360: Generative Reconstruction from Sparse Panoramas for Spatial Rendering and Intelligence**
- **arXiv:** 2610.19502 · <https://arxiv.org/abs/2610.19502>
- **Submitted:** 2026-10-14
- **Authors:** Yuanyuan Gao, Zhirui Liu, Yuning Gong, Yifei Liu, Yifan Zhan, Kuixuan Jiao, Xiaolong Zhou, Yifan Yang, Hongjie Zhang, Xue Yang, Dan Xu, Zhihang Zhong
- **Qualifying affiliation(s):** Tencent — Yuning Gong
- **Categories:** cs.CV
- **Open release:** none stated (a dataset/benchmark, Holi360, is introduced but no explicit release link was found on the page)
- **Shipped counterpart:** none found

**Summary:** Holi-Spatial 360 turns sparse real-estate panoramas of multi-room homes into annotated, photorealistic 3D environments, addressing the shortage of large-scale, semantically labeled indoor 3D data that typically requires costly LiDAR capture.
**Purpose:** Existing indoor 3D datasets are mostly room-scale and depend on expensive LiDAR scanning, limiting data available for training spatially aware vision-language models.
**Breakthrough:** The authors report the Holi360 dataset contains over 1K multi-room 3DGS scenes, more than 100K instance annotations, and 2M spatial question-answer pairs.
**Tools & method:** A frozen feed-forward reconstruction model supplies cross-view correspondences that anchor the initial 3DGS optimization from sparse panoramas; fine-tuned image and video generative models fill in missing views along completed camera trajectories, distilled back into the scene.
**Limitation:** No explicit limitations section was surfaced in the fetched content; the method still depends on generative priors to "hallucinate" unseen appearance/geometry from sparse panorama inputs, which is an inherent approximation rather than ground-truth capture.
