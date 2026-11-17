**[A03] Reference Forcing: Long Video Generation with Region-Guided Drift Correction**
- **arXiv:** 2611.21559 · <https://arxiv.org/abs/2611.21559>
- **Submitted:** 2026-11-16 (v1)
- **Authors:** Sheng Zhao et al.
- **Qualifying affiliation(s):** Adobe — Haitian Zheng (co-authors otherwise at University of Rochester)
- **Categories:** cs.CV
- **Open release:** code/demo — project page with visualizations and code at <https://zhaosheng-thu.github.io/reference-force/> (no model weights mentioned)
- **Shipped counterpart:** none found

**Summary:** Long autoregressive video generators drift in subject/background appearance over time because they are distilled over short windows and KV-cache history can itself have drifted.
**Purpose:** To stop long (minutes-scale) autoregressively generated videos from losing a consistent subject/background appearance over time, a known failure of distillation-based fast video generators.
**Breakthrough:** The authors report that a teacher model forces each region of a new frame to attend to the matching region in the initial frames (found via off-the-shelf segmentation), then distills this into a student attention path needing no external models at inference, plus a "value correction" step that pulls drifted KV-cache values back toward the clean initial-frame values.
**Tools & method:** Built on top of frozen LongLive-1.3B and Self-Forcing 1.3B base models (only the new "anchor path" is trained), evaluated with VBench-Long metrics, DINOv2-based L-Consistency, MiraBench tracking strength, a 7-participant user study, and a VLM judge, against baselines MemRoPE, LongLive-RAG, ∞-RoPE, and Deep Forcing.
