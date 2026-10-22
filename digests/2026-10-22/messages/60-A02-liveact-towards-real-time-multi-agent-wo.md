**[A02] LiveAct: Towards Real-Time Multi-Agent World Models with Heterogeneous Action Interfaces**
- **arXiv:** 2610.29408 · <https://arxiv.org/abs/2610.29408>
- **Submitted:** 2026-10-21 (v1)
- **Authors:** Xinyu Wang et al.
- **Qualifying affiliation(s):** Kuaishou Technology — Huafeng Shi, Teng Xi, Guoxin Zhang, Pengfei Wan (listed as "Kling Team," Kuaishou's video-generation research group)
- **Categories:** cs.CV
- **Open release:** none stated
- **Shipped counterpart:** none found

**Summary:** The paper studies multi-agent interactive video world models that generate one joint visual future for several independently controlled agents, which may take heterogeneous controls ranging from game buttons to continuous robot commands.
**Purpose:** The authors state that most existing interactive video world models assume a single controlled agent and a task-specific action interface, so they target the harder problem of independently controlling multiple agents with differently-typed action spaces (e.g., game vs. robot controls) within one generated video.
**Breakthrough:** The authors report 0.898 and 0.942 agent-attribution accuracy for games and robot manipulation respectively, without using agent locations or identity crops, and report their causal generator reaches 17.70 FPS at 512×448 resolution.
**Tools & method:** LiveAct is instantiated and evaluated on six multi-agent data sources spanning games and multi-robot manipulation, using teacher forcing and rollout-aware distribution matching to transfer the interface to a blockwise causal (streaming) generator, measured on visual quality, action following, agent attribution, and latency.
**Limitation:** The available text does not include an explicit "Limitations" section; the appendix discusses failure modes of comparison baselines (e.g., scene drift, frames degrading to black, game-track quality decaying over time) rather than stating LiveAct's own acknowledged weaknesses.
