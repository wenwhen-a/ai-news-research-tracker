**[B02 · Update] Kling 4.0 — native 4K and HDR added to the video-generation API**
- **Company:** Kuaishou (Kling)
- **Status:** GA · **Released:** 2026-11-19 · **Update**
- **Surface:** Cloud API (video generation)
- **Primary source:** <https://kling.ai/document-api/updates/api.md>
- **Underlying research:** no traceable paper for this specific capability (a related system, Kling-Omni, has a technical report at arXiv:2512.16776, but it is not confirmed to be the same model generation as Kling 4.0)
- **Availability:** Kling 4.0 and Kling 4.0 Flash text-to-video, image-to-video and omni-reference-to-video API endpoints; `settings.resolution` now accepts `4k`; new `settings.dynamic_range` parameter enables HDR at 1080p or 4K; HDR adds a per-second fee.

**What shipped:** Update since 2026-10-15: Kling's API changelog (dated 2026-11-19) shows the Kling 4.0 video-generation API now actually supports 4K resolution and HDR output.
**What research it translates:** Kuaishou does not cite a specific new paper for this change; it is a capability/parameter extension of the already-shipped Kling 4.0 model rather than a new model generation.
**Practical significance:** Kuaishou's own API documentation states developers can now request native 4K and HDR output directly from the existing Kling 4.0 and Kling 4.0 Flash endpoints across text-to-video, image-to-video and omni-reference workflows.
**Engineering details:** Resolution is set via `settings.resolution: "4k"`; HDR is toggled via a new `settings.dynamic_range: "hdr"` parameter, available at the 1080p and 4K tiers; billing adds a per-second surcharge for HDR output.
**Limitation / caveats:** The changelog gives no latency figures or regional availability limits for the new tiers, and HDR playback requires HDR-capable display/decoding to show any benefit.
