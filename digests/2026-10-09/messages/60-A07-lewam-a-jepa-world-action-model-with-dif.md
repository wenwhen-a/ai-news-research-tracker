**[A07] LeWAM: A JEPA World Action Model with Diffusion-Steering-Based MPC**
- **arXiv:** 2610.12407 · <https://arxiv.org/abs/2610.12407>
- **Submitted:** 2026-10-08 (v1)
- **Authors:** Shashank Hegde, Alexander Popov, Elie Aljalbout, Nikolai Smolyanskiy
- **Qualifying affiliation(s):** NVIDIA — all four authors (sole affiliation listed in HTML author block)
- **Categories:** cs.RO (primary), cs.AI, cs.CV
- **Open release:** none stated
- **Shipped counterpart:** none found

**Summary:** LeWAM is a bidirectional transformer that performs forward dynamics, backward dynamics, inverse dynamics, and policy prediction on a shared, decoder-free JEPA latent, trained end-to-end across all four modes.
**Purpose:** The authors aim to replace the noisy, redundant reconstruction-based representations typically used by world action models with a cleaner JEPA latent, and to improve planning by not sampling raw actions directly.
**Breakthrough:** The authors report that linear probes read robot and object state from LeWAM's latent better than from a forward-only JEPA world model, while the latent still ignores visual distractors as well as that forward-only model (and better than a reconstruction-based WAM).
**Tools & method:** The core method is a JEPA-based latent trained jointly for forward, backward, and inverse dynamics plus policy prediction, combined with diffusion-steering-based model predictive control (MPC).
**Limitation:** The abstract states that sampling raw actions during MPC planning "lets MPC exploit dynamics-model inaccuracies," which is the specific failure mode their noise-space planning is designed to avoid; no other limitations are stated in the abstract.
