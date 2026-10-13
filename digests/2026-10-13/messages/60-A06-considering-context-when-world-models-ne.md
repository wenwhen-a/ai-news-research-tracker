**[A06] Considering Context: When World Models Need Context Encoders**
- **arXiv:** 2610.06651 · <https://arxiv.org/abs/2610.06651>
- **Submitted:** 2026-10-05
- **Authors:** Oleg Smirnov et al.
- **Qualifying affiliation(s):** Microsoft — King AI Labs, Microsoft Gaming (all five authors; Sara Karimi also lists KTH Royal Institute of Technology)
- **Categories:** cs.LG
- **Open release:** code — anonymous reference codebase at <https://anonymous.4open.science/r/considering_context/> (source, configs, protocols)
- **Shipped counterpart:** none found

**Summary:** Model-based reinforcement learning commonly assumes an agent cannot infer the latent context governing environment dynamics from its own experience, so systems supply that context externally (e.g., to a world model like DreamerV3).
**Purpose:** To determine when and how much context-aware mechanisms (e.g., explicit context encoders) actually help model-based RL world models, versus when an agent's own learned state already implicitly captures the needed information.
**Breakthrough:** The authors report that predictive headroom from context does not simply follow the environment's MDP class — in some settings, agent behavior already implicitly identifies context so context-aware mechanisms add nothing (e.g., near-zero headroom for DreamerV3, DALI-S, and cRSSM-D on their "identifiable" CARL DMC Walker Walk setting), while in a "hard" setting the learned state captures only part of the available headroom (e.g., LILAC-style shows 3.49 ± 0.68 headroom with 0.73 ± 0.29 residual gain).
**Tools & method:** Evaluated on MiniGrid Empty-8x8 (Wind/Resistance variants), a custom Point-Mass-Attractor environment, CARL DMC Walker Walk (identifiable and "hard" settings), RWRL Walker (non-i.i.d. parameter drift), and a linear-Gaussian calibration environment with a hidden Markov regime; compared methods include DreamerV3, DALI-S, LILAC-style, and cRSSM-D.
