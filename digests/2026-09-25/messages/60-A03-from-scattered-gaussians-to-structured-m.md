**[A03] From Scattered Gaussians to Structured Maps: Efficient Gaussian Splatting Coding via Dual-phase Morton Sorting**
- **arXiv:** 2609.29041 · <https://arxiv.org/abs/2609.29041>
- **Submitted:** 2026-09-24
- **Authors:** Bolin Chen et al.
- **Qualifying affiliation(s):** Alibaba — Bolin Chen (also Fudan University/Hupan Lab), Ru-Ling Liao and Yan Ye listed at DAMO Academy, Alibaba Group
- **Categories:** cs.MM
- **Open release:** none stated
- **Shipped counterpart:** none found

**Summary:** The paper addresses the storage and bandwidth cost of 3D Gaussian Splatting (3DGS), whose unstructured millions-of-primitives representation resists standard video-codec compression.
**Purpose:** Prior orderings such as PLAS and plain Morton sorting either cost too much to compute or fail to preserve enough spatial coherence once splats are reshaped into a 2D grid; the authors aim for an ordering that is both fast and coherent enough for codec-friendly compression.
**Breakthrough:** The authors report BD-rate gains of 1.29% (RGB-PSNR), 1.69% (YUV-PSNR) and 3.19% (YUV-SSIM) over a plain-Morton baseline, and 1.15%/0.88%/0.45% over PLAS on the same three metrics.
**Tools & method:** The method applies Morton-code (Z-order) sorting to each Gaussian's 3D mean position first, then re-maps that 1D-sorted sequence onto a 2D grid using 2D Morton indexing rather than row-major reshaping, so neighboring 1D indices land on spatially neighboring pixels; the same permutation is applied consistently across position, scale, rotation, opacity, and spherical-harmonics attributes.
**Limitation:** The authors note the gains are scene-dependent: "some challenging content, such as gymnast and flowerdance, exhibits noticeable BD-rate losses, likely due to complex motion and highly non-uniform appearance distributions," and state the method's benefit "can vary depending on scene characteristics" rather than being uniform across content types.
