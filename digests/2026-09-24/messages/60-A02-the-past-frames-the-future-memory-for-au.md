**[A02] The Past Frames the Future: Memory for Autoregressive Video Generation**
- **arXiv:** 2609.28466 · <https://arxiv.org/abs/2609.28466>
- **Submitted:** 2026-09-23
- **Authors:** Harold Haodong Chen et al.
- **Qualifying affiliation(s):** NVIDIA — Ser-Nam Lim, per the paper's affiliation list (HKUST, CityUHK, FDU, ZODA, CMU, NYU, HKUST(GZ), NUS, Georgia Tech, PKU, MBZUAI, NVIDIA, UCF, UNITN, NTU, UC Merced)
- **Categories:** cs.CV
- **Open release:** none stated (the authors reference an accompanying GitHub repository tracking related literature, not code/weights for a model of their own)
- **Shipped counterpart:** none found

**Summary:** This is a survey/framework paper (not an empirical model paper) organizing how autoregressive video generators maintain memory of past frames — entity identities, spatial layout, dynamics — under bounded context windows, covering discrete-token, diffusion, flow, and Transformer-based generators, including long-horizon and interactive world modeling.
**Purpose:** The authors argue that as generated video sequences expand, models cannot retain full history due to context-window limits, so historical information can become inaccessible before its relevance to the current frame has passed; the paper aims to systematize how existing work addresses this rather than propose a new method.
**Breakthrough:** The authors propose a five-perspective taxonomy — memory forms (visual/pixel-VAE, implicit state, explicit state, adaptive parametric), functions (identity, spatial, dynamic, semantic, causal), operations (query, retrieval, integration, writing, updating), learning objectives, and evaluation protocols — and define memory as "persistent representation of past observations maintained across autoregressive steps and systematically conditioning subsequent generation."
