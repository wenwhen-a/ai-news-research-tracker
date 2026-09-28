# Part B — Research → Product: Western big tech + publishers
Window: 2026-06-30 to 2026-09-28 (today 2026-09-28 UTC)
Scope: Google/DeepMind, Microsoft, Meta, Amazon, Apple, Sony, Ubisoft, Electronic Arts
Topics: 3D generation, world models, character animation, game engines/tooling

## Summary of findings
No genuinely new GA or Public-beta items were verified for this company group in the 90-day window beyond what is already recorded in `state/product_seen.json` (which already covers, for this group: Apple RealityKit Gaussian Splatting + Reality Composer Pro 3 [visionOS 27, 2026-09-14], Sony PSSR in Doom: The Dark Ages [2026-07-07], and EA Markerless Motion Capture / EA Create Capture [2026-08-07]). Those are **previously reported** and were not re-verified in depth per instructions.

One new **Announced-only** item qualified: Meta's "Hologram" photorealistic avatar feature, unveiled at Meta Connect on 2026-09-23.

No new qualifying items were found for Google/DeepMind, Microsoft, Amazon, or Ubisoft in this window on the 4 tracked topics. See "Near-misses / excluded leads" below for what was checked and why each was excluded.

## Previously reported (from product_seen.json, this company group — not re-verified)
- Apple — RealityKit Gaussian Splatting support (visionOS 27) — https://developer.apple.com/visionos/whats-new/ — GA, 2026-09-14
- Apple — Reality Composer Pro 3 ("Reality Composer Pro Assistant") — https://developer.apple.com/reality-composer-pro/ — GA, 2026-09-14
- Sony (platform feature; post authored by id Software) — Upgraded PSSR in Doom: The Dark Ages on PS5 Pro — https://blog.playstation.com/2026/06/24/upgraded-pssr-comes-to-doom-the-dark-ages-on-ps5-pro/ — GA, 2026-07-07
- Electronic Arts — Markerless Motion Capture (EA Create Capture) — https://www.ea.com/news/ea-markerless-motion-capture — GA (internal studio tool), 2026-08-07
- No status-tier changes or clear new versions observed on any of the above during this run.

---

## Google / DeepMind
No new qualifying GA/beta or announced-only items found in the window. Checked: deepmind.google/discover/blog, blog.google (Gemini app), developers.googleblog.com, Android XR developer blog, Vertex AI / AI Studio release notes.

- Gemini app "Generate 3D models and interactive charts" — https://blog.google/innovation-and-ai/products/gemini-app/3d-models-charts/ — published 2026-04-09, **outside the 90-day window**; also primarily interactive WebGL simulations/charts rather than 3D-asset generation. Excluded.
- Project Genie / Genie 3 — launched 2026-01-29; Street View integration at Google I/O 2026 (~May) — both outside window; Genie 3 has no public API as of 2026-09 (Google AI Ultra subscription only, unchanged this window). Excluded.
- Veo 3.1 — released 2025-10-15, outside window. No Veo update found dated within the window.
- Android XR "Tooling, Engine Support, and Ecosystem Updates" (Unreal/Godot support, Engine Hub) — https://android-developers.googleblog.com/2026/06/what-is-new-android-xr.html — published 2026-06-15, **outside the 90-day window** (window starts 2026-06-30). No qualifying successor post found within the window.

## Microsoft
No new qualifying GA/beta or announced-only items found in the window. Checked: microsoft.com/en-us/research/blog, developer.microsoft.com/en-us/games/blog, Xbox Wire, Azure AI Foundry model catalog.

- Xbox Gaming Copilot — expanding to current-gen Xbox consoles "later in 2026" (per GDC 2026 panel coverage) — not clearly on any of the 4 tracked topics (it is a gameplay-assistant/chat feature, not 3D generation, world model, character animation, or engine tooling). Excluded as off-topic.
- Muse (WHAM) — published in Nature May 2026; no new product surface (game, app, API) found shipping in this window. Still a research model without a customer-facing product. Excluded.
- Microsoft Research publication "Animate Any Character in Any World" — a research paper, not a product surface; belongs in Part A, not here.

## Meta
### Announced only (not yet usable)
- **Hologram** (photorealistic real-time avatar for calls, formerly "Codec Avatars") · Meta · announced 2026-09-23 at Meta Connect · sources: https://about.fb.com/news/2026/09/new-features-for-meta-ray-ban-display-navigation-hologram/ and https://www.meta.com/blog/meta-connect-2026-everything-we-announced/ — Meta states Hologram "begins rolling out in Early Access on WhatsApp to Meta Ray-Ban Display users in the US later this fall" and "will be available on Meta VR Glasses when they launch next spring [2027]." Not usable by any customer today, so Announced-only per the criteria test. No underlying paper is cited by Meta's announcement; the closest topical match found via arXiv/company-lab search is Meta's own Codec Avatars Lab paper "Audio Driven Real-Time Facial Animation for Social Telepresence" (arXiv:2510.01176, SIGGRAPH Asia 2025, Lee et al., Codec Avatars Lab @ Meta + Seoul National University), which describes real-time audio-driven photorealistic 3D facial-avatar animation matching Hologram's described mechanism ("infers your expression from what you're saying and how you're saying it") — flagged as an inferred match, not an explicit citation.

No other new Meta items qualified. Checked and excluded as **not new** (all predate the window): Horizon Worlds Mesh/Texture Generation (2025-04-14), Horizon Worlds Environment Generation + embodied LLM NPCs (2025-08-27).

