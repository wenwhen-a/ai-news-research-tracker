**[A02] DSD: Learning Diverse and Reusable Motor Skills via Diffusion Skill Discovery**
- **arXiv:** 2609.17682 · <https://arxiv.org/abs/2609.17682>
- **Submitted:** 2026-09-15
- **Authors:** Sun Woo Kim, Xue Bin Peng
- **Qualifying affiliation(s):** NVIDIA — Xue Bin Peng (also Simon Fraser University)
- **Categories:** cs.LG (procedural animation, reinforcement learning)
- **Open release:** none stated
- **Shipped counterpart:** none found

**Summary:** DSD trains a diffusion model alongside a control policy to discover diverse, reusable motor skills for simulated characters by approximating entropy gradients over states, rather than relying on discriminator-based skill discovery.
**Purpose:** The authors aim to learn character motor skills that are both diverse (covering distinct behaviors, and spatial/temporal variation) and reusable for downstream zero-shot control tasks.
**Breakthrough:** The authors report their diffusion-based entropy approximation yields skills with distinct behaviors as well as spatial and temporal variation, evaluated on three motion datasets: Reallusion (~30 min of gladiator-style sword/shield motions), LaFAN1 (~160 min of everyday/expressive motions), and MimicKit (2.5 min of highly dynamic behaviors).
**Tools & method:** The method combines a diffusion model with a reinforcement-learning policy trained under a state-marginal-entropy objective, conditioned on latent skill variables.
**Limitation:** The authors acknowledge the current objective does not explicitly organize the latent space according to semantic relationships, and that zero-shot control performance depends on whether a suitable behavior was recorded in the offline trajectory pool.
