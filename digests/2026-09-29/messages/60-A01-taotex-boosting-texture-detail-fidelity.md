**[A01] TaoTex: Boosting Texture Detail Fidelity for Native 3D Material Generation**
- **arXiv:** 2609.34934 · <https://arxiv.org/abs/2609.34934>
- **Submitted:** 2026-09-28
- **Authors:** Xiuchao Wu, Shuichang Lai, Jiangjing Lyu, Chengfei Lyu
- **Qualifying affiliation(s):** Alibaba Group — all authors
- **Categories:** cs.CV
- **Open release:** none found (no GitHub, project page, weights, or demo mentioned)
- **Shipped counterpart:** none found

**Summary:** TaoTex is a diffusion-based model for native 3D material/texture generation that targets texture-detail fidelity, using a data construction agent, multi-level feature fusion, and a latent-to-pixel loss transition.
**Purpose:** The paper addresses texture-reconstruction limitations of existing native 3D generation methods, particularly loss of high-frequency detail and inconsistency across viewpoints.
**Breakthrough:** The authors report single-view PSNR of 25.15 (vs. 21.92 for TRELLIS.2), SSIM of 0.914 (vs. 0.879), and LPIPS of 0.049 (vs. 0.096).
**Tools & method:** A data construction agent uses Qwen-3.8 (MLLM) to write Blender scripts for procedural geometry and Qwen-Image-3.0-Pro for UV-space texture synthesis, producing 50K high-frequency-textured (HFT) assets to fill dataset gaps.
**Limitation:** The authors state TaoTex "remains constrained by voxel resolution when reconstructing minute text or patterns," attributed to GPU memory constraints during high-resolution training.
