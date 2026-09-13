**[A18] Building Pretraining Data for World Models: An Unreal Engine-Based Pipeline for Action-Conditioned Video Generation**
- **arXiv:** 2609.03557 · https://arxiv.org/abs/2609.03557
- **Submitted:** 2026-09-03
- **Authors:** Haoyu Wang, Songchun Zhang, Haoran Li, Haoyang Huang, Zeyue Xue, Nan Duan
- **Qualifying affiliation(s):** JD (Joy Future Academy) — Haoyu Wang, Songchun Zhang, Haoyang Huang, Nan Duan; FLAG: borderline (JD.com)
- **Categories:** cs.CV, cs.GR
- **Open release:** none stated (project page https://echo-team-joy-future-academy-jd.github.io/Echo-1.5-Page/wm/)
- **Shipped counterpart:** none found

**Summary:** A production pipeline on Unreal Engine that generates synthetic, action-conditioned, multi-view video for training interactive world models, combining physics simulation of character trajectories with offline cinematic rendering.
**Purpose:** Large-scale, precisely action-aligned pretraining data for action-conditioned video models, given the scarcity of controllable real-world video.
**Breakthrough:** The authors report about 2,691 hours of 1080p and 6,076 hours of 720p five-camera video from 429 curated Unreal Engine levels and 40 characters on a 200-GPU farm (25 nodes of 8 NVIDIA RTX 5090), with non-forward actions making up 46.6% of trajectories.
**Tools & method:** Stage I physics simulation for trajectories; Stage II offline rendering through Unreal Engine's Movie Render Queue; asset curation and cache-aware scheduling across 2,384 Fab asset packs.
**Limitation:** The authors state the system prioritises controllability and scale over cinematic quality, that actions are limited to locomotion (no jumping, climbing or complex interaction), and that it is infrastructure rather than a new world-model architecture.
