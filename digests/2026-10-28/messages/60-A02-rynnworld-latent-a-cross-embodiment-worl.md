**[A02] RynnWorld-Latent: A Cross-Embodiment World Model Conditioned on Universal Latent Actions**
- **arXiv:** 2610.36791 · <https://arxiv.org/abs/2610.36791>
- **Submitted:** 2026-10-27
- **Authors:** Haoyu Zhao et al.
- **Qualifying affiliation(s):** Alibaba — DAMO Academy, Alibaba Group / Hupan Lab: Minghao Zhu, Dongchi Huang, Xingyue Zhao, Kehan Li, Xin Li, Zhenyu Zeng, Mingxiu Chen, Deli Zhao
- **Categories:** cs.RO
- **Open release:** code — homepage at <https://alibaba-damo-academy.github.io/RynnWorld-Latent.github.io> and GitHub repo at <https://github.com/alibaba-damo-academy/RynnWorld-Latent>
- **Shipped counterpart:** none found

**Summary:** RynnWorld-Latent is a video world model that uses latent actions from RynnLAM as a shared conditioning interface, letting it train on human videos, robot demonstrations, and simulation rollouts without needing a common action space.
**Purpose:** The authors address the problem that cross-embodiment world models normally need a shared action representation to learn from heterogeneous data sources (human video, robot demos, simulation), which is hard to define across different embodiments.
**Breakthrough:** The authors report better video prediction quality, higher downstream policy success on LIBERO and LIBERO-Plus when using synthetic mid-training, and gains on two real-robot platforms.
**Tools & method:** The method conditions a pretrained video transformer on latent actions extracted by RynnLAM, pretrains on 23 datasets (~553.5M frames) spanning human video, robot demonstrations, and simulation, and then adapts to target robot platforms.
**Limitation:** This is a world model whose downstream evaluation is entirely on robot-manipulation benchmarks (LIBERO, LIBERO-Plus, two real-robot platforms), not on game or general video-generation tasks (observed, not stated).
