**[A03] FutureWorlds: Learning Robotic World Models from Alternative Futures**
- **arXiv:** 2610.01019 · <https://arxiv.org/abs/2610.01019>
- **Submitted:** 2026-10-01
- **Authors:** Hao Wu, Shengju Qian, Weiyan Wang, Fan Xu, Fan Zhang, Yuanpeng He, Qingsong Wen, Yuxuan Liang
- **Qualifying affiliation(s):** Tencent — Weiyan Wang
- **Categories:** cs.CV; cs.RO
- **Open release:** code (GitHub: <https://github.com/Alexander-wu/FutureWorlds>)
- **Shipped counterpart:** none found

**Summary:** FutureWorlds is a framework for learning robotic world models from "alternative futures": it unifies candidate future-scene construction, persistent memory for diverging trajectories, and learning from relative quality comparisons between candidates.
**Purpose:** Robotic world models predict action-conditioned future scenes, but the authors note that turning multiple alternative predictions into a useful learning signal is difficult: similar candidates give little comparative information, while diverging trajectories require persistent tracking of their individual histories.
**Breakthrough:** The authors report that FutureWorlds reduces LPIPS for 32-frame predictions by 14.78%, 20.84%, and 9.12% on RT-1, BridgeV2, and RoboCasa respectively, relative to the strongest baseline on each dataset.
**Tools & method:** The method uses diverse beam search during reinforcement learning to construct candidate futures balancing confidence and diversity, and candidate-specific bounded memory to keep generation and policy-scoring histories consistent.
**Limitation:** The authors state that autoregressive beam search incurs added inference latency, and that validating the approach in closed-loop planning and real robot control is left to future work.
