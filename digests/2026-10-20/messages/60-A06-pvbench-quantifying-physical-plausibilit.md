**[A06] PVBench: Quantifying Physical Plausibility in Video Generation with Object-Level Physical Measurements**
- **arXiv:** 2610.26711 · <https://arxiv.org/abs/2610.26711>
- **Submitted:** 2026-10-19
- **Authors:** Kaiwei Chen, Moran Li, Zhenye Gan, Yabiao Wang, Chengjie Wang, Kexin Zhang, Yong Liu, Jiangning Zhang
- **Qualifying affiliation(s):** Tencent — Tencent Youtu Lab
- **Categories:** cs.CV
- **Open release:** none (authors state intent to release the benchmark, prompts, and calibration protocol, but no link was found)
- **Shipped counterpart:** none found

**Summary:** PVBench scores the physical plausibility of generated videos across 46 dimensions spanning seven domains, using 600 paired text-to-video/image-to-video prompt groups (30% involving embodied agents such as robot arms and humanoids).
**Purpose:** To move evaluation of video generation from semantic impressions toward computable physical quantities checked against physical laws, moving video generation from "looking good" to "physically usable" as the authors put it.
**Breakthrough:** The authors evaluate six T2V/I2V model configurations (~7,200 videos total), including MiniMax H3, SANA-Video 2.0, Wan2.1, Wan2.2, Seedance 2.5, and LingBot-Video, reporting the protocol's physical scores track human judgment while most benchmark dimensions remain unresolved by current generators.
**Tools & method:** Paired T2V/I2V prompt groups were drafted with GPT-5.6 and screened by humans; reference images were made with GPT-image-2; a multimodal LLM scores only dimensions that are hard to quantify numerically (materials, phase change).
**Limitation:** The authors note results depend on specialized vision models and that unobservable cases are skipped; material and phase-change dimensions still rely on MLLM scoring rather than measurement, and most dimensions lack ground-truth references.
