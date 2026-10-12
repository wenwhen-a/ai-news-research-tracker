**[A02] GLIMPSE: Global-Local Indexing with Multi-Precision Spectral Encoding for Explorable Video World Models**
- **arXiv:** 2610.13706 · <https://arxiv.org/abs/2610.13706>
- **Submitted:** 2026-10-09 (v1)
- **Authors:** Zhufeng Xu et al.
- **Qualifying affiliation(s):** Kuaishou — Yikang Ding, Xiaoqiang Liu, Guoxin Zhang (affiliated with Kling AI, a Kuaishou Technology subsidiary)
- **Categories:** cs.CV
- **Open release:** none found
- **Shipped counterpart:** none found

**Summary:** GLIMPSE is a memory architecture for camera-controlled, explorable video world models, designed to keep previously-seen regions of a scene consistent when the camera revisits them.
**Purpose:** The authors target the consistency problem in long-horizon, camera-controllable video world models: feature-rerendering memory methods turn depth/pose errors into ghosting or duplicated structure, while positional-transport memory applies full positional precision even to inaccurate projections.
**Breakthrough:** The authors report that, under matched retrieval and read budgets, GLIMPSE achieves better geometric correspondence and photometric consistency than deterministic positional transport, using band-wise multi-precision coordinates, geometry-conditioned spectral attenuation, and footprint-guided retrieval under a fixed local read budget.
**Tools & method:** The system uses cached Depth Anything 3 geometry, a frozen CUT3R with MeMix for recurrent global memory, GIM-DKM for correspondence matching, and OpenCV USAC_MAGSAC for inlier estimation; it is trained with AdamW on 8 GPUs and evaluated on WorldScore against UCM, SPMem, GEN3C, VMem, and ReWorld baselines, using training data from SpatialVID, RealCam-Vid, ReCamMaster, and Context-as-Memory.
