**[A02] Code Plans, Diffusion Renders: Open-Ended Generative World Modeling**
- **arXiv:** 2609.26458 · <https://arxiv.org/abs/2609.26458>
- **Submitted:** 2026-09-22
- **Authors:** Zixun Fang, Yawen Shao, Kai Zhu, Jie Xiao, Shihan Chen, Yu Liu, Xueyang Fu, Yang Cao, Wei Zhai, Zheng-Jun Zha
- **Qualifying affiliation(s):** Alibaba — TongYi Lab co-authors (alongside USTC academic co-authors)
- **Categories:** cs.CV
- **Open release:** planned — "Code and model weights will be made publicly available" (project page: becauseimbatman0.github.io/CoDeR); no functioning release link confirmed at time of check
- **Shipped counterpart:** none found

**Summary:** CoDeR is a world-modeling system that explicitly constructs an executable world using code, then uses a video generation model for visual realization, rather than implicitly encoding dynamics purely in a video model's weights.
**Purpose:** The paper targets limitations of existing video world models, which represent dynamics only implicitly through visual observations, limiting long-term memory, open-ended interaction, autonomous evolution, and multi-agent persistence.
**Breakthrough:** The authors report their framework "substantially extends the capabilities of existing world models" on long-term memory, open-ended interaction, autonomous evolution and persistent multi-agent dynamics, with state-of-the-art performance across multiple evaluation settings (WorldScore, VBench) as they state it.
**Tools & method:** The Creator/Executor roles run on "GPT-6 Astra," described as an advanced multimodal LLM-based coding agent, generating executable code for a whitebox 3D world built in Three.js; human/hand-object motion is represented with SMPL-H.
**Limitation:** The authors state that at roughly 5,000 frames, "noticeable degradation appears" due to accumulated errors from chunk-based generation.
