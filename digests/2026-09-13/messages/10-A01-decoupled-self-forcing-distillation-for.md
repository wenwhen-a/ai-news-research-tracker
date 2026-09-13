**[A01] Decoupled Self-Forcing Distillation for Streaming Talking Head Generation**
- **arXiv:** 2609.10317 · https://arxiv.org/abs/2609.10317
- **Submitted:** 2026-09-09
- **Authors:** Yanru An, Ruiyan Wang, Wenwu Wei, Rui Bu, Qi Wang, Hongwei Hu, Zhengxue Cheng, Rong Xie, Li Song, Wenjun Zhang
- **Qualifying affiliation(s):** Ant Group — Rui Bu (others: Shanghai Jiao Tong University); FLAG: borderline
- **Categories:** cs.CV
- **Open release:** none stated
- **Shipped counterpart:** none found

**Summary:** A streaming talking-head generator that fuses audio in a low-dimensional, identity-disentangled motion space rather than at the pixel level; a small causal autoregressive transformer produces motion latents that a pretrained diffusion renderer turns into video.
**Purpose:** Real-time, low-latency audio-driven talking-head video without quality loss, and mitigation of exposure bias in autoregressive streaming.
**Breakthrough:** The authors report 15.4 FPS at 1.3 s latency "with no quality degradation," with a motion generator of only 77M parameters.
**Tools & method:** "Decoupled self-forcing distillation" from a frozen bidirectional teacher into a block-causal renderer; MEAD and Hallo3 data; X-NeMo, umT5-base, wav2vec2-base and Qwen2.5-VL-7B components; trained on 4 A100 GPUs, evaluated on one H200.
**Limitation:** The authors note slightly higher first-frame latency than AvatarForcing and that visual quality is capped by the renderer backbone.
