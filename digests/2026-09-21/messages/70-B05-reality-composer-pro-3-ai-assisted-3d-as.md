**[B05] Reality Composer Pro 3 — AI-assisted 3D asset generation ("Reality Composer Pro Assistant")**
- **Company:** Apple
- **Status:** GA · **Released:** 2026-09-14 (previewed as beta from WWDC26, June 2026) · **New**
- **Surface:** Studio/authoring tool (standalone macOS app, no longer bundled inside Xcode)
- **Primary source:** <https://developer.apple.com/reality-composer-pro/> ; <https://developer.apple.com/documentation/realitycomposerpro/working-with-the-reality-composer-pro-assistant> ; <https://www.apple.com/newsroom/2026/06/apple-aids-app-development-with-new-intelligence-frameworks-and-advanced-tools/>
- **Underlying research:** no traceable paper — Apple has not disclosed the generative model(s) behind the Assistant's 3D object/material generation (Apple has published adjacent research, e.g. "DSplats: 3D Generation by Denoising Splats-Based Multiview Diffusion Models," but no confirmed link to this shipping feature)
- **Availability:** Free download for Apple developers, standalone app (previously bundled in Xcode). Requires macOS 26.5+. Builds content for visionOS and iOS apps.

**What shipped:** Reality Composer Pro 3 shipped as a standalone Mac app with a built-in "Reality Composer Pro Assistant" panel that takes natural-language prompts and generates 3D objects and materials directly inside the 3D scene editor, plus new node-based Animation Graph and Script Graph tools for character/interaction logic.
**What research it translates:** It packages text-to-3D-asset generative AI as an in-editor authoring feature, following the broader industry shift toward prompt-driven 3D content creation.
**Practical significance:** Apple states the tool is meant to "close the gap between idea and experience" for designers and engineers building spatial apps, letting non-specialists generate placeholder or usable 3D objects/materials from a prompt without leaving the editor.
