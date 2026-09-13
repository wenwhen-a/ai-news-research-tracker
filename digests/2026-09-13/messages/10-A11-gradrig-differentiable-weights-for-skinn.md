**[A11] GradRig: Differentiable Weights for Skinned Gaussian Splat Deformation**
- **arXiv:** 2609.05127 · https://arxiv.org/abs/2609.05127
- **Submitted:** 2026-09-04
- **Authors:** Nina Vesseron, Élie Michel
- **Qualifying affiliation(s):** Adobe — Nina Vesseron (also ENSAE-CREST), Élie Michel
- **Categories:** cs.GR
- **Open release:** none stated
- **Shipped counterpart:** none found

**Summary:** GradRig deforms 3D Gaussian splats with skinning by using spatial gradients of skinning weights, since splats lack mesh connectivity and rigid per-splat transforms open holes when shapes stretch; an optional adaptive resampling splits problematic splats.
**Purpose:** Mesh-free rigged deformation of Gaussian-splat representations at real-time rates.
**Breakthrough:** The authors report more accurate stretching than rigid-only transformation while keeping real-time rendering, compared against RigAnything (Liu et al., 2025).
**Tools & method:** Skinning-weight gradients plus adaptive resampling; scenes from 85K to 850K splats; benchmarked on an Apple M1 Max (32 GB) in a WebGL viewer.
**Limitation:** The authors state that storing weight gradients adds memory overhead, that linear interpolation does not improve their dictionary lookup, and that resampling applies to the rest shape rather than the deformed shape.
