**[A04] Flow Matching Reinforcement for 3D Mesh Generation via Dynamic Homing Optimization**
- **arXiv:** 2610.01233 · <https://arxiv.org/abs/2610.01233>
- **Submitted:** 2026-10-01
- **Authors:** Zhen Zhou et al.
- **Qualifying affiliation(s):** Tencent Hunyuan — Zhen Zhou, Zhiwei Ning, Puhua Jiang, Sheng Zhang, Yifei Tang, Jie Yang, Xintong Han, Wei Liu, Chunchao Guo (paper header also lists Shanghai Jiao Tong University and Communication University of China as affiliations, without per-author markers)
- **Categories:** cs.CV
- **Open release:** none
- **Shipped counterpart:** none found

**Summary:** The paper introduces Dynamic Homing Optimization (DHO), a forward-process reinforcement-learning method for flow-matching models that reformulates negative-trajectory optimization as attraction toward matched positive samples.
**Purpose:** The authors argue that RL objectives adapted from 2D visual generation (DPO-, GRPO-, and NFT-style) mainly steer predicted velocities away from negative directions without specifying a target velocity toward preferred samples, which they find yields limited geometric-quality gains when applied directly to 3D mesh generation.
**Breakthrough:** The authors report that Minimum-Cost Attractive Matching (an optimal-transport assignment via the Hungarian algorithm) combined with Time-Aware Dynamic Correction, applied through asynchronous online DHO post-training, improves geometric quality over RL objectives applied directly from the 2D setting.
**Tools & method:** Flow3D-Pro was trained in two stages: supervised fine-tuning on 32 H20 GPUs for 5K steps over 5K curated artist-created and AI-generated meshes, followed by DHO training (28 GPUs for rollout, 4 for policy updates) using 1K reference images spanning cartoon and photorealistic styles, evaluated via ULIP/Uni3D scores and an expert user study on GenMesh-Test and LATTICE-Bench.
