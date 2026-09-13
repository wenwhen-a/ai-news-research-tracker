**[A43] GameWAM: A World Action Model for Video Games**
- **arXiv:** 2608.26200 · https://arxiv.org/abs/2608.26200
- **Submitted:** 2026-08-25
- **Authors:** Yuncheng Guo, Zhanqiu Zhang, Yiwen Guo, Weijia Li
- **Qualifying affiliation(s):** LIGHTSPEED — Zhanqiu Zhang (the paper's affiliation footnote reads only "LIGHTSPEED"; not identified in the paper as Tencent's Lightspeed Studios); FLAG: borderline
- **Categories:** cs.AI, cs.CV, cs.LG
- **Open release:** none stated (project page https://yunncheng.github.io/GameWAM/)
- **Shipped counterpart:** none found

**Summary:** GameWAM is presented as the first World Action Model for native closed-loop video-game play and GUI control, jointly generating future observations and executable keyboard-mouse action trajectories through parallel visual and action generative processes with block-causal conditioning and flow matching.
**Purpose:** To unify game-playing control policies with world-model-style visual prediction, since prior agents map perception to actions without modelling dynamics while interactive world models predict visuals without acting.
**Breakthrough:** The authors report competitive task success with fewer executed native actions than compared agents, and identify a failure mode they call "Low-Frequency Action Source Imprinting," where low-frequency components of the sampled action source steer coarse camera motion.
**Tools & method:** Block-cycle control coordinating prediction, execution and replanning; mode-specific prediction distributions and continuous-action normalisation; trained on synchronised gameplay and GUI trajectory data the authors constructed.
**Limitation:** The authors state GameWAM "is designed as a low-level closed-loop controller rather than a standalone high-level planner," with no symbolic task graph or long-horizon search.
