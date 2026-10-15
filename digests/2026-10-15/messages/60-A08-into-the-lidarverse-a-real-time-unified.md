**[A08] Into the LidarVerse: A Real-Time Unified LiDAR World Model Across Tasks and Sensors**
- **arXiv:** 2610.19201 · <https://arxiv.org/abs/2610.19201>
- **Submitted:** 2026-10-13
- **Authors:** Henry Che et al.
- **Qualifying affiliation(s):** NVIDIA — Henry Che, Laura Leal-Taixé, Shengyu Huang
- **Categories:** cs.CV, cs.RO
- **Open release:** project page at <https://research.nvidia.com/labs/sil/projects/lidarverse>; no separate code repository for LidarVerse itself was found (it uses NVIDIA's existing Cosmos-Drive-Dreams toolkit only as a preprocessing dependency)
- **Shipped counterpart:** none found

**Summary:** LidarVerse is a single conditional generative world model for simulating LiDAR sensor data, intended to combine the accuracy of per-scene reconstruction methods with the scalability of generative approaches.
**Purpose:** The authors aim for a unified, real-time LiDAR world model that generalizes across driving-simulation tasks and sensor configurations, rather than requiring per-scene fitting (as reconstruction methods do) or sacrificing long-sequence consistency (as prior generative methods do).
**Breakthrough:** The authors report state-of-the-art results on most metrics across three evaluation protocols, that the model can be distilled into a faster autoregressive student running at about 11 FPS on a single H100 GPU, and that the tokenizer generalizes to an unseen scan pattern it was not trained on.
**Tools & method:** The model conditions on past LiDAR frames, HD maps, and a spatial memory to generate future LiDAR observations; it is distilled into an autoregressive student model for real-time inference; NVIDIA's Cosmos-Drive-Dreams toolkit is used for LiDAR-to-range-map preprocessing.
