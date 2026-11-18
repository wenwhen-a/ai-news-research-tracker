**[A05] FVScore: Specification-Driven Neuro-Symbolic Video Evaluation**
- **arXiv:** 2611.22673 · <https://arxiv.org/abs/2611.22673>
- **Submitted:** 2026-11-17
- **Authors:** Do Xuan Long, Long T. Le, Yiwen Song, Min-Yen Kan, Tomas Pfister, Yale Song
- **Qualifying affiliation(s):** Google Cloud AI Research — Long T. Le, Yiwen Song, Tomas Pfister, Yale Song
- **Categories:** cs.CV, cs.AI
- **Open release:** demo (project page: <https://dxlong2000.github.io/FVSCORE/>); no code/weights link found
- **Shipped counterpart:** none found

**Summary:** FVScore is a neuro-symbolic framework for evaluating specification-driven video generation. It converts each video into explicit propositions covering both the prompt's stated requirements and unstated physical, temporal, and cross-modal constraints, then checks them with specialized perception tools.
**Purpose:** The work targets evaluation of video-generation outputs more faithfully than existing holistic or agent-based evaluators, particularly for complex, multi-event videos.
**Breakthrough:** The authors report that FVScore correlates better with human judgments than holistic and agent-based evaluators on public and complex multi-event benchmarks.
**Tools & method:** Soft temporal operators inspired by Linear Temporal Logic evaluate confidence traces produced by the perception tools, and a significance-aware calibration step filters these down to perceptually significant violations, producing a timestamp- and evidence-grounded report.
**Limitation:** No explicit limitation is stated in the fetched abstract.
