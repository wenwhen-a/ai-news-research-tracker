**[A01] What Matters for World Modeling in Vision-Language-Action Models?**
- **arXiv:** 2610.19825 · <https://arxiv.org/abs/2610.19825>
- **Submitted:** 2026-10-14
- **Authors:** Qisen Ma, Yixiang Chen, Yuan Xu, Peiyan Li, Jiabing Yang, Kai Wang, Jianhua Yang, Jianlou Si, Jun Huang, Jing Liu, Nianfeng Liu, Yan Huang, Liang Wang
- **Qualifying affiliation(s):** Alibaba Group — Jianlou Si, Jun Huang
- **Categories:** cs.RO (primary), cross-listed cs.CV
- **Open release:** none stated
- **Shipped counterpart:** none found

**Summary:** This is a controlled empirical study of how to integrate world models into Vision-Language-Action (VLA) robot policies so they predict future dynamics instead of only mapping observations to actions.
**Purpose:** Prior work conflates world representation choice, integration strategy, and policy backbone, making it unclear which design choices actually matter for world modeling in VLAs.
**Breakthrough:** The authors report that 2D semantic representations give consistent gains across paradigms, that no single paradigm wins everywhere though the decoupled MoT Future Expert is competitive overall (especially out-of-domain), and that world modeling outperforms action-only baselines, with the largest gains on long-horizon and dynamic tasks.
**Tools & method:** The unified framework evaluates world-model paradigms on Qwen3-VL-2B with a cross-DiT action expert and on π0.5, using benchmarks including LIBERO, LIBERO-Plus, RoboTwin 2.0, DOMINO, and four real-world robot tasks.
**Limitation:** The study reports that gains are paradigm- and setting-dependent (e.g., WM-Align improves in-domain LIBERO but drops performance on π0.5/RoboTwin's Clean2Random setting from 46.4% to 41.0%), indicating no universally best configuration.
