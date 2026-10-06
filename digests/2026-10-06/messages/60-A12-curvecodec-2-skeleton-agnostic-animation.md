**[A12] CurveCodec 2: Skeleton-agnostic animation compression with a learned entropy model**
- **arXiv:** 2610.04211 · <https://arxiv.org/abs/2610.04211>
- **Submitted:** 2026-10-03
- **Authors:** Mingyi Shi et al.
- **Qualifying affiliation(s):** Adobe Research — Xuelin Chen
- **Categories:** cs.GR; cs.AI; cs.RO
- **Open release:** demo/project page (<https://rubbly.cn/publications/curvecodec/>)
- **Shipped counterpart:** none found

**Summary:** The paper presents CurveCodec 2, a skeleton-agnostic skeletal-motion compression codec that asks which part of a production codec a learned model should take over, building on the authors' earlier CurveCodec.
**Purpose:** The authors state that skeletal animation is stored as every joint's transform at every frame even though most of it is implied by the body, and that a production codec must guarantee a stated error bound for any skeleton; their earlier CurveCodec matched ACL's mean error but not its worst case, and measured payload in floats rather than bits, motivating this follow-up that targets bit-rate and worst-case guarantees.
**Breakthrough:** On a held-out test set of 4,472 clips from 33 datasets, the authors report CurveCodec 2 needs 0.37x of ACL's bytes at ACL's default precision of 0.01 cm under the worst-case contract, and 0.22x at 0.1 cm under the mean contract, while decoding on a single CPU core and transferring without retraining to a species absent from training data.
