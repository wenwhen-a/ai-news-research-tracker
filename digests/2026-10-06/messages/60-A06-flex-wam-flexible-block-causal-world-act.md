**[A06] FLEX-WAM: Flexible Block-Causal World-Action Models for Long-Horizon Imagination and Planning**
- **arXiv:** 2610.05483 · <https://arxiv.org/abs/2610.05483>
- **Submitted:** 2026-10-04
- **Authors:** R. Khorrambakht, Joseph Amigo, Félix Lebel, Leon Seetoo, Jean Ponce, Zhenzhen Li, Ludovic Righetti
- **Qualifying affiliation(s):** NVIDIA — Zhenzhen Li
- **Categories:** cs.RO, cs.AI
- **Open release:** none confirmed (authors state code/checkpoints "will be released upon acceptance")
- **Shipped counterpart:** none found

**Summary:** FLEX-WAM is a flexible block-causal world-action model that predicts action-conditioned futures, generates feasible actions, and supports planning in imagination, while handling variable-length context and stable long multi-step autoregressive rollouts.
**Purpose:** Existing world/action models struggle to jointly serve as both policy and outcome predictor over long horizons without losing action responsiveness; the authors address this with gradient balancing and a "Forward-Dynamics elasticity" training mechanism.
**Breakthrough:** The authors report stable long-horizon imagination and planning performance across simulated tasks (LIBERO, OGBench 4×4 visual puzzles) and real-robot tasks (PushT, Unitree G1 play data, OpenArm), with training on 8 NVIDIA H100 GPUs for ~150k steps (about 4 days) and inference on up to 4 NVIDIA RTX6000 Pro MaxQ cards.
**Tools & method:** The model is evaluated on LIBERO simulation, 4 hours of real-world PushT play data, OGBench visual puzzles, Unitree G1 play data, and OpenArm real-robot counterfactual-detection tasks.
**Limitation:** The authors state that executing imagined plans in the real world and using detected mismatches for continual model improvement remain future work; OGBench puzzle success was measured only in imagination (not real-world execution); and text conditioning was excluded because it competes with action information for predicting futures.
