**[A06] Joints, Camera, Action! Co-Generating 3D Motion and Video for Arbitrary Rigs**
- **arXiv:** 2610.28632 · <https://arxiv.org/abs/2610.28632>
- **Submitted:** 2026-10-20 (v1)
- **Authors:** Noam Rotstein et al.
- **Qualifying affiliation(s):** NVIDIA — all eight authors carry an NVIDIA affiliation marker in the paper's author block; several also hold secondary academic affiliations (Technion — Rotstein, Maron, Litany, Kasten; Bar-Ilan University — Chechik)
- **Categories:** cs.CV (primary); cs.AI, cs.GR, cs.LG, cs.RO (cross-listed)
- **Open release:** project page only (<https://research.nvidia.com/labs/par/projects/jca/>); no code or weights stated
- **Shipped counterpart:** none found

**Summary:** Video generation models produce realistic motion, but that motion stays in pixels and cannot easily be reused as replayable 3D animation in a 3D scene.
**Purpose:** The goal is to let a single system turn a text or video prompt into replayable 3D motion for arbitrary skeletons — not just humans — correctly placed in its 3D scene, rather than only generating pixel-level video.
**Breakthrough:** The authors report that keeping 3D motion in a separate model connected to a pretrained video backbone via a small set of cross-attention layers lets the system learn skeleton motion from motion-only data; their evaluations state the model animates diverse rigs from text more faithfully than video-first pipelines and that its motion responds to the surrounding scene.
**Tools & method:** The model builds on the Wan2.2 I2V-A14B video backbone and a generative video editor ("Bernini") used to place animated 3D assets from Objaverse/Objaverse-XL into matching scenes, producing the authors' own "Objaverse in Video" dataset and, combined with human and robot video, nearly 200K training pairs.
