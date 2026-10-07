**[A02] Efficient Gaussian Splatting Sequence Compression with Standard Video Codecs**
- **arXiv:** 2610.07795 · <https://arxiv.org/abs/2610.07795>
- **Submitted:** 2026-10-06
- **Authors:** Qi Yang, Shuting Xia, Le Yang, Geert Van Der Auwera, Zhu Li
- **Qualifying affiliation(s):** Qualcomm — Geert Van Der Auwera
- **Categories:** cs.CV
- **Open release:** code — <https://github.com/Qi-Yangsjtu/GSCV>
- **Shipped counterpart:** none found

**Summary:** The paper presents GSCV, a Gaussian Splatting (GS) sequence compression method built on standard video codecs.
**Purpose:** The goal is to compress GS sequences effectively using off-the-shelf video codecs even when tracked primitive correspondence across frames is not available, which the authors identify as a gap in existing anchors such as GSCodec Studio.
**Breakthrough:** The authors report that GSCV shows "obviously improved performance" over MPEG video- and point-cloud-based anchors in GS sequence compression, and that it achieves better performance than video- and point-cloud-based anchors used in the current MPEG standardization study on both tracked and semi-tracked sequences.
**Tools & method:** GSCV introduces "Inter-PLAS," a method that produces visually close images between I-frames and P-frames of a GS sequence to strengthen inter-frame correlation for the video codec.
**Limitation:** The authors state that PLAS-derived images differ substantially from natural images, which restricts the compression ratios achievable with generic video codecs.
