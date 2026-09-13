**[A09] RenderFormer-V2: Neural Rendering with Heterogeneous Scene Primitives**
- **arXiv:** 2609.05738 · https://arxiv.org/abs/2609.05738
- **Submitted:** 2026-09-04
- **Authors:** Chong Zeng et al.
- **Qualifying affiliation(s):** Microsoft Research — Yue Dong
- **Categories:** cs.CV, cs.GR, cs.LG
- **Open release:** code and weights (the paper states "The trained RenderFormer-V2 model and code can be found at: https://renderformer.github.io/v2")
- **Shipped counterpart:** none found

**Summary:** RenderFormer-V2 is a transformer that renders images from heterogeneous scene primitives (triangles with textures or displacement, voxels, triangular lights, environment maps), handling caustics, volumetric scattering, environment lighting and out-of-distribution materials "without per-scene training or specialized code."
**Purpose:** A single learned model covering diverse light-transport effects and primitive types as a complement to physics-based renderers, scaling beyond the 44k-primitive limit of the original RenderFormer.
**Breakthrough:** The authors report handling more than 100k primitives; at 64K triangles they report LPIPS 0.0873 versus 0.3070 for RenderFormer, and 0.0999 versus 0.4772 at 128K, with average test-scene PSNR 28.25 / SSIM 0.8982 / LPIPS 0.0997 and about 2 to 3 seconds per frame at 64K primitives on an A100.
**Tools & method:** A 207M-parameter two-stage transformer: a 12-layer view-independent stage with sliding-window attention and rendering-informed attention sinks, and a 6-layer view-dependent stage with cross-attention and SWIN windowed attention; BRDF-agnostic neural material embeddings; trained 19 days on 32 A100 GPUs on about 10M sampled scenes (about 70 TB) at 256² to 2048².
**Limitation:** The authors state limits of 88 light sources per scene and a fixed 32x32 texture resolution per triangle, no explicit temporal coherence, and that adding a new primitive type "typically requires significant retraining."
