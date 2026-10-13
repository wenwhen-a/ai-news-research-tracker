**[A04] GenIA: Generative Reconstruction with Test-Time Input Alignment**
- **arXiv:** 2610.12388 · <https://arxiv.org/abs/2610.12388>
- **Submitted:** 2026-10-08
- **Authors:** Stefano Esposito, Naama Pearl, Polina Karpikova, Samuel Rota Bulò, Lorenzo Porzi, Peter Kontschieder, Andreas Geiger, Jonathon Luiten
- **Qualifying affiliation(s):** Meta Reality Labs — Samuel Rota Bulò, Lorenzo Porzi, Peter Kontschieder, Jonathon Luiten (other authors are Tübingen AI Center / University of Tübingen)
- **Categories:** cs.CV
- **Open release:** none found
- **Shipped counterpart:** none found

**Summary:** Generative 3D models can hallucinate plausible geometry for unseen parts of an object from one or a few views, but their outputs often don't match the observed geometry, appearance, or pose.
**Purpose:** To align a frozen generative reconstruction model's output with real observations (pose, scale, appearance) at inference time, improving single/few-view 3D object reconstruction for both static and dynamic objects.
**Breakthrough:** The authors report better pose estimation and reconstruction than recent optimization-based, per-frame image-to-3D, and video-to-4D baselines; depth-grounded translation/scale reduce reprojection error by 1.4–2.8x and relative jitter by 2–4x, and ICP halves Chamfer distance on static reconstruction.
**Tools & method:** Built on top of the SAM3D generative model, with dynamic-object geometry supplied by an external predictor, ActionMesh.
**Limitation:** Dynamic-object geometry depends on the external ActionMesh predictor rather than being grounded directly in observations, so its errors or misplacements can strongly degrade results; rotation remains largely prior-driven and is corrected only by a noise-sensitive ICP step.
