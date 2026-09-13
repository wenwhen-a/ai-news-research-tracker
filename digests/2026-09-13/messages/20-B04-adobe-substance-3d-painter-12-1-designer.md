**[B04] Adobe Substance 3D Painter 12.1, Designer 16 and Sampler update (OpenPBR)**
- **Company:** Adobe
- **Status:** GA · **Released:** 2026-07-21 · **New**
- **Surface:** studio tool
- **Primary source:** https://blog.adobe.com/en/publish/2026/07/21/adobe-substance-3d-unveils-new-innovations-deliver-faster-workflows-openpbr-everywhere-digital-twins-scale
- **Underlying research:** no traceable paper
- **Availability:** Substance 3D Collection desktop apps; Adobe states it released its "production-proven OpenPBR implementation as open source on GitHub."

**What shipped:** Adobe states Painter 12.1 adds Skew Map Painting, Auto Rebake (rebakes only affected mesh portions), a Hard Surface Auto UV mode and OpenPBR support; Designer 16 adds a Shape Splatter v2 node, Signed Distance Field nodes, a 3D Viewer node and new displacement controls; Sampler adds Material Creation Templates.
**What research it translates:** Adoption of the open OpenPBR shading model across the texturing pipeline, plus procedural-geometry (SDF) authoring inside Designer.
**Practical significance:** Adobe states the Assets library now holds 23,516 assets and that "14,000+ materials, decals, and atlases are being converted to OpenPBR," giving artists a portable material standard across tools.
**Engineering details:** OpenPBR supported end to end from Sampler through Painter; SDF and 3D Viewer nodes in Designer 16; open-source OpenPBR implementation on GitHub.
**Limitation / caveats:** No generative (Firefly) 3D features are mentioned in this release (observed, not stated). Pricing and subscription terms are not stated in the post.
