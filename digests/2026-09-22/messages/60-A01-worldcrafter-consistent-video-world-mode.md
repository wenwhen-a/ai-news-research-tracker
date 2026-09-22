**[A01] WorldCrafter: Consistent Video World Model with Implicit 3D-aware Memory**
- **arXiv:** 2609.24984 · <https://arxiv.org/abs/2609.24984>
- **Submitted:** 2026-09-21
- **Authors:** Wangbo Yu, Kunhao Liu, Wenbo Hu, Shenghai Yuan, Chaoran Feng, Haiyang Zhou, Yukun Huang, Yiran Wang, Wang Zhao, Yingmin Luo, Ying Shan
- **Qualifying affiliation(s):** Tencent — Yukun Huang, Yiran Wang, Wang Zhao, Yingmin Luo, Ying Shan (ARC Lab, Tencent IEG); other authors are Peking University
- **Categories:** cs.CV, cs.AI, cs.GR
- **Open release:** none confirmed in text beyond a project website (<https://drexubery.github.io/WorldCrafter);> no explicit code/weights link found
- **Shipped counterpart:** none found

**Summary:** WorldCrafter is a video world model that maintains long-horizon and multi-view consistency using an implicit, camera-queryable 3D-aware memory.
**Purpose:** The authors aim to solve the consistency problem in video world models — i.e., maintaining coherent scene content when a camera revisits previously seen viewpoints during long, interactive generation.
**Breakthrough:** The authors report a memory encoder with pose-conditioned readout that integrates historical observations into denoising without explicit depth correspondences, and claim a "47.6% improvement relative to the strongest baseline" in revisit consistency.
**Tools & method:** Training combines Open-Sora-Plan, DL3DV, and MIND synthetic datasets across four sequential training stages (~19,000 iterations) using up to 32 GPUs.
**Limitation:** The authors acknowledge that consistency can still break down along particularly complex or extended trajectories.
