**[A06] FlexiWorld: Learning and Planning via Flexible Action Chunks Across Multiple Time Scales**
- **arXiv:** 2609.35138 · <https://arxiv.org/abs/2609.35138>
- **Submitted:** 2026-09-28
- **Authors:** Shidu Ren, Qilin Gu, Zhenghao Ni, Junhan Sun, Jiaqi Wang, Damien Scieur, Yunze Liu
- **Qualifying affiliation(s):** Tencent Jarvis Lab — Jiaqi Wang (co-authors also affiliated with University of Toronto, Zhejiang University, Tsinghua University, Mila/Université de Montréal, Samsung SAIL)
- **Categories:** cs.LG
- **Open release:** weights (<https://huggingface.co/ryanren0330/FlexiWorld)> | code (<https://github.com/Shidu-Ren/FlexiWorld);> project page: <https://shidu-ren.github.io/FlexiWorld-Project-Page/>
- **Shipped counterpart:** none found

**Summary:** FlexiWorld is a JEPA-based world model that plans using variable-length action chunks across multiple time scales, jointly training a world model, causal action encoder, and autoregressive actor.
**Purpose:** The paper targets long-horizon control performance in world-model-based planning, where fixed action-chunk lengths limit either responsiveness or planning efficiency.
**Breakthrough:** The authors report "89.29% mean success" with ARCEM versus 83.98% for the strongest baseline (INTACT) across four benchmarks (PushT, OGBench-Cube, Reacher, TwoRoom), and on PushT at 100-step distance, success improves from 12.67% to 33.44%.
**Tools & method:** Training uses mixed-span goal supervision (35/55/75 primitive steps) with randomly partitioned variable-length action chunks (1–10 primitives), plus "Student Forcing" to address training-execution mismatch.
**Limitation:** The authors state that "reliable plan selection and execution remain challenges," and that Student Forcing "leaves recovery from perturbed physical states untested," identifying state perturbations and uncertainty-triggered reobservation as future work.
