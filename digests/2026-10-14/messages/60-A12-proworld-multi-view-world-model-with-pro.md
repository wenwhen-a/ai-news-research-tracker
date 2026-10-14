**[A12] ProWorld: Multi-View World Model with Proprioceptive Feedback for Closed-Loop Policy Evaluation**
- **arXiv:** 2610.15294 · <https://arxiv.org/abs/2610.15294>
- **Submitted:** 2026-10-11
- **Authors:** Zijun Wang et al.
- **Qualifying affiliation(s):** Meituan — Xiaoyu Guo (footnote: "Work done during an internship at Meituan"); FLAG: borderline (Meituan is not on the explicit qualified list; other co-authors are Sun Yat-sen University / University of Macau / MBZUAI / South China University of Technology)
- **Categories:** cs.RO
- **Open release:** demo/project page — <https://zijunwa.github.io/proworld/> (no code repo link found on the abs page)
- **Shipped counterpart:** none found

**Summary:** ProWorld is an action-conditioned world model that jointly predicts multi-view video and robot proprioceptive state, feeding both back to a frozen policy to serve as a closed-loop test environment for robot manipulation policies.
**Purpose:** Repeated physical trials to evaluate robot policies are costly, so the authors ask whether a generative world model can substitute for real robots while still tracking real success/failure rates.
**Breakthrough:** The authors report ProWorld achieves "the highest overall TriWorldBench score among the compared methods," and across three policies and four local manipulation tasks attains a Pearson correlation of 0.95 and Spearman correlation of 0.94 between generated-environment and real-robot success rates (their claim).
**Tools & method:** A shared transformer jointly generates multi-view video and robot state; Shared-Time View Encoding preserves temporal synchronization across camera views; training data is augmented with failure trajectories gathered in high-fidelity simulation to reduce "interaction hallucinations."
