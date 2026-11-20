**[A01] VideoRNG: Relightable Neural Gaussians from Generative Video Models**
- **arXiv:** 2611.25338 · <https://arxiv.org/abs/2611.25338>
- **Submitted:** 2026-11-19
- **Authors:** Bowen Xue et al.
- **Qualifying affiliation(s):** NVIDIA — Bowen Xue, Saeed Hadadan, Fabrice Rousselle, Zahra Montazeri, Miloš Hašan
- **Categories:** cs.CV, cs.GR
- **Open release:** none found
- **Shipped counterpart:** none found

**Summary:** VideoRNG creates relightable 3D assets from a text prompt or single image in two stages: a fine-tuned video diffusion model first generates an RGBA turntable video under known pose, camera, and lighting, and a feed-forward reconstruction model then maps latent frames from selected views into millions of anisotropic 3D Gaussians with learned appearance features.
**Purpose:** The authors argue that realistic 3D assets, especially those with fine geometry or complex light transport, are hard to express with standard meshes and physically based materials, and that existing Gaussian-splatting generators typically bake in fixed lighting.
**Breakthrough:** The authors report that their method can produce assets with fine, hard-to-model structures (fur, feathers, webs) that remain relightable and interactively renderable, which they attribute to the combination of video-diffusion generation with a Gaussian-based relightable representation.
**Tools & method:** Stage one fine-tunes a video diffusion model to produce an RGBA turntable video under known pose/camera/lighting; stage two feed-forward reconstructs latent frames from selected views into anisotropic 3D Gaussians with learned appearance features, rendered via a shared directional decoder and a stochastic ray tracer.
**Limitation:** The accessible text does not state an explicit limitations section; no code, weights, or demo release statement was found in the portion of the paper reviewed.
