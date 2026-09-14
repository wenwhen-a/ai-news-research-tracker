**[B03] RTX Remix 1.5**
- **Company:** NVIDIA
- **Status:** GA · **Released:** 2026-06-16 · **New**
- **Surface:** studio tool (free game-modding/remastering toolkit + runtime, distributed via GitHub/NVIDIA)
- **Primary source:** https://github.com/NVIDIAGameWorks/rtx-remix/releases/tag/remix-1.5.2 (official NVIDIAGameWorks repo; full changelog also at https://docs.omniverse.nvidia.com/kit/docs/rtx_remix/latest/docs/changelog/remix-releasenotes.html)
- **Underlying research:** no traceable paper (engineering release; builds on NVIDIA's existing RTX/neural-rendering stack, e.g. NRC)
- **Availability:** Free; Toolkit + Runtime components; Windows/D3D9 games; downloadable via GitHub releases and NVIDIA's RTX Remix site.

**What shipped:** NVIDIA shipped RTX Remix 1.5.2, adding "Remix Skills" — text-based context files that let AI coding agents act as collaborators to add features and bring previously-unsupported D3D9 titles into RTX Remix compatibility.
**What research it translates:** This is primarily a shipping-tool update rather than a direct paper-to-product translation; it packages NVIDIA's existing neural radiance caching (NRC) and RTX path-tracing/neural-rendering pipeline into modding tooling.
**Practical significance:** NVIDIA states RTXIO compression and packaging changes cut mod install sizes substantially (trade press reports up to ~37% smaller, and the Half-Life 2 RTX demo shrinking from roughly 80GB to 50GB).
**Engineering details:** Runtime adds GPU/CPU smooth normals, 32-bit index buffers, PointInstancer GPU culling (~2M objects), a Unity Y-axis clip-space rendering fix, and CJK/Cyrillic UTF-8 text handling; DebugView statistics overhead was cut from ~42ms to ~1ms at 4K.
**Limitation / caveats:** Applies only to Direct3D 9 titles (the RTX Remix scope), not modern engines or later D3D versions.
