**[A02] DUET-DINO: Simultaneous Cross-View World Modeling for Latent Planning in Robot Manipulation**
- **arXiv:** 2609.10506 · https://arxiv.org/abs/2609.10506
- **Submitted:** 2026-09-09
- **Authors:** Nisarga Nilavadi, Ralf Römer, Moritz Reuss, Michael Krawez, Tobias Jülg, Angela P. Schoellig, Rudolf Lioutikov, Wolfram Burgard
- **Qualifying affiliation(s):** NVIDIA — Moritz Reuss (also Intuitive Robots Lab, KIT)
- **Categories:** cs.RO, cs.CV
- **Open release:** code planned (the paper states "the code and model checkpoints will be open-sourced"; project page https://utn-air.github.io/DUET-DINO)
- **Shipped counterpart:** none found

**Summary:** A dual-view latent world model for robot manipulation that fuses side-view and wrist-camera observations through cross-view attention and extends latent planning to a full 7-DoF end-effector action space.
**Purpose:** Single-view latent world models struggle to predict the fine translational, rotational and gripper-state changes needed for 7-DoF control.
**Breakthrough:** The authors report that DINOv3 captures action-conditioned visual dynamics better than V-JEPA 2, and that their normalised dual-view cost optimisation reaches 92% reach success, 72.5% angled-reach success and 60% lift-to-home success.
**Tools & method:** Cross-view conditioned latent prediction with CEM planning; trained on DROID (62,877 trajectories) and RoboArena (5,856 trajectories); evaluated in the RoboLab simulator and on a Franka Research 3 with two ZED cameras.
**Limitation:** The authors state CEM planning "limits real-time control" because of its computational cost and suggest vision-language-action models to accelerate planning.
