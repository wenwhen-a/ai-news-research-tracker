**[A03] OverSeer: Multi-Agent World Models Beyond What Agents See**
- **arXiv:** 2610.28554 · <https://arxiv.org/abs/2610.28554>
- **Submitted:** 2026-10-20 (v1)
- **Authors:** Runjia Li, Kam Woh Ng, Minghao Chen, Junlin Han, Jianyuan Wang, Zhaochong An, Juan-Manuel Perez-Rua, Andrea Vedaldi, Shikun Liu
- **Qualifying affiliation(s):** Meta (Meta AI) — Li, Ng, Han, Wang, An, Perez-Rua, Vedaldi, and Liu are listed with a Meta AI affiliation (Li, Han, Wang, and Vedaldi also list University of Oxford); Chen is listed with University of Oxford only
- **Categories:** cs.CV
- **Open release:** none stated
- **Shipped counterpart:** none found

**Summary:** Video world models are hard to extend to multiple agents because each agent needs its own video stream, and those streams must stay consistent over time and with each other.
**Purpose:** The aim is to improve temporal and cross-agent consistency in multi-agent world models without requiring each agent's egocentric view alone to carry the full world state.
**Breakthrough:** The authors report that because the auxiliary views are fixed in space, changes in them map directly to localized changes in world state, and that experiments in Minecraft and Doom show improved world and agent consistency versus their baseline; qualitative results on real-world multi-camera captures are presented as evidence the approach is not tied to game engines.
**Tools & method:** The redundant, largely static auxiliary views are compressed with a delta-VAE that encodes only changes relative to a static reference image, reducing the token count needed to process them; per the appendix, the model was trained with a batch size of 64 across 64 NVIDIA GB300 GPUs.
**Limitation:** The authors' "Limitations and Future Work" appendix states that OverSeer's benefits depend on auxiliary coverage, and that fast-changing scenes such as Doom can lose consistency under aggressive residual compression.
