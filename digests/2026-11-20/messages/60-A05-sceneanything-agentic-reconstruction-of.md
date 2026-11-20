**[A05] SceneAnything: Agentic Reconstruction of Large-Scale Mesh Scenes from a Single Video**
- **arXiv:** 2611.25340 · <https://arxiv.org/abs/2611.25340>
- **Submitted:** 2026-11-19
- **Authors:** Bowen Xue, Saeed Hadadan, Fabrice Rousselle, Zahra Montazeri, Ravi Ramamoorthi, Milos Hasan
- **Qualifying affiliation(s):** NVIDIA — Bowen Xue, Saeed Hadadan, Fabrice Rousselle, Milos Hasan
- **Categories:** cs.CV, cs.GR
- **Open release:** none found (authors state plans to release the harness, agent instructions, libraries, and scenes, but no link is given yet)
- **Shipped counterpart:** none found

**Summary:** SceneAnything is an automated system that reconstructs editable, large-scale mesh scenes from a single real or generated video, and can also support text-to-scene creation when paired with a video generator.
**Purpose:** The goal is to turn a single video into an editable, large-scale mesh scene usable in standard 3D/graphics pipelines, rather than an opaque implicit representation.
**Breakthrough:** As the authors report, the agentic pipeline outperforms direct-agent reconstruction on original-view fidelity and outperforms compared video-to-3D baselines on novel-view similarity across 100 scenes.
**Tools & method:** Agents plan the environment using shared camera, depth, and segmentation estimates, then write parameterized Blender programs; revisions are checked both programmatically and visually before acceptance.
**Limitation:** The accessible text does not state explicit limitations beyond noting that unseen regions are inferred (not directly observed) and marked as such; code/data are not yet released, so independent reproduction is not currently possible.
