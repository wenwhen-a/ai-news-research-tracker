**[B04] RealityKit Gaussian Splatting support (visionOS 27)**
- **Company:** Apple
- **Status:** GA · **Released:** 2026-09-14 · **New**
- **Surface:** Engine/rendering API (RealityKit, part of visionOS 27 / Xcode 27 SDK)
- **Primary source:** <https://developer.apple.com/visionos/whats-new/> ; API reference <https://developer.apple.com/documentation/realitykit/gaussiansplatcomponent>
- **Underlying research:** "3D Gaussian Splatting for Real-Time Radiance Field Rendering" (Kerbl, Kopanas, Leimkühler, Drettakis, SIGGRAPH 2023, arXiv:2308.04079) — the general technique; not an Apple-authored paper, RealityKit is a renderer implementation for it
- **Availability:** Ships with visionOS 27 and Xcode 27; free SDK feature for all registered Apple developers, no waitlist. Previewed to developers at WWDC26 (June 2026, session 279) as beta, reached GA with the public visionOS 27 release.

**What shipped:** RealityKit in visionOS 27 gained native rendering support for 3D Gaussian Splats via a new `GaussianSplatComponent`/`GaussianSplatResource` API, so apps can place photorealistic scanned/reconstructed scenes and objects directly into spatial experiences.
**What research it translates:** Gaussian Splatting (Kerbl et al. 2023) replaced NeRF-style volumetric rendering with an explicit, GPU-rasterizable point-based radiance-field representation that renders in real time.
**Practical significance:** Apple states this "enables you to incorporate photorealistic scans of real-world objects into your virtual experiences," letting visionOS developers use captured/reconstructed 3D content without hand-rolling a splat renderer.
**Engineering details:** New APIs: `GaussianSplatResource`, `GaussianSplatResource.BufferResource`, `GaussianSplatComponent`.
**Limitation / caveats:** No first-party splat file format or capture pipeline — developers must source/parse splat data themselves.
