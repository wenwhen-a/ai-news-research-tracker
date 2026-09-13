**[A44] ExMesh++: From Multi-View Images to Relightable UV-PBR Mesh Assets via Topology-Adaptive Reconstruction and Decomposition**
- **arXiv:** 2608.24109 · https://arxiv.org/abs/2608.24109
- **Submitted:** 2026-08-25
- **Authors:** Chuanjin Fan, Lifan Wu, Wenjie Chang, Hanzhi Chang, Wenfei Yang, Tianzhu Zhang
- **Qualifying affiliation(s):** Alibaba Group (Amap) — Wenjie Chang
- **Categories:** cs.GR, cs.CV
- **Open release:** none
- **Shipped counterpart:** none found

**Summary:** A staged multi-view reconstruction pipeline that yields editable, relightable UV-PBR mesh assets: geometry and topology are refined with consistent UV updates, then PBR maps and environment lighting are optimised on the fixed mesh with one-bounce indirect illumination.
**Purpose:** To close the gap between surface-only multi-view reconstruction and production-ready assets for standard DCC workflows.
**Breakthrough:** The authors report average Chamfer distance 0.58 on DTU (102K-vertex meshes, 13-minute runtime); on Synthetic4Relight, relighting PSNR 34.19 dB, albedo PSNR 30.16 dB and roughness MSE 0.005; on Stanford-ORB, novel-view PSNR-H 31.27 dB, relighting PSNR-H 26.60 dB and Chamfer 0.30.
**Tools & method:** Topology-adaptive vertex splitting and merging with UV consistency; two-stage inverse rendering; one-bounce diffuse indirect illumination via secondary ray tracing; about 30 minutes per scene on one NVIDIA RTX A6000.
**Limitation:** The authors state the method is limited to opaque isotropic metallic-roughness BRDFs, that the one-bounce model excludes multi-bounce transport and indirect specular reflection, and that CPU-based UV regeneration bottlenecks high-resolution meshes.
