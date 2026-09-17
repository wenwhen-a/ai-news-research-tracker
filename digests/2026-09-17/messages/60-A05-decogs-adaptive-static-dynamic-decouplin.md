**[A05] DecoGS: Adaptive Static-Dynamic Decoupling of 3D Gaussians for Free-Viewpoint Video Streaming**
- **arXiv:** 2609.17230 · <https://arxiv.org/abs/2609.17230>
- **Submitted:** 2026-09-15 (v1)
- **Authors:** Idil Sulo, Alexey Supikov, Ilke Demir, Sainan Liu
- **Qualifying affiliation(s):** Intel Labs — Sainan Liu (co-authors listed with University of Bonn/Almetra, V3DEO, and Cauth AI affiliations)
- **Categories:** cs.CV
- **Open release:** none found
- **Shipped counterpart:** none found

**Summary:** DecoGS is a method for efficient online training of 3D Gaussians from streaming video, targeting free-viewpoint video (FVV) streaming.
**Purpose:** Streaming 3D reconstruction needs both speed and temporal fidelity, but existing methods undermine this by indiscriminately updating every Gaussian every frame even in static regions.
**Breakthrough:** The authors report DecoGS achieves 34.55 dB PSNR on N3DV and 31.60 dB PSNR on MeetRoom, "outperforming all streaming and offline baselines," while rendering at 261 FPS and achieving 70x lower temporal flicker than the best prior method, without requiring large-scale pretraining.
**Tools & method:** DecoGS integrates region-aware Gaussian management via gradient gating and efficient visibility filtering to maintain temporal coherence and a compact memory footprint.
**Limitation:** The authors state that current change detection could be extended with semantic or foundation-model cues for more intent-aware dynamic-region detection, since the current approach relies on heuristics that don't distinguish transient objects from persistent background.
