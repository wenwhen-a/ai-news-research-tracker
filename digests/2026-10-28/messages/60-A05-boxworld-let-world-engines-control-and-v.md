**[A05] BoxWorld: Let World Engines Control and Video Generators Render**
- **arXiv:** 2610.36371 · <https://arxiv.org/abs/2610.36371>
- **Submitted:** 2026-10-26
- **Authors:** Zike Wu, Ahmed Hatem, Chintan Trivedi, Wallace Michel Pinto Lira, Xuebin Qin, Lele Wang, Renjie Liao
- **Qualifying affiliation(s):** Huawei Canada — Ahmed Hatem, Chintan Trivedi, Wallace Michel Pinto Lira, Xuebin Qin; FLAG: borderline (Huawei is a comparable top-tier industry lab not on the illustrative list, per tracker rules)
- **Categories:** cs.CV
- **Open release:** demo/project page only — project page at <https://boxworld-web.github.io>; no code or weights release stated in the abstract
- **Shipped counterpart:** none found

**Summary:** BoxWorld builds real-time interactive video worlds with user-defined rules by separating interaction logic from video rendering.
**Purpose:** The authors target a limitation of end-to-end video world models: learning interaction dynamics purely inside the video generator makes it hard to specify object-level rules or reason about their consequences.
**Breakthrough:** The authors report that BoxWorld substantially outperforms end-to-end world models and remains competitive across multiple public benchmarks.
**Tools & method:** The system uses a coding agent to build the rule-based Box World Engine, and a three-stage training strategy for the renderer: object grounding from open-domain videos, state-transition learning from automatically annotated gameplay videos, and rollout distillation on self-generated histories.
**Limitation:** The authors note that rendering the evolving state stream is "non-trivial" because the renderer must respond to object-level state updates in real time while staying coherent with generated history (stated as a design challenge, not fully resolved).
