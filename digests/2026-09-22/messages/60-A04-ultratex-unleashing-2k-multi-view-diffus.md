**[A04] UltraTex: Unleashing 2K Multi-View Diffusion for 3D Texturing**
- **arXiv:** 2609.23169 · <https://arxiv.org/abs/2609.23169>
- **Submitted:** 2026-09-19
- **Authors:** Yibo Zhang, Ze Yuan, Nan Cao, Li Zhang, Yan-Pei Cao, Yuan-Chen Guo, Rui Ma
- **Qualifying affiliation(s):** VAST, Beijing — Yan-Pei Cao, Yuan-Chen Guo; FLAG: borderline (VAST is an industry 3D-generation company but not on the confirmed top-tier list; other authors are Jilin University, University of Hong Kong, Tongji University, Fudan University, Shanghai Innovation Institute)
- **Categories:** cs.CV
- **Open release:** code/data at <https://yiboz2001.github.io/UltraTex> (per paper statement "Code and data is at ...")
- **Shipped counterpart:** none found

**Summary:** UltraTex is an efficient multi-view diffusion framework for generating high-quality 3D object textures at 2K (2048) resolution.
**Purpose:** The authors aim to overcome the computational limitations that prevent multi-view diffusion texturing methods from operating at high (2K) resolution.
**Breakthrough:** The authors report three techniques — background token dropping, block-sparse attention over the compressed foreground sequence, and foreground-aware VAE decoding — that together preserve texture quality while cutting cost.
**Tools & method:** The team built the G-buffer TexVerse dataset covering over 268,000 3D assets with multi-view renderings up to 4096×4096 resolution.
**Limitation:** The authors acknowledge the method may struggle with objects containing highly repetitive texture patterns, and that quality is bounded by the capability of the pretrained FLUX backbone.
