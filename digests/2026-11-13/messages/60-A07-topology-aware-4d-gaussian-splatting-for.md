**[A07] Topology-Aware 4D Gaussian Splatting for Egocentric Videos**
- **arXiv:** 2611.16012 · <https://arxiv.org/abs/2611.16012>
- **Submitted:** 2026-11-11
- **Authors:** Leonardo Vanni, Stefano Gasperini, Federico Tombari, Chiara Plizzari
- **Qualifying affiliation(s):** Google — Federico Tombari (listed as Technical University of Munich; Google)
- **Categories:** cs.CV
- **Open release:** none yet — paper states "Code and data will be made publicly available"; project page at <https://topoego.github.io>
- **Shipped counterpart:** none found

**Summary:** The paper introduces TopoEgo, a benchmark of egocentric video clips with topology-changing object interactions (cutting, assembly, opening, closing), and Topo-4DGS, a 4D Gaussian Splatting method built to handle those topology changes.
**Purpose:** Existing 4D Gaussian Splatting methods deform a fixed representation and struggle with everyday topology-changing interactions in monocular egocentric video, producing visual artifacts.
**Breakthrough:** The authors report full-scene PSNR of 27.95 for Topo-4DGS versus 27.80 for the best baseline (Def-3DGS without hands), with larger gains isolated to the changing object: 23.52 PSNR (+0.92 dB) and, on post-event frames specifically, 24.30 PSNR (about +4.47 dB over the best baseline).
**Tools & method:** Topo-4DGS has two components: "Motion Bifurcation," which routes an object's Gaussians to independent rigid motions per part via a time-independent spatial branch and an event-gated temporal branch; and "Topological Boundary Resolution," which activates Gaussians for newly exposed surfaces and deactivates those for concealed/obsolete ones.
**Limitation:** The method assumes reliable event specifications and approximately piecewise-rigid parts; automatic topology discovery and strongly deformable objects are left as future work.
