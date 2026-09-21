**[B07] Omniverse Kit 110.3**
- **Company:** NVIDIA
- **Status:** GA · **Released:** 2026-08 (exact day not published in release notes) · **New**
- **Surface:** Studio/developer tool (Omniverse Kit SDK, underlies Omniverse apps and RTX tools)
- **Primary source:** <https://docs.omniverse.nvidia.com/dev-guide/latest/release-notes/110_3_highlights.html>
- **Underlying research:** no traceable paper (engineering/correctness release)
- **Availability:** Free via NVIDIA NGC/Omniverse distribution channels for Kit-based application developers.

**What shipped:** Kit 110.3 is a feature-and-stability release adding directional marquee viewport selection, fixing long-standing rendering artifacts (ghosting, incorrect specular/transmission), and delivering reliability improvements to physics simulation, the Fabric Scene Delegate, and the Replicator synthetic-data-generation annotator pipeline (including eliminating a ~36% throughput regression).
**What research it translates:** Primarily correctness/reliability engineering rather than new research productization.
**Practical significance:** NVIDIA frames this as improving reliability of synthetic-data-generation workflows used to train robotics/AV perception models, and fixing rendering-correctness issues that previously produced silently wrong output.
**Engineering details:** Adds `omni.usd.PickingMode.FULLY_ENCLOSED` for viewport selection and supports latlong-format backplates; fixes affect Fabric Scene Delegate instancing/transform behavior under scene partitioning.
**Limitation / caveats:** This is a maintenance/incremental release for SDK developers, not a consumer-visible feature launch; the exact release date was not published on the primary docs page (only "August 2026").
