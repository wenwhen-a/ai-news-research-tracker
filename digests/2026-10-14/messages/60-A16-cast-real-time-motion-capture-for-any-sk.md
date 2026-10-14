**[A16] CAST: Real-Time Motion Capture for Any Skeleton Topology**
- **arXiv:** 2610.14856 · <https://arxiv.org/abs/2610.14856>
- **Submitted:** 2026-10-10
- **Authors:** Pu Pang, Zhongfei Qing, Ling-Hao Chen, Songnan Li, Hua Huang, Bo Hu
- **Qualifying affiliation(s):** Tencent — Zhongfei Qing, Songnan Li, Bo Hu (marked "Project leader")
- **Categories:** cs.CV
- **Open release:** code — <https://github.com/fankewen/CAST>
- **Shipped counterpart:** none found

**Summary:** CAST recovers motion from monocular video and retargets it onto a target skeleton whose topology differs from the filmed subject's, addressing joint-rotation errors that previously propagated down the kinematic hierarchy.
**Purpose:** Cross-topology motion capture — mapping a performance captured on one body/skeleton onto an arbitrary target skeleton — remains error-prone because small joint-rotation mistakes compound along the skeletal hierarchy.
**Breakthrough:** An "observability analysis" formally characterizes which rotational degrees of freedom outgoing bone directions can and cannot constrain, which motivates GRACE's reliability-gated parent-to-child correction.
**Tools & method:** The motion predictor and GRACE correction module are trained jointly with motion-derived supervision on top of a frozen image encoder (DINOv3 features mentioned in the appendix); GRACE applies rank-based geometric correction only to the rotation components that outgoing bone directions can observably constrain, leaving the rest to the learned predictor.
**Limitation:** The authors state GRACE can only correct rotational components constrained by outgoing bone directions — leaf joints and collinear bone chains leave axial twist undetermined, which they illustrate as visible head-orientation ("twist") errors even when joint positions are accurate.
