**[A02] TaoFlowForge: Progressive Native Mesh Generation via Cascaded Flow Matching**
- **arXiv:** 2609.37139 · <https://arxiv.org/abs/2609.37139>
- **Authors:** Xianze Fang, Qiyuan Feng, Dongfang Sun, Yan Zhang, Xiuchao Wu, Jingnan Gao, Jiangjing Lyu, Chengfei Lyu, Gang Yu
- **Submitted:** 2026-09-29 (v1)
- **Qualifying affiliation(s):** Alibaba Group — Taobao3D Team (all authors)
- **Categories:** cs.CV
- **Open release:** planned but not yet available — authors state "we will release all the code and weights together with a portion of our test dataset"; project blog at alibaba.github.io/Taobao3D/blog/taoflowforge/
- **Shipped counterpart:** none found

**Summary:** TaoFlowForge is an artistic mesh foundation model that generates production-ready 3D meshes by decomposing generation into coarse-to-fine vertex generation and edge/connectivity prediction.
**Purpose:** Prior mesh generators (autoregressive or SDF-based) struggle to produce lightweight, editable, topologically clean meshes that are directly usable in production 3D pipelines (rigging, animation, rendering).
**Breakthrough:** The authors report state-of-the-art results among open-source mesh topology generators and outperformance versus autoregressive methods under image-conditioned generation, tested on both out-of-distribution hand-crafted assets and public benchmark datasets.
**Tools & method:** A two-stage coarse-to-fine cascaded flow-matching process generates vertices; a separate connectivity-affinity estimation step predicts edges between vertices along with per-vertex normals to determine face orientation.
**Limitation:** No dedicated "Limitations" section for TaoFlowForge's own method was found in the fetched HTML (the only "limitation" mentions found describe shortcomings of prior autoregressive mesh-generation work, in the related-work discussion) — none is stated here to avoid inventing one.
