**[A26] CAER: Causal Action Effect Reweighting for World Model Training**
- **arXiv:** 2608.30897 · https://arxiv.org/abs/2608.30897
- **Submitted:** 2026-08-31
- **Authors:** Jianjie Fang, Xvyuan Liu, Ziyou Wang, Rongze Tang, Zhaolu Wang, Zhuohang Li, Xin Zhang, Haisheng Su, Chen Gao, Wei Wu, Xinlei Chen, Yong Li
- **Qualifying affiliation(s):** Manifold AI — Xin Zhang, Haisheng Su, Wei Wu; FLAG: borderline (company tier unclear)
- **Categories:** cs.AI
- **Open release:** none
- **Shipped counterpart:** none found

**Summary:** CAER reweights the training loss of action-conditioned video world models toward action-responsive tokens, since a uniform space-time MSE lets static background dominate gradients while sparse interaction dynamics stay under-optimised.
**Purpose:** To focus supervision on tokens causally affected by actions.
**Breakthrough:** The authors report consistent improvements across heterogeneous action-conditioned tasks, an online method to identify action-responsive tokens without external annotation, and a theoretical analysis of when focused reweighting beats uniform averaging.
**Tools & method:** Wan 2.2 5B backbone trained on eight NVIDIA H20 GPUs; evaluated on LIBERO, RoboTwin 2.0, RealEstate10K and PoseAnything.
**Limitation:** The authors note sensitivity to hyperparameters (about 10% action dropout, fixed noise level 0.50) and open questions about scaling to longer horizons and larger models.
