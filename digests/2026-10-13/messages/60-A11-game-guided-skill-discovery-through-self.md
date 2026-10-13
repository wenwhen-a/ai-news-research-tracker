**[A11] Game-Guided Skill Discovery through Self-Play for Playable Agent Control**
- **arXiv:** 2609.40137 · <https://arxiv.org/abs/2609.40137>
- **Submitted:** 2026-09-30
- **Authors:** Seungeun Rho, Jeonghwan Kim, Xue Bin Peng, Sehoon Ha
- **Qualifying affiliation(s):** NVIDIA — Xue Bin Peng (listed as "Simon Fraser University and NVIDIA")
- **Categories:** cs.LG (primary), cs.AI, cs.RO
- **Open release:** demo — <https://ggsd-demo.github.io> (interactive demo)
- **Shipped counterpart:** none found

**Summary:** The paper presents Game-Guided Skill Discovery (GGSD), which uses self-play in games to discover a small set of motor skills that a human can control directly, like a video-game character controller.
**Purpose:** The authors aim to discover skills that are not just useful for autonomous agents but are directly "playable" by a human, i.e., controllable and composable in real time.
**Breakthrough:** The authors report that skill transitions produce emergent combo behaviors not explicitly trained for.
**Tools & method:** The approach combines self-play (agent vs. past selves) with hierarchical reinforcement learning: a discrete high-level skill selector and per-skill low-level policies.
**Limitation:** The abstract/HTML reviewed did not state explicit acknowledged limitations; the environments used (Ant, Franka-arm, Unitree G1) appear to be simulated rather than deployed on physical hardware, which bounds the generality of the human-playability claims.
