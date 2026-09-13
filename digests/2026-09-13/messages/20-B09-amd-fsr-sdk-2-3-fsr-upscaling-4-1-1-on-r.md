**[B09] AMD FSR SDK 2.3 — FSR Upscaling 4.1.1 on RDNA 3**
- **Company:** AMD — FLAG: not on the tracked list; comparable GPU vendor, included for the reader to judge
- **Status:** GA · **Released:** 2026-06-24 · **New**
- **Surface:** SDK
- **Primary source:** https://gpuopen.com/learn/amd-fsr-sdk-2-3-blog/
- **Underlying research:** no traceable paper
- **Availability:** AMD states "AMD FSR SDK 2.3 binaries and limited source are now available on GitHub"; ML-based FSR Upscaling 4.1.1 now supports Radeon RX 7000 Series (RDNA 3) discrete GPUs.

**What shipped:** SDK bundling FSR Upscaling 4.1.1, FSR Frame Generation 4.0.1 and FSR Ray Regeneration 1.2.0, extending the ML upscaler from RDNA 4 to RDNA 3 cards.
**What research it translates:** AMD's machine-learning upscaling model family made available to a previous GPU generation.
**Practical significance:** AMD states RDNA 3 owners get "image quality that closely matches what is already available on" RDNA 4, once developers integrate the SDK.
**Engineering details:** Frame Generation and Ray Regeneration remain "AMD Radeon RX 9000 Series GPUs and above" with analytical fallbacks for older hardware; distributed as binaries plus limited source.
**Limitation / caveats:** Requires per-game integration by developers; AMD gives no numeric performance metrics; RDNA 2 not included.
