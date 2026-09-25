**[A01] OmniFabric: Coherent UV Space Texture Synthesis for 3D Garment Reconstruction**
- **arXiv:** 2609.30234 · <https://arxiv.org/abs/2609.30234>
- **Submitted:** 2026-09-24
- **Authors:** Ding-Jiun Huang et al.
- **Qualifying affiliation(s):** Google — Hugo Bertiche, Alexandru-Eugen Ichim, Thabo Beeler listed at Google (other authors at CMU, University of Washington, Texas A&M)
- **Categories:** cs.CV
- **Open release:** none stated
- **Shipped counterpart:** none found

**Summary:** OmniFabric targets automated creation of production-ready 3D garment textures from a single reference image, a task where existing methods "bake environmental illumination and shadows directly into the texture map" or lose global coherence, making the result unsuitable for physical simulation or relighting.
**Purpose:** The authors aim to produce clean, normalized, sewing-pattern-space texture maps — free of baked lighting — that can be reused across simulation and relighting pipelines, rather than a single fixed-lighting render.
**Breakthrough:** On their synthetic test set the authors report LPIPS of 0.092 versus 0.223–0.311 for FabricDiffusion, Paint3D, and Hunyuan3D-2.0, and CLIP-score 0.963 versus 0.890–0.924 for those baselines.
**Tools & method:** A first stage uses Gemini 3 Pro to repose the input garment into a canonical A-pose and Veo 3 to synthesize a 360° rotation, from which four orthogonal views are projected onto unwrapped sewing patterns to build a coarse but globally coherent texture; a second stage trains a LoRA-fine-tuned Diffusion Transformer, conditioned on the coarse texture, a frontal rendering, and a 3D position map, to remove baked shadows and distortions.
**Limitation:** The authors state the method "does not yet explicitly disentangle albedo from shading in a strictly principled, physics-based manner," and that highly reflective or metallic fabrics with strong view-dependent effects remain challenging.
