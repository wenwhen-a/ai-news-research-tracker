**[A01] Vector-Quantized World Model: Latent Feedback Motion Planning for Robot Manipulation**
- **arXiv:** 2610.25600 · <https://arxiv.org/abs/2610.25600>
- **Submitted:** 2026-10-19
- **Authors:** Xuezhou Xu, Chung-Pang Wang, Zhenzhen Li, Benjamin Riviere
- **Qualifying affiliation(s):** NVIDIA — affiliation block lists "New York University" and "NVIDIA" without an explicit per-author mapping in the fetched HTML
- **Categories:** cs.RO
- **Open release:** none found
- **Shipped counterpart:** none found

**Summary:** The paper proposes VQ-WM, a latent feedback motion planner that searches over vector-quantized latent states (using a learned world model) for short paths to a goal, while a separate continuous visual-feedback controller tracks each planned state and corrects drift.
**Purpose:** The authors target long-horizon robot manipulation and locomotion planning, where visual world models typically fail because autoregressive prediction errors compound and long action sequences are hard to optimize directly.
**Breakthrough:** On a physical four-disk Tower of Hanoi task (WidowX arm), the authors report 100% success on the full 15-move solution using only short "play" demonstrations, versus baselines Cosmos Policy (5%), π0.5 (3%), and V-JEPA 2-AC* with manual subgoals (27%) on non-expert data.
**Tools & method:** The pipeline uses a frozen V-JEPA 2 encoder, a goal-conditioned controller, a continuous latent predictor, and a discrete latent predictor/codebook built via a greedy set-cover over FPT-estimated regions of attraction.
**Limitation:** The authors note experiments use only a single plan per episode, so the benefits of replanning are unexplored, and the method relies on a learned latent world model for its FPT reachability estimates (with a rejection class excluding unseen transitions from graph search).
