**[A05] PartiCam: Camera Controlled Video Generation with Reward Guidance**
- **arXiv:** 2609.39504 · <https://arxiv.org/abs/2609.39504>
- **Submitted:** 2026-09-30
- **Authors:** Amine Ouasfi, Runjia Li, Junlin Han, Eric Marchand, Philip H.S. Torr, Adnane Boukhayma
- **Qualifying affiliation(s):** Meta — Junlin Han (affiliation listed as Meta and University of Oxford)
- **Categories:** cs.CV; cs.AI
- **Open release:** none (no code, weights, or demo link found; the lead's claim of a Tencent affiliation could not be verified — no Tencent mention appears anywhere in the paper)
- **Shipped counterpart:** none found

**Summary:** PartiCam is a training-free, inference-time method for making video diffusion models follow a specified camera trajectory, addressing drift in existing score-modulation guidance and the data/generalization cost of training-based camera-control approaches.
**Purpose:** The authors want precise, controllable camera trajectories in generated video without retraining the underlying video diffusion model, and without the instability/quality degradation of naive restart-based sampling schemes.
**Breakthrough:** On static scenes, the authors report an Absolute Trajectory Error (ATE) of 0.526 versus 0.767 for the NVS-Solver baseline; on dynamic scenes, ATE improves from a baseline 2.308 to 0.807. They summarize this as roughly a 6× reduction in translation error and 4× reduction in ATE relative to NVS-Solver.
**Tools & method:** The method layers global SMC trajectory exploration (propagation, reward-based weight update, resampling) with local guided restarts, run over roughly 100 diffusion iterations with local refinement active at iterations 8–32 and global SMC at 8–40, both updated every 4 iterations.
**Limitation:** The authors state the method can require a larger denoising budget because it maintains multiple candidate trajectories simultaneously, increasing inference cost.
