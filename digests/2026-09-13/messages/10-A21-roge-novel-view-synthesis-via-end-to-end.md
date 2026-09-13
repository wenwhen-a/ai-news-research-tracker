**[A21] RoGe: Novel View Synthesis via End-to-End Implicit Reconstruction and Generation**
- **arXiv:** 2609.02847 · https://arxiv.org/abs/2609.02847
- **Submitted:** 2026-09-02
- **Authors:** Xiaolei Lang, Ze Kang, Zehao Huang, Naiyan Wang
- **Qualifying affiliation(s):** Xiaomi EV — Xiaolei Lang, Zehao Huang, Naiyan Wang; FLAG: borderline
- **Categories:** cs.CV
- **Open release:** none (project page https://jerry-locker.github.io/roge/, no code stated)
- **Shipped counterpart:** none found

**Summary:** RoGe fuses implicit 3D reconstruction and video-diffusion generation end to end for novel view synthesis: from a few posed images and a camera trajectory it produces a temporally coherent fly-through video without an explicit 3D intermediate.
**Purpose:** Hybrid reconstruction-plus-generation methods pass lossy rendered images or explicit 3D through to generation and give reconstruction no corrective signal back; RoGe removes that bridge.
**Breakthrough:** The authors report that on DL3DV, RoGe outperforms reconstruction-based, generation-based and hybrid baselines on image metrics and video temporal consistency, with ablations showing ray-queried implicit features beat raw reconstruction tokens and rendered RGB as conditioning.
**Tools & method:** A feed-forward reconstruction model builds an implicit scene representation; target camera rays query it for per-view features injected into a video diffusion model; both are trained jointly on DL3DV.
**Limitation:** Evaluation is restricted to DL3DV and the compute cost of joint training is not discussed (observed, not stated).
