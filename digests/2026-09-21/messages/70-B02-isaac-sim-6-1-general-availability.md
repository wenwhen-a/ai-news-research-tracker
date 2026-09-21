**[B02] Isaac Sim 6.1 (General Availability)**
- **Company:** NVIDIA
- **Status:** GA · **Released:** 2026-09-15 · **New**
- **Surface:** Studio/simulation tool (robotics simulation platform, part of the Omniverse ecosystem)
- **Primary source:** <https://forums.developer.nvidia.com/t/isaac-sim-6-1-general-availability/383280> (supporting: <https://docs.isaacsim.omniverse.nvidia.com/latest/overview/release_notes.html)>
- **Underlying research:** FoundationStereo: Zero-Shot Stereo Matching (arXiv:2501.09898, CVPR 2025 Best Paper nomination); BundleSDF: Neural 6-DoF Tracking and 3D Reconstruction of Unknown Objects (arXiv:2303.14158, CVPR 2023) — both underlie the new "3D Object Reconstruction" pipeline. No paper found for the new Behavior Tree system.
- **Availability:** Free, GA download via Isaac Sim/Omniverse channels and GitHub (isaac-sim/IsaacSim); requires an NVIDIA RTX-class GPU.

**What shipped:** Isaac Sim 6.1 moved from early-developer preview to full general availability, adding a synthetic-data-generation example that uses NVIDIA's "3D Object Reconstruction" framework to turn stereo video of a real object into a textured USD asset.
**What research it translates:** The 3D Object Reconstruction workflow chains NVIDIA's FoundationStereo (zero-shot stereo depth), SAM2 segmentation, and BundleSDF (neural 6-DoF pose tracking + implicit-surface reconstruction) into a pipeline that outputs a sim-ready textured mesh from stereo video — a direct productization of published NVIDIA computer-vision research.
**Practical significance:** NVIDIA states this lets developers digitize real-world objects into simulation-ready 3D assets without manual modeling, feeding Isaac Sim's synthetic-data pipelines for robot training.
**Engineering details:** Outputs are standard USD/OBJ assets compatible with Isaac Sim, Omniverse and downstream game engines; the behavior-tree system ships via a new `omni.ai.behavior_tree_gen` Kit extension.
