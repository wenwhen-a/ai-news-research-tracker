**[A02] Persistent Planar Memory for Video World Models**
- **arXiv:** 2610.23795 · <https://arxiv.org/abs/2610.23795>
- **Submitted:** 2026-10-16 (v1)
- **Authors:** Yuze He et al.
- **Qualifying affiliation(s):** Ant Group — Bin Tan, Zelin Gao, Yujun Shen, Nan Xue, Yinghao Xu (He and Liu are Tsinghua University). FLAG: borderline — screen matched "Alibaba," but the actual industry affiliation is Ant Group (a separate fintech/AI affiliate), which is on the borderline-company watch list.
- **Categories:** cs.CV
- **Open release:** none (project page only, <https://hyzcluster.github.io/ppmem>; no code/weights release stated)
- **Shipped counterpart:** none found

**Summary:** PPMem is a video world model that maintains a persistent, compact 3D memory built from plane primitives rather than point clouds, enabling long, geometrically consistent video generation under large camera motion.
**Purpose:** The paper targets the need for video world model memory that is simultaneously compact, geometrically explicit, consistent across viewpoints, and able to update as new content is generated — properties the authors say prior point-cloud, surfel, TSDF, or frame-retrieval memories only partially satisfy.
**Breakthrough:** The authors report PPMem outperforms the point-cloud-based baseline Gen3C on DL3DV and RealEstate10K (e.g., PSNR 16.99 vs 15.74, LPIPS 0.335 vs 0.474 at N=49 on DL3DV), keeps a ~0.27 DINOv2-similarity lead over the next-best method at frame 300 in ~350-frame rollouts, and uses roughly 5 MB of memory for a full scene versus 1.7 GiB for an equivalent point cloud.
**Tools & method:** Built on the Wan 2.2 TI2V 5B diffusion transformer, PPMem regresses 7-parameter plane primitives per ~25-frame chunk and merges them into a pool via occlusion deletion, quality-based deduplication, and forward-looking pruning, training in two stages (video fine-tuning, then frozen-backbone geometry LoRA) on DL3DV and RealEstate10K.
