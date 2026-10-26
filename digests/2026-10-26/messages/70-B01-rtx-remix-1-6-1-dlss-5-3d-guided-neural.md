**[B01] RTX Remix 1.6.1 — DLSS 5 3D-Guided Neural Rendering in the modding toolkit**
- **Company:** NVIDIA
- **Status:** GA · **Released:** 2026-10-23 · **New**
- **Surface:** Studio tool / modding plugin (RTX Remix)
- **Primary source:** <https://github.com/NVIDIAGameWorks/rtx-remix/releases/tag/remix-1.6.1>
- **Underlying research:** no traceable paper
- **Availability:** Free download via GitHub; adds Windows-on-ARM (ARM64/ARM64EC) support with day-one Portal RTX, Half-Life 2 RTX Demo and RTX Remix for Minecraft (Beta); requires NVIDIA driver 616.92+; supersedes remix-1.5.2 (2026-06-16).

**What shipped:** NVIDIA shipped RTX Remix 1.6.1, bringing DLSS 5 with "3D-Guided Neural Rendering" and live artistic controls into the RTX Remix modding toolkit, alongside a beta Frame Generation performance preset, 5x/6x Multi Frame Generation, and ComfyUI 2.0 replacing the legacy AI texture/mesh generation tools.
**What research it translates:** This retrofits the DLSS 5 3D-Guided Neural Rendering model NVIDIA introduced for NBA 2K27 in September 2026 into classic-game remastering workflows; the release notes cite no separate research paper.
**Practical significance:** NVIDIA's release notes state modders can apply the same neural-rendering, ray-reconstruction and AI-asset-generation pipeline used in modern DLSS 5 titles to decades-old D3D8/9 games remastered through RTX Remix, including on Windows-on-ARM devices from day one.
**Engineering details:** The release adds global/per-material model-selection controls (Preset A/B/C) for the frame-generation and neural-rendering models, a compact-GBuffer sparse-rendering path paired with DLSS Ray Reconstruction, and OpenEXR texture/skybox support without an 8-bit intermediate conversion.
