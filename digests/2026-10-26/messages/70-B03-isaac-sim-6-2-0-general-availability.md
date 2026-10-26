**[B03] Isaac Sim 6.2.0 (General Availability)**
- **Company:** NVIDIA
- **Status:** GA · **Released:** 2026-10-14 · **New**
- **Surface:** Studio/developer tool (robotics & simulation platform)
- **Primary source:** <https://github.com/isaac-sim/IsaacSim/releases/tag/v6.2.0>
- **Underlying research:** no traceable paper
- **Availability:** Free GA release via GitHub/Omniverse channels; built on Omniverse Kit SDK 110.4.0; supersedes Isaac Sim 6.1 GA (2026-09-15). A parallel Isaac Sim 7.0.0 Alpha 1 pre-release also exists (2026-09-18).

**What shipped:** NVIDIA shipped Isaac Sim 6.2.0 as a full GA release, upgrading its Kit SDK to 110.4.0 and its Newton physics engine to 1.6.1 (with MuJoCo 3.12.0 and Warp 1.17.0). It adds automatic AI-model selection for synthetic action/event data generation and deformable-object synthetic data with 3D bounding boxes.
**What research it translates:** The release packages NVIDIA's Newton open physics engine and Replicator (1.13.38) synthetic-data-generation research into the shipped robotics-simulation product; no dedicated paper is cited for this specific version.
**Practical significance:** NVIDIA's release notes state the update targets robotics teams building sim-to-real training pipelines, with zero-copy live sensor-reading APIs and batched Newton actuator drives with gravity/Coriolis compensation.
**Engineering details:** The URDF exporter now supports UDIM texture export; RtxCamera can instantiate multiple camera prims from a path list or regex; `get_sensor_reading()` now returns an owned snapshot — a stated breaking API change from 6.1.
**Limitation / caveats:** The Cortex module was removed in this release; most changes are robotics/physics/tooling fixes and API breaks rather than new generative-3D or world-model capability.
