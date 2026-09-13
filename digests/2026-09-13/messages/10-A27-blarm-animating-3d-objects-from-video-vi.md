**[A27] BLARM: Animating 3D Objects from Video via Blending Latent Rigid Motion Primitives**
- **arXiv:** 2608.31113 · https://arxiv.org/abs/2608.31113
- **Submitted:** 2026-08-31
- **Authors:** Pradyumn Goyal, Yizhak Ben-Shabat, Hsueh-Ti Derek Liu, Haomiao Jiang, Snehasish Mukherjee, Kyle Spence, Mark Stauber, Evangelos Kalogerakis, Yunze Zeng
- **Qualifying affiliation(s):** Roblox — Yizhak Ben-Shabat, Hsueh-Ti Derek Liu, Haomiao Jiang, Snehasish Mukherjee, Kyle Spence, Mark Stauber, Yunze Zeng (Pradyumn Goyal as a Roblox intern)
- **Categories:** cs.CV
- **Open release:** none
- **Shipped counterpart:** none found

**Summary:** A feed-forward method that animates a static 3D mesh from monocular video, predicting a temporally coherent animated mesh without skeletons, cages or manual rigs, by representing motion as a compact set of learned time-varying rigid primitives blended with time-invariant per-vertex skinning weights.
**Purpose:** Automatic animation of arbitrary 3D objects from a single video, replacing manual rigging or dense per-vertex prediction.
**Breakthrough:** The authors report the best results on ActionBench (CD-3D 1.71, CD-4D 3.07, CD-Motion 7.15, FVD 426.72 versus baseline ranges 2.49 to 3.30 / 5.01 to 5.61 / 9.24 to 11.12 / 787 to 1270) and Motion80, with the fastest inference among compared methods (3.13 s per 16-frame video).
**Tools & method:** A transformer combining geometry-conditioned deformation latents with video features via factorised spatial-temporal attention; trajectory reconstruction loss, entropy regularisation for sparse skinning and motion-aware contrastive learning; about 10,000 Objaverse shapes rendered at 512x512, trained on 8 NVIDIA H200 GPUs for about 1.5 days.
**Limitation:** The authors acknowledge incorrect vertex-to-component assignment and "part entanglement" when nearby regions look alike but should move independently, and that the mesh topology must suit the target motion.
