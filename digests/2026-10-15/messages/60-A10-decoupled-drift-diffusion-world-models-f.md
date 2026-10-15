**[A10] Decoupled Drift-Diffusion World Models for Consistent Future Frame Prediction**
- **arXiv:** 2610.19212 · <https://arxiv.org/abs/2610.19212>
- **Submitted:** 2026-10-13
- **Authors:** Anton Arapin et al.
- **Qualifying affiliation(s):** NVIDIA — Jun Gao (all five authors are also listed with University of Michigan)
- **Categories:** cs.CV
- **Open release:** project page at <https://anton-arapin.github.io/d3wm-site/>; the paper's AI-use statement mentions "polishing code for the release" but no code repository link was found yet
- **Shipped counterpart:** none found

**Summary:** D3WM (Decoupled Drift-Diffusion World Model) predicts future video frames conditioned on action sequences by combining a deterministic transformer prediction with a diffusion model gated by a learned spatial uncertainty map.
**Purpose:** The goal is more consistent future-frame prediction in action-conditioned world models, avoiding both over-smoothed deterministic predictions and unnecessary stochastic variation in parts of a scene that are actually predictable.
**Breakthrough:** The authors report that D3WM shows improved results over competitive baselines across two distinct types of action spaces, and that the spatial location of stochastic changes is itself learnable rather than fixed.
**Tools & method:** A transformer trained with a Gaussian negative-log-likelihood objective outputs both a deterministic next-state prediction and a spatial aleatoric-uncertainty map; that map gates a conditional diffusion model; the method is evaluated on robotic tabletop manipulation and camera-motion prediction tasks using two reference input views.
