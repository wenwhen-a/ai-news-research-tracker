**[A09] Clean Forcing: Drift-Resistant Autoregressive Video Diffusion with a Frozen Base**
- **arXiv:** 2610.25634 · <https://arxiv.org/abs/2610.25634>
- **Submitted:** 2026-10-19
- **Authors:** Wenqing Wang et al.
- **Qualifying affiliation(s):** NVIDIA — Jonathan Tremblay, Chan Hee Song (affiliation block lists NVIDIA alongside Seoul National University and Northeastern University; footnote states one author's work was done during an NVIDIA internship and two authors are co-last authors)
- **Categories:** cs.CV, cs.LG
- **Open release:** demo (paper states "representative rollouts appear on the project page"; no link found in fetched text)
- **Shipped counterpart:** none found

**Summary:** Autoregressive video diffusion models generate streaming video by conditioning each chunk on previously generated (imperfect) frames, which causes compounding "drift" that degrades quality within seconds.
**Purpose:** The paper targets exposure bias in autoregressive video diffusion used for long, streaming video generation — including the kind of real-time generative world models used for driving and game simulation — where prior fixes required expensive full retraining or gave inconsistent training-free corrections.
**Breakthrough:** On 50-second text-to-video generation with Wan2.1-T2V-1.3B, the authors report Δ-drift falling from +11.3 (adapted base) to +1.65 using zero real videos, and to −0.16 using 40 real clips, which they say beats the best published result (+3.57) while using over 150× less data.
**Tools & method:** The corrector is a rank-16 LoRA (5.9M params, 0.4% of the base) on the q/k/v/o self-attention projections across all 30 DiT blocks, trained with AdamW; evaluation uses 128 held-out MovieGenVideoBench prompts and VBench + Δ-drift (MUSIQ-based) metrics.
