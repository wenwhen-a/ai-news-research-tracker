**[A12] Map2Vid: Embodied Navigation Video Generation with Human-Friendly Motion Control**
- **arXiv:** 2610.25223 · <https://arxiv.org/abs/2610.25223>
- **Submitted:** 2026-10-18
- **Authors:** Yulin Dai, Yuqian Fu, Tianwen Qian, Zhen Xing, Bojia Zi, Xiaoling Wang
- **Qualifying affiliation(s):** Alibaba Group — Zhen Xing (Qwen Team, Alibaba Group, Hangzhou)
- **Categories:** cs.CV
- **Open release:** none (paper mentions only an examples directory in supplementary material; no stated code/weights release)
- **Shipped counterpart:** none found

**Summary:** Map2Vid frames embodied-navigation video generation as turning a bird's-eye-view (BEV) map of a scene and intended route into an egocentric video, as an alternative to vague text prompts or low-level camera-trajectory controls.
**Purpose:** The authors argue existing navigation-video controls are poorly suited to embodied navigation: text prompts are spatially vague, and camera-trajectory control relies on low-level motion parameters that are not human-friendly.
**Breakthrough:** The authors report that BEV-map control is a viable direction for navigation video generation across several tested foundation generation models, with curriculum training letting the model run on map-only input at inference.
**Tools & method:** Benchmark built by replaying R2R trajectories in the Habitat simulator over Matterport3D scenes; evaluated with large DiT-based video generation backbones.
**Limitation:** The authors state their conclusions are "limited to a simulation-based benchmark rather than real-world deployment," and that the dataset covers only static indoor layouts without dynamic obstacles or human-agent interaction.
