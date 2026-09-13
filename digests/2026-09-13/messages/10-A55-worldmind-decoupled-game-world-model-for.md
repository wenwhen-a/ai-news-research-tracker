**[A55] WorldMind: Decoupled Game World Model for State-Aware NPC Behavior**
- **arXiv:** 2608.21439 · https://arxiv.org/abs/2608.21439
- **Submitted:** 2026-08-18
- **Authors:** Zhiyang Deng, Boran Zhang, Danze Chen, Yeying Jin
- **Qualifying affiliation(s):** Tencent — all authors (with National University of Singapore; work done during Tencent research internships)
- **Categories:** cs.CV
- **Open release:** demo (project page https://teawhite.cn/worldmind_projectpage/)
- **Shipped counterpart:** none found

**Summary:** WorldMind is described as the first decoupled framework for state-aware NPC behaviour in game world models, separating interactive world modelling into Understanding, Decision, Control and Generation layers.
**Purpose:** To ground NPC behaviour in the evolving game state (boss-player distance, skill cooldowns), which is not achieved when behaviour is implicit in video generation or driven only by external control signals.
**Breakthrough:** The authors introduce BOSS-140K, gameplay videos paired with internal game states collected by an automated agent, and report WorldMind preferred over baselines in about 70% of pairwise comparisons for "more tactically appropriate and coherent NPC behavior."
**Tools & method:** The Understanding layer reconstructs a compact state from generated frames; the Decision layer uses a general-purpose language model to plan; the Generation layer renders gameplay in real time with a video diffusion model.
**Limitation:** The authors state "the Decision Layer shows partial cross-game generalization and remains state-sensitive, whereas compact-state reconstruction requires target-domain adaptation."
