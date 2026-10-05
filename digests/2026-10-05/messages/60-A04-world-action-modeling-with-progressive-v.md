**[A04] World Action Modeling with Progressive Visual Planning**
- **arXiv:** 2610.02508 · <https://arxiv.org/abs/2610.02508>
- **Submitted:** 2026-10-01
- **Authors:** Fei Zhang, Zhaochong An, Duncan Frost, Yikai Wang, Pengfei Liu, Ya Zhang, Michal Drozdzal, Amir Bar
- **Qualifying affiliation(s):** Meta — Zhaochong An, Duncan Frost, Yikai Wang, Michal Drozdzal
- **Categories:** cs.AI (primary), cs.CV, cs.RO
- **Open release:** demo/project page at <https://sii-ferenas.github.io/ProWAM-page> (license noted as CC BY-NC-ND 4.0; no separate code/weights link confirmed)
- **Shipped counterpart:** none found

**Summary:** The paper introduces ProWAM, a world action model that jointly predicts future actions and an ordered sequence of sparse visual sub-goals from an initial observation and instruction, instead of generating dense full video rollouts.
**Purpose:** Prior "world action models" face a trade-off: generating dense, pixel-level video rollouts gives strong short-horizon visual guidance for action planning but is computationally expensive, while cheaper alternatives lack the intermediate visual guidance needed to anchor long-horizon action generation.
**Breakthrough:** The authors report a progressive/sparse visual sub-goal representation — using a normalized progress value where r=0 is the current observation and r=1 is the trajectory endpoint — that provides explicit, ordered visual anchors for action generation without needing dense frame-by-frame rollouts.
**Tools & method:** ProWAM combines a video-generation-style module that predicts sparse, progress-ordered visual sub-goals with a lightweight action-generation head conditioned on those sub-goals.
**Limitation:** The fetched abstract/introduction does not report failure modes or ablations in detail; the real-world evaluation is described as zero-shot with a 70.0% success rate, implying roughly 3 in 10 real-world trials still fail.
