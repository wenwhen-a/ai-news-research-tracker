**[B02] AMD Advanced Shader Delivery (ASD) State Object Compiler**
- **Company:** AMD (FLAG: borderline — comparable-standing company, not on the core tracked list)
- **Status:** GA · **Released:** 2026-10-01 · **New**
- **Surface:** engine/rendering developer tool (shader pipeline)
- **Primary source:** <https://gpuopen.com/news/asd-compiler-launch/>
- **Underlying research:** no traceable paper
- **Availability:** Free download via NuGet; runs on any x64 Windows PC/server (no GPU required) to compile; targets AMD RDNA–RDNA4 GPUs; end users need Windows 11 24H2+ or Xbox Gaming Services 37.113.11003.0+.

**What shipped:** AMD shipped a Direct3D 12 State Object Compiler plugin that converts a game's shader State Object Database (SODB) into a Precompiled Shader Database (PSDB) for Microsoft's Advanced Shader Delivery (ASD) system. Developers use it to pre-compile and test shader delivery locally before registering builds with a storefront.
**What research it translates:** No academic paper; this is a production engineering tool built against Microsoft's ASD platform feature to reduce shader-compilation stutter.
**Practical significance:** AMD states the tool aims to reduce first-launch shader-compile stutter on Radeon GPUs by letting studios pre-bake and validate shader delivery packages ahead of release.
**Engineering details:** Distributed via NuGet; the compiler itself needs no GPU; targets AMD RDNA through RDNA4 across recent Adrenalin driver versions; end-user requirement is Windows 11 24H2+ (or Xbox Gaming Services 37.113.11003.0+).
**Limitation / caveats:** Niche, developer-facing tooling rather than a consumer-facing feature; AMD does not use the word "GA" on the page itself.
