**[B10] Unreal Engine 5.8 (MetaHuman Animator markerless capture, MetaHuman Collections, Mesh Terrain, MegaLights, MCP plugin)**
- **Company:** Epic Games
- **Status:** GA · **Released:** 2026-06-17 · **New**
- **Surface:** engine
- **Primary source:** https://forums.unrealengine.com/t/unreal-engine-5-8-released/2729274 (Epic staff announcement; the unrealengine.com news page returned HTTP 403 to fetch)
- **Underlying research:** no traceable paper
- **Availability:** "Download now on the Epic Games Launcher, GitHub, or our Linux page"; standard UE licensing.

**What shipped:** Epic states "MetaHuman Animator now supports markerless motion capture, enabling full-body and facial performance capture using something as simple as a single webcam"; MetaHuman Collections for scalable crowds; Mesh Terrain, "a new 3D mesh-based landscape system"; MegaLights "now Production-Ready"; a new MCP plugin that "connects LLMs directly to Unreal Engine"; and Lumen Lite.
**What research it translates:** Markerless video-based performance capture for MetaHuman characters and a production-ready many-light renderer.
**Practical significance:** Developers can capture body and face animation from a single webcam and light scenes with large numbers of dynamic shadowed lights, per Epic. Epic states Lumen Lite is "up to twice as fast as Lumen High Quality."
**Engineering details:** Hotfix 5.8.1 followed on 2026-07-28 with "over 260 fixes and updates" per Epic staff; 5.8.2 followed later.
**Limitation / caveats:** Mesh Terrain and MetaHuman Collections are labelled experimental in Epic's announcement; markerless capture quality is not quantified.
