# Part B — Research → Product
Window: last 90 days (2026-06-22 to 2026-09-20). Qualifying products: 14 (1 new, 13 previously reported, 0 flagged). Announced-only (new): 0. Open releases moved to Part A: 0.

---
## 007 First Light — Path Tracing & DLSS 4.5 Ray Reconstruction Update
- **Company:** NVIDIA (feature shipped in IO Interactive's 007 First Light)
- **Status:** GA · **Released:** 2026-09-15 · **New**
- **Surface:** shipped game (PC, GeForce RTX) / GeForce NOW
- **Primary source:** https://www.nvidia.com/en-us/geforce/news/007-first-light-path-tracing-dlss-4-5-ray-reconstruction-update-out-now/
- **Underlying research:** no traceable paper
- **Availability:** Free update for existing owners of 007 First Light on PC with GeForce RTX 50-series GPUs (RTX 5090 down to RTX 5070 given as reference tiers); also playable via GeForce NOW Ultimate membership without local RTX hardware.

**What shipped (≤3 sentences):** NVIDIA and developer IO Interactive shipped a free update adding path tracing plus DLSS 4.5 Ray Reconstruction to 007 First Light. The update also carries forward existing DLSS Super Resolution and Dynamic Multi Frame Generation support.
**What research it translates (≤3 sentences):** No specific arXiv paper is cited by the primary source for this update; DLSS Ray Reconstruction builds on NVIDIA's broader, previously-announced neural denoising/reconstruction research line, but this release does not name a new paper.
**Practical significance (≤3 sentences):** NVIDIA states the update gives the game "extra-detailed lighting, shadows and reflections," with path tracing enabling more accurate ambient occlusion and global illumination; players without qualifying RTX hardware can access the visuals via GeForce NOW streaming instead.
**Engineering details (≤3 sentences):** NVIDIA's reference performance tiers list RTX 5090 for 1440p High, RTX 5080 for 1440p Medium, RTX 5070 Ti for 1080p High, and RTX 5070 for 1080p Medium; NVIDIA recommends the latest Game Ready Driver for the update.
**Limitation / caveats (≤3 sentences):** Full local path-traced performance is restricted to GeForce RTX 50-series GPUs per NVIDIA's stated reference tiers; no cross-platform (console) availability is mentioned in the primary source.

### Previously reported (still in window)
- NVIDIA DLSS 5 with 3D-Guided Neural Rendering (in NBA 2K27) · NVIDIA · GA · Released 2026-09-03 · https://www.nvidia.com/en-us/geforce/news/dlss-5-3d-guided-neural-rendering/
- HappyOyster 1.0 "Adventure" mode (happyoyster-1.0-adventure) via Alibaba Cloud Model Studio Open API · Alibaba (ATH Innovation Business Group / Bailian) · GA · Released 2026-09-17 · https://help.aliyun.com/zh/model-studio/newly-released-models
- Roblox Scene Generator (prompt-to-scene for Build & Studio) · Roblox · Announced only · Released 2026-09-11 · https://about.roblox.com/newsroom/2026/09/rdc-2026-the-world-needs-more-play
- RDC 2026 roadmap items — NPC Dynamic Behavior, New Default Movement, Silhouette-preserving Layered Clothing · Roblox · Announced only · Released 2026-09-12 · https://devforum.roblox.com/t/rdc26-what-we-announced/4865880
- Markerless Motion Capture (EA Create Capture) · Electronic Arts · GA (internal studio tool) · Released 2026-08-07 · https://www.ea.com/news/ea-markerless-motion-capture
- NVIDIA DLSS 4.5 Ray Reconstruction, 2nd-generation transformer model · NVIDIA · Public beta/preview (NVIDIA App early access) · Released 2026-08-25 · (see state/product_seen.json)
- Autodesk 3ds Max 2027.2 — native 3D Gaussian Splat support · Autodesk · GA · Released 2026-07-22 · (see state/product_seen.json)
- Adobe Substance 3D Painter 12.1, Designer 16 and Sampler updates · Adobe · GA · Released 2026-07-21 · (see state/product_seen.json)
- Fortnite / UEFN v41.20 — Control Rig for Sidekicks, in-world features · Epic Games · GA · Released 2026-07-16 · (see state/product_seen.json)
- Roblox Build — mobile AI creation tab (public alpha, New Zealand) · Roblox · Public beta/preview (public alpha) · Released 2026-07-28 · (see state/product_seen.json)
- Upgraded PSSR in Doom: The Dark Ages on PS5 Pro (Free Update) · Sony Interactive Entertainment · GA · Released 2026-07-07 · (see state/product_seen.json)
- 《逆水寒：新世界》 (Justice Online: New World) character rendering update · NetEase · GA · Released 2026-06-26 · (see state/product_seen.json)
- AMD FSR SDK 2.3 — FSR Upscaling 4.1.1 on RDNA 3 · AMD · GA · Released 2026-06-24 · (see state/product_seen.json)

### Announced only (not yet usable)
(none new this run)

Near-misses: none this run.

Verification: This was a light daily check (not the Monday full sweep) of ~10 primary surfaces — NVIDIA developer blog, GeForce news, Unreal Engine news, Unity blog, Roblox newsroom, Adobe blog, Tencent Hunyuan, ByteDance Seed, Alibaba Model Studio release notes, Kling AI, and PlayStation Blog — for items dated in the last 7 days on the four tracked topics. Only the NVIDIA GeForce item above was independently fetched and confirmed against its own primary-source page (release date, platforms, features, hardware tiers). Unreal Engine's release-notes page and Kling AI's site returned no fetchable dated content (JS-rendered pages); Unity, Adobe, Roblox, Tencent Hunyuan, ByteDance Seed, and Alibaba Model Studio showed no new qualifying items in the window as of this check. Products already in state/product_seen.json were not re-verified; the 13 above remain inside the 90-day window (cutoff 2026-06-22) and are listed compactly per the incremental-tracking rule. Four older entries (Unreal Engine 5.8, HappyOyster 1.0 original release, NVIDIA ACE Game Agent SDK, RTX Remix 1.5.2 — all released 2026-06-16/17) have aged out of the 90-day window and are omitted from this list, though they remain in state/product_seen.json for dedup purposes.
