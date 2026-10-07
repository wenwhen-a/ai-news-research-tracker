**[A13] SUAVE: Unified Video-Action Models via Masked Diffusion**
- **arXiv:** 2610.04009 · <https://arxiv.org/abs/2610.04009>
- **Submitted:** 2026-10-02
- **Authors:** Rhythm Syed et al.
- **Qualifying affiliation(s):** Toyota Research Institute — Jean Mercat, Sedrick Keh, Kushal Arora, Paarth Shah, Aykut Onol, Mengchao Zhang (and Rhythm Syed, dual-affiliated with Columbia University and Toyota Research Institute) (FLAG: borderline)
- **Categories:** cs.RO; cs.CV; cs.LG
- **Open release:** none confirmed
- **Shipped counterpart:** none found

**Summary:** The paper presents SUAVE, a unified video-action model in which a masked diffusion transformer generates video and robot actions conditioned on language, with all three modalities represented as discrete tokens in one shared sequence.
**Purpose:** The authors state that vision-language-action models are typically optimized to predict actions without imagining future observations, while world-action models built on video diffusion can imagine the future but treat language as frozen conditioning, and unified approaches so far either decode autoregressively token-by-token or bolt an auxiliary action head onto continuous video — motivating a single shared-token architecture for both.
**Breakthrough:** The authors report that a single SUAVE model predicts long-horizon video and acts as a policy competitively with dedicated world models/specialized policies on static and dynamic manipulation tasks, and that on a real robot it generates subgoal images plus a one-second action chunk in 1,030 ms on an RTX 5090 GPU, sustaining closed-loop control at 2.5 actions per second; pretraining on robot video plus co-training on human video substantially improves policy performance and zero-shot robustness to distribution shift.
