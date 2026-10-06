**[A10] Neuroll: Real-Time Neural Strand-Based Hair Simulation via Simulator-in-the-Loop Unrolling**
- **arXiv:** 2610.04689 · <https://arxiv.org/abs/2610.04689>
- **Submitted:** 2026-10-03
- **Authors:** Gene Wei-Chin Lin et al.
- **Qualifying affiliation(s):** Meta — Gene Wei-Chin Lin, Jessica Jia-En Lee, Yu Ju (Edwin) Chen, Egor Larionov (Meta Reality Labs); NVIDIA — Tuur Stuyck
- **Categories:** cs.GR
- **Open release:** none confirmed
- **Shipped counterpart:** none found

**Summary:** The paper presents Neuroll, a neural time integrator for strand-based hair simulation designed to mirror the input-output formulation of classical time integrators (previous hair states, material stiffness, collision geometry).
**Purpose:** The authors state that optimized classical time integration can simulate thousands of hair strands in real time but is still too computationally demanding for commodity hardware, while existing learning-based alternatives tend to produce less physically plausible motion and often fail to generalize to out-of-distribution scenarios.
**Breakthrough:** The authors report stable long-horizon rollouts with linear per-strand scaling and real-time performance: total inference time for 3,000 strands is 0.460 ms (0.273 ms body-field autoencoder + 0.187 ms neural integrator) on an NVIDIA RTX 4080 Laptop GPU, and the method naturally extends to quasi-static simulation by resetting hair states.
**Tools & method:** Training used grooms from the CT2Hair dataset plus synthetic artist-created hairstyles; generalization testing used 4 selected grooms (straight to curly, including ponytails) and 6 motion sequences (13,161 frames) of indoor/outdoor activity.
