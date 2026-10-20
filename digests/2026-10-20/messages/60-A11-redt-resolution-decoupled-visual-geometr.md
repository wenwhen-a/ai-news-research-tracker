**[A11] ReDT: Resolution-Decoupled Visual Geometry Transformer**
- **arXiv:** 2610.25517 · <https://arxiv.org/abs/2610.25517>
- **Submitted:** 2026-10-18
- **Authors:** Abteen Arab, Guile Wu, Dongfeng Bai
- **Qualifying affiliation(s):** Huawei Noah's Ark Lab — Abteen Arab (also University of British Columbia; footnote says work done during an internship at Huawei Canada), Guile Wu, Dongfeng Bai; FLAG: borderline
- **Categories:** cs.CV
- **Open release:** none found
- **Shipped counterpart:** none found

**Summary:** ReDT is a feed-forward transformer for multi-view 3D reconstruction built on the VGGT family (specifically VGGT-Ω), designed to handle high-definition inputs without the quality degradation and quadratic cost that standard-definition-trained models show at higher resolutions.
**Purpose:** The authors aim to let a visual geometry transformer trained at lower resolution generalize to much higher resolutions (SD to 2K) without retraining, motivated by an empirical finding that intermediate per-view features keep a nearly constant effective rank as resolution and view count grow.
**Breakthrough:** On ETH3D at 2K, the authors report a 16× speedup (6.35s vs 102.70s), 34% peak-memory reduction (64.47GB vs 98.09GB), and 33% Chamfer-distance reduction (0.1140 vs 0.1702) versus VGGT-Ω.
**Tools & method:** The encoder uses a quadtree to merge low-entropy patches into 2×2/4×4/8×8 regions, and DIVA blocks replace standard attention with learned softmax assignments mapping N tokens to K fixed basis tokens, using test-time training (TTT) for cross-view reasoning in the basis space.
**Limitation:** The paper has no dedicated limitations section, but the appendix states overall complexity remains quadratic in token count because the DPT decoder head is left unchanged, and peak memory still grows with resolution.
