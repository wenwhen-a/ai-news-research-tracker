**[A05] LiteNWM: Efficient Latent World Models for Onboard Visual Navigation in the Wild**
- **arXiv:** 2610.12368 · <https://arxiv.org/abs/2610.12368>
- **Submitted:** 2026-10-08 (v1)
- **Authors:** Linkai Liu et al.
- **Qualifying affiliation(s):** Sony AI — Chen Chen, Lingjuan Lyu. Other co-authors are at Nanjing University, Imperial College London, and Beijing University of Posts and Telecommunications.
- **Categories:** cs.RO
- **Open release:** none stated
- **Shipped counterpart:** none found

**Summary:** LiteNWM is a latent navigation world model for visual robot navigation that shares visual encoding across candidate trajectories and predicts their action-conditioned future representations at multiple time horizons, with a learned scorer choosing among them.
**Purpose:** The authors want navigation policies that get the foresight benefit of world-model rollouts (evaluating likely future outcomes) without the computational cost of rendering a full visual rollout per candidate.
**Breakthrough:** The authors report LiteNWM reduces macro-averaged trajectory error by 17.56% relative to NoMaD+NWM-XL on offline benchmarks (RECON, SCAND, SACSoN), with a 128.00-fold end-to-end speedup on an RTX 5090. They report the same evaluator transfers from the NoMaD proposer to MBRA without retraining (reducing MBRA's error by 16.2%), and that in real-robot tests in unseen indoor/outdoor environments it raised navigation success from 43.3% to 83.3% relative to NoMaD.
**Tools & method:** The method shares a visual encoder across candidate trajectories, predicts action-conditioned future latent representations at several horizons, and uses a learned scorer for trajectory selection; it is evaluated offline on RECON/SCAND/SACSoN and on a physical robot, with speed measured on an RTX 5090 GPU.
**Limitation:** The abstract does not state explicit limitations.
