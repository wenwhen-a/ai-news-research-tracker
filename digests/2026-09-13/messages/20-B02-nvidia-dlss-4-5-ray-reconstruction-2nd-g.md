**[B02] NVIDIA DLSS 4.5 Ray Reconstruction, 2nd-generation transformer model (early access)**
- **Company:** NVIDIA
- **Status:** Public beta/preview (NVIDIA App early access) · **Released:** 2026-08-25 · **New**
- **Surface:** app feature / driver
- **Primary source:** https://www.nvidia.com/en-us/geforce/news/gamescom-2026-dlss-4-5-ray-reconstruction-release-announcements-trailers/
- **Underlying research:** no traceable paper
- **Availability:** Opt in via NVIDIA App (Settings > About > Early Access releases); requires GeForce Game Ready Driver 580.88 WHQL or newer; applicable to 30 games at time of writing (Alan Wake 2, Cyberpunk 2077, Portal with RTX, Indiana Jones and the Great Circle, Star Wars Outlaws among them). NVIDIA states "an official release will follow in September."

**What shipped:** NVIDIA states a "new 2nd generation transformer model" for DLSS Ray Reconstruction with "35% more compute capability" that "processes 20% more parameters, while maintaining similar performance to the previous model." It is available now as an early-access download.
**What research it translates:** An updated neural denoiser/reconstruction model for ray- and path-traced imagery in the DLSS Ray Reconstruction line. No paper is named.
**Practical significance:** Owners of RTX GPUs can apply the new model to 30 existing titles through the NVIDIA App without waiting for per-game patches.
**Engineering details:** Distributed via NVIDIA App override rather than game updates; driver 580.88 or newer required.
**Limitation / caveats:** Early-access status; NVIDIA gives only "September" for the official release and no numeric image-quality metrics. Whether the official release landed before 2026-09-13 was not confirmed from a primary source (observed, not stated).
