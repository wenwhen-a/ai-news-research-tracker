**[A01] Past as State, Present as Attention: Persistent-State Blockwise Flow Matching for Long-Horizon Co-Speech Motion Generation**
- **arXiv:** 2610.32373 · <https://arxiv.org/abs/2610.32373>
- **Submitted:** 2026-10-23
- **Authors:** Yi Liu, Xiangyue Zhang, Jianfang Li, Jia Ma, Yisheng He, Jianqiang Ren
- **Qualifying affiliation(s):** Alibaba Group — Jianfang Li (corresponding author), Yisheng He, Jianqiang Ren, and Yi Liu (listed with a dual Tongji University / Alibaba Group affiliation). Xiangyue Zhang is affiliated with The University of Tokyo; Jia Ma with Tongji University.
- **Categories:** cs.CV (primary); cs.GR; cs.MM
- **Open release:** none found (no code/project link located on the abstract or HTML page)
- **Shipped counterpart:** none found

**Summary:** The paper tackles long-horizon co-speech motion generation, where existing segment-by-segment methods either drift (short recent-frame conditioning) or become costly and hard to train (ever-growing explicit histories).
**Purpose:** Long-duration co-speech motion generation must remain temporally coherent and stylistically consistent, but existing segment-based generation approaches either drift over time or require expensive, hard-to-learn long explicit histories.
**Breakthrough:** The authors report state-of-the-art FGD (Fréchet Gesture Distance) on public benchmarks along with improved style preservation over long sequences compared to prior methods.
**Tools & method:** The method uses blockwise flow matching with multi-block supervision for training on variable-length histories, prefill-decode state caching for efficient rollout, and hybrid classifier-free guidance for history and speech conditioning.
**Limitation:** Not stated by the authors (not surfaced in the available abstract/summary text).
