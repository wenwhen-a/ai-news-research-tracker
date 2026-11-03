**[A09] GSExplorer: Interactive World Generation with a Persistent 3D Gaussian World State**
- **arXiv:** 2611.01543 · <https://arxiv.org/abs/2611.01543>
- **Submitted:** 2026-11-01
- **Authors:** Sicheng Yu, Liu Liu, Xinjie Wang, Xinjiang Wang, Taojun Ding, Wenhao Hu, Beizhen Zhao, Puxin Yan, Zhizhong Su, Hao Wang
- **Qualifying affiliation(s):** Horizon Robotics — Puxin Yan (also The University of Hong Kong; listed as Project Leader) — FLAG: borderline (Horizon Robotics)
- **Categories:** cs.CV (primary), cs.AI
- **Open release:** none found
- **Shipped counterpart:** none found

**Summary:** GSExplorer is a framework for interactive world generation that pairs a video generator with a persistent 3D Gaussian Splatting scene representation.
**Purpose:** The authors aim to enable interactive, explorable 3D world generation that maintains a persistent, revisitable scene state, rather than regenerating inconsistent content each time the camera returns to a previously seen location.
**Breakthrough:** The authors report the best WorldScore results among compared methods, including a Camera Control score of 99.07 in single-step extrapolation, and strong revisit consistency over 481-frame leave-and-return rollouts.
**Tools & method:** The method combines a video generation model with SLAM-based 3D Gaussian Splatting reconstruction, filtering inconsistent generated content and applying cross-chunk bundle adjustment to maintain a persistent 3D Gaussian world state.
**Limitation:** The authors state the method adds additional runtime compared with purely feed-forward video generation.
