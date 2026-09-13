**[A33] R2M-Bench: Evaluating Revisit Memory via Relative Consistency in Interactive Video World Models**
- **arXiv:** 2608.27328 · https://arxiv.org/abs/2608.27328
- **Submitted:** 2026-08-27
- **Authors:** Qiwen Gu, Bingjie Gao, Rui Chen, Geng Li, Jifan Li, Qishuai Wen, Li Niu, Jing Tang, Xiangxiang Chu, Junqiao Zhao
- **Qualifying affiliation(s):** Alibaba Group (DreamX Team) — Rui Chen, Geng Li, Jifan Li, Qishuai Wen, Jing Tang, Xiangxiang Chu
- **Categories:** cs.CV
- **Open release:** code (https://github.com/AMAP-ML/R2MBench)
- **Shipped counterpart:** none found

**Summary:** R2M-Bench tests whether video world models genuinely remember previously seen scenes rather than merely changing little, by comparing a revisit pair against two same-rollout controls (a gap-matched non-revisit pair and a short-range pair).
**Purpose:** The authors note that "high similarity between first-visit and return frames does not necessarily show that a video world model remembered the scene."
**Breakthrough:** The authors report their Normalised Memory Ratio correlates with human judgments at Spearman 0.547 and is far less correlated with generated motion (0.072) than raw revisit similarity (0.207); across seven models, DreamX-World-Memo scores highest (0.706), ahead of HY-WorldPlay (0.485), Matrix-Game 3.0 (0.403) and Lyra-2 (0.310).
**Tools & method:** 100 reference scenes and three leave-and-return trajectory templates form 300 instances, scoring appearance fidelity, identity, local geometry and persistent state.
**Limitation:** The authors state the benchmark "evaluates observable revisit-selective consistency rather than identifying an internal memory mechanism," that automatic metrics "inherit backbone, viewpoint, and prompt biases," and that object interaction and deliberately evolving state are out of scope.
