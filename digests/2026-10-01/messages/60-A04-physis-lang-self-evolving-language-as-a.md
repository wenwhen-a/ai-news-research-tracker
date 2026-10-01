**[A04] Physis-Lang: Self-Evolving Language as a Physical Representation for Video World Model**
- **arXiv:** 2609.40358 · <https://arxiv.org/abs/2609.40358>
- **Submitted:** 2026-09-30
- **Authors:** Liming Lu et al. (17 authors)
- **Qualifying affiliation(s):** NVIDIA — Liming Lu, Wenhang Ge, Yuchao Gu, Yunze Liu, Han Cai, Ming-Yu Liu, Song Han et al. (most of the author list); co-authors also from University of Oxford and MIT
- **Categories:** cs.CV
- **Open release:** none (no code, weights, or demo link found on the abstract page or in the paper)
- **Shipped counterpart:** none found

**Summary:** Video world models often generate visually plausible videos that violate basic physical principles, and this paper argues language has not yet been fully exploited as a representation of physical processes.
**Purpose:** The authors aim to make physical plausibility an explicit, optimizable training signal rather than something video generators must infer implicitly from pixels.
**Breakthrough:** The authors report consistent improvements on four physical-video benchmarks when fine-tuning Wan and Cosmos3 backbones with Physis-Lang-curated data: PhyGenBench 61.67→71.04, Physics-IQ Verified 40.23→43.41, VideoPhy-2 60.41→68.02, and PhyGround 65.18→69.90. They report that their Cosmos3-Nano-based models surpass the proprietary Veo 3.1 model on three of these four benchmarks, and that distilling a 4B "PhysThinker" vision-language model cut their re-captioning cost from about $24.12K to near $0.
**Tools & method:** The pipeline combines an iterative, GPT-5.5-based physics-aware captioning/critic loop, deficiency-guided video retrieval that converts model weaknesses into text queries, and fine-tuning on a curated 183K video-caption dataset (71K filtered WISA-80K + 112K retrieved).
