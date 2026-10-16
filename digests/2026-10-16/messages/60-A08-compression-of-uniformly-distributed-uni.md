**[A08] Compression of Uniformly Distributed Unit Quaternions**
- **arXiv:** 2610.22052 · <https://arxiv.org/abs/2610.22052>
- **Submitted:** 2026-10-15 (v1, 15:19:24 UTC)
- **Authors:** Carsten Faber, Bastian Kuth, Rinaldo Schuster, Daniel Pauls, Quirin Meyer
- **Qualifying affiliation(s):** AMD, Germany — Bastian Kuth, Quirin Meyer (other co-authors at Coburg University of Applied Sciences and Arts, Germany); **FLAG: borderline** (AMD).
- **Categories:** cs.GR
- **Open release:** code (reference C implementation at <https://github.com/GeoFlowResearch/UnitQuaternionCompressionSupplemental>)
- **Shipped counterpart:** none found

**Summary:** The paper compares parameterizations for compressing uniformly distributed unit quaternions, a problem relevant to reducing memory and bandwidth for rotations in computer graphics.
**Purpose:** Unit quaternions are the standard representation for 3D rotations in graphics (skeletal animation, tangent-space normal mapping, Gaussian splatting) but consume significant memory at scale.
**Breakthrough:** The authors report that at 32 bits, ℓ∞cub achieves a compactness factor of 135°, 13.4% below the ℓ∞tan baseline.
**Tools & method:** ℓ∞cub projects quaternions via an ℓ∞ norm, applies a cubic warp with one optimized parameter (a* ≈ 0.373964), and uses mixed-radix packing with range quantization.
**Limitation:** The authors state the analysis assumes uniformly distributed quaternions and does not adapt the coding range per track or segment, so concentrated rotation sets can be coded more compactly by other methods.
