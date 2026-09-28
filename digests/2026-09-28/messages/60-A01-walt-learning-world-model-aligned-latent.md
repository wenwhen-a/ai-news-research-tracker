**[A01] WALT: Learning World-Model-Aligned Latent Trajectories for Autonomous Driving**
- **arXiv:** 2609.30436 · <https://arxiv.org/abs/2609.30436>
- **Submitted:** 2026-09-24
- **Authors:** Mingkai Jia et al.
- **Qualifying affiliation(s):** Horizon Robotics — Mingkai Jia, Zhijian Shu, Jiawei Xu, Mingxiao Li, Wei Yin; FLAG: borderline (Horizon Robotics is not on the core tracked list; kept per the "comparable labs, flag" rule)
- **Categories:** cs.RO, cs.CV
- **Open release:** none (no code/project page found in the paper)
- **Shipped counterpart:** none found

**Summary:** The paper proposes WALT (World-Model Alignment for Latent Trajectories), a method that builds a compact generative trajectory latent space by transferring knowledge from a frozen, pretrained driving world model (EponaV2) into a dual-branch trajectory autoencoder.
**Purpose:** The authors state that driving world models learn rich predictive visual representations, but accurate visual prediction does not automatically translate into effective trajectory planning because visual world states and raw geometric trajectories are misaligned.
**Breakthrough:** The authors report that rather than generating raw waypoints directly, their dual-branch trajectory autoencoder imports semantic knowledge from the frozen visual world model into trajectory representations via Joint-Embedding Predictive Architecture and Representation Alignment techniques.
**Tools & method:** The tokenizer stage was trained for 100 epochs on 32 H20 GPUs with a fixed learning rate of 1×10⁻⁴, using a frozen EponaV2 world model and a latent configuration of two 32-dimensional tokens (24 semantic + 8 reconstruction channels each).
