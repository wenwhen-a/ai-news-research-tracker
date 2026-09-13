**[A06] Flexible Motion Generation from Language and Style References**
- **arXiv:** 2609.08032 · https://arxiv.org/abs/2609.08032
- **Submitted:** 2026-09-07
- **Authors:** Kai Weixian Lan, Bodie Criswell, Briana Fedkiw, Zhan Zhang, Joseph Teran, Daniel Holden
- **Qualifying affiliation(s):** Epic Games — Zhan Zhang, Joseph Teran, Daniel Holden (the first three authors' contributions were made during Epic Games internships)
- **Categories:** cs.CV, cs.GR, cs.LG
- **Open release:** none stated
- **Shipped counterpart:** none found

**Summary:** FlexMoGen generates human motion conditioned jointly on a text prompt (content) and a style-reference motion clip (timing, limb articulation, dynamics), learning a variational style encoder without style labels.
**Purpose:** To give users control over both content and style, including long, time-varying multi-style synthesis that label-based methods could not generalise to.
**Breakthrough:** The authors report FlexMoGen "achieves the best balance between content fidelity and style reflection" relative to prior methods; accepted at Pacific Graphics 2026.
**Tools & method:** Joint pretraining of the style encoder and a text-to-motion latent diffusion model, a lightweight adaptation module and a relative positional encoding; trained on 100STYLE (100 styles, 8 gaits) and an internal MoCap set of 3,089 clips (about 6.4 hours).
**Limitation:** The authors report transfer is "hit or miss" for styles outside 100STYLE and that outputs tend to be over-smoothed, suppressing rapid limb movement.
