**[A02] Generative Structure from Motion with Native 3D Diffusion**
- **arXiv:** 2610.35522 · <https://arxiv.org/abs/2610.35522>
- **Submitted:** 2026-10-26
- **Authors:** Haobin Duan, Binbin Huang, Mochu Xiang, Yiqun Zhao, Zibo Zhao, Yi Ma, Shenghua Gao
- **Qualifying affiliation(s):** Tencent — Zibo Zhao (the HTML page's per-author affiliation block tags Zibo Zhao solely with "Tencent"; the other six authors are tagged "The University of Hong Kong" and "Transengram").
- **Categories:** cs.CV, cs.AI
- **Open release:** none found beyond a project page (<https://dotb1ue.github.io/GenSfm/>); no code or weights link was located on that page or in the paper text.
- **Shipped counterpart:** none found

**Summary:** The paper proposes GenSfM, which recovers 3D object structure and camera pose from a few uncalibrated views by integrating image-based 3D reconstruction with a native 3D diffusion model.
**Purpose:** The authors target the gap between classical structure-from-motion methods (geometrically faithful but unable to recover unseen regions) and native 3D generation methods (plausible but not necessarily faithful to input images), and the error cascading that occurs when the two are simply concatenated.
**Breakthrough:** On Toys4k and GSO with 4 uncalibrated views, the authors report GenSfM improves novel-view PSNR by 3.2–4.5 dB and reduces median Chamfer distance by 2.8–3.8x over a strong native-3D generation baseline.
**Tools & method:** The method uses a multi-modal diffusion transformer with shared self-attention to jointly denoise shape and pose latents, a 3D-native UV-volume tokenization, and a pose-aware refinement stage that samples per-voxel image features at recovered camera poses.
**Limitation:** The paper states its results are restricted to object-centric inputs at N=4 views, with scene-level inputs and in-the-wild captures left as future work.
