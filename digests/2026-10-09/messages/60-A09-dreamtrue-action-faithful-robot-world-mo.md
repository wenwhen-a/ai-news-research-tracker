**[A09] DreamTrue: Action-Faithful Robot World Model with Counterfactual Post-Training**
- **arXiv:** 2610.12468 · <https://arxiv.org/abs/2610.12468>
- **Submitted:** 2026-10-08 (v1)
- **Authors:** Junyan Li, Ruizhi Li, Yu Liu, Xiangshuo Liu, Mingchao Sun, Hongyu Pan, Mu Xu, Lue Fan, Zhaoxiang Zhang
- **Qualifying affiliation(s):** Alibaba Group / Amap — Yu Liu, Mingchao Sun, Hongyu Pan, Mu Xu (per HTML author block). Other authors are at NLPR, Institute of Automation, Chinese Academy of Sciences (CASIA).
- **Categories:** cs.RO (primary), cs.CV
- **Open release:** project page only, no code/weights stated — <https://brave-eai.github.io/DreamTrue>
- **Shipped counterpart:** none found

**Summary:** DreamTrue is a multi-view, cross-embodiment robot world model trained to predict videos that follow given actions and stay physically plausible.
**Purpose:** The authors aim to improve action-faithfulness and physical plausibility of robot world-model video prediction across different robot embodiments and camera views.
**Breakthrough:** The authors report state-of-the-art action following on the AgiBot benchmark and say their counterfactual post-training cuts the human-assessed interaction defect rate from 48.12% to 6.25%.
**Tools & method:** Action trajectories are rendered as image-space conditions with offline geometric calibration to align them with target videos; counterfactual post-training perturbs recorded trajectories to cover a wider range of actions and contact configurations.
**Limitation:** The abstract does not state explicit limitations; evaluation is reported on the AgiBot dataset/challenge only, so generalization beyond that benchmark is not characterized in the abstract (observed, not stated).
