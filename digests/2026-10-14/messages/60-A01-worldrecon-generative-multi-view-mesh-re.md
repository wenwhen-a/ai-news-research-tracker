**[A01] WorldRecon: Generative Multi-View Mesh Reconstruction for Large-Scale 3D World**
- **arXiv:** 2610.18846 · <https://arxiv.org/abs/2610.18846>
- **Submitted:** 2026-10-13
- **Authors:** Mengchen Zhang, Yang Li, Chunshi Wang, Tong Wu, Chunchao Guo
- **Qualifying affiliation(s):** Tencent (Tencent Hunyuan) — Yang Li, Chunchao Guo (also Mengchen Zhang, Chunshi Wang dual-affiliated with Zhejiang University and Tencent Hunyuan)
- **Categories:** cs.CV
- **Open release:** none (project page only, no code/weights found) — <https://kszpxxzmc.github.io/WorldRecon-website/>
- **Shipped counterpart:** none found

**Summary:** WorldRecon is a generative framework for reconstructing complete, large-scale 3D scene meshes from unposed RGB images.
**Purpose:** The authors target the problem that existing multi-view reconstruction methods struggle to produce complete, generative (not just depth-fused) meshes across large indoor environments while keeping geometry and materials consistent block-to-block.
**Breakthrough:** The authors report that neighbor-aware latent inpainting plus a causal block-generation process let WorldRecon achieve lower Chamfer distance and higher F-score than baselines including VGGT-Ω+TSDF, Murre, MonoSDF, FineRecon, and GenRecon, with claimed generalization from synthetic training to real indoor scenes.
**Tools & method:** The model is trained on two synthetic indoor datasets, 3D-FRONT and SAGE-10k (~117k block-level training blocks), using up to 32 NVIDIA GPUs, and evaluated on 30 held-out 3D-FRONT scenes plus 30 real-world ScanNet++ scenes.
**Limitation:** The authors state training data covers only indoor scenes, so current applicability "is limited to indoor environments," and the representation uses a single layer of 4m-high blocks, which restricts reconstruction to single-story buildings.
