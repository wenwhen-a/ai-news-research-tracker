**[A08] Learning-to-Memorize: Dynamic Context Management for Long-Horizon Autoregressive Video Generation**
- **arXiv:** 2611.01858 · <https://arxiv.org/abs/2611.01858>
- **Submitted:** 2026-11-01
- **Authors:** Haowei Zhu, Qijie Wang, Jia Li, Xing Wang, Tianyu Zhao, Jiexi Wang, Xurui Peng, Xinglong Wu, Junhai Yong, Bin Wang
- **Qualifying affiliation(s):** ByteDance Seed — Haowei Zhu (also Tsinghua University), Jia Li, Xing Wang, Tianyu Zhao, Jiexi Wang, Xurui Peng, Xinglong Wu
- **Categories:** cs.CV
- **Open release:** none found
- **Shipped counterpart:** none found

**Summary:** The paper proposes Learning to Memorize (L2M), a learned framework that decides which historical frames to keep, evict, or update during long-horizon autoregressive video generation, operating under a fixed KV-cache budget.
**Purpose:** The authors target the degradation in temporal consistency and quality that long-horizon autoregressive video generation suffers from when context management relies on naive fixed windows or hand-crafted heuristics.
**Breakthrough:** The authors report better long-horizon video quality and temporal consistency than existing context-management baselines.
**Tools & method:** L2M uses a lightweight importance-prediction router to score historical frames, degradation-aware training to make the model robust to noisy retained context, and teacher-student distillation with sparsity regularization to fit a fixed KV-cache budget during autoregressive generation.
**Limitation:** The authors state the router adds computational overhead during training and inference, though its lightweight design keeps this cost small.
