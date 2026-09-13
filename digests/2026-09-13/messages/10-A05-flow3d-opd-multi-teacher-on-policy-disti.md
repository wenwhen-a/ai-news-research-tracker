**[A05] Flow3D-OPD: Multi-Teacher On-Policy Distillation for 3D Geometry Generation with Flow-Matching Diffusion Transformer**
- **arXiv:** 2609.07137 · https://arxiv.org/abs/2609.07137
- **Submitted:** 2026-09-07
- **Authors:** Zhiwei Ning, Zhen Zhou, Puhua Jiang, Xintong Han, Gengming Zhang, Jie Yang, Zhonglong Zheng, Yuanjie Zheng, Wei Liu, Chunchao Guo
- **Qualifying affiliation(s):** Tencent (Tencent Hunyuan3D) — Zhiwei Ning, Zhen Zhou, Puhua Jiang, Xintong Han, Chunchao Guo
- **Categories:** cs.CV, cs.AI
- **Open release:** none
- **Shipped counterpart:** none found

**Summary:** A two-stage post-training framework for image-to-3D flow-matching diffusion transformers that applies multi-teacher on-policy distillation to improve mesh geometry quality after pretraining.
**Purpose:** It addresses the difficulty of defining reinforcement-learning rewards for 3D geometric quality and the gradient interference that arises when optimising several heterogeneous quality objectives jointly.
**Breakthrough:** The authors first train domain-specialised teachers via direct preference optimisation guided by an agentic verifier, then consolidate them into one student by on-policy distillation with hard task-routing and gradient accumulation; they report the student surpasses every teacher on the average metric (win ratios: Teacher1 47.8%, Teacher2 53.0%, Teacher3 56.9%, Ours 61.0%).
**Tools & method:** Flow-matching DiT image-to-3D pipeline with VAE decoding and isosurface extraction; ULIP/Uni3D-based teachers; an agentic verifier as reward model; DPO for teacher training.
**Limitation:** No code or weight release is mentioned (observed, not stated); the paper's stated limitations were not captured by the fetch.
