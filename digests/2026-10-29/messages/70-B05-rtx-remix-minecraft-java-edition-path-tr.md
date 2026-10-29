**[B05 · Update] RTX Remix — Minecraft: Java Edition path-tracing beta (update to RTX Remix 1.6.1)**
- **Company:** NVIDIA
- **Status:** GA (RTX Remix 1.6 release) / Public beta (the Minecraft integration specifically) · **Released:** 2026-10-28 · **Update**
- **Surface:** modding/rendering toolkit (RTX Remix) + consumer game (Minecraft: Java Edition)
- **Primary source:** <https://www.nvidia.com/en-us/geforce/news/remix-1-6-dlss-5-comfyui-2-0-minecraft-rtx-beta/>
- **Underlying research:** no traceable paper
- **Availability:** Minecraft: Java Edition 1.21.1 (Microsoft account required); Windows 10/11 x64 or ARM64; GeForce RTX 30-series+ (driver 616.92 WHQL+) or RTX Spark (driver 621.01 WHQL+); open-source beta, free

**Update since 2026-10-26: what changed.** This GeForce News writeup of the RTX Remix 1.6 release (the same release already logged on 2026-10-26 as RTX Remix 1.6.1 from GitHub) adds a flagship-game integration not previously reported in `product_seen.json`: an open-source beta that renders Minecraft: Java Edition with DLSS-accelerated full path tracing, RTX Dynamic Illumination, RTX Global Illumination, volumetric lighting, caustics, and subsurface scattering, plus a ComfyUI 2.0-based pipeline replacing RTX Remix's legacy AI texture/mesh generation tools, and Multi Frame Generation extended to "up to 6X.":** 
**What research it translates:** Not separately stated; builds on the same DLSS path-tracing/denoising and 3D-Guided Neural Rendering techniques already covered under the previously-logged DLSS 5 and DLSS 4.5 entries.
**Practical significance:** NVIDIA states the Minecraft beta ships with a sample world from Blockworks and an NVIDIA PBR materials pack, letting any Minecraft Java Edition player try path-traced rendering without installing a separate community mod.
