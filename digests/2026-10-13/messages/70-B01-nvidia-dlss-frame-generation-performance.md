**[B01] NVIDIA DLSS Frame Generation Performance Mode ("Preset C")**
- **Company:** NVIDIA
- **Status:** Public beta/preview · **Released:** 2026-10-13 · **New**
- **Surface:** NVIDIA App (GPU driver / RTX graphics stack feature used across DLSS-enabled games)
- **Primary source:** <https://www.nvidia.com/en-us/geforce/news/dlss-4-5-crossout-remastered-modern-warfare-4-frame-gen-beta/>
- **Underlying research:** no traceable paper
- **Availability:** Opt-in beta via the NVIDIA App (enable beta features in Settings > About, install the beta app update, then select "Preset C" under Graphics > Driver Settings > DLSS Override - Model Presets > Frame Generation). Supported on GeForce RTX 40 Series, RTX 50 Series GPUs, and RTX Spark laptops. Not GA.

**What shipped:** NVIDIA shipped a new, faster "Performance Mode" (internally Preset C) for DLSS Frame Generation, Multi Frame Generation, and Dynamic Multi Frame Generation, available as an opt-in preset inside an NVIDIA App beta update released October 13, 2026. NVIDIA states it is up to 35% faster than the standard preset on a GeForce RTX 5060.
**What research it translates:** NVIDIA states the mode replaces the second AI model in the Frame Generation pipeline — the one that computes optical flow for elements such as UI and ray-traced effects — with a lighter algorithm.
**Practical significance:** NVIDIA states the preset trades "minor image quality" for a meaningful frame-rate gain, giving players on RTX 40/50 Series cards and RTX Spark laptops a faster frame-generation option without needing new hardware.
**Engineering details:** NVIDIA describes the swap as substituting the optical-flow sub-model used for UI/ray-traced-effect motion estimation with a lighter-weight algorithm, while keeping the primary frame-generation model unchanged.
