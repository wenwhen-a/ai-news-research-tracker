**[A01] WINGS: Reference-Free Gaussian Splatting Inpainting with 3D-Native Generative Priors**
- **arXiv:** 2609.37816 · <https://arxiv.org/abs/2609.37816>
- **Submitted:** 2026-09-29 (v1)
- **Authors:** Noé Lallouet, Michael Fischer, Elie Michel
- **Qualifying affiliation(s):** Adobe (all three authors; Noé Lallouet also affiliated with MILES/LAMSADE, Paris Dauphine – PSL University)
- **Categories:** cs.CV
- **Open release:** none found (preprint under review)
- **Shipped counterpart:** none found

**Summary:** WINGS inpaints missing/masked regions of 3D Gaussian Splatting (3DGS) scenes natively in 3D, rather than via 2D diffusion models applied to reference views.
**Purpose:** Prior 3DGS inpainting relies on 2D diffusion models to generate one or more reference views, which suffers from multi-view inconsistency and lengthy per-scene optimization.
**Breakthrough:** The authors report their method avoids multi-view inconsistency by construction and is faster than comparable 2D-based inpainting approaches, validated through quantitative experiments and a user study; they describe it as the first Gaussian-splatting inpainting method operating in a 3D-native generative prior's learned representation space without reference views.
**Tools & method:** The method uses the embedding space of a large pretrained 3D prior (built on a TRELLIS VAE-style decoder) combined with a structure-completion network to reconstruct masked-region geometry and appearance directly in 3D Gaussian space.
**Limitation (≤3 sentences, authors' own):** The authors state that content generation for complex/intricate patterns in latent space is biased toward axis-aligned patterns and struggles with misaligned motifs (partly addressed with an axis-alignment heuristic), and that the TRELLIS VAE decoder's architecture prevents generating higher-order spherical harmonic components of the inpainted splats.
