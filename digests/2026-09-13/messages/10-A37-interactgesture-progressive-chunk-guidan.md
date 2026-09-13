**[A37] InteractGesture: Progressive Chunk Guidance for Continuous Streaming Co-Speech Gesture Control**
- **arXiv:** 2608.25734 · https://arxiv.org/abs/2608.25734
- **Submitted:** 2026-08-26
- **Authors:** Ekkasit Pinyoanuntapong, Ajinkya Deogade, Paul Streli, Wenjing Zhang, Joanna Materzynska, Pu Wang, Vittorio Ferrari, Jie Shen
- **Qualifying affiliation(s):** Meta — Ajinkya Deogade, Paul Streli, Wenjing Zhang, Joanna Materzynska, Vittorio Ferrari, Jie Shen
- **Categories:** cs.CV
- **Open release:** demo (project page https://exitudio.github.io/interactgesture-page)
- **Shipped counterpart:** none found

**Summary:** Adds inference-time per-joint spatial control to pretrained co-speech gesture generators through a diffusion sampler and differentiable decoder, with "Progressive Chunk Guidance" that keeps editable staggered chunk latents so constraints propagate across streaming chunk boundaries.
**Purpose:** Co-speech gesture generators lack per-joint spatial control (for example pointing at a target) in a streaming setting.
**Breakthrough:** On BEAT2 with GestureLSM the authors report FGD 0.431 with Progressive Chunk Guidance versus 0.442 synchronous, and average control error 6.335 cm streaming versus 11.701 cm for a Sequential Chunk Guidance baseline.
**Tools & method:** BEAT2 dataset, GestureLSM backbone, 30 FPS in 128-frame chunks with fixed-step DDIM sampling; hardware not disclosed.
**Limitation:** The authors state excessive post-sampling optimisation "can diminish naturalness."
