**[A05] Pixels to Keys: Exploring Spatial and Motion Cues in Gameplay Inverse Dynamics**
- **arXiv:** 2609.37907 · <https://arxiv.org/abs/2609.37907>
- **Submitted:** 2026-09-29 (v1)
- **Authors:** Abhishek Pillai, Ekta Prashnani, Joohwan Kim, Iuri Frosio
- **Qualifying affiliation(s):** NVIDIA (all four authors)
- **Categories:** cs.AI; cs.CV
- **Open release:** none found
- **Shipped counterpart:** none found

**Summary:** The paper studies Inverse Dynamics Models (IDMs) that recover a player's keyboard/mouse inputs purely from gameplay video, since gameplay footage rarely comes with recorded inputs.
**Purpose:** Video games offer rich, embodied-agent settings for studying perception and control, but gameplay videos lack accompanying player-input labels.
**Breakthrough:** The authors report their best IDM reaches F1 scores of 0.920 (steering), 0.869 and 0.870 (accel/decel) on Trackmania — only modestly above a CNN trained via behavior cloning (~0.9 / ~0.8 / ~0.8) — and attribute the small gap partly to the IDM learning the dataset's average policy rather than a precise visual-to-key mapping.
**Tools & method:** IDMs combine RGB frames with motion cues (including RAFT optical flow) and are evaluated with balanced metrics and ablations over frame resolution, pretrained embeddings, and loss functions.
**Limitation (≤3 sentences, authors' own):** The authors state that camera motion creates visual ambiguity — gameplay projects 3D motion into 2D while the camera moves independently, so optical flow measures displacement but not its cause (e.g., a reversing vehicle can look like forward camera motion).
