**[B05 · Update] AMD FSR SDK 2.4 (FSR Upscaling 4.1.2 on RDNA 2, Vulkan parity, driver-assisted frame pacing)**
- **Company:** AMD
- **Status:** GA · **Released:** 2026-10-28 · **Update**
- **Surface:** SDK / engine plugin (cross-engine, cross-API)
- **Primary source:** <https://gpuopen.com/manuals/fsr_sdk/whats-new/>
- **Underlying research:** No traceable paper.
- **Availability:** Free, available now via GitHub (precompiled binaries plus limited source) and GPUOpen; DirectX 12 and (new) Vulkan.

**What shipped:** Update since 2026-09-13: AMD's FSR SDK moved from 2.3 to 2.4, extending full-INT8 AI model support for FSR Upscaling 4.1.2 down to Radeon RX 6000 (RDNA 2) discrete GPUs, and bringing several FSR effects to feature parity on Vulkan alongside DirectX 12. It also adds Driver-Assisted Frame Pacing, limited to RX 9000-series GPUs and newer.
**What research it translates:** AMD has not published the underlying model architecture as a paper; GPUOpen's own documentation describes the SDK as a packaging of AMD's existing "Redstone" ML upscaling and frame-generation models.
**Practical significance:** AMD states this gives RX 6000-series owners access to the full-quality INT8 model, and gives Vulkan-based titles the same FSR 4 feature set as DirectX 12 games. Ray Regeneration and Radiance Caching remain DirectX-12-only and RDNA 4+-only.
**Engineering details:** The SDK ships as precompiled binaries plus limited source code on AMD's GitHub repository.
**Limitation / caveats:** Driver-Assisted Frame Pacing is gated to RX 9000-series-and-newer hardware only. No independent benchmarks of the RX 6000 full-INT8 model's performance impact were found.
