**[A01] When Should a World Model Move? Loss-Conditioned State Execution**
- **arXiv:** 2609.15801 · https://arxiv.org/abs/2609.15801
- **Submitted:** 2026-09-14
- **Authors:** Jintao Xu, Zhengyu Chen, Ben Zhang, Yongzhi Qi, Jianshen Zhang
- **Qualifying affiliation(s):** JD.com (Supply Chain Tech Team Y) — all five authors; **flagged — JD is a borderline/comparable lab, not on the core tracked list**
- **Categories:** cs.AI, cs.LG, math.OC
- **Open release:** none found (no code/weights link stated; uses public benchmarks plus a proprietary JD.com dataset)
- **Shipped counterpart:** none found

**Summary:** The paper introduces "loss-conditioned state execution," a model-agnostic decision rule for whether a world model should actually update ("move") its state or simply persist the current one.
**Purpose:** Standard world-model evaluation focuses on likelihood/calibration, leaving open whether a prediction should replace the current state under a specific declared loss.
**Breakthrough:** The authors report and prove that proposal benefit is always bounded by state movability, and demonstrate empirically that a model with strong occurrence ranking (AUROC 0.819) on JD.com's inventory data still produces worse MAE than simply persisting — showing high predictive discrimination can be actively misleading.
**Tools & method:** The method builds Bayes-corrected state proposals from a predictive distribution, then certifies them via an independent calibration set using Hoeffding concentration bounds (with union-bound correction across pre-declared groups), executing only where a lower confidence bound on loss gain exceeds zero.
**Limitation:** The confidence-based gating substantially reduces update frequency (22.2% → 14% on M4), trading coverage for statistical safety, and results are sensitive to how per-step losses aggregate within episodes and to the pre-declared grouping/bounding choices.
