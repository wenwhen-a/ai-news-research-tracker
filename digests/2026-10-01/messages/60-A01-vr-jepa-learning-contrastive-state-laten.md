**[A01] VR-JEPA: Learning Contrastive-State Latent Guidance for Generation-based Video Reasoning**
- **arXiv:** 2609.40129 · <https://arxiv.org/abs/2609.40129>
- **Submitted:** 2026-09-30
- **Authors:** Zehua Ma et al. (12 authors)
- **Qualifying affiliation(s):** Tencent (author affiliation #4 in the paper's institution list)
- **Categories:** cs.CV
- **Open release:** none (no code, weights, or demo link found)
- **Shipped counterpart:** none found

**Summary:** The paper targets generation-based visual reasoning, where a video diffusion model is used to "think" by generating a rollout, but plain generation lacks guidance on which visual states matter for the reasoning task and is prone to physical/structural inconsistencies.
**Purpose:** The authors want generation-based reasoning models to focus supervision on the visual states and regions that are actually informative for a task, rather than optimizing uniformly over every generated frame.
**Breakthrough:** The authors report an 11.33% relative improvement over "the cutting-edge generation-based reasoning baseline" on VBVR-Pro-Bench, moving overall accuracy from 50.3% to 56.0%.
**Tools & method:** The method has two parts: Localized Contrastive-State Learning (LCL), which contrasts successful videos against task-matched generated candidates in V-JEPA feature space to weight supervision toward informative states/regions, and a Skill-Routed Mixture of Experts (SR-MoE) with seven skill-specific experts (e.g., spatial reasoning, numerical reasoning, dynamics) combined via adaptive routing.
**Limitation:** The authors' own ablations show the gain is much smaller out-of-domain (1.0 point) than in-domain (10.5 points), indicating the contrastive-state guidance generalizes less robustly to held-out reasoning types.
