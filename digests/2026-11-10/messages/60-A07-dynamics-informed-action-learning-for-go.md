**[A07] Dynamics-Informed Action Learning for Goal-Conditioned Latent Planning**
- **arXiv:** 2611.10660 · <https://arxiv.org/abs/2611.10660>
- **Submitted:** 2026-11-07
- **Authors:** Yinuo Jiang, Guangzhi Wang, Yiran Wang, Junfu Pu, Cheng Cheng, Honghao Chen, Ying Shan
- **Qualifying affiliation(s):** Tencent ARC Lab — Yiran Wang, Cheng Cheng, Ying Shan (Ying Shan is Tencent ARC Lab's well-known lead; author-to-footnote mapping was partly garbled in the HTML but the Tencent ARC Lab affiliation is clearly listed)
- **Categories:** cs.CV (primary), cs.RO
- **Open release:** none found
- **Shipped counterpart:** none found

**Summary:** The paper introduces Dynamics-Informed Action Learning (DIAL), a method for latent world models used in visual control planning.
**Purpose:** The authors aim to align latent world-model training with how the model is actually used at planning/test time, closing the train-test mismatch between teacher-forced dynamics training and autoregressive rollout-based planning.
**Breakthrough:** The authors report a rollout-alignment training scheme that exposes the forward model to its own predictions, paired with a lightweight inverse dynamics head that infers actions from latent transitions and is also applied (frozen) to model-generated rollouts.
**Tools & method:** The method is evaluated on latent world models for visual control, using a Cross-Entropy Method (CEM) planner refined from the learned inverse-dynamics-informed initialization, tested across four visual control benchmarks in both standard and long-horizon scenarios.
**Limitation:** Not stated by the authors in the abstract or main text reviewed.
