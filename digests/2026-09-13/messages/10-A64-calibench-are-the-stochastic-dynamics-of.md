**[A64] CaliBench: Are the Stochastic Dynamics of Video World Models Physically Calibrated?**
- **arXiv:** 2608.16829 · https://arxiv.org/abs/2608.16829
- **Submitted:** 2026-08-17
- **Authors:** Jonathan Sadeghi, Jenny Seidenschwarz, Jesse Allardice, Sirish Srinivasan, Benjamin Graham, Jeffrey Hawke
- **Qualifying affiliation(s):** Odyssey — all authors; FLAG: borderline (world-model startup, not on the tracked list)
- **Categories:** cs.LG, cs.AI
- **Open release:** code (https://github.com/odysseyml/calibench)
- **Shipped counterpart:** none found

**Summary:** CaliBench tests whether video world models reproduce the correct statistical distribution of physical outcomes, evaluating six image-to-video models on nine scenes with analytically known outcome distributions (Galton boards, dice, roulette, cards and others).
**Purpose:** To measure distributional calibration, split into "scorability" (share of valid generations) and "calibration" (distance from the true outcome distribution).
**Breakthrough:** The authors report "severe probability mass over-concentration" in most models despite plausible individual frames, across 1,728 generations and 5,184 VLM queries; models include WAN-2.7, SeeDance-2.0, HappyHorse-1.0, Veo 3.1, Runway Gen-4.5 and Cosmos3-Super.
**Tools & method:** A Mean Normalised Total Variation metric over nine discrete-outcome scenes with closed-form references; VLM-based outcome extraction validated at 93.8% agreement.
**Limitation:** The authors state the benchmark covers image-to-video pipelines only, that VLM extraction adds noise, that it tests marginal outcome distributions rather than trajectories, and that it cannot audit commercial training corpora.
