**[A03] Simulation Priors for Rapid Adaptation in Model-Based RL for Autonomous Racing**
- **arXiv:** 2610.26757 · <https://arxiv.org/abs/2610.26757>
- **Submitted:** 2026-10-19
- **Authors:** Adrian Remonda, Jiajun Xi, Nicklas Hansen, Marcus Greiff, Thomas Lew, John Talbot, John Subosits, Xiaolong Wang
- **Qualifying affiliation(s):** Toyota Research Institute (Los Altos, CA); FLAG: borderline
- **Categories:** cs.LG, cs.RO, eess.SY
- **Open release:** none (authors state they release code and datasets, but no link was located)
- **Shipped counterpart:** none found

**Summary:** The paper proposes Prior-Informed Adaptation (PIA), an offline-to-online model-based RL framework for autonomous racing that pretrains a world model on low- and high-fidelity simulated trajectories, then adapts it online with limited real interaction.
**Purpose:** To address the high cost and risk of RL data collection in settings like racing, enabling quick adaptation to new tracks/surfaces without requiring an exact simulator.
**Breakthrough:** The authors report that treating simulated trajectories as biased priors — rather than as an environment for direct policy transfer — combined with a mixed sim/target replay buffer and uncertainty-regularized latent planning (Q-ensemble disagreement) enables adaptation validated on a real full-size race car (the F317).
**Tools & method:** Assetto Corsa Gym (ACGym), a high-fidelity racing simulator, plus a lightweight low-fidelity ODE vehicle model sharing ACGym's interface; the authors report a released dataset covering 15 tracks and more than 740 hours of Assetto Corsa driving data, with simulation experiments on 9 tracks.
**Limitation:** The authors state PIA requires a model/simulator sharing the target's observation-action interface, making image- or LiDAR-heavy inputs harder to use, and that experiments focus on dynamics mismatch rather than strong exogenous randomness (e.g. opponent vehicles).
