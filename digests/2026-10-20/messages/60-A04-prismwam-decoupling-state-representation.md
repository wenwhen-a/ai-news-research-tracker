**[A04] PrismWAM: Decoupling State Representations in World Action Models**
- **arXiv:** 2610.26564 · <https://arxiv.org/abs/2610.26564>
- **Submitted:** 2026-10-19
- **Authors:** Tianyu Xin, Wanqi Zhong, Bowen Hu, Zhangchi Guo, Lijie Wang, Yiming Wang, Haoran Liao, Heyang Yu, Xiaoyu Tian, Zhiding Yu, Yiming Li
- **Qualifying affiliation(s):** NVIDIA (co-affiliation alongside Tsinghua University)
- **Categories:** cs.CV
- **Open release:** demo — project page <https://prism-wam.github.io/>
- **Shipped counterpart:** none found

**Summary:** PrismWAM argues that the video latents used by World Action Models (WAMs) conflate appearance (texture, color) with physical configuration (occupancy, pose), which is a poor state representation for action.
**Purpose:** To determine what the internal "state" of a world-action model should be, and to argue it should separate how the world looks from how it physically changes under action.
**Breakthrough:** The authors report strong performance in both simulation and the real world without any embodied action pretraining, using sparse RGB goal supervision combined with dense depth supervision and a "chain attention" mask controlling information flow between an RGB planning stream and a depth rollout stream.
**Tools & method:** A Mixture-of-Transformers architecture (main model ~6B parameters, PrismWAM* variant 15B) with depth-VAE pretraining on ~2,300 hours of depth data from AgiBotWorld-Beta plus simulated RoboTwin depth; evaluated on RoboTwin 2.0, LIBERO/LIBERO-Plus/LIBERO-Pro, and RoboDojo, and on real single/dual-arm Piper-X robots with Orbbec Gemini 335 RGB-D cameras.
**Limitation:** The authors state that large-scale real-world manipulation data with synchronized depth remains limited, constraining how much depth pretraining is currently possible, though they expect this to improve as depth sensing becomes more accessible.
