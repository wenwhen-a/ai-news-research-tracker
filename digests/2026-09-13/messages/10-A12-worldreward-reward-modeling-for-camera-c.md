**[A12] WorldReward: Reward Modeling for Camera-Conditioned World Models**
- **arXiv:** 2609.03952 · https://arxiv.org/abs/2609.03952
- **Submitted:** 2026-09-03
- **Authors:** Yibin Wang, Zehan Wang, Junshu Tang, Zhimin Li, Yujie Zhou, Jiazi Bu, Pengyang Ling, Feng Han, Zhixiong Zhang, Long Xing, Shengyuan Ding, Ziang Li, Cheng Jin, Yuhang Zang, Jiaqi Wang, Tianyu Pang
- **Qualifying affiliation(s):** Tencent Hunyuan — Zehan Wang, Junshu Tang, Zhimin Li, Tianyu Pang
- **Categories:** cs.CV
- **Open release:** none stated (project page https://codegoat24.github.io/WorldReward)
- **Shipped counterpart:** none found

**Summary:** WorldReward is a VLM-based pairwise reward model for camera-conditioned world models that splits videos into action-aligned chunks, scores each with structured visual evidence, and aggregates separate action-consistency and visual-quality scores.
**Purpose:** To supply a reward signal for reinforcement-learning post-training of camera-conditioned video world models that covers action fidelity and visual quality in one evaluator.
**Breakthrough:** The authors describe it as the "first VLM-based pairwise reward model that unifies action-consistency and visual-quality evaluation," report that it improves RL post-training of Tencent's HY-WorldPlay 1.5, and release WorldReward-Bench with 760 human-annotated video pairs.
**Tools & method:** Trained on 50,000 reasoning-augmented video pairs from eight world models across 224 trajectories, built through frontier-VLM distillation, agent-assisted auditing and human calibration.
**Limitation:** The paper discusses trade-offs between action and visual rewards but states no formal limitations in the retrieved content (observed, not stated).
