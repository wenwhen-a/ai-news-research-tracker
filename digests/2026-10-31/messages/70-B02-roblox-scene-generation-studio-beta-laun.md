**[B02 · Update] Roblox Scene Generation — Studio Beta launch (update to the RDC 2026 "Scene Generator" announcement)**
- **Company:** Roblox
- **Status:** Public beta/preview (Studio Beta) · **Released:** 2026-10-30 · **Update**
- **Surface:** studio tool (Assistant `/generate_scene` command, or right-click viewport > Generate > Scene, in Roblox Studio)
- **Primary source:** <https://devforum.roblox.com/t/introducing-scene-generation-prototype-scenes-faster/4966611> (updates the previously logged key <https://about.roblox.com/newsroom/2026/09/rdc-2026-the-world-needs-more-play>, first_seen 2026-09-17, tier "Announced only")
- **Underlying research:** arXiv 2503.15475, "Cube: A Roblox View of 3D Intelligence" — the paper explicitly reports text-to-scene generation as an application of its shape tokenizer; not cited by name in this devforum post
- **Availability:** Free, Studio-only beta; no stated region restriction or waitlist

**Update since 2026-09-17: what changed.** Roblox's September 11 RDC 2026 announcement described Scene Generator only as something that "will power prompt-to-scene functionality across both Build and Studio" (tier: Announced only, no usable surface). On 2026-10-30, Roblox shipped it as a working Studio Beta feature — a genuine tier change from Announced-only to Public beta/preview, usable today by any opted-in developer with no waitlist.:** 
**What research it translates:** Cube's shape tokenizer (arXiv 2503.15475) is described by its authors as supporting "text-to-scene generation" directly, working with existing LLMs for scene analysis; Scene Generation's text/image-to-scene pipeline lines up with that capability, though this post does not name Cube explicitly.
