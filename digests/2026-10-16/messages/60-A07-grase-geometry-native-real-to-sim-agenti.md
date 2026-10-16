**[A07] GRASE: Geometry-native Real-to-sim Agentic Scene Modeling from Video**
- **arXiv:** 2610.21498 · <https://arxiv.org/abs/2610.21498>
- **Submitted:** 2026-10-15 (v1, 08:34:00 UTC)
- **Authors:** Zhaorui Lin, Haohan Liu, Zhen Chen, Xiangru Huang
- **Qualifying affiliation(s):** Adobe Systems — Zhen Chen (other authors: Xi'an Jiaotong University, Fuzhou University, Westlake University)
- **Categories:** cs.CV
- **Open release:** none found (no Comments field, project page, or code link on the abstract page)
- **Shipped counterpart:** none found

**Summary:** GRASE is an agentic framework that turns a captured multi-view video of a real indoor space into an editable, simulation-ready 3D scene, treating the original video as a persistent reference it checks against throughout.
**Purpose:** The authors target error accumulation in one-pass real-to-sim pipelines, where mistakes made in early stages (layout fitting, object placement) propagate uncorrected into the final scene.
**Breakthrough:** On the authors' Imaginarium benchmark (15 scenes) and 8 Replica scenes, the authors report GRASE substantially lowers scene-level Chamfer Distance versus the strongest baseline (e.g., Imaginarium: 3.14 cm vs. 11.00 cm for GPT-6 + TRELLIS.2 + point cloud) and raises object instance mIoU (e.g., Imaginarium: 0.74 vs. 0.21).
**Tools & method:** The pipeline samples video frames, runs Depth Anything 3 and SAM 3 for depth/segmentation, fits the room shell with RANSAC and parametric patches for curved surfaces, and places/generates objects via TRELLIS.2 or Blender-MCP-built primitives.
**Limitation:** The authors acknowledge reconstruction is limited in heavily occluded regions with insufficient geometric evidence, which are completed by extending surfaces or generative priors and marked as inferred rather than observed.
