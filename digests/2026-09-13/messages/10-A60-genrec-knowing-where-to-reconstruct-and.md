**[A60] GenRec: Knowing Where to Reconstruct and Where to Generate**
- **arXiv:** 2608.17832 · https://arxiv.org/abs/2608.17832
- **Submitted:** 2026-08-18
- **Authors:** Ata Çelen, Jaewoo Jung, Federico Tombari, Marc Pollefeys, Sunghwan Hong, Michael Niemeyer, Daniel Barath
- **Qualifying affiliation(s):** Google — Federico Tombari, Daniel Barath; Microsoft — Marc Pollefeys
- **Categories:** cs.CV
- **Open release:** none
- **Shipped counterpart:** none found

**Summary:** GenRec is a multi-view flow-matching model for generative novel view synthesis that separates "reconstruction" of pixels visible in source views from "generation" of disoccluded pixels, using an observation mask and a monocular depth estimator to guide a backbone that jointly denoises RGB and scene-coordinate maps, followed by pixel-space refinement.
**Purpose:** Existing generative NVS methods apply one uniform loss to both reconstructable and purely generative regions, blurring the line between geometric fidelity and hallucination.
**Breakthrough:** The authors report the best reconstruction fidelity in observed regions and higher perceptual quality than purely generative baselines in unobserved regions on RealEstate10K, DL3DV-10K and Mip-NeRF 360, for single-view extrapolation and two-view interpolation.
**Tools & method:** Multi-view flow-matching backbone; observation mask from source cameras; monocular depth front-end; evaluated on RealEstate10K, DL3DV-10K, Mip-NeRF 360.
**Limitation:** The authors state the method inherits the limitations of its monocular depth front-end, that compute limits training to a small number of views per scene, and that Gen3C beats it on relative-pose metrics for RealEstate10K narrow-baseline cases.
