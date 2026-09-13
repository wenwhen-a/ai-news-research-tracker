**[A20] SolarWM: Open Data and Scalable Training for Long-Horizon Video World Models**
- **arXiv:** 2609.02886 · https://arxiv.org/abs/2609.02886
- **Submitted:** 2026-09-02
- **Authors:** Junchao Huang, Guian Fang, Shengju Qian, Xianghao Kong, Zhuoran Zhao, Wei Huang, Yihua Du, Zixin Zhang, Justin Cui, Yuchao Gu, Yukang Chen, Xinting Hu, Tianyu He, Shaoshuai Shi, Zhuotao Tian, Xin Wang, Mike Zheng Shou, Li Jiang
- **Qualifying affiliation(s):** NVIDIA — Wei Huang, Yuchao Gu, Yukang Chen; Microsoft Research Asia — Tianyu He
- **Categories:** cs.CV
- **Open release:** weights, code and data (https://github.com/Junchao-cs/SolarWM; https://huggingface.co/datasets/junchaoh-cs/SolarWM-Data)
- **Shipped counterpart:** none found

**Summary:** SolarWM is an open foundation for interactive video world models: a reconfigurable data engine (1.43M clips from 10 datasets, about 25.85 TB) plus a backbone-native adaptation framework instantiated as four 5B to 33B models built on Wan2.2, LTX-2.5 and MiniMax-H3.
**Purpose:** A reproducible open foundation (data, recipe, weights) for long-horizon interactive world models, addressing inconsistent supervision from naive multi-source mixing.
**Breakthrough:** The authors report causal models that sustain real-time interaction over rollouts from minutes to hours despite training on 5-second sequences, via bidirectional adaptation, teacher-forced autoregressive initialisation and distribution-matching distillation.
**Tools & method:** A frame-aligned data contract covering observations, metric camera geometry, captions and quality metadata; sources include ABOT-World, DL3DV, MiraData, RealCam-Vid, SpatialVID, Sekai-Game, Sekai-Walking, MIND, MultiCamVideo and OmniWorld.
**Limitation:** No explicit limitations section was found in the retrieved content (observed, not stated).
