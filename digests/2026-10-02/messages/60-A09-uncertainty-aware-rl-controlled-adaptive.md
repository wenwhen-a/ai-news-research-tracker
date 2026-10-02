**[A09] Uncertainty-Aware RL-Controlled Adaptive 3D Mapping**
- **arXiv:** 2610.00188 · <https://arxiv.org/abs/2610.00188>
- **Submitted:** 2026-09-17
- **Authors:** Alpay Ozkan et al.
- **Qualifying affiliation(s):** Microsoft — Daniel Barath (listed as ETH Zurich, Microsoft, ETH AI Center)
- **Categories:** cs.LG; cs.CV; cs.GR; eess.IV
- **Open release:** weights, code (GitHub: <https://github.com/alpayozkan/UnRL>)
- **Shipped counterpart:** none found

**Summary:** The paper (project name "UnRL") proposes an adaptive 3D voxel mapping framework that refines voxel resolution based on semantic entropy, geometric curvature, and texture richness, paired with a reinforcement-learning agent that learns voxel-subdivision policies under a user-specified memory budget.
**Purpose:** The authors note that fixed-resolution TSDF volumetric mapping wastes memory in uniform regions and loses detail in complex ones, and that prior adaptive methods like MAP-ADAPT require hand-tuned, dataset-specific semantic class lists and give no explicit control over memory usage.
**Breakthrough:** The authors report that their multi-resolution TSDF approach matches or surpasses MAP-ADAPT and fixed-resolution baselines in geometric accuracy, semantic consistency, and memory-accuracy trade-offs on both synthetic and real-world datasets, replacing hand-tuned thresholds with a single user-specified memory-budget parameter.
**Tools & method:** The RL subdivision policy is trained with PPO across 4 parallel environments for 10M timesteps on a single workstation (Intel Core i7-14700K, NVIDIA GeForce RTX 3080, 10GB VRAM); evaluation uses the ScanNet and HSSD datasets, with additional experiments using SegFormer.
**Limitation:** The authors state their evaluation is currently limited to the indoor RGB-D setting of ScanNet and HSSD, and that extending the method to outdoor and larger-scale mapping scenarios is left to future work.
