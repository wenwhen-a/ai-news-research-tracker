**[A02] Rethinking Actions: Continuity-Aware Priors for World-Model Planning**
- **arXiv:** 2611.16645 · <https://arxiv.org/abs/2611.16645>
- **Submitted:** 2026-11-12
- **Authors:** Shaobo Yang, Zichen Ai, Ziyang Ma, Qian Yang, Bin Fang
- **Qualifying affiliation(s):** Alibaba Group — Qian Yang; (other authors are at Beijing University of Posts and Telecommunications; Bin Fang's affiliation is ambiguous in the HTML, with an Ant Group email domain visible — FLAG: borderline on that one author only, but Qian Yang/Alibaba alone satisfies the gate)
- **Categories:** cs.RO (primary), cs.LG
- **Open release:** code — github.com/oliverstack-byte/LG-DKGP (no weights/demo statement)
- **Shipped counterpart:** none found

**Summary:** The paper studies whether action proposals that better respect the temporal continuity of expert action sequences improve goal-directed planning with learned visual world models.
**Purpose:** Standard planning with visual world models (e.g., via CEM-style sampling) often proposes actions that ignore how real/expert action sequences evolve smoothly over time, hurting planning efficiency and success.
**Breakthrough:** The authors report LG-DKGP reaches 87.07% macro success across five environments (PushT, OGBench Cube, LIBERO Caddy, LIBERO Scene2, RoboTwin), versus 71.03% for INTACT, 61.66% for PRISM, and 58.66% for LeWM (averaged over five seeds).
**Tools & method:** LG-DKGP combines recent and longer-range executed action history via gated attention to predict a neural continuation mean, adds a temporal Gaussian-process residual, and uses CEM search seeded around that mean with a scale derived from expert action increments; a frozen world model scores goal progress during search.
**Limitation:** The value of history-only versus visually-conditioned proposals is task-dependent (history-only wins on three of five tasks).
