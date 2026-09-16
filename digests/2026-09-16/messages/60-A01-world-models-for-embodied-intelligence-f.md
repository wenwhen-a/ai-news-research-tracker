**[A01] World Models for Embodied Intelligence: From Plausible to Controllable to Actionable**
- **arXiv:** 2609.16697 · <https://arxiv.org/abs/2609.16697>
- **Submitted:** 2026-09-15 (v1)
- **Authors:** Nanjie Yao et al.
- **Qualifying affiliation(s):** Tencent — Jiafei Lyu; Alibaba Group — Steven Hoi, Dacheng Tao, Deheng Ye
- **Categories:** cs.RO; cs.AI
- **Open release:** none (project page only, no code/weights/demo stated) — <https://3dagentworld.github.io/EmbodiedWM/>
- **Shipped counterpart:** none found

**Summary:** This survey proposes a three-tier framework — Plausible, Controllable, Actionable — for organizing and evaluating world models used in embodied AI, tied to a 3×4 "grounding–improvement" matrix.
**Purpose:** The authors aim to give the field a shared way to evaluate world models by what they contribute to downstream behavior rather than by visual realism alone.
**Breakthrough:** The authors report that a "Plausible" model preserves task-relevant temporal, geometric, or physical structure; a "Controllable" model additionally predicts how interventions alter that structure; and an "Actionable" model further translates predictions into measurable gains in planning, action, learning, evaluation, verification, recovery, or data selection.
**Tools & method:** The paper is a literature survey structured around this three-tier taxonomy and the 3×4 grounding–improvement matrix, covering manipulation, navigation, locomotion, and autonomous driving applications; it introduces no new model, dataset, or benchmark of its own.
**Limitation:** The authors identify open problems including persistent state drift, modeling causal action effects, decision utility under computational budget constraints, joint grounding, uncertainty calibration, and reproducibility of evaluation; no dedicated "Limitations" section is present.