## Amazon
No new qualifying items found in the window on any of the 4 topics. Checked: aws.amazon.com/blogs/gametech (all July–September 2026 posts reviewed — Perforce storage, GameLift Streams/Servers, DDoS protection, Kubernetes migration, agentic infra/cheat-detection; none touch 3D generation, world models, character animation, or engine tooling), amazon.science/blog, Amazon Bedrock/Nova model catalog (Nova Reel/Canvas/Sonic — no 3D-asset or world-model additions found in-window).
- Near-miss (out of window, and not a product): "Open source 3D game asset generation using AWS" — https://aws.amazon.com/blogs/gametech/open-source-3d-game-asset-generation-using-aws/ — published 2026-06-11, before the window, and the post itself states it is "focused on testing the quality of assets and experimentation, rather than on creating production-ready assets," built on open-source models (TripoSG, MV-Adapter) run on customer-owned EC2 — a tutorial/guidance post, not an AWS product/service. Would not qualify as Part B even if in-window.

## Apple
No new items beyond what's already in `product_seen.json` (RealityKit Gaussian Splatting, Reality Composer Pro 3, both visionOS 27 / 2026-09-14, previously reported). Confirmed these trace to the June 2026 WWDC26 sessions but shipped at GA with visionOS 27 in September, matching the existing record; no additional Apple product surface found in the window.

## Sony
No new qualifying items in the window. Checked: blog.playstation.com, ai.sony, sie.com/en/blog, XYN (mocopi) product pages.
- Near-miss (out of window): "Mockingbird" internal AI facial-animation tool (performance-capture-to-3D-facial-animation), disclosed by Sony as part of a PlayStation Studios AI strategy briefing around 2026-05-11/13 and used in Horizon Zero Dawn Remastered — announcement predates the 90-day window (window starts 2026-06-30) and no primary Sony blog/newsroom post (only secondary press coverage) was found; would need a primary source (e.g., a PlayStation Blog or investor-relations post) to verify even retroactively. Flagged for a future run if a primary Sony source surfaces.
- mocopi Receiver Plugin for 3ds Max — open-sourced September 2026 — excluded per Part B rules (open-source code drops belong in Part A, not Part B).
- mocopi Pro Kit — shipped 2025, no in-window update found.

## Ubisoft
No new qualifying GA/beta items in the window. Checked: news.ubisoft.com, ubisoft.com/en-us/studio/laforge.
- Near-miss: **Teammates** (GenAI NPC R&D prototype, built on Snowdrop engine + Google Gemini + in-house middleware) — first revealed 2025-11-21, shown again at GDC 2026 (~March 2026) — both outside the 90-day window, and it remains an internal R&D experiment with "no plans to implement it into its pipeline in the near future" — would be Announced-only even if in-window.
- Near-miss: **Assassin's Creed Black Flag Resynced** (Ubisoft Singapore, Anvil engine, released 2026-07-09 — within window) — a full engine rebuild with "modern motion capture technology" for Kenway's facial animation and refined movement animation. Excluded: Ubisoft's own coverage (Xbox Wire "What's New" post, ubisoft.com product page) describes conventional performance-capture and hand-tuned animation work, not a named AI/ML method or research-derived technique, so it does not clearly meet the "research → product" bar despite being a shipped, in-window title with animation improvements.
- Ubisoft "Smart Intel" (personalized player tips in Ubisoft Connect) — not on any of the 4 tracked topics. Excluded as off-topic.

## Electronic Arts
No new qualifying items beyond the already-recorded EA Create Capture entry. Checked: ea.com/news, ea.com/seed/news, ea.com/seed/publications.
- EA SPORTS UFC 6 (shipped 2026-06-19, just before the window) and EA SPORTS FC — both use markerless motion capture, which is the same EA Create Capture initiative already recorded in `product_seen.json` (2026-08-07). No separate new item.
- EA SEED's GDC Festival of Gaming 2026 talk on "stabilizing facial motion for photo-real avatars" traces to the pre-existing SEED research paper "A Theory of Stabilization by Skull Carving" (SIGGRAPH Asia 2024 / arXiv:2411.05827) — a research presentation, not a new product surface. Excluded (Part A territory, and not new).
- Texture Sets (EA Motive/SEED) — released on GitHub as open source — excluded per Part B rules (open-source drops belong in Part A).

---

## Announced only (not yet usable) — consolidated
- Hologram (photorealistic avatar) · Meta · 2026-09-23 · https://about.fb.com/news/2026/09/new-features-for-meta-ray-ban-display-navigation-hologram/

## Near-misses (consolidated)
- AWS "Open source 3D game asset generation" blog tutorial (open-source models on customer EC2, not an AWS product; also pre-window).
- Sony "Mockingbird" AI facial-animation tool (pre-window disclosure; no primary Sony source located, only secondary press).
- Ubisoft "Teammates" GenAI NPC R&D prototype (pre-window; still an internal experiment, not shipped).
- Ubisoft "Assassin's Creed Black Flag Resynced" animation/engine rebuild (in-window, shipped, but conventional mocap — no clear AI-research linkage).
- EA SEED facial-stabilization research talk at GDC 2026 (research presentation of a 2024 paper, not a new product).

## Coverage gaps worth flagging
- Amazon continues to have very little activity on these 4 topics through its official primary sources; AWS for Games blog in this window skewed entirely toward game-server infrastructure (GameLift, DDoS, storage), not generative 3D/animation/world-model features.
- Microsoft's Xbox/Muse world-model research has not surfaced in any new customer-facing product or game since the Nature publication; Gaming Copilot's console rollout, while notable, falls outside this tracker's 4 topics.
- Sony's "Mockingbird" internal tool is a credible lead but currently only sourced from secondary press; worth re-checking PlayStation Blog / investor materials for a primary citation in a future run.
