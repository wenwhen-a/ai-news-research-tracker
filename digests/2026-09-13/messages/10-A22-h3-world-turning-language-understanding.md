**[A22] H3-World: Turning Language Understanding into World Control**
- **arXiv:** 2609.01560 · https://arxiv.org/abs/2609.01560
- **Submitted:** 2026-09-01
- **Authors:** Danze Chen, Zeqing Wang, Ziyue Lin, Xingyi Yang, Yeying Jin
- **Qualifying affiliation(s):** Tencent — Danze Chen, Zeqing Wang, Yeying Jin (also National University of Singapore)
- **Categories:** cs.CV, cs.AI
- **Open release:** weights and code (https://github.com/Danzer1xxxxChan/H3-World; https://huggingface.co/DANNY621/H3-World)
- **Shipped counterpart:** none found

**Summary:** H3-World turns the MiniMax-H3 video generator into an interactive world model by using natural language as the control interface for character and camera actions, aligning instructions to video latent intervals with temporal attention routing.
**Purpose:** To show that a large pretrained video generator can become a controllable interactive world model without a dedicated action module.
**Breakthrough:** The authors report effective character and camera control with only 0.199% trainable parameters (rank-32 LoRA, 10,000 steps).
**Tools & method:** 7,872 gameplay clips from ABot-World-Explorer-500h (128 held out), 124 frames per clip at 24 fps and 832x480; LoRA fine-tuning at learning rate 1e-4.
**Limitation:** The authors state the work is limited to short-horizon generation, lacks systematic evaluation across action combinations, and does not yet support persistent world state, real-time interaction, planning or policy learning.
