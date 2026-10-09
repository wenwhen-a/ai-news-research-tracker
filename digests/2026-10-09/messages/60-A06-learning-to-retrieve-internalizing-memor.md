**[A06] Learning to Retrieve: Internalizing Memory Retrieval for Video World Models (L2R)**
- **arXiv:** 2610.11444 · <https://arxiv.org/abs/2610.11444>
- **Submitted:** 2026-10-08 (v1)
- **Authors:** JiaKui Hu, Tailai Chen, Yuqi Pan, Xuerui Qiu, Jialun Liu, Xiao Cao, Zhenxin Zhu, Guang Chen, Hangjun Ye, Bing Wang, Yanye Lu
- **Qualifying affiliation(s):** Xiaomi EV — JiaKui Hu, Zhenxin Zhu, Guang Chen, Hangjun Ye, Bing Wang (flag: Xiaomi EV is Xiaomi's electric-vehicle division; Xiaomi is not on the default list but is a comparable large-scale tech company — kept and flagged). Other authors: Peking University, CASIA, University of Queensland, NUS (academic).
- **Categories:** cs.CV
- **Open release:** none stated in the abstract
- **Shipped counterpart:** none found

**Summary:** Video world models generate explorable, 3D-consistent scene video from camera trajectories, and existing systems use external memory to retrieve earlier content and limit scene drift. The authors note these memory pathways sit outside the model's generative process, so the model cannot learn when or what to retrieve.
**Purpose:** To make memory retrieval learnable and internal to the model rather than an external, hand-engineered system.
**Breakthrough (≤3 sentences, attributed):** The authors report that L2R improves long-term scene consistency across several base models and camera-revisit benchmarks, without needing an external memory bank or 3D conditioning.
**Tools & method:** L2R treats the model's own persistent internal state as memory; a camera-conditioned retrieval gate selects relevant history, and a retrieval trigger — supervised with a 3D re-visibility signal — decides when to use it, activating only when previously seen content re-enters view.
**Limitation:** Not stated in the available abstract text.
