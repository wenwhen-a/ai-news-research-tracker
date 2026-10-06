**[A01] Real-time Rendering of Pre-integrated Neural Emitters**
- **arXiv:** 2610.06762 · <https://arxiv.org/abs/2610.06762>
- **Submitted:** 2026-10-05
- **Authors:** Arno Coomans et al.
- **Qualifying affiliation(s):** Huawei Technologies — Floor Verhoeven, Edoardo A. Dominici, Markus Steinberger (FLAG: borderline)
- **Categories:** cs.GR
- **Open release:** none confirmed
- **Shipped counterpart:** none found

**Summary:** The paper introduces Neural Emission Fields (NEF), a neural field that precomputes direct illumination in the volume around a light emitter, conditioned on position, normal, view direction and material, so that rendering requires only a single network evaluation per shading point instead of runtime integration.
**Purpose:** Real-time integration of illumination from complex-shaped, textured or deforming light emitters is computationally expensive; the authors aim to move that integration offline into a reusable, transformable lighting asset.
**Breakthrough:** The authors report diffuse NEF evaluation in 1.2 ms and glossy NEF evaluation in 2.5 ms at 1920×1080 on an RTX 4090, inherently handling internal reflections, self-occlusion, spatially-varying emission and mesh deformation "at zero additional runtime cost," with training times from 1 minute (simple planar emitters) to 3 hours (complex interreflections).
**Tools & method:** NEF uses a dual-architecture neural network trained in the emitter's local coordinate frame, evaluated on scenes including Sponza, Bistro, Cornell Box and custom emitter geometries (Pierced Sphere, Dragon mesh, Lattice Box, Whiteroom, Living Room) against LTC and ReSTIR DI baselines using FLIP and relative MSE metrics, on an RTX 4090.
