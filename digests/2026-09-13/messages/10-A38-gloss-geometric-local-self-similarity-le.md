**[A38] GLOSS: Geometric Local Self-Similarity Learning for Faithful Reference-Guided Texture Fill**
- **arXiv:** 2608.25461 · https://arxiv.org/abs/2608.25461
- **Submitted:** 2026-08-26
- **Authors:** Chenyue Cai, Anita Hu, James Lucas, Szymon Rusinkiewicz, Masha Shugrina
- **Qualifying affiliation(s):** NVIDIA — Anita Hu, James Lucas, Masha Shugrina
- **Categories:** cs.GR, cs.CV, cs.LG
- **Open release:** code, weights and a Blender add-on announced (the authors state they "will release the code, the model checkpoint and Blender add-on" at https://chenyuecai.github.io/gloss-page/)
- **Shipped counterpart:** none found

**Summary:** A shape-specific local texture generation model trained on single-view renderings of one object that exploits geometry-texture self-similarity to perform reference-guided texture inpainting on a mesh without large 3D texture datasets.
**Purpose:** Interactive, geometry-consistent texture fill and editing on a single 3D shape in a small-data, per-shape regime.
**Breakthrough:** The authors report LPIPS 0.282 (per-mesh) / 0.302 (fine-tuned) and DreamSim 0.352 (fine-tuned), better than TEXGen (LPIPS 0.436) and competitive with Hunyuan2.1 and MV-Adapter, which train on much larger data.
**Tools & method:** Batch multi-attention learning over self-similarity within one object; an automated data pipeline built on off-the-shelf image generators; a Blender add-on prototype pilot-tested with 5 professional 3D artists.
**Limitation:** The authors state the small-data regime limits generalisation and raises per-shape cost, that the method assumes strong geometry-texture correlation, and that PBR generation is preliminary.
