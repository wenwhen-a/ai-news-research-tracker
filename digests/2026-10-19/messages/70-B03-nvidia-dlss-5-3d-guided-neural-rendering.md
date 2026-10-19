**[B03 · Update] NVIDIA DLSS 5 (3D-Guided Neural Rendering) — 2X-Faster Model + RTX Spark Rollout**
- **Company:** NVIDIA
- **Status:** GA (NBA 2K27 + RTX Spark laptops + GeForce NOW) · **Released:** 2026-10-16 · **Update**
- **Surface:** shipped game + new hardware platform (GeForce RTX 50 Series, RTX Spark laptops, GeForce NOW)
- **Primary source:** <https://www.nvidia.com/en-us/geforce/news/dlss-5-faster-ai-model-hogwarts-legacy-rtx-spark-laptops/> ; <https://www.nvidia.com/en-us/geforce/news/rtx-spark-dlss-reflex-ray-tracing-games/>
- **Underlying research:** no traceable paper (proprietary transformer-based upscaling model)
- **Availability:** Live since 2026-10-16 on GeForce RTX 50 Series GPUs, RTX Spark laptops (new Blackwell-GPU + Grace-CPU platform launched the same day), and GeForce NOW, for NBA 2K27. Hogwarts Legacy (2026-11-05) and Where Winds Meet ("late November 2026") are scheduled but not yet live — listed below as announced-only.

**What shipped:** Update since 2026-09-13 (last update 2026-10-13): NVIDIA shipped a 2X-faster, 24%-smaller (~118M-parameter) version of the DLSS 5 3D-Guided Neural Rendering model, live in NBA 2K27 (NVIDIA states up to a 1.4X frame-rate boost) on GeForce RTX 50 Series, the newly launched RTX Spark laptop platform, and GeForce NOW as of 2026-10-16.
**What research it translates:** Continues NVIDIA's transformer-based neural-rendering line underpinning DLSS 5; no separate academic paper was found for this specific speed/size optimization.
**Practical significance:** NVIDIA ties the model's first availability to the RTX Spark laptop launch (a new Blackwell-GPU + Grace-CPU Windows 11 platform shipping 2026-10-16 with preorders open).
**Engineering details:** Model shrunk to ~118M parameters for ~2X throughput; rollout is staged per game/platform rather than a single driver flag.
