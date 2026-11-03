**[A05] Xiaomi Auto World Model 2.0: Causal World Models for Real-World Driving and Embodied Intelligence**
- **arXiv:** 2611.01677 · <https://arxiv.org/abs/2611.01677>
- **Submitted:** 2026-11-01
- **Authors:** Zhenxin Zhu et al.
- **Qualifying affiliation(s):** Xiaomi (paper authored and titled by the Xiaomi Auto World Model Team; Xiaomi logo on title page; model feeds "Xiaomi's autonomous driving stack") — FLAG: borderline (Xiaomi)
- **Categories:** cs.AI (primary), cs.LG
- **Open release:** demo (project page with videos) — <https://xiaomiautoworldmodel.github.io/CausalWorldModel/>
- **Shipped counterpart:** none found

**Summary:** The paper presents Xiaomi Auto World Model 2.0, a unified streaming causal world model for "Physical AI" that models physical scene evolution and unifies heterogeneous conditioning inputs within a shared representation space for view-consistent generation.
**Purpose:** The authors aim to build a single world model that can serve as a simulator for both training and evaluation, and as a component of a World Action Model (WAM) for prediction, policy learning, and action generation in driving and embodied-robotics settings.
**Breakthrough:** The authors report that the model supports closed-loop simulation, closed-loop training, and World Action Model applications including world-state prediction, policy learning, and action generation.
**Tools & method:** The architecture integrates View-Temporal Attention and multi-view rotary position encoding to capture cross-view and temporal relationships, with Gated Linear Attention in temporal layers to reduce compute and KV-cache memory during streaming inference.
**Limitation:** Not stated in the portions of the paper retrieved; a dedicated limitations section was not located in the parts of the HTML version read for this entry.
