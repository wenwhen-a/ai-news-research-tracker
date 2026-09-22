**[A02] GameHorizon Suite: Multi-Horizon Data and Evaluation in Gameplay**
- **arXiv:** 2609.25001 · <https://arxiv.org/abs/2609.25001>
- **Submitted:** 2026-09-21
- **Authors:** Yiran Wang, Xingyilang Yin, Junfu Pu, Guangzhi Wang, Kaifeng Li, Mingyu Ouyang, Huiqiang Sun, Lingen Li, Cheng Cheng, Wangbo Yu, Honghao Chen, Xiaodong Cun, Chi-Man Pun, Zhiguo Cao, Ying Shan
- **Qualifying affiliation(s):** Tencent — ARC Lab, Tencent (majority of authors, including Ying Shan); other affiliations include Great Bay University, University of Macau, National University of Singapore, HUST, MMLab CUHK
- **Categories:** cs.CV, cs.AI
- **Open release:** code (GitHub: <https://github.com/TencentARC/GameHorizon)> and project page (<https://gamehorizon-suite.github.io);> authors state they "will release our dataset, annotator, and benchmark"
- **Shipped counterpart:** none found

**Summary:** GameHorizon Suite is an evaluation framework for AI game-playing models spanning multiple task horizons.
**Purpose:** The authors aim to systematically measure how well current models handle gameplay tasks across short, medium, and long time horizons, an area they argue lacks standardized data and evaluation.
**Breakthrough:** The authors report a dataset of "5,000 hours of recordings from 21 games" with 6,184,036 distinct instructions and 411.03 million keyboard-mouse action events from 100 expert players, plus an offline benchmark of 5,000 multiple-choice questions and an online, stepwise gameplay evaluation.
**Tools & method:** The suite includes GameHorizon-Annotator (a three-level instruction pyramid pipeline), GameHorizon-Data (4,571 videos at 60fps across 21 AAA titles), and GameHorizon-Bench (offline MCQs plus online resettable gameplay testing).
**Limitation:** The authors acknowledge the online evaluation track is limited to Minecraft because most AAA titles don't expose underlying game state.
