**[A06] Evolve in Panorama, Render in View: Panoramic World State Evolution for Video World Models**
- **arXiv:** 2611.22733 · <https://arxiv.org/abs/2611.22733>
- **Submitted:** 2026-11-17
- **Authors:** Longtao Jiang, Mingfei Han, Jianmin Bao, Tingjun Dai, Jinjie Wei, Zhiran Zhang, Xin Tao, Zhihui Li, Salman Khan, Xiaojun Chang
- **Qualifying affiliation(s):** Kuaishou Technology — the paper's affiliation block lists Mohamed bin Zayed University of Artificial Intelligence and Kuaishou Technology as the only two institutions; Xin Tao is independently confirmed (public researcher profile) as Senior Researcher/Tech Lead in Kuaishou's Visual Generation ("Kling") Group. Exact per-author mapping was not fully resolvable from the HTML rendering.
- **Categories:** cs.CV
- **Open release:** none yet (abstract states "code, models, and data will be released")
- **Shipped counterpart:** none found

**Summary:** PanoEvo is a video world model that keeps the entire scene evolving even when the camera isn't looking at parts of it, using a Panoramic Evolver that updates scene state in the latent space of a panoramic video diffusion model so every viewing direction changes consistently over time.
**Purpose:** The authors target a gap in current video world models, which they say only update what the camera currently sees rather than maintaining a persistently evolving world.
**Breakthrough:** The authors report the best overall score among 23 publicly evaluated models on WRBench and the highest total score on STEVO-Bench.
**Tools & method:** The Evolver is trained coarse-to-fine as an image-to-panoramic-video model on PanoEvo-Data, a new event-centric dataset built from real 360° videos; the Perspective Renderer, built on a perspective video diffusion model, reads world state via latent-space projection and direction-restricted cross-attention.
**Limitation:** No explicit limitation is stated in the fetched abstract.
