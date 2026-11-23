**[B04 · Update] Unreal Engine 5.9 Preview (Unreal Canvas, AnimGen AI animation, MCP/agent tooling)**
- **Company:** Epic Games
- **Status:** Public beta/preview · **Released:** 2026-11-19 (Preview 2) · **Update**
- **Surface:** Engine / editor (Preview build)
- **Primary source:** <https://dev.epicgames.com/documentation/unreal-engine/unreal-engine-5-9-release-notes>
- **Underlying research:** "Control Operators for Interactive Character Animation," Ruiyu Gou (Epic Games), ACM Transactions on Graphics, Dec. 2025 — describes a controller-agnostic framework shown on a flow-matching-based autoregressive motion model. No arXiv preprint found.
- **Availability:** Free public Preview download via Epic Games Launcher/source; Epic states it "should be considered unstable until the final release."

**What shipped:** Update since 2026-11-09: the UE5.9 Preview build was revised (Preview 2, last updated 2026-11-19) adding the experimental UAF AnimGen plugin — a trained, flow-matching neural character controller that drives an AnimNode frame-by-frame — alongside the already-announced experimental Unreal Canvas collaborative workspace and expanded Python/Unreal MCP agent tooling.
**What research it translates:** AnimGen's controller uses flow matching and a neural network to synthesize character poses in real time, matching the approach Epic's own Ruiyu Gou published in ACM TOG (Control Operators).
**Practical significance:** Epic states this gives developers an experimental path to AI-driven procedural character animation (AnimGen) and agent-operable editing (Canvas, MCP) directly in a Preview build anyone can download today.
**Engineering details:** AnimGen is built on Epic's Universal Animation Framework (UAF) and includes an AutoEncoder plus multiple behavior classes driving the pose-generation AnimNode.
