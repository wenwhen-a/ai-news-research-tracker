**[A05] PhysSkin++: Real-Time and Generalizable Physics-Based Animation via Self-Supervised Neural Skinning**
- **arXiv:** 2610.26067 · <https://arxiv.org/abs/2610.26067>
- **Submitted:** 2026-10-19
- **Authors:** Yuanhang Lei, Baofei Liu, Xingxuan Li, Tao Cheng, Zixuan Wang, Boming Zhao, Yujun Shen, Siyuan Huang, Ruizhen Hu, Peter Yichen Chen, Hujun Bao, Zhaopeng Cui
- **Qualifying affiliation(s):** Ant Group — Yujun Shen; FLAG: borderline
- **Categories:** cs.CV (cross-listed cs.GR)
- **Open release:** demo — project page <https://zju3dv.github.io/PhysSkin_plus/>
- **Shipped counterpart:** none found

**Summary:** PhysSkin++ is a physics-informed framework that learns continuous neural skinning fields from static 3D geometry to build compact deformation subspaces for real-time, generalizable physics-based animation, supporting meshes, point clouds, and 3D Gaussians as well as rig-complementary animation.
**Purpose:** To generalize real-time physics-based animation across different 3D shapes and spatial discretizations without relying on simulation trajectories or annotated skinning data.
**Breakthrough:** The authors introduce a rig-complementarity loss that lets the model learn physically-grounded elastic responses on top of artist-authored rig animation, and report supporting controllable, collision-aware animation with Dirichlet boundary conditions, user dragging, gravity, floor contact, and rigid/deformable multi-object contact.
**Tools & method:** A Neural Skinning Fields Autoencoder (transformer shape encoder + cross-attention decoder) is trained with a self-supervised strategy (PISSL) combining potential-energy, smoothness, and orthogonality losses with conflict-aware gradient correction (ConFIG).
**Limitation:** The authors state the current formulation "does not incorporate semantic priors for modeling complex geometries" and plan to explore such priors in future work.
