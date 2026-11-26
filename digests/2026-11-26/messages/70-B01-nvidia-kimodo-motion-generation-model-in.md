**[B01] NVIDIA Kimodo motion-generation model in Unreal Engine 5.9's guided animation framework**
- **Company:** NVIDIA (research/model), integrated by Epic Games into Unreal Engine 5.9
- **Status:** Public beta/preview · **Released:** 2026-11-19 (available in Unreal Engine 5.9 Preview 2) · **New**
- **Surface:** Engine tool — Unreal Engine 5.9 Preview Sequencer (guided animation framework)
- **Primary source:** <https://developer.nvidia.com/blog/whats-new-for-game-developers-ai-animation-and-rtx-tools/>
- **Underlying research:** NVIDIA Kimodo tech report, "Kimodo" project page (<https://research.nvidia.com/labs/sil/projects/kimodo>), NVIDIA Spatial Intelligence Lab — no arXiv preprint found; NVIDIA links a tech-report PDF, GitHub code, and a Hugging Face model/demo instead.
- **Availability:** Accessible only inside Unreal Engine 5.9 Preview (not yet a numbered GA release); GPU-accelerated; no standalone pricing/license stated outside the UE5.9 Preview terms.

**What shipped:** NVIDIA states Kimodo is "the first model integrated with" Unreal Engine 5.9 Preview's new guided animation framework, letting animators generate character motion directly inside Sequencer's timeline editor.
**What research it translates:** Kimodo is a kinematic motion-diffusion model from NVIDIA's Spatial Intelligence Lab, trained on 700 hours of optical motion-capture data and controllable via text prompts plus kinematic constraints (full-body keyframes, sparse joint positions/rotations, 2D waypoints/paths).
**Practical significance:** NVIDIA states this lets animators direct character motion with constraints rather than hand-keying every frame, without leaving Unreal's Sequencer.
**Engineering details:** The research page describes a two-stage denoiser separating root and body motion prediction, built on a kinematic (not physics-based) diffusion formulation.
