**[A03] Rollout-Marginal Distillation for Long-Horizon Autoregressive Video Generation**
- **arXiv:** 2609.37925 · <https://arxiv.org/abs/2609.37925>
- **Submitted:** 2026-09-29 (v1)
- **Authors:** Chenjian Gao, Zhihao Hu, Jianqi Ma, Jun Zhang, Weidong Zhang, Tianfan Xue
- **Qualifying affiliation(s):** Tencent AIPD — Jianqi Ma, Weidong Zhang (Chenjian Gao: MMLab, CUHK)
- **Categories:** cs.CV; cs.AI
- **Open release:** code + pretrained weights — project page <https://cjeen.github.io/RMD/> and GitHub github.com/cjeen/RMD (confirmed non-empty repo with training/inference code and weights via Hugging Face)
- **Shipped counterpart:** none found

**Summary:** The paper addresses error accumulation in autoregressive (chunk-by-chunk) video generation, where quality degrades far beyond the training horizon.
**Purpose:** Long-horizon autoregressive video generators accumulate error over successive chunks, degrading quality as rollouts extend past their training length.
**Breakthrough:** The authors report that RMD "maintains high visual quality far beyond its training horizon" compared to existing methods; the project's own tagline states the model is trained on 5-second clips and can "generate far beyond" that length (e.g., minute-long videos).
**Tools & method:** Two-stage distillation: (1) chunk-level distillation, scoring each generated chunk against a chunk teacher while retaining generated history for prediction, then (2) video-level processing to restore cross-chunk temporal consistency.
**Limitation:** No dedicated "Limitations" section was found in the fetched paper HTML.
