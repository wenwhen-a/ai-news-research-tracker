**[A08] One Prior, Two Dynamics: Repurposing Video Diffusion Transformers for Self-Supervised Latent Action Learning**
- **arXiv:** 2611.26617 · <https://arxiv.org/abs/2611.26617>
- **Submitted:** 2026-11-19
- **Authors:** Yuxin Jiang et al.
- **Qualifying affiliation(s):** Tencent — listed in the paper's affiliation block alongside Show Lab/NUS, A*STAR, and Stanford for the first five authors (Jiang, Sun, Li, Gu, Zhang); the HTML affiliation block does not map "Tencent" to one specific name, but the affiliation itself is explicitly present (not a false-match); FLAG: borderline (exact author-to-Tencent mapping unverifiable from the rendered page)
- **Categories:** cs.CV (primary), cs.AI, cs.LG, cs.RO
- **Open release:** code (<https://github.com/showlab/O2LaF>), project page (<https://showlab.github.io/o2laf>)
- **Shipped counterpart:** none found

**Summary:** The paper proposes O²LaF, a self-supervised latent-action framework that initializes both an inverse-dynamics encoder (IDM) and a forward-dynamics video generator (FDM) from the same pretrained video diffusion transformer (Wan2.2-TI2V-5B), trained end-to-end through a compact latent bottleneck, with no action labels required.
**Purpose:** Prior latent-action learning largely trains inverse- and forward-dynamics models from scratch or on frozen features, leaving a gap between the two and underusing pretrained video generators.
**Breakthrough:** The authors report state-of-the-art few-shot action probing on camera navigation (e.g., 94.37% joint exact-match for 3rd-person at k=50) and robot manipulation (EEF R² of 0.277 vs. 0.149 for DreamDojo), plus better zero-shot action transfer across visual contexts and embodiments than AdaWorld and Olaf-World on their reported metrics.
