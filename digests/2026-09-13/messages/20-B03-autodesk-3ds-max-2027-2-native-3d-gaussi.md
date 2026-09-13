**[B03] Autodesk 3ds Max 2027.2 — native 3D Gaussian Splat support**
- **Company:** Autodesk — FLAG: not on the tracked list; comparable DCC vendor, included for the reader to judge
- **Status:** GA · **Released:** 2026-07-22 per trade press (CG Channel, 80.lv, CGPress); Autodesk's own pages are undated — FLAG · **New**
- **Surface:** studio tool (DCC application)
- **Primary source:** https://help.autodesk.com/cloudhelp/2027/ENU/3dsMax-WhatsNew/files/GUID-D11D1F34-C9FF-4981-AAE3-5A969986FCF4.html
- **Underlying research:** no traceable paper (Autodesk does not cite the 3DGS literature on the page)
- **Availability:** Included in the 3ds Max 2027.2 update for subscribers; Arnold for 3ds Max (MAXtoA) 5.9.3.0 bundled.

**What shipped:** Autodesk states "New 3D Gaussian Splat (3DGS) support in 3ds Max 2027.2 provides fast rendering, simple editing, and hyper-accurate output," with a new point object type and point-data modifiers to "edit 3DGS data or create point data from scratch." Arnold "now works with native 3ds Max 3DGS data."
**What research it translates:** Gaussian-splat radiance-field captures become a native, editable asset type in a mainstream DCC tool.
**Practical significance:** 3ds Max users can import, edit with standard modifiers, and render splat captures in Arnold without third-party plugins, per Autodesk.
**Engineering details:** New Points object type and Point Instance modifier (also usable for render-time instancing); Arnold 5.9.3.0 adds 3DGS rendering, a Shader to RGBA node and denoiser updates. Trade coverage lists PLY, SPZ and LCC import formats; the Autodesk What's New page fetched does not list formats.
**Limitation / caveats:** Release date not stated on Autodesk's own documentation pages (observed, not stated). No performance numbers given for splat rendering.
