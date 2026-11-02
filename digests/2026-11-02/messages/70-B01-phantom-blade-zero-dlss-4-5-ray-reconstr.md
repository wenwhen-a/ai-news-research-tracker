**[B01] Phantom Blade Zero — DLSS 4.5 Ray Reconstruction & Path Tracing**
- **Company:** NVIDIA (feature shipped in S-GAME's Phantom Blade Zero)
- **Status:** GA · **Released:** 2026-10-28 · **New**
- **Surface:** Shipped game (Unreal Engine title) on GeForce RTX PCs/laptops and RTX Spark; GeForce Game Ready Driver
- **Primary source:** <https://www.nvidia.com/en-us/geforce/news/phantom-blade-zero-path-tracing-dlss-4-5-ray-reconstruction/>
- **Underlying research:** no traceable paper (NVIDIA has an internal technical write-up, "Technical Insights into DLSS 4: Multi Frame Generation and Transformer-Based Architectures," but it is not posted on arXiv)
- **Availability:** Free at launch for all owners on Steam/Epic Games Store; no separate paywall for the DLSS features; GeForce RTX and RTX Spark required for the path-tracing/DLSS 4.5 path

**What shipped:** NVIDIA states Phantom Blade Zero launched October 28, 2026 on GeForce RTX and RTX Spark with the full DLSS 4.5 feature set, including DLSS 4.5 Ray Reconstruction and Dynamic Multi Frame Generation (up to 6X).
**What research it translates:** Ray Reconstruction replaces NVIDIA's hand-tuned denoiser chain with a learned, transformer-based denoising network that infers a cleaner image directly from the raw ray-traced signal; the second-generation transformer (introduced with DLSS 4.5 in late August 2026, already tracked) processes more input data and parameters than the first-generation model at a similar compute budget.
**Practical significance:** NVIDIA states this is one of the highest-profile day-one AAA integrations of the complete DLSS 4.5 stack (Ray Reconstruction plus 6X frame generation) in a shipped, Unreal Engine-based action game rather than a tech demo.
**Engineering details:** The integration is engine-level: path tracing substitutes Unreal Engine's Lumen GI with NVIDIA's ReSTIR GI implementation rather than running alongside it.
