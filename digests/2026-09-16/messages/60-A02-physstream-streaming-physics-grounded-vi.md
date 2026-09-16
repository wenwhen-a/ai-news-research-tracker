**[A02] PhysStream: Streaming Physics-Grounded Video Generation with Structured Scene Memory and Fine-Grained Motion Control**
- **arXiv:** 2609.17521 · <https://arxiv.org/abs/2609.17521>
- **Submitted:** 2026-09-15
- **Authors:** Chuhao Chen et al.
- **Qualifying affiliation(s):** Snap Inc. — Peter Wonka (also KAUST), Chaoyang Wang, Sergey Tulyakov; **FLAG: borderline — Snap Inc. is not on the core tracked list, treated as a comparable industry lab**
- **Categories:** cs.CV, cs.AI, cs.GR
- **Open release:** none stated — project page only, no code/weights/demo link given: <https://czzzzh.github.io/PhysStream>
- **Shipped counterpart:** none found

**Summary:** PhysStream is an autoregressive, physics-grounded image-to-video model that lets a user interactively steer multi-object rigid-body scenes with sparse 3D velocity-increment signals during generation, rather than requiring a full pre-planned control schedule.
**Purpose:** The authors state that prior interactive video-control methods either require the entire control sequence specified upfront or use pixel-space signals (e.g., drag points) that dictate object positions directly rather than encoding real physical dynamics.
**Breakthrough:** On a synthetic multi-object benchmark, the authors report PhysStream reduces motion-distribution distance (FVMD) by 33% and trajectory error by 12% versus the strongest baselines (FVMD 787.0 vs.
**Tools & method:** The model fine-tunes a Wan2.2-TI2V-5B backbone in two stages — first bidirectional fine-tuning with velocity-increment conditioning, then conversion to a causal autoregressive model via teacher-forcing that adds the online scene-memory signals (estimated with Depth-Anything-3 and SAM2) — using shifted channel concatenation to inject conditions without frame leakage.
