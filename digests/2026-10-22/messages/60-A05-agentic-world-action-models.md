**[A05] Agentic World Action Models**
- **arXiv:** 2610.30136 · <https://arxiv.org/abs/2610.30136>
- **Submitted:** 2026-10-21 (v1)
- **Authors:** Zhuoyang Liu et al.
- **Qualifying affiliation(s):** NVIDIA — Jing Wang, Ruijie Zheng, Yuvan Sharma, Runyu Lu, Jiaming Liu, Danfei Xu, Yuke Zhu, Guanzhi Wang, Linxi "Jim" Fan (per paper's own numbered affiliation footnotes: 1=UC Berkeley, 2=NVIDIA, 3=UPenn; Dantong Niu is 1,2)
- **Categories:** cs.RO
- **Open release:** none stated as released; project page only (agentic-wam.github.io)
- **Shipped counterpart:** none found

**Summary:** The paper introduces AW-0, an "agentic world action model" that jointly generates code, future video, and robot actions as three coupled streams in one mixture-of-transformers architecture.
**Purpose:** The authors state that existing world action models give visual foresight for robot manipulation but lack mechanisms for reusing skills compositionally, while agentic/code-based robotics planning lacks grounding in physical dynamics prediction.
**Breakthrough:** The authors report improved task performance over VLA (vision-language-action) and WAM (world action model) baselines on RoboTwin 2.0 and physical bimanual manipulation tasks, with additional reported gains in language following, semantic reasoning, and robustness.
**Tools & method:** The architecture uses three 28-layer transformer "experts" (code, video, action) sharing a 2,048-dimensional joint attention space, trained via masked joint attention; training data comes from an automated curation pipeline that annotates robot/human demonstration video with programs.
