**[A04] GAD: Geometry Attention Distillation for Consistent Video Generation**
- **arXiv:** 2610.18779 · <https://arxiv.org/abs/2610.18779>
- **Submitted:** 2026-10-13
- **Authors:** Junfeng Ni, Ziyu Zhu, Fan Jiang, Yu Liu, Chiyu Wang, Jiawei Zhang, Zhaoxu Sun, Mu Xu, Siyuan Huang, Yixin Chen
- **Qualifying affiliation(s):** Alibaba (AMAP, Alibaba Group) — Ziyu Zhu, Fan Jiang, Chiyu Wang, Jiawei Zhang, Zhaoxu Sun, Mu Xu (Junfeng Ni also dual-affiliated, work partly done at AMAP)
- **Categories:** cs.CV
- **Open release:** none (project page only, no code/weights found) — <https://fantasy-amap.github.io/GAD/>
- **Shipped counterpart:** none found

**Summary:** GAD addresses the tendency of video diffusion models to lose stable scene geometry and object structure over time because their video attention fails to find reliable cross-frame correspondences.
**Purpose:** The goal is to improve long-range and dynamic temporal consistency in video generation without adding extra inference-time modules or changing model architecture.
**Breakthrough:** The authors report that on Wan2.2 5B, GAD raises cross-frame matching accuracy by at least 30% over baseline on two long-range benchmarks (RealEstate10K and DL3DV-10K, 15-second generation) and also improves 5-second dynamic generation on OmniWorld-Game, across three video backbones.
**Tools & method:** Training used a 35K-clip corpus with reference correspondences drawn from 50 DL3DV scenes (static) and 30 dynamic scenes from TAPVid-DAVIS, run for 10 epochs on 32 NVIDIA A800 GPUs (inference cost measured on a single A800).
**Limitation:** The authors note GAD's training targets come from VGGT-Ω attention, so distillation quality depends on that teacher's own matching ability, especially under occlusion or ambiguous appearance.
