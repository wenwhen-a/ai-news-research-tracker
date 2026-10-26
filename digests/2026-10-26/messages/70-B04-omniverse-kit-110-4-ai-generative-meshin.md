**[B04] Omniverse Kit 110.4 — AI generative meshing from point clouds**
- **Company:** NVIDIA
- **Status:** GA · **Released:** 2026-10 · **New**
- **Surface:** Engine/SDK (Omniverse Kit, underlying Isaac Sim, USD Composer and other Omniverse apps)
- **Primary source:** <https://docs.omniverse.nvidia.com/dev-guide/latest/release-notes/110_4_highlights.html>
- **Underlying research:** no traceable paper
- **Availability:** GA, free; ships as the Kit SDK bundled into Isaac Sim 6.2.0 and other Omniverse applications; supersedes Kit 110.3 (2026-08-16).

**What shipped:** NVIDIA shipped Omniverse Kit 110.4 with a new "generative meshing" feature that uses AI models to turn point-cloud regions into textured 3D meshes, plus GPU-accelerated point-cloud-to-mesh conversion and DeepStream-powered GPU video textures (including RTSP streams, usable on Dome Lights).
**What research it translates:** This extends point-cloud-to-mesh AI reconstruction — in the same family as the "3D Object Reconstruction" framework NVIDIA introduced via Isaac Sim 6.1 for turning stereo video of real objects into textured USD assets — into a general Kit-level feature; the release notes name no specific paper.
**Practical significance:** NVIDIA states the feature lets developers convert scanned/point-cloud data directly into textured, simulation-ready meshes inside the same tool used across Isaac Sim, USD Composer and other Omniverse apps, aimed at robotics and digital-twin asset pipelines.
**Engineering details:** A new public Storage and Authentication API supports custom backends for the point-cloud workflow; OpenUSD is upgraded to 25.11; RTX Real-Time 2.0 scene partitioning now supports up to 32K indices (16,384 environments), and MDL materials now work inside USDZ packages.
