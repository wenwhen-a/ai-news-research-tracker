**[B01] QSSR (Quick Spectral Super Resolution) on PS5**
- **Company:** Sony Interactive Entertainment (post authored by Daniel Craig, Principal Engineer, Graphics R&D, SIE)
- **Status:** GA · **Released:** 2026-10-01 · **New**
- **Surface:** Platform feature (console-level AI upscaler), shipped day-one in patches for two games
- **Primary source:** <https://blog.playstation.com/2026/10/01/ai-upscaling-is-coming-to-ps5/>
- **Underlying research:** no traceable paper
- **Availability:** Live now on base PS5 (not PS5 Pro) as an in-game graphics option; patched into Marvel's Wolverine and Ghost of Yōtei on 2026-10-01; free, no waitlist. Sony states it "will be offered broadly to all PlayStation developers" for future titles.

**What shipped:** Sony shipped QSSR, a new AI upscaler for the base (non-Pro) PS5, distinct from PSSR which remains the standard on PS5 Pro.
**What research it translates:** Sony states QSSR came out of Project Amethyst, SIE's ongoing machine-learning graphics research collaboration with AMD, using "a streamlined neural network architecture" and a "hand-tuned implementation" built for PS5's more limited compute budget relative to PS5 Pro.
**Practical significance:** Sony states QSSR brings "notable improvements to both image detail and image stability on PS5," and developers quoted in the post say it "adds more pixel-level clarity and stability" with temporal stability "that hasn't been possible on the PS5 console until now." It extends PSSR-class ML upscaling, previously PS5-Pro-exclusive, down to the much larger base-PS5 install base at no cost to players.
**Engineering details:** Delivered as a per-game, per-title integration (not an OS-level automatic toggle) via day-one patches to Marvel's Wolverine and Ghost of Yōtei; Sony did not disclose model size, inference cost, or hardware-level details beyond "streamlined" versus PSSR.
