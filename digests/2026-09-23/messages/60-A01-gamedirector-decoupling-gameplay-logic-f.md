**[A01] GameDirector: Decoupling Gameplay Logic from Rendering for Player-Configurable Game World Models**
- **arXiv:** 2609.25652 · <https://arxiv.org/abs/2609.25652>
- **Submitted:** 2026-09-22
- **Authors:** Zijun Lin et al.
- **Qualifying affiliation(s):** Tencent — Zijun Lin, Zhiyang Deng, Yuzhe Wu, Yeying Jin (all also list Singapore-based academic affiliations: NTU, NUS, A*STAR)
- **Categories:** cs.CV
- **Open release:** none stated (project page only: <https://jimntu.github.io/gamedirector/,> no code/weights commitment in the paper text)
- **Shipped counterpart:** none found

**Summary:** GameDirector is presented as "the first agentic framework that decouples rule-based gameplay logic from visual rendering" in game world models.
**Purpose:** The paper argues existing end-to-end game world models combine perception, memory, state transitions and rendering in one pixel-supervised model, which "still falls short of delivering a complete gameplay experience" because games need explicit mechanics like health deduction and combat rules that generative models cannot reliably enforce.
**Breakthrough:** The authors report the framework achieves accurate state tracking and improved boss action quality (>39.9%) versus end-to-end baselines across three games: "No Rest for the Wicked," an anonymized vampire-themed game, and "Hollow Knight." Deployment is reported at roughly 17 FPS on one-, two-, and four-GPU configurations (attributed to the authors; no third-party benchmark cited).
**Tools & method:** Two ResNet-18 models (SituationNet for character distance/angle, AttackNet for hit detection) process frames at different sampling frequencies; an explicit state tracker deterministically updates health points and boss skill meters from detected hit signals.
