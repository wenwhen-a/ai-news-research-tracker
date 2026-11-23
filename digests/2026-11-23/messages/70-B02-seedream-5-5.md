**[B02] Seedream 5.5**
- **Company:** ByteDance
- **Status:** GA · **Released:** 2026-11-09 · **New**
- **Surface:** Consumer apps (Dreamina/即梦, Doubao) + cloud API (Volcano Engine Ark / BytePlus)
- **Primary source:** <https://seed.bytedance.com/blog/more-realistic-images-more-stable-editing-across-100-rounds-introducing-seedream-5-5>
- **Underlying research:** no traceable paper (prior generations have arXiv technical reports — e.g. "Seedream 4.0: Toward Next-generation Multimodal Image Generation" — but no 5.5-specific report was found on the launch page)
- **Availability:** ByteDance's own Seed blog/product page offers access via the "Dola" chat app and the BytePlus Playground, plus a "Get API" and an "Enterprise" path; no resolution tiers or pricing are stated on the primary page itself.

**What shipped:** ByteDance's Seed team shipped Seedream 5.5, a new image generation/editing model, on 2026-11-09, reachable today through ByteDance's own Dola app, the BytePlus Playground, and a developer API/enterprise path.
**What research it translates:** ByteDance states the model improves multi-turn edit stability and adds native transparent (RGBA) output, extending the Seedream image-generation line whose earlier generations (3.0, 4.0) were documented in ByteDance's own arXiv technical reports.
**Practical significance:** ByteDance states that unedited regions of an image stay pixel-level stable across up to 100 successive edit rounds, aimed at iterative production work (e.g., e-commerce, marketing, game-asset, and fashion imagery) where earlier models would drift after a few edits.
**Engineering details:** The primary page highlights three capability pillars — multi-turn editing with pixel-level preservation, native RGBA transparent-background generation, and more naturalistic lighting/material/skin rendering — but gives no architecture, parameter-count, or resolution-ceiling details.
