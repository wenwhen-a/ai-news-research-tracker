**[A05] Spatial Memory Intelligence: Endowing World Models with Understanding-Driven Long-Term Memory**
- **arXiv:** 2610.02521 · <https://arxiv.org/abs/2610.02521>
- **Submitted:** 2026-10-01
- **Authors:** Ying Yang, Guiyu Zhang, Lianghua Huang, Chang Nie, Chenyang Si, Haofan Wang, Shaoshuai Shi, Li Jiang
- **Qualifying affiliation(s):** Alibaba Group — Guiyu Zhang, Lianghua Huang, Haofan Wang
- **Categories:** cs.CV
- **Open release:** demo/project page at spatial-memory-intelligence.github.io (no explicit code/weights link confirmed)
- **Shipped counterpart:** none found

**Summary:** The paper introduces Spatial Memory Intelligence (SMI), a framework that uses multimodal large language models' spatial-reasoning ability to manage long-term memory in long-video, action-conditioned world models.
**Purpose:** Video world models that generate long, action-conditioned sequences accumulate ever-growing observation histories, which raises storage/compute cost, makes it hard to retrieve the right past observation when revisiting a location, and lets generation errors compound over time.
**Breakthrough:** The authors report that using an MLLM's own semantic and spatial understanding to drive the memory pipeline — rather than relying on purely geometric or heuristic compression — lets a single unified mechanism jointly handle efficiency, consistency, and reliability.
**Tools & method:** SMI decomposes memory management into spatial clustering of observations, redundancy sparsification within each cluster, action-conditioned retrieval of relevant past memory, and reliability-based filtering of unreliable generated content, all driven by a multimodal LLM's spatial/semantic reasoning.
**Limitation:** The paper frames this as addressing memory management specifically for long-horizon, action-conditioned video generation; it does not claim to fix underlying generation-quality or drift issues in the base world model itself.
