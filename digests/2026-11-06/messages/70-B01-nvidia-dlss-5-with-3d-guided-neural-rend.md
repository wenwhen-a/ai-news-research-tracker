**[B01 · Update] NVIDIA DLSS 5 with 3D-Guided Neural Rendering (in NBA 2K27)**
- **Company:** NVIDIA
- **Status:** GA · **Released:** 2026-09-03 · **Update**
- **Surface:** game-ready driver feature (shipped in specific titles)
- **Primary source:** <https://www.nvidia.com/en-us/geforce/news/hogwarts-legacy-war-thunder-dlss-5-3d-guided-neural-rendering/>
- **Underlying research:** no traceable paper
- **Availability:** RTX 50 Series GPUs/laptops, RTX Spark PCs, GeForce NOW Ultimate; requires the November 4, 2026 Game Ready Driver

**What shipped:** Update since 2026-09-03: NVIDIA states DLSS 5 with 3D-Guided Neural Rendering is "available now" in Hogwarts Legacy as of November 5, 2026, enabled in-game via a "Neural Rendering" toggle after installing the Game Ready Driver released November 4. NVIDIA also confirmed War Thunder will get it in mid-November (as part of the game's "Eagle's Shadow" update) and Where Winds Meet on November 23, 2026.
**What research it translates:** No traceable paper; NVIDIA describes the feature as a final-stage neural pass that reprocesses a game's own rendered frame (geometry, textures, lighting buffers) using an AI model, without naming an underlying publication.
**Practical significance:** NVIDIA reports (its own figures, not independently measured) up to 300 fps at 4K and 370 fps at 1440p in Hogwarts Legacy on an RTX 5090 with max settings, ray tracing, DLSS 5, 6X Multi Frame Generation, Ray Reconstruction, and Reflex enabled together; for War Thunder it reports up to 400 fps at 4K and 550 fps at 1440p (Ultra preset) on desktop RTX 50-series, and up to 300/490 fps on RTX 5090 Laptop/RTX 50-series laptops.
**Engineering details:** The developer-facing SDK lets studios choose among several AI models and adjust "Structure Intensity" and "Tone Intensity," plus semantic and engine-level masking (per NVIDIA's own prior disclosures referenced in the update's context).
