**[A01] PlayGen2: Learning Real-Time Playable Worlds with Explicit 3D State**
- **arXiv:** 2611.07867 · <https://arxiv.org/abs/2611.07867>
- **Submitted:** 2026-11-05
- **Authors:** Jihai Zhang et al.
- **Qualifying affiliation(s):** Tencent — Junyou Li, Deheng Ye (Jihai Zhang's internship was at Tencent; other authors: Chinese University of Hong Kong, Wellington College, Nanyang Technological University)
- **Categories:** cs.CV, cs.LG
- **Open release:** code + weights — <https://github.com/MajorDavidZhang/PlayGen-2> (paper states "code and pretrained model weights are publicly available")
- **Shipped counterpart:** none found

**Summary:** PlayGen2 is a real-time interactive world model that separates learned 3D state evolution from neural rendering, keeping a persistent world memory (a volumetric occupancy grid for static geometry plus identity-indexed 3D states for the player and other entities) and a separate neural renderer that turns depth/semantic projections of that state into first-person views.
**Purpose:** The paper targets real-time, interactive "playable world" generation where a game can be played rather than merely watched, addressing the gap between video-generation-style world models (which tend to drift and lack persistent, explicit state) and traditional game engines.
**Breakthrough:** The authors report backend latency of about 160ms on a consumer MacBook Pro (M4 Pro) — 200.6ms serial / 275.7ms pipelined at 8 denoising steps, 4.98–7.16 FPS — using a 41.2M-parameter world-state model and a 29.1M-parameter renderer (plus a 55.3M-parameter VAE) at 160×120 resolution.
