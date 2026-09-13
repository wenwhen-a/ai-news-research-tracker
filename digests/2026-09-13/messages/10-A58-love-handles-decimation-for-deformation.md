**[A58] Love Handles: Decimation for Deformation Handles with Compact Support and Low Memory Footprints**
- **arXiv:** 2608.17930 · https://arxiv.org/abs/2608.17930
- **Submitted:** 2026-08-18
- **Authors:** David IW Levin, Paul Kry, Kartic Subr, Ryan Schmidt, Etienne Vouga, Teseo Schneider
- **Qualifying affiliation(s):** NVIDIA — David IW Levin (also University of Toronto)
- **Categories:** cs.GR
- **Open release:** none
- **Shipped counterpart:** none found

**Summary:** A decimation-based algorithm that computes sparse, compactly supported deformation handles for reduced-order elastodynamic simulation on arbitrary volumetric meshes.
**Purpose:** To lower per-timestep cost of physically based deformation for real-time, game and robotics use while bounding error against target modes such as linear vibration modes.
**Breakthrough:** The authors report reducing a 200,000-vertex basketball mesh to 268 handles at 5% error on 25 linear modes, 150 simulation steps per second for nonlinear elastodynamics, and up to 15.12x lower error than Brandt et al. (2018) at equal memory, with per-timestep cost rarely above 55 ms.
**Tools & method:** Iterative algebraic mesh decimation jointly optimising handle placement, weights and a spectrally informed reduced cubature; 15 tetrahedral meshes (699 to 201,942 vertices) on an NVIDIA DGX Spark.
**Limitation:** The authors state preprocessing can take up to 36 hours in worst cases, that the method is less effective on already-coarse meshes, and that it needs precomputed target displacement fields.
