**[B01] Gears of War: E-Day — DLSS 4.5 and RTX Mega Geometry (first shipped game)**
- **Company:** NVIDIA (feature shipped in The Coalition's *Gears of War: E-Day*, published by Xbox Game Studios)
- **Status:** GA · **Released:** 2026-10-01 · **New**
- **Surface:** shipped game (PC, GeForce RTX + GeForce NOW)
- **Primary source:** <https://www.nvidia.com/en-us/geforce/news/gears-of-war-e-day-dlss-4-5-ray-tracing-rtx-mega-geometry/>
- **Underlying research:** no traceable paper (NVIDIA documents RTX Mega Geometry via its developer blog, SIGGRAPH/GDC talks and OptiX samples, not an arXiv publication)
- **Availability:** Premium Edition early access from October 1, 2026; general release October 6, 2026. Playable on GeForce RTX PCs/laptops and GeForce NOW. Full DLSS 4.5 feature set requires GeForce RTX hardware; 6X Frame Generation requires an RTX 50-series GPU.

**What shipped:** NVIDIA states *Gears of War: E-Day* is the first shipped game to support RTX Mega Geometry, which lets the game ray-trace its full-detail Unreal Engine 5 Nanite geometry (foliage, debris, rubble) instead of a separate simplified proxy mesh used for acceleration structures.
**What research it translates:** NVIDIA's blog post attributes RTX Mega Geometry to "6 years of research and development" on ray-tracing acceleration structures for extremely dense, Nanite-style clustered geometry (the Cluster Acceleration Structure/CLAS approach NVIDIA has described in prior developer-blog and SIGGRAPH/GDC material).
**Practical significance:** NVIDIA states this removes a long-standing limitation where ray-traced Nanite scenes needed a lower-detail proxy mesh for the acceleration structure, which caused shadow/reflection flicker and detail loss as geometry moved or changed.
