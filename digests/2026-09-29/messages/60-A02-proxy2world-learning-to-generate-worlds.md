**[A02] Proxy2World: Learning to Generate Worlds From Lightweight Proxies without Seeing Them**
- **arXiv:** 2609.35023 · <https://arxiv.org/abs/2609.35023>
- **Submitted:** 2026-09-28
- **Authors:** Hongli Xu, Weilong Yan, Anbang Wang, Chunyu Zou, Siyu Hong, Jingwei Huang
- **Qualifying affiliation(s):** Tencent — all authors
- **Categories:** cs.CV
- **Open release:** none found (project page only: <https://dumdumgura.github.io/proxy2world/;> no code repo, weights, or public demo confirmed in the HTML)
- **Shipped counterpart:** none found

**Summary:** Proxy2World is a controllable world model that learns to generate high-fidelity video worlds conditioned on lightweight geometric proxies, without requiring paired proxy-video training data.
**Purpose:** The paper addresses the difficulty of training proxy-conditioned world models when paired (proxy, video) supervision from posed RGBD videos is unavailable at inference.
**Breakthrough:** At inference, "proxy-camera hybrid denoising" is used to preserve structural fidelity while generating detailed visuals; the authors report a geometric alignment score of 0.6795 and an adherence win rate of 64.18% versus 72.26% for the Cosmos-Depth baseline, alongside first-place ranking in human preference evaluation.
**Tools & method:** Training used 120,624 RGBD clips from DL3DV, RealEstate10K, and a gameplay dataset (81 frames at 480x832, 16 FPS), on 48 GPUs with AdamW.
**Limitation:** The authors state "long-horizon interactive generation remains future work."
