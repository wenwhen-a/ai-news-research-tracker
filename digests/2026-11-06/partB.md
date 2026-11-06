# Part B — Research → Product
Window: last 90 days (2026-08-08 to 2026-11-06). Retrieval: light check (not the Monday full sweep) — ~10 primary surfaces checked for the last 7 days (NVIDIA developer blog & GeForce news, Unreal Engine news, Unity blog, Roblox newsroom, Adobe blog, Tencent Hunyuan, ByteDance Volcano Engine/Seed, Alibaba Cloud blog/Model Studio, Kuaishou Kling, PlayStation Blog). Products: 0 new, 1 updated.

---
## NVIDIA DLSS 5 with 3D-Guided Neural Rendering (in NBA 2K27)
- **Company:** NVIDIA
- **Status:** GA · **Released:** 2026-09-03 · **Update**
- **Surface:** game-ready driver feature (shipped in specific titles)
- **Primary source:** https://www.nvidia.com/en-us/geforce/news/hogwarts-legacy-war-thunder-dlss-5-3d-guided-neural-rendering/
- **Underlying research:** no traceable paper
- **Availability:** RTX 50 Series GPUs/laptops, RTX Spark PCs, GeForce NOW Ultimate; requires the November 4, 2026 Game Ready Driver

**What shipped (≤3 sentences):** Update since 2026-09-03: NVIDIA states DLSS 5 with 3D-Guided Neural Rendering is "available now" in Hogwarts Legacy as of November 5, 2026, enabled in-game via a "Neural Rendering" toggle after installing the Game Ready Driver released November 4. NVIDIA also confirmed War Thunder will get it in mid-November (as part of the game's "Eagle's Shadow" update) and Where Winds Meet on November 23, 2026.
**What research it translates (≤3 sentences):** No traceable paper; NVIDIA describes the feature as a final-stage neural pass that reprocesses a game's own rendered frame (geometry, textures, lighting buffers) using an AI model, without naming an underlying publication.
**Practical significance (≤3 sentences):** NVIDIA reports (its own figures, not independently measured) up to 300 fps at 4K and 370 fps at 1440p in Hogwarts Legacy on an RTX 5090 with max settings, ray tracing, DLSS 5, 6X Multi Frame Generation, Ray Reconstruction, and Reflex enabled together; for War Thunder it reports up to 400 fps at 4K and 550 fps at 1440p (Ultra preset) on desktop RTX 50-series, and up to 300/490 fps on RTX 5090 Laptop/RTX 50-series laptops. NVIDIA states these are model-processing performance figures, not independently verified in-game frame-rate benchmarks.
**Engineering details (≤3 sentences):** The developer-facing SDK lets studios choose among several AI models and adjust "Structure Intensity" and "Tone Intensity," plus semantic and engine-level masking (per NVIDIA's own prior disclosures referenced in the update's context). The current Neural Rendering model is roughly 118M parameters, about 24% smaller, running 2x faster and using 20% less 4K VRAM than the version NVIDIA shipped in September 2026 (per the October 2026 update already on file).
**Limitation / caveats (≤3 sentences):** The feature is gated to RTX 50 Series GPUs/laptops, RTX Spark PCs, and GeForce NOW Ultimate — RTX 40-series and older hardware is not supported. NVIDIA's performance figures are vendor-reported and describe neural-model processing efficiency rather than independently measured end-to-end frame rates.

### Announced only (not yet usable)
(none)

Near-misses: 1 (NVIDIA's November 2, 2026 developer blog announced new Cosmos 3 Nano/Embodied simulation checkpoints, an expanded Cosmos Framework, and a new Cosmos NIM inference package — but these are robotics/autonomous-vehicle and surgical-simulation focused, not a game-industry product, and the post does not state GA vs. preview status for the new items, so it is not counted as a Part B item here).
Verification: all claims above re-confirmed against the cited NVIDIA primary source before writing; the product_seen.json entry's `updates` list was appended (not overwritten) and `last_update` set to 2026-11-05.
