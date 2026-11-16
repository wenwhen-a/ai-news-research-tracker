**[A03] Gamer: A Generalist Vision-Language-Action Foundation Model for Long-Horizon Real-Time Game Agents**
- **arXiv:** 2611.18397 · <https://arxiv.org/abs/2611.18397>
- **Submitted:** 2026-11-13
- **Authors:** Run Luo et al.
- **Qualifying affiliation(s):** miHoYo (Honkai AI R&D Team) — all authors listed under this team affiliation
- **Categories:** cs.CL (primary), cs.AI, cs.CV
- **Open release:** code/weights — authors state they open-source the inference engine and checkpoints for CPT scaling behaviors; project page <https://mihoyo-gamer.github.io/>
- **Shipped counterpart:** none found

**Summary:** Gamer is a generalist vision-language-action agent framework built by miHoYo's Honkai AI R&D Team for long-horizon, real-time play across both 2D interfaces and 3D open-world games, including miHoYo's own title Honkai: Star Rail (HSR).
**Purpose:** The authors aim to build a single agent that generalizes across long-horizon tasks in complex interactive environments, rather than a game-specific bot, as a step toward agents that operate across digital and physical worlds.
**Breakthrough:** The authors report that Gamer achieves generalization and efficiency comparable to skilled human players across several 3D open-world games and competitive results on conventional 2D game benchmarks (MCU, ViZDoom, OmniGameArena, GameWorld), evaluated with real-time (RT) scores against time-paused (TP) baselines.
**Tools & method:** Continued pretraining used roughly 2.4K hours of public gameplay data (VPT, D2E, OpenP2P) plus ~6.3B tokens of general vision-language data and additional HSR gameplay (85% gameplay/15% general mix); SFT drew on ~68K HSR sessions (~11K hours), filtered to ~3.2K sessions (~1K hours) for annotation, yielding ~261K operation-level, ~211K subgoal-level, and ~234K task-level samples.
