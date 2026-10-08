**[A01] RoboJEPA: Scaling Robotic Latent World Models**
- **arXiv:** 2610.10515 · <https://arxiv.org/abs/2610.10515>
- **Submitted:** 2026-10-07
- **Authors:** Artem Zholus et al.
- **Qualifying affiliation(s):** Meta — 9 of 12 authors listed as "FAIR at Meta," including joint last authors Nicolas Ballas and Mahmoud Assran; three co-authors are from Chandar Research Lab/Mila/Polytechnique Montréal
- **Categories:** cs.AI (primary), cs.RO (cross-list)
- **Open release:** none (abstract states checkpoints and training/deployment code will be released, but no repository link is given anywhere on the arXiv page)
- **Shipped counterpart:** none found

**Summary:** RoboJEPA is a Joint Embedding Predictive Architecture (JEPA) world model trained on 23 public manipulation datasets spanning 12 robot platforms, scaled from 22M to 8B parameters.
**Purpose:** The authors aim to establish compute-scaling laws for robotic world models and to find a training-time proxy (rollout error) that predicts real-robot planning performance without requiring costly on-hardware evaluation at every checkpoint.
**Breakthrough:** The authors report the 8B model is "the largest JEPA predictor model trained to date," fit with a second-order (not simple) power law whose extrapolation to held-out 4B/8B scales lands within 0.6×10⁻³ (DROID) and 1.4×10⁻³ (RoboCasa) of observed error.
**Tools & method:** Training data totals ~2.87M episodes (~15,022 hours of video, ~6,692 hours with synchronized actions) from datasets including DROID, RoboSet, RoboMIND, LeRobot (SO-101), RoboCasa365 (sim), 1X humanoid, AgiBot World, and nine Open-X Embodiment datasets; the predictor sits on a frozen V-JEPA 2.1 encoder.
