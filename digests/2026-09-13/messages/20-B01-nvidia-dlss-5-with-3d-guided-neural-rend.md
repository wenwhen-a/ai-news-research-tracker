**[B01] NVIDIA DLSS 5 with 3D-Guided Neural Rendering (in NBA 2K27)**
- **Company:** NVIDIA
- **Status:** GA · **Released:** 2026-09-03 · **New**
- **Surface:** shipped game feature (driver + game integration)
- **Primary source:** https://www.nvidia.com/en-us/geforce/news/nba-2k27-dlss-5-3d-guided-neural-rendering-geforce-game-ready-driver/
- **Underlying research:** no traceable paper (NVIDIA's post cites none)
- **Availability:** GeForce RTX 50 Series GPUs only at launch; requires GeForce Game Ready Driver 616.64 WHQL; first and only title is NBA 2K27; no extra cost beyond the game and GPU.

**What shipped:** NVIDIA states "DLSS 5 is available now in the newly-released NBA 2K27" and that DLSS 5 introduces "3D-Guided Neural Rendering, infusing games with lifelike lighting and materials using advanced artist-guided AI models." It ships alongside Game Ready Driver 616.64.
**What research it translates:** NVIDIA describes an AI model that takes per-frame game colour and motion data and infers lighting and materials, positioned as the successor to the upscaling and frame-generation stages of earlier DLSS versions. No paper is cited.
**Practical significance:** Owners of RTX 50 Series hardware and NBA 2K27 get AI-modified lighting and materials (skin, hair, contact shadows per NVIDIA's description) in a shipped title today. NVIDIA reports NBA 2K27 reaching "370 FPS at 4K at Ultra Settings, with ray tracing, on a GeForce RTX 5090" with DLSS enabled.
**Engineering details:** Delivered through the GeForce driver and a game-side integration; inputs are the game's rendered colour and motion vectors; RTX 50 Series exclusive at launch.
**Limitation / caveats:** NVIDIA states RTX 40 Series support is planned but not available at launch. Only one game supports DLSS 5 as of the window's end (observed, not stated).
