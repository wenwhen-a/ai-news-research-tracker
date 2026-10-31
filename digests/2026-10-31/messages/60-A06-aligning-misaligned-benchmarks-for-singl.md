**[A06] Aligning Misaligned Benchmarks for Single-View Novel View Synthesis**
- **arXiv:** 2610.38349 · <https://arxiv.org/abs/2610.38349>
- **Submitted:** 2026-10-28
- **Authors:** Yang-Che Tseng, Erqun Dong, Jeong-gi Kwak, Gopal Sharma, Shakiba Kheradmand, Stephan Garbin, Hossam Isack, Kwang Moo Yi
- **Qualifying affiliation(s):** Google — Stephan Garbin, Hossam Isack
- **Categories:** cs.CV, cs.AI
- **Open release:** none (no project page, code, or demo link found on the abstract page)
- **Shipped counterpart:** none found

**Summary:** The authors argue that single-view novel-view-synthesis methods are hard to compare fairly because each method's output must first be pose-aligned to ground truth, and common test-time pose optimization is ill-posed, leaving methods evaluated at arbitrary local optima.
**Purpose:** The goal is to standardize evaluation for single-view novel view synthesis by removing the confound of ill-posed test-time pose optimization, so method comparisons reflect actual reconstruction quality rather than alignment artifacts.
**Breakthrough:** The authors report that, under their corrected alignment and co-visible-region evaluation, explicit 3D Gaussian methods achieve state-of-the-art results.
**Tools & method:** The method replaces test-time pose optimization with traditional 2D-to-2D and 2D-to-3D image matching to align 3D reconstructions to ground truth, then restricts evaluation metrics to the co-visible regions between views.
**Limitation:** The authors state that while their findings could apply to other novel-view-synthesis settings, such as few-shot or dynamic novel view synthesis, they have not yet explored those extensions.
