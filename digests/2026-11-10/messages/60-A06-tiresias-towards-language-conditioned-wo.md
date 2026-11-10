**[A06] Tiresias: Towards Language-Conditioned World Models**
- **arXiv:** 2611.10392 · <https://arxiv.org/abs/2611.10392>
- **Submitted:** 2026-11-07
- **Authors:** Fengyi Wu, Yifei Dong, Yetong Sha, Lingdong Kong, Qiyu Hu, Bohan Xiong, Qi Dai, Alexander G. Hauptmann, Zhi-Qi Cheng
- **Qualifying affiliation(s):** Microsoft Research — Qi Dai
- **Categories:** cs.CV
- **Open release:** none found (benchmark LCWM-Bench used but no confirmed public release found)
- **Shipped counterpart:** none found

**Summary:** The paper argues that language-conditioned world modeling is fragmented across domains with different action spaces, datasets, and evaluation protocols.
**Purpose:** The authors aim to unify the scattered landscape of language-conditioned world-model research under one task formulation and one cross-domain benchmark, to enable fair comparison across navigation, robotics, gaming, and driving settings.
**Breakthrough:** The authors report the introduction of LCWM-Bench, a 15-dataset benchmark spanning four domains, plus Tiresias, an agent that imagines candidate-trajectory outcomes with a video-pretrained world model and ranks them with trajectory and visual rankers before acting.
**Tools & method:** Tiresias combines a diffusion policy for action-sequence proposals, trajectory and visual rankers for selecting among imagined futures, and a video-pretrained world model for outcome imagination, evaluated on LCWM-Bench's train/val-seen/val-unseen splits covering navigation, robotics, gaming, and driving data.
**Limitation:** The authors state (Appendix D) that evaluation covers real and simulated data within LCWM-Bench but does not deploy Tiresias on physical robots, so its effectiveness on real hardware "remains to be validated," deferring physical navigation/manipulation deployment to future work.
