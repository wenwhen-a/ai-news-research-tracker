**[A63] SCALE: State-Calibrated Latent Embeddings for JEPA Planning in the Right Geometry**
- **arXiv:** 2608.16287 · https://arxiv.org/abs/2608.16287
- **Submitted:** 2026-08-17
- **Authors:** Jiaming Hu, Yan Zheng, Tian Wang, Florian Dubost, Alejandro Mottini, Junze Liu, Arvind Srinivasan, Kai Zhong, Kun Qian, Sharon Gao, Qingjun Cui
- **Qualifying affiliation(s):** Unity Technologies — Yan Zheng, Tian Wang, Florian Dubost, Alejandro Mottini, Junze Liu, Arvind Srinivasan, Kai Zhong, Kun Qian, Sharon Gao, Qingjun Cui (Jiaming Hu as a Unity intern, Boston University)
- **Categories:** cs.LG
- **Open release:** none found
- **Shipped counterpart:** none found

**Summary:** Compares two ways to obtain non-collapsed representations in JEPA world models used for planning, inheriting a pretrained feature space (DINO-WM) versus end-to-end training with anti-collapse regularisation (LeWM), and adds SCALE, a training-time regulariser that aligns latent distances with distances in a task-relevant state space.
**Purpose:** To give LeWM's end-to-end representation the planning geometry observed in DINO-WM without replacing its encoder.
**Breakthrough:** The authors report SCALE improves every one of 15 task-solver combinations (5 tasks, 3 solvers) over baseline LeWM across five compute budgets, and that a control matching SCALE's decodability "yields less consistent planning gains," attributing the benefit to geometry.
**Tools & method:** A single lightweight regulariser correlating sampled pairwise latent distances with standardised state distances; no planning-time overhead.
**Limitation:** The authors state SCALE requires simulator state during training (image-only at test time), that state selection "acts as a task-dependent inductive bias," and that gains range from modest (Push-T, Reacher) to substantial (Two-Room, PointMaze).
