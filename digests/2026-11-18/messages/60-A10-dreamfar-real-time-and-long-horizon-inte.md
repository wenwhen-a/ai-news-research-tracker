**[A10] DreamFAR: Real-Time and Long-Horizon Interaction with Diverse Objects**
- **arXiv:** 2611.22001 · <https://arxiv.org/abs/2611.22001>
- **Submitted:** 2026-11-16
- **Authors:** Yiming Dou et al.
- **Qualifying affiliation(s):** Amazon — the paper's affiliation block lists "Amazon FAR" (Amazon's Frontier AI & Robotics team, confirmed as a real Amazon research group via amazon.jobs listings) alongside Cornell University, University of Maryland College Park, and University of Pennsylvania; per-author mapping was not separable in the HTML.
- **Categories:** cs.RO
- **Open release:** project page — <https://www.yimingdou.com/DreamFAR/> (no code/weights released yet per abstract/comments)
- **Shipped counterpart:** none found

**Summary:** Existing robot-manipulation world models either overfit to a single environment or fail to simulate long-horizon, contact-rich interactions.
**Purpose:** To build a world model for robot manipulation that generalizes across diverse objects and long, contact-rich interactions in real time, usable for policy evaluation and for mixed real/generated data co-training.
**Breakthrough:** The authors report that DreamFAR outperforms existing world models at predicting long-horizon futures despite its smaller size, and demonstrate its use both for evaluating policies and for co-training with mixed real and generated data.
**Tools & method:** A dynamics model trained from scratch (no internet-video pretraining) on a large robot-native teleoperation dataset, with an architecture and training recipe tailored to robot-native data; runs at 10 FPS on a commercial GPU.
**Limitation:** The abstract and comments state no explicit limitations; the training dataset is described only as "a large robot-native teleoperation dataset" without being named, and training hardware is not specified (only inference hardware, "a commercial GPU").
