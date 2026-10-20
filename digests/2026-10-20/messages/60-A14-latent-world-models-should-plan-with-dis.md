**[A14] Latent World Models Should Plan with Distances Along the Latent Manifold**
- **arXiv:** 2610.25013 · <https://arxiv.org/abs/2610.25013>
- **Submitted:** 2026-10-18
- **Authors:** Zunzhi You, Linwei Tao, Siyu Xu, Yunke Wang, Chang Xu
- **Qualifying affiliation(s):** Apple — Linwei Tao (Machine Learning Research, Apple, in addition to University of Sydney)
- **Categories:** cs.LG (cross-listed cs.RO)
- **Open release:** code · <https://github.com/youzunzhi/ngc-latent-manifold>
- **Shipped counterpart:** none found

**Summary:** The paper studies latent world models (e.g., LeWM) that plan by picking action sequences whose predicted latent is closest to a goal latent under Euclidean (L2) distance.
**Purpose:** The goal is to fix long-horizon planning failures in latent world models caused by treating the latent space as globally Euclidean when it instead sits on a curved, low-dimensional manifold.
**Breakthrough:** The authors report NGC improves LeWM's planning success on all four tested benchmarks and nearly solves TwoRoom and Reacher; at the farthest goal offsets tested it reaches 95% and 100% success versus 27% and 81% for the L2 baseline.
**Tools & method:** Evaluated on four benchmarks: TwoRoom, Reacher, Cube, and PushT, built on the LeWM latent world model.
**Limitation:** The authors state NGC still falls short on the contact-rich Cube and PushT tasks even with an oracle predictor, because nearby physical states (e.g., a gripper near contact) can respond very differently to the same action, and contact introduces asymmetric transitions an undirected graph cannot express.
