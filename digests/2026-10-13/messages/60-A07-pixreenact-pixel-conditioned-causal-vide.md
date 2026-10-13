**[A07] PixReenact: Pixel-Conditioned Causal Video Diffusion for Streaming Head-Avatar Reenactment**
- **arXiv:** 2610.05233 · <https://arxiv.org/abs/2610.05233>
- **Submitted:** 2026-10-04
- **Authors:** Gavriel Habib, Dvir Samuel, Or Shimshi, Rami Ben-Ari
- **Qualifying affiliation(s):** NVIDIA — Dvir Samuel (other authors: OriginAI, Israel). Real author affiliation confirmed in the paper's own header, not a GPU-hardware mention or project-host artifact.
- **Categories:** cs.CV
- **Open release:** none stated; project page only — <https://gavriel-habib.github.io/pixreenact/>
- **Shipped counterpart:** none found

**Summary:** PixReenact is a streaming system that animates a reference face using a live driving video, operating directly on encoded image frames rather than specialized identity/motion features extracted by external models (which the authors argue inherits those extractors' errors).
**Purpose:** To enable robust, low-latency, streaming head-avatar reenactment that stays stable over long sessions and handles extreme viewpoints, occlusions, and strong expressions better than prior feature-extractor-based pipelines.
**Breakthrough:** The authors report strong gains over PersonaLive on identity preservation under extreme conditions (ID 0.727 vs. 0.472) and especially on self-reenactment fidelity (TalkingHead-1KH PSNR 37.48 vs. 19.55, FVD 8.2 vs. 199.4; VFHQ-Test FVD 5.5 vs. 83.8).
**Tools & method:** Trained with pseudo cross-identity pairs and dual-teacher distillation; evaluated on CelebV-HQ (extreme-condition drivers), FFHQ (references), TalkingHead-1KH, VFHQ-Test, NeRSemble (15 held-out subjects), and HDTF/self-collected YouTube videos for long-horizon streaming tests.
**Limitation:** The authors note PixReenact is slower per-chunk than the PersonaLive baseline (238.9 ms vs. 211.1 ms, 16.74 vs. 18.95 FPS), and fewer denoising steps (3- or 2-NFE) cut latency further but visibly degrade motion and distribution quality.
