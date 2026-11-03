**[A02] History Forcing: Distilling History-Dependent Continuations for Long-Horizon Video World Models**
- **arXiv:** 2611.02782 · <https://arxiv.org/abs/2611.02782>
- **Submitted:** 2026-11-02
- **Authors:** Hangyi Kuang et al.
- **Qualifying affiliation(s):** Microsoft Research — Yuke Zhao, Zisu Huang, Yifan Yang (listed with a dual Zhejiang University / Microsoft Research affiliation). Other authors are affiliated with Zhejiang University, Monash University, and Adelaide University. (Note: a "Google" flag from the screening tool was checked and found to be a false positive — the term does not appear anywhere on the paper's page; the real qualifying affiliation is Microsoft Research.)
- **Categories:** cs.CV
- **Open release:** code (<https://github.com/ziplab/History-Forcing>); project page (<https://ziplab.github.io/History-Forcing-Project-Page/>)
- **Shipped counterpart:** none found

**Summary:** The paper addresses weak historical conditioning in few-step autoregressive video diffusion world models, which causes drift and inconsistency over long video horizons.
**Purpose:** Few-step autoregressive video diffusion enables efficient generation, but existing few-step generators under-use historical context, limiting consistency and quality in long-horizon video world models.
**Breakthrough:** The authors report state-of-the-art results among 1.3B-parameter models, with a VBench quality score of 85.07 on 15-second videos and a VBench-Long score of 79.82 on 60-second videos.
**Tools & method:** The method distills a bidirectional teacher into a few-step autoregressive student using a history-dependence residual weighted into the score/velocity distillation target; experiments use 1.3B teacher/student models for long-video generation and a 5B backbone for world modeling, evaluated on UltraVideo-Long, VidProM, Pexels, PlayWorld, and MemoBench.
