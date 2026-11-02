**[A01] Hierarchical World Models with Implicit Dynamics**
- **arXiv:** 2610.42146 · <https://arxiv.org/abs/2610.42146>
- **Submitted:** 2026-10-30
- **Authors:** Gaoyue Zhou, Yvonne Wu, Zichen Jeff Cui, Nicolas Ballas, Mido Assran, Lerrel Pinto, Yann LeCun
- **Qualifying affiliation(s):** Meta-FAIR — Nicolas Ballas, Mido Assran (affiliation marker "2" = Meta-FAIR in the author block)
- **Categories:** cs.RO (primary), cs.AI
- **Open release:** demo (project page with videos, <https://id-wm.github.io>; no code/weights release found)
- **Shipped counterpart:** none found

**Summary:** The paper introduces ID-WM (Implicit Dynamics World Models), a hierarchical world model for embodied planning that separates state-space reachability from local control.
**Purpose:** The authors target long-horizon planning with world models, where existing hierarchical methods use rigid macro-actions or latent skills that produce brittle representations and limited fine-grained control.
**Breakthrough:** The authors report a 38.5% improvement over state-of-the-art policy and diffusion-based planners across three navigation and manipulation suites.
**Tools & method:** The method combines a high-level transition sampler operating in a diffusion latent space with a low-level inverse-dynamics world model; inference-time wall-clock cost was measured on a single NVIDIA L40S GPU against baselines including GCBC, HIQL, Diffuser, and H-Diffuser.
**Limitation:** The authors state that ID-WM's reliance on search-based optimization within a diffusion latent space incurs higher inference time than reactive policies or deterministic world models, and note future work on amortized or gradient-based planning to address this.
