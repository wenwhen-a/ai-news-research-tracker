**[A10] WEVO: World Model-Enabled VLA Optimization for Whole-Body Loco-Manipulation**
- **arXiv:** 2611.25251 · <https://arxiv.org/abs/2611.25251>
- **Submitted:** 2026-11-18
- **Authors:** Qianzhong Chen, Muyuan Lin, Yuyin Sun, Mac Schwager, Cheng-Hao Kuo, Roberto Martín-Martín
- **Qualifying affiliation(s):** Amazon — listed in the paper's affiliation block; a footnote states "Work done during an internship at Amazon."; FLAG: borderline topic (robotics-focused)
- **Categories:** cs.RO
- **Open release:** none found
- **Shipped counterpart:** none found

**Summary:** WEVO post-trains a whole-body humanoid vision-language-action (VLA) policy inside an action-conditioned video world model, avoiding unsafe exploration directly on the humanoid robot.
**Purpose:** The authors note that reinforcement learning can push VLA policies beyond imitation learning, but exploring directly on a humanoid is unsafe, and RL trained purely in simulation can exploit sim-to-real gaps.
**Breakthrough:** As the authors report, across three real-robot tasks, RL inside the video world model raised mean success from 23.3% (initial) to 75.0%, compared with 48.3% for RL performed directly on the real robot.
**Tools & method:** The pipeline combines simulation-based play data (for broad coverage and policy initialization), a video world model refined by real-robot rollouts (for deployment alignment), and closed-loop RL with dense progress rewards over the VLA, whole-body controller, and world model jointly.
**Limitation:** The accessible text does not state an explicit limitations section beyond the paper's own framing of the problem (unsafe real-world exploration, sim-to-real gap); this is a robotics loco-manipulation paper without a game/3D-content angle.
