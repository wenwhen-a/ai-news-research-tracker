**[A03] Motion-guided Contrastive Regularization For Latent World Models**
- **arXiv:** 2611.06901 · <https://arxiv.org/abs/2611.06901>
- **Submitted:** 2026-11-04
- **Authors:** Yiwen Chen, Qiqi Hou, Jisoo Jeong, Yinhao Zhu, Huaizu Jiang, Amir Said
- **Qualifying affiliation(s):** Qualcomm AI Research — Qiqi Hou, Jisoo Jeong, Yinhao Zhu, Amir Said (Yiwen Chen and Huaizu Jiang are at Northeastern University; a footnote states the work was done during an internship at Qualcomm)
- **Categories:** cs.CV
- **Open release:** none (paper mentions a "video demo" but gives no URL; no code/weights link found)
- **Shipped counterpart:** none found

**Summary:** The paper studies JEPA-style latent world models, which learn action-conditioned dynamics without reconstructing observations, and identifies a failure mode it calls "static collapse," where the encoder keeps episode-specific background content and drops manipulation-relevant state changes.
**Purpose:** The authors address the gap between good reconstruction-free world-model representations and robust downstream planning when visual backgrounds vary, a setting where existing latent world models lose task-relevant signal.
**Breakthrough:** Combined with latent prediction and SIGReg, the authors report planning success rising from 52% to 78% on OGBench-Cube with randomized backgrounds and from 14% to 54% on LIBERO-Object, over the LeWorldModel baseline, while staying comparable on four other visual-control benchmarks.
**Tools & method:** The method builds on the LeWorldModel JEPA-style architecture and is evaluated on OGBench-Cube and LIBERO-Object plus four other visual-control benchmarks, using optical-flow-derived similarity to weight contrastive targets from the same episode.
**Limitation:** The authors state the method depends on sufficient action coverage and is sensitive to shifts in action representations and visual appearance (e.g., rendering-engine changes).
