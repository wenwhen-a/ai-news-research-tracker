**[A57] LumiTokens: 3D Relighting via Token-Space Lighting Transformation**
- **arXiv:** 2608.18215 · https://arxiv.org/abs/2608.18215
- **Submitted:** 2026-08-18
- **Authors:** Yiwen Chen, Matheus Gadelha, Huaizu Jiang
- **Qualifying affiliation(s):** Adobe Research — Matheus Gadelha
- **Categories:** cs.CV
- **Open release:** none
- **Shipped counterpart:** none found

**Summary:** Performs 3D relighting as a direct transformation in a learned token space, without explicit material decomposition or physically based re-rendering.
**Purpose:** To replace costly inverse-rendering pipelines with a token-space method that handles environment maps, point lights and area lights through one interface.
**Breakthrough:** The authors report multi-view PSNR 30.48 dB (versus 28.40 dB for Neural Gaffer) and novel-view PSNR 27.76 dB (versus 26.17 dB for TensoIR) from only 8 input views versus 30 to 50 for other methods, at 3.79 s inference versus 3952.91 s for TensoIR.
**Tools & method:** Scene and lighting encoded as Plücker ray tokens edited by a self-attention Scene Token Editor; trained on 20,000 Objaverse objects under 16 lighting conditions (about 20.8M images) plus 3,000 multi-object scenes on 8 NVIDIA H100 GPUs.
**Limitation:** The authors state that extending to real captures with complex materials and imperfect poses remains future work.
