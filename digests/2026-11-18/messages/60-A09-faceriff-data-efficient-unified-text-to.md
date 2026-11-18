**[A09] FaceRiff: Data-Efficient Unified Text-to-3D Face Asset Synthesis via Geometric Conditioning**
- **arXiv:** 2611.21867 · <https://arxiv.org/abs/2611.21867>
- **Submitted:** 2026-11-16
- **Authors:** Elly Akhoundi, Mathieu Lamarre, Thibault Goyallon, Patrick Anderson, Étienne Danvoye
- **Qualifying affiliation(s):** Electronic Arts — all five authors (HTML affiliation block lists "Electronic Arts, Vancouver/Montréal/Toronto, Canada" for each)
- **Categories:** cs.CV (primary); cs.AI; cs.GR
- **Open release:** none found
- **Shipped counterpart:** none found

**Summary:** FaceRiff generates complete 3D face assets — mesh, albedo, and displacement — from text prompts in a shared UV space.
**Purpose:** To address the scarcity of high-resolution facial datasets with consistent UV-mapped geometry, albedo, and physically-based displacement, and to produce diverse, production-usable 3D face assets from text without large specialized datasets or per-instance optimization.
**Breakthrough:** The authors report greater per-prompt diversity than prior methods FaceG2E and DreamFace while preserving prompt alignment and UV consistency, plus lighting-independent albedo suitable for PBR relighting and pore-scale displacement.
**Tools & method:** Pretrained SDXL backbone adapted with task-specific LoRA adapters (updating under 3% of backbone parameters per task); UV normal maps provide geometric conditioning, with per-instance normals guiding albedo/displacement and a dataset-mean normal anchoring mesh generation.
**Limitation:** No explicit limitations are stated in the abstract or comments; the GPU model used for training is not specified, and the scan dataset is not named.
