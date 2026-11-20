**[A02] ViDecide: Teaching Video Diffusion Models to Reason and Plan Step by Step**
- **arXiv:** 2611.26389 · <https://arxiv.org/abs/2611.26389>
- **Submitted:** 2026-11-19
- **Authors:** Kaiwen Zhang, Yiming Gao, Zeqi Xiao, Xintao Wang, Pengfei Wan, Kun Gai, Xingang Pan
- **Qualifying affiliation(s):** Kuaishou — Yiming Gao, Pengfei Wan, Kun Gai (listed under "KlingAI Research")
- **Categories:** cs.CV
- **Open release:** project page (<https://kevin-thu.github.io/ViDecide>)
- **Shipped counterpart:** none found

**Summary:** The paper proposes ViDecide, which trains video diffusion models to predict state transitions causally, one segment at a time, and to decide when to stop via a learned end-of-sequence frame, rather than treating a solution as one fixed-length clip.
**Purpose:** The authors argue leading video generators break physical/logical rules in multi-step reasoning and planning even after reasoning-data training or diffusion RL, because standard training generates clips jointly rather than as a sequence of decisions, and video-level rewards give poor credit assignment.
**Breakthrough:** The authors report an average strict success rate of 83.8%, versus 23.3% for standard fine-tuning and 67.8% for the strongest prior method, with causal generation alone contributing +48.2 points and a decision-focused noise schedule adding +37.0 points.
**Tools & method:** The method combines causal diffusion with adaptive termination (a learned EOS frame), a decision-focused noise schedule that shifts training mass toward high-noise timesteps, and CFT, which branches from rollout failure points and trains the failed noise toward successful continuations mixed with expert data.
**Limitation:** The authors state the model is trained on one benchmark at a time and relies on rule-based verifiers for post-training, and they plan to extend it to broader reasoning data, learned verifiers, and real-world robot planning.
