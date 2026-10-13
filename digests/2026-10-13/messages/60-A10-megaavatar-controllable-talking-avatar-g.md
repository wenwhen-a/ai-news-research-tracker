**[A10] MegaAvatar: Controllable Talking Avatar Generation**
- **arXiv:** 2609.39273 · <https://arxiv.org/abs/2609.39273>
- **Submitted:** 2026-09-30
- **Authors:** Junyao Gao, Sibo Liu, Weidong Zhang, Cairong Zhao, Jun Zhang
- **Qualifying affiliation(s):** Tencent — Junyao Gao, Sibo Liu, Weidong Zhang (listed as "Affiliation: Tencent"; footnote: "done during Junyao Gao's internship at AIPD, Tencent")
- **Categories:** cs.CV
- **Open release:** none yet — authors state code, dataset, and models "will be released on GitHub" (not yet confirmed live)
- **Shipped counterpart:** none found

**Summary:** MegaAvatar is a controllable talking-avatar generation framework built on the Wan2.2-TI2V-5B video diffusion model.
**Purpose:** The authors aim to generate talking avatar videos with controllable full-body and head motion, fine-grained expression, and preserved identity, rather than face-only talking-head synthesis.
**Breakthrough:** The authors report high-quality results with controllable body and head motion and consistent identity preservation across different resolutions and video lengths.
**Tools & method:** Built on Wan2.2-TI2V-5B; adds a lightweight 3D convolutional encoder for dense SMPL-X mesh frames, audio and face cross-attention modules, and an audio-to-SMPL-X motion predictor.
**Limitation:** The abstract/HTML reviewed did not state explicit acknowledged limitations or quantitative benchmark numbers beyond qualitative claims of "high-quality" and "controllable" results.
