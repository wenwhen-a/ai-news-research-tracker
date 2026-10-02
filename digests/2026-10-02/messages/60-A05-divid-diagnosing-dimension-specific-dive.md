**[A05] DiVid: Diagnosing Dimension-Specific Diversity Collapse in Video Generation Models**
- **arXiv:** 2610.01661 · <https://arxiv.org/abs/2610.01661>
- **Submitted:** 2026-10-01
- **Authors:** Huanran Hu, Zihui Ren, Dingyi Yang, Zhinan Song, Guozheng Wu, Tiezheng Ge, Qin Jin
- **Qualifying affiliation(s):** Alibaba Group — Tiezheng Ge
- **Categories:** cs.CV
- **Open release:** none (authors state "the framework will be released to facilitate future research")
- **Shipped counterpart:** none found

**Summary:** DiVid is a diagnostic framework that decomposes video-generation diversity into six interpretable dimensions — Semantic, Style, Subject, Scene, Motion, and Camera — each measured with reproducible computer-vision pipelines alongside quality and instruction-faithfulness metrics.
**Purpose:** The authors note that video generation models frequently produce similar outputs from identical prompts, constraining creative applications, and that prior aggregate diversity metrics obscure which specific factors are collapsing.
**Breakthrough:** The authors report that models with strong aggregate diversity scores still show collapse in particular factors, notably Motion and Camera, and identify two bottlenecks they call "default mode convergence" (models fall back to dominant patterns under ambiguous prompts) and "realization gaps" (models fail to faithfully execute explicitly requested diverse alternatives).
**Tools & method:** Evaluation used 206 prompts compiled from VBench-Category, VBench-Dimension, and T2V-CompBench, including controlled prompt experiments and classifier-free-guidance (CFG) scale adjustments across the six dimensions.
**Limitation:** The authors state that motion and camera estimation for generated video "remains the hardest part" of their pipeline, and that factor-level measurement accuracy depends on the automatic extraction tools used.
