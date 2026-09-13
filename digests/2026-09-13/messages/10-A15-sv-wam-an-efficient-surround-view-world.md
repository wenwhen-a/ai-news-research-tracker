**[A15] SV-WAM: An Efficient Surround-View World-Action Model for End-to-End Autonomous Driving**
- **arXiv:** 2609.03602 · https://arxiv.org/abs/2609.03602
- **Submitted:** 2026-09-03
- **Authors:** Jinyang Wang, Shiwei Li, Junjian Wang, Zhiqiang Deng, Jianbin Gao, Yihang Zhao, Liu Liu, Yongjia Zhao, Jinlong Chen, Huirui Xu, Yifeng Pan, Kangwei Liu, Fan Ren, Ji Tao, Minghao Yang
- **Qualifying affiliation(s):** Chongqing Changan Technology Co., Ltd. — Junjian Wang, Zhiqiang Deng, Jianbin Gao, Yifeng Pan, Kangwei Liu, Fan Ren, Ji Tao; FLAG: borderline (automaker R&D, comparable to Toyota Research / Wayve)
- **Categories:** cs.CV, cs.RO
- **Open release:** none
- **Shipped counterpart:** none found

**Summary:** SV-WAM is a surround-view world-action model for end-to-end driving that keeps six-camera context through an action-centred causal mask, co-trains with future-video prediction, and drops the video branch at inference.
**Purpose:** Low-latency closed-loop planning that retains the full surround context that front-view-only planners lack.
**Breakthrough:** The authors report 91.0 EPDMS on NAVSIMv2 at 342 ms latency, aided by a differentiable drivable-area compliance regulariser.
**Tools & method:** Trained on the NAVSIM trainval split on 16 NVIDIA H800 GPUs (about 24 h per stage); evaluated closed-loop on NAVSIMv2 and zero-shot open-loop on nuScenes; inference on one NVIDIA H20 (341.6 ± 2.1 ms).
**Limitation:** The authors state the roughly 5B-parameter backbone "remains relatively large for deployment on resource-constrained on-board platforms" and plan distillation, pruning, quantisation and real-vehicle closed-loop tests.
