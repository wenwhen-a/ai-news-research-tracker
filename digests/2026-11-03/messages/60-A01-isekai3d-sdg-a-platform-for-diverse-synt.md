**[A01] Isekai3D SDG: A Platform for Diverse Synthetic Gameplay Visual Data**
- **arXiv:** 2611.03626 · <https://arxiv.org/abs/2611.03626>
- **Submitted:** 2026-11-02
- **Authors:** Rafał Karp, Gene Liu, Shih-Hsin Li, Eric Courtemanche, Shengze Wang, Josef Spjut, David Pankratz, Mischa Kolbe, Michael Stengel, Sven Elflein, Adam Grygielski, Liwen Wu, Anjul Patney
- **Qualifying affiliation(s):** NVIDIA — all 13 listed authors
- **Categories:** cs.CV
- **Open release:** none found (no code/dataset/project-page link in the paper; only references to Unreal Engine/Fab and the arXiv/build pages)
- **Shipped counterpart:** none found

**Summary:** The paper presents Isekai3D SDG, a platform for simulating and capturing synthetic 3D gameplay data for vision and world-model research.
**Purpose:** The authors aim to make it easier to generate diverse synthetic gameplay visual data with frame-aligned camera, character, and action metadata, in a format ready for model training.
**Breakthrough:** The authors report that separating simulation from capture lets a single recorded gameplay session produce multiple output variants without re-simulating, and that the platform uploads generated data directly in a training-friendly format, reducing intermediate storage and manual processing.
**Tools & method:** The system is built as Unreal Engine plugins around a packaged game; it decouples a simulation pass (recording world/character/action/camera state) from a capture pass (replaying the recording to render selected output modalities).
**Limitation:** The paper has no dedicated limitations section.
