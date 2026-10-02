**[A07] 4Director: Controlling Video World Models with Rigid 3D Geometry**
- **arXiv:** 2610.02160 · <https://arxiv.org/abs/2610.02160>
- **Submitted:** 2026-10-01
- **Authors:** Wei Cao et al.
- **Qualifying affiliation(s):** Stability AI — Wei Cao, Hao Zhang, Vikram Voleti, Yuqun Wu, Mallikarjun B R, Shimon Vainer, Mark Boss; FLAG: borderline (not on the explicit qualified-company list but a comparable top-tier lab)
- **Categories:** cs.CV
- **Open release:** demo (project page with video results: <https://stability-ai.github.io/4director/>)
- **Shipped counterpart:** none found

**Summary:** 4Director is a video world model conditioned on an explicit 4D scene representation: each object is reconstructed once from an input image as a canonical mesh, and its motion is specified by one prescribed rigid transformation per frame.
**Purpose:** The authors target a gap in prior motion-control methods, which control objects only coarsely via image-plane cues (ambiguous in depth/rotation) or via 3D tracks/blobs that lack complete geometry and lose consistency across viewpoint changes.
**Breakthrough:** The authors report that conditioning on explicit per-object rigid 3D geometry gives precise camera and object trajectory control while the generator still synthesizes realistic appearance and lighting, evaluated on their new RealCOD-Rigid dataset of 20,774 annotated clips.
**Tools & method:** Training ran for three epochs on 24 GPUs at 832×480 resolution with 81 frames, using AdamW with a peak learning rate of 5×10⁻⁵, a Motion Adapter initialized from released VACE branch weights, and the RealCOD-Rigid dataset derived from RealCOD-25K.
**Limitation:** The authors state the representation controls motion only at the rigid-body level, so an articulated or deforming object moves as one whole; finer motion such as running, jumping, or limb movement cannot be prescribed and is left to the generator.
