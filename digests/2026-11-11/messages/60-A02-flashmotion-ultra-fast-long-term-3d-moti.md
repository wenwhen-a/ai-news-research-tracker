**[A02] FlashMotion: Ultra-Fast Long-Term 3D Motion Generation**
- **arXiv:** 2611.13626 · <https://arxiv.org/abs/2611.13626>
- **Submitted:** 2026-11-10
- **Authors:** Kaixing Yang et al.
- **Qualifying affiliation(s):** Tencent — Mingshuang Luo, Zijiao Zeng ("This work was conducted at Tencent IEG Motus Group")
- **Categories:** cs.CV
- **Open release:** none found
- **Shipped counterpart:** none found

**Summary:** FlashMotion is a framework for generating long 3D human motion sequences — text-to-motion, music-to-dance, and speech-to-gesture — under a tight inference budget.
**Purpose:** The authors target existing motion-generation methods being too slow for long-sequence or interactive use, aiming to cut both the number of required sampling steps and the compute cost per step.
**Breakthrough:** The authors report their 4-step model reaches 46,303 FPS at 10,000 frames on BABEL text-to-motion — 13.6× the throughput of the fastest external text-to-motion baseline they compare against — while reporting mixed quality results: FID of 0.907 on BABEL trails FloodDiffusion's 0.542, and FIDg of 21.13 on FineDance trails FlowerDance's 19.59, though FIDk (15.15 vs. 29.73) and BEAT2 FGD (0.3242 vs. SemTalk's 0.356) lead.
**Tools & method:** The method uses kinematic/dynamic-consistency-constrained MeanFlow sampling plus an Adaptive Soft masking mechanism for motion editing, evaluated on BABEL, FineDance, and BEAT2; benchmarks ran on an NVIDIA RTX 3090 GPU with an Intel Xeon Gold 5218 CPU, and a mobile test generated 200 frames in ~400ms on an iPhone 17.
**Limitation:** The paper has no dedicated limitations section; the conclusion lists future directions (finer facial/finger modeling, reducing motion artifacts in longer-sequence generation) and the method section notes 1-step sampling does not support motion editing.
