**[A03] LongForcing: Scaling Temporal Manifold Matching for Long-Horizon World Rollout**
- **arXiv:** 2610.18289 · <https://arxiv.org/abs/2610.18289>
- **Submitted:** 2026-10-13
- **Authors:** Ziyu Zhu, Zhaoxu Sun, Fan Jiang, Mengchao Wang, Junfeng Ni, Ting-Bing Xu, Zhicheng Liu, Mu Xu
- **Qualifying affiliation(s):** Alibaba (AMAP, Alibaba Group) — Ziyu Zhu, Zhaoxu Sun, Fan Jiang, Mengchao Wang, Ting-Bing Xu, Zhicheng Liu, Mu Xu
- **Categories:** cs.CV
- **Open release:** code — <https://github.com/Fantasy-AMAP/LongForcing>
- **Shipped counterpart:** none found

**Summary:** LongForcing targets the drift that autoregressive video-diffusion world models exhibit when rolled out well past their training horizon — degrading visual quality, inconsistent motion, and eroding object identity as generated frames re-enter as context.
**Purpose:** The authors aim to close the gap between short-horizon training supervision and the long-horizon behavior needed for extended world-model rollouts (e.g., minutes to hours of generated video).
**Breakthrough:** The authors report a VBench Quality score of 85.52 on text-to-video generation and a 23.9-point gain on the WorldRoamBench 60-second action score in first-person ablations, plus qualitative rollouts shown out to 24 hours — well beyond the training horizon.
**Tools & method:** Training ran for 10 epochs on 32 NVIDIA A800 GPUs; evaluation used VBench and WorldRoamBench, with inference cost measured on a single A800.
**Limitation:** The authors state the method's guarantees are conditional on teacher quality and student–teacher mismatch, tied to "the specified model, domain, and action protocol," and that determining a sufficient horizon for a new task requires evaluating these dependencies over the intended deployment duration.
