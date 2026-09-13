**[A59] Hydra-0: Action Flow for Generalist World Modeling and Control**
- **arXiv:** 2608.18077 · https://arxiv.org/abs/2608.18077
- **Submitted:** 2026-08-18
- **Authors:** Hongyu Li, Bowen Wen, Xinghao Zhu, Yixuan Wang, Yilun Du, Yunzhu Li, George Konidaris, Stan Birchfield, Soha Pouya, Chenran Li, Yan Chang
- **Qualifying affiliation(s):** NVIDIA — Hongyu Li, Bowen Wen, Xinghao Zhu, Yixuan Wang, Yilun Du, Stan Birchfield, Soha Pouya, Chenran Li, Yan Chang
- **Categories:** cs.RO
- **Open release:** demo (project page https://nvidia-isaac.github.io/video_to_data/hydra-0/)
- **Shipped counterpart:** none found

**Summary:** Hydra-0 is a generalist world model that represents robot actions as "action flow," pixel motion, as a unified interface across robots, tasks and environments, so action consequences are learned once and reused across embodiments.
**Purpose:** A world model that generalises across robot morphologies and supports zero-shot composition of skills rather than being tied to one action space.
**Breakthrough:** The authors report a Pearson correlation of 0.96 between replayed and reference success rates on their RoboLab benchmark and an "emergent inverse mode" that predicts robot motion from object flow in human demonstrations.
**Tools & method:** A Wan2.2 I2V-A14B backbone trained for five days over 40,000 steps on 32 NVIDIA H100 GPUs.
**Limitation:** No explicit limitations paragraph was found in the fetched text (observed, not stated).
