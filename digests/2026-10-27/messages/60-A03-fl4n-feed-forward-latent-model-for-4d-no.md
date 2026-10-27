**[A03] FL4N: Feed-forward Latent Model for 4D Novel View Synthesis**
- **arXiv:** 2610.35854 · <https://arxiv.org/abs/2610.35854>
- **Submitted:** 2026-10-26
- **Authors:** Eunbeen Hong et al.
- **Qualifying affiliation(s):** Google DeepMind — the HTML author block lists two team affiliations, "KAIST AI" and "Google DeepMind," for the full author group; the page carries no per-author superscripts, so the exact author(s) tied to Google DeepMind cannot be isolated from the page itself.
- **Categories:** cs.CV
- **Open release:** code + weights — GitHub: github.com/cvlab-kaist/FL4N (link present on project page; direct fetch returned HTTP 403, likely bot-blocking rather than absence); HuggingFace model page: huggingface.co/eunbeen-hong/FL4N (returned HTTP 200); project page: <https://cvlab-kaist.github.io/FL4N/>
- **Shipped counterpart:** none found

**Summary:** FL4N is presented as the first feed-forward latent model for 4D novel view synthesis (NVS), rendering dynamic scenes across new viewpoints and timestamps from monocular video without explicit 4D Gaussian primitives.
**Purpose:** The paper targets a limitation of existing monocular feed-forward 4D NVS methods, which rely on explicit 4D Gaussian representations and are prone to temporal inconsistency and rendering artifacts.
**Breakthrough:** The authors report that modeling temporal dynamics as residuals on top of a pretrained static latent prior enables effective 4D modeling even with limited dynamic training data.
**Tools & method:** The method is a feed-forward latent 4D NVS model built on a static latent prior plus a residual dynamic encoder trained with an image synthesis objective (no explicit 4D Gaussian splatting).
