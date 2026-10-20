**[A07] Mise-en-Video: Fine-Grained 3D Control for Multi-Shot Video Generation**
- **arXiv:** 2610.26801 · <https://arxiv.org/abs/2610.26801>
- **Submitted:** 2026-10-19
- **Authors:** Yingshuang Zou, Xiaoyu Shi, Yawen Luo, Ziang Li, Qinghe Wang, Mengfei Li, Chengfeng Zhao, Xintao Wang, Pengfei Wan, Kun Gai, Yuan Liu
- **Qualifying affiliation(s):** Kuaishou — KlingAI Research (Xintao Wang, Pengfei Wan, Kun Gai)
- **Categories:** cs.CV, cs.AI
- **Open release:** none (a 160K-video dataset is described but no release link was found on the abstract page)
- **Shipped counterpart:** none found

**Summary:** Mise-en-Video (MeV) is a framework for multi-shot video generation in which creators stage each shot in 3D before generation, combining hierarchical attention for cross-shot narrative consistency with 3D-aware layout guidance for per-shot spatial control.
**Purpose:** To give creators fine-grained control over subject placement, orientation, and motion within and across shots of a multi-shot video while preserving consistency across shots.
**Breakthrough:** The authors report better video quality, inter-shot consistency, and subject-level control than baselines including MultiShotMaster and EchoShot, evaluated on 100 multi-shot prompts generated with Gemini 2.5.
**Tools & method:** Subject Layout Guidance encodes subjects as oriented 3D boxes with a NOCS-based color scheme, projects them into per-frame 2D layout maps, and injects them via a ControlNet-style branch; Hierarchical Context Attention splits text into global/shot/subject levels with masked attention.
**Limitation:** The authors state that overall generation quality is capped by the pretrained backbone's relatively small parameter count, limiting performance on high-quality dynamic videos, and they plan to use larger backbones and/or larger controllable modules.
