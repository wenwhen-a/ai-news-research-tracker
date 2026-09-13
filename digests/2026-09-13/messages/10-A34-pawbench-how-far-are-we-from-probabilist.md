**[A34] PAWBench: How Far Are We from Probabilistically Aligned World Modeling?**
- **arXiv:** 2608.27345 · https://arxiv.org/abs/2608.27345
- **Submitted:** 2026-08-27
- **Authors:** Yuandong Pu, Le Zhuo, Sayak Paul, Gabriel Jorge Menezes, Avram Đorđević, Shiyang Li, Yifan Zhou, Bin Fu, Wenlong Zhang, Junjun He, Yu Qiao, Yihao Liu, Jinbo Xing, Xi Chen
- **Qualifying affiliation(s):** Alibaba (Tongyi Lab) — Yihao Liu
- **Categories:** cs.CV, cs.AI
- **Open release:** none stated (project page https://pawbench.github.io)
- **Shipped counterpart:** none found

**Summary:** PAWBench tests whether video generators behave as probabilistically aligned world models: whether repeated rollouts from identical initial conditions and actions recover the correct distribution over futures rather than one plausible video.
**Purpose:** To formalise and measure probabilistic alignment as a distributional criterion for world models.
**Breakthrough:** The authors report benchmarking 11 video generation systems, including Veo 3.1 Fast, Kling 3 and Seedance 2, and find that none consistently matches reference probabilities while also covering valid futures.
**Tools & method:** 50 scenarios in two tracks, PAW-Calibration (analytically specified distributions) and PAW-Coverage (recovery of valid outcomes), with a PAWEval protocol built on Gemini 3.5 Flash to map videos to terminal outcomes.
**Limitation:** The authors state the benchmark scores only terminal outcomes rather than full trajectories, that finite rollout budgets limit distribution estimates, and that it covers controlled, visually parseable scenarios rather than interactive settings.
