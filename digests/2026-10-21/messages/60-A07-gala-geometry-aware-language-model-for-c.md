**[A07] GALA: Geometry-Aware Language Model for Controllable Object Arrangement**
- **arXiv:** 2610.28280 · <https://arxiv.org/abs/2610.28280>
- **Submitted:** 2026-10-20 (v1)
- **Authors:** Chucheng Xiang et al.
- **Qualifying affiliation(s):** Tencent — Zhi Deng (listed as corresponding author, Tencent, Shenzhen) and several co-authors (e.g. Chucheng Xiang, Runze Wang, Yuxuan Xie, Hanliu Wang) carry dual Tencent + university (USTC / Tsinghua) affiliations per the paper's affiliation block. Not borderline — direct Tencent affiliation confirmed.
- **Categories:** cs.GR (primary); cs.AI; cs.CV
- **Open release:** dataset "will be open-sourced" per the abstract (not yet released); no code/weights stated; project page: <https://xccelephant.github.io/paper/gala/>
- **Shipped counterpart:** none found

**Summary:** GALA is a geometry-aware language model that predicts the 6D pose of one target object at a time for controllable 3D object arrangement, using explicit point-cloud perception instead of oriented-bounding-box (OBB) approximations.
**Purpose:** The paper targets fine-grained placement constraints such as support and containment that existing OBB-based scene-layout methods cannot reason about because OBBs are blind to detailed object geometry.
**Breakthrough:** The authors report their 0.7B-parameter model reaches 65.62% Within Valid Rate and 78.59% Instruction Valid Rate on their held-out test split, versus 22.53%/42.29% for a zero-shot GPT-OSS-120B baseline and 10.96%/37.71% for an adapted LayoutVLM baseline (Table 1).
**Tools & method:** GALA combines a point-cloud perception module with a geometry-to-text projection layer inside an interleaved multimodal context, trained via the two-stage strategy above.
