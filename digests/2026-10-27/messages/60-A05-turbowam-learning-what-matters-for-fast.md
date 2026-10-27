**[A05] TurboWAM: Learning What Matters for Fast World Action Models**
- **arXiv:** 2610.33941 · <https://arxiv.org/abs/2610.33941>
- **Submitted:** 2026-10-24
- **Authors:** Guile Wu et al.
- **Qualifying affiliation(s):** Huawei (Noah's Ark Lab / Department of Foundation Model) — Guile Wu, Xingxin Chen, Chengjie Huang, Sam Hosseini, Tongtong Cao, Yingxue Zhang, Dongfeng Bai, and Shuangzhi Li (dual-affiliated with University of Alberta; footnote states the work was done during an internship at Huawei Canada). FLAG: borderline (Huawei is explicitly named as a borderline example in the task brief).
- **Categories:** cs.CV
- **Open release:** none found beyond a project page (<https://turbowam.github.io/>); the only GitHub link on that page is a template credit (nerfies), not the authors' own code.
- **Shipped counterpart:** none found

**Summary:** TurboWAM is a fast world action model (WAM) for robot policy learning that reduces inference latency by adaptively aggregating world-model-layer representations according to their relevance to action prediction, rather than using every layer uniformly.
**Purpose:** The paper targets high inference latency in world action models, a bottleneck for real-world deployment, noting that prior efficiency methods reduce future-frame imagination or speed up action prediction but still use every world-model layer without weighting their relevance to action prediction, causing redundant computation.
**Breakthrough:** At inference, the authors report TurboWAM runs fewer world-model layers and caches representations across denoising steps to substantially reduce computational overhead.
