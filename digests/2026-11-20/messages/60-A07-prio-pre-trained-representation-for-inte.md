**[A07] PRIO: Pre-trained Representation for Interactive Objects in 4D Worlds**
- **arXiv:** 2611.25500 · <https://arxiv.org/abs/2611.25500>
- **Submitted:** 2026-11-19
- **Authors:** Shixun Huang, Lifu Wei, Yue Chang, Chen Geng, Heng Zhang, Jinhyung Ahn, Caoliwen Wang, Siyuan Chen, Donglai Xiang, Jiajun Wu, Peter Yichen Chen
- **Qualifying affiliation(s):** NVIDIA — Donglai Xiang
- **Categories:** cs.CV
- **Open release:** none found
- **Shipped counterpart:** none found

**Summary:** PRIO is a pre-trained model that, given an object's static 3D geometry (mesh, point cloud, or 3D Gaussians), predicts an object-specific low-dimensional configuration space in a single forward pass.
**Purpose:** The authors note that reconstructed or generated 3D scenes typically contain only static objects that cannot move or deform realistically, limiting interactivity.
**Breakthrough:** The authors report that PRIO generalizes to unseen shapes after being pre-trained on diverse 4D trajectories, and that it generates dynamics faster and follows user actions more faithfully than existing 4D generation methods.
**Tools & method:** The method predicts a per-object configuration space in one forward pass, then simulates motion via Lagrangian mechanics parameterized by those coordinates, precomputing the (linear) dynamics so no further network inference is needed at run time.
**Limitation:** The accessible text does not state explicit limitations beyond what is implied by the method (restricted to the learned configuration-space formulation); none are asserted here beyond what is verifiable.
