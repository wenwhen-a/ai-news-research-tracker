**[B06] AMD FSR plugin for Unreal Engine 5.8**
- **Company:** AMD (FLAG: borderline per product-criteria.md)
- **Status:** GA · **Released:** 2026-08-27 · **New**
- **Surface:** Official Unreal Engine 5.8 plugin (FidelityFX integration)
- **Primary source:** <https://gpuopen.com/learn/amd-fsr-plugin-updated-for-unreal-engine-58/>
- **Underlying research:** no traceable paper
- **Availability:** Free, public Unreal Engine 5.8 plugin distributed via AMD's FidelityFX framework; bundles FSR Upscaling 4.1.1, FSR Frame Generation 4.0.1 and FSR Ray Regeneration 1.2. Supports AMD Radeon RX 9000 Series (RDNA 4) and, newly with this update, AMD Radeon RX 7000 Series (RDNA 3); older GPUs fall back to the non-ML FSR 3 analytical path. No waitlist; updates can also be pushed later via AMD Software: Adrenalin Edition without a game patch.

**What shipped:** AMD updated its official FidelityFX Super Resolution plugin for Unreal Engine 5.8, extending the ML-based FSR Upscaling 4.1.1 and Frame Generation 4.0.1 pipeline — previously RDNA4-only in-engine — to also run on RDNA 3 (Radeon RX 7000 Series) cards inside UE5.8 projects.
**What research it translates:** This packages AMD's existing FSR 4.1.1 ML upscaling and temporal frame-generation techniques (already shipped as the standalone FSR SDK 2.3, tracked separately, released 2026-06-24) directly into Epic's engine as a first-party plugin rather than requiring per-title custom integration.
**Practical significance:** Any Unreal Engine 5.8 developer can now enable ML-based FSR upscaling and frame generation for RDNA 3 GPU owners without writing custom FidelityFX integration code, lowering the bar for RDNA 3 (not just the newer RDNA 4) players to get AMD's AI upscaler in UE5.8 titles.
