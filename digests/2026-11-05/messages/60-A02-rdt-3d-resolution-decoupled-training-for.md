**[A02] RDT-3D: Resolution-Decoupled Training for High-Fidelity 3D Geometry Generation**
- **arXiv:** 2611.06141 · <https://arxiv.org/abs/2611.06141>
- **Submitted:** 2026-11-04
- **Authors:** Jiale Zhang, Yang Liu, Chengyang Li, Jin Yuan, Qianxi Jia, Taicheng Huang
- **Qualifying affiliation(s):** JD.com, Beijing, China — all listed authors (single affiliation block for the whole author group)
- **Categories:** cs.CV
- **Open release:** none yet (the authors say they "will open-source Dual3D-300K," but give no link)
- **Shipped counterpart:** none found

**Summary:** The paper targets high-fidelity 3D geometry generation, which needs both global structural coherence and fine surface detail.
**Purpose:** The authors aim to fix oversmoothed thin structures and rounded sharp edges that they attribute to the resolution mismatch in existing coarse-to-fine 3D generation pipelines.
**Breakthrough:** RDT anchors RoPE guidance at 512 resolution while supervising geometry at 1536 resolution; the authors report this substantially improves sharp geometric regions.
**Tools & method:** Training used the Dual3D-300K dataset (coarse/fine coordinate-aligned point clouds and rendered images) with AdamW, learning rate 1e-5, bfloat16 precision, batch size 64, 300k training steps, and 10,240 latent tokens; the paper states training ran on 88 NVIDIA B200 GPUs (figure may contain a typo for 8).
**Limitation:** The paper has no dedicated limitations section.
