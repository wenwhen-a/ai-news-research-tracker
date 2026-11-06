**[A04] Bri3D: Bridging the Object-Scene Gap in Single-Image 3D Generation via Scene-Anchor**
- **arXiv:** 2611.07961 · <https://arxiv.org/abs/2611.07961>
- **Submitted:** 2026-11-05
- **Authors:** Hongye Hou et al.
- **Qualifying affiliation(s):** Alibaba — one of Hongye Hou / Shuai Zhang / Hongjie Li at Taobao & Tmall Group of Alibaba (the paper lists Hong Kong University of Science and Technology (Guangzhou), Taobao & Tmall Group of Alibaba, and Hong Kong University of Science and Technology as the three affiliations but the author-to-affiliation mapping was lost in page extraction)
- **Categories:** cs.CV
- **Open release:** none
- **Shipped counterpart:** none found

**Summary:** Bri3D generates compositional 3D scenes from a single image by first predicting a color-coded scene scaffold of coarse object geometry and layout, extracting each object as a voxel "scene anchor," refining it into a pose-preserving support, and then using a frozen object generator to synthesize detailed textured geometry within that anchor.
**Purpose:** The paper addresses a stated failure mode of existing single-image object-to-scene 3D generators: under limited scene-level supervision they struggle to coordinate multiple objects, and naively extending object generators to whole scenes can corrupt geometry, instance scale, orientation, and pose.
**Breakthrough:** On the MIDI-cleaned 3D-FRONT test split, the authors report CD-S 0.87 and BBox IoU 0.7540 versus the best baseline SAM3D's CD-S 2.11 and BBox IoU 0.6271; on a 300-scene cross-dataset test (HSSD/BlendSwap) Bri3D scores CD-S 3.42 versus SAM3D's 3.85. Full-scene generation takes 78.4s versus 230.2s (SceneGen) and 179.6s (SAM3D), with a reported object-collision rate of 4% versus 14–38% for the three baselines.
