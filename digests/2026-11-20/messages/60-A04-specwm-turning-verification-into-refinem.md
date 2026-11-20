**[A04] SpecWM: Turning Verification into Refinement for Streaming World Models**
- **arXiv:** 2611.26211 · <https://arxiv.org/abs/2611.26211>
- **Submitted:** 2026-11-19
- **Authors:** Jiaming Li, Lingzhen Li, Xiaze Yang, Chenyu Zhu, Kaiqi Liu, Xiaotong Zhao, Songlian Li, Toyota Li, Alan Zhao, Haobin Zhong, Yue Ma, Zhiyuan Ma
- **Qualifying affiliation(s):** Tencent — Jiaming Li, Xiaotong Zhao, Songlian Li, Toyota Li, Alan Zhao, Haobin Zhong
- **Categories:** cs.CV
- **Open release:** none found
- **Shipped counterpart:** none found

**Summary:** SpecWM is a training-free inference framework for streaming video world models that verifies draft video chunks using the target model's own latent velocity field rather than an external reward model, and reuses that verification as a correction signal.
**Purpose:** The authors note larger streaming world models give better quality and control but run slowly, while smaller draft models run fast but less accurately, and existing reward-based speculative methods regenerate rejected chunks wholesale with no reusable correction.
**Breakthrough:** On WBench Navigation (LingBot-World 2.0, 1.3B draft/14B target), the authors report a 1.63× speedup over target-only generation while raising NavScore from the draft's 75.99 to 85.63, versus 85.49 for target-only.
**Tools & method:** Each draft chunk gets one final-stage target-model probe whose prediction can be committed directly or used as a seed for 2-3 further target denoising steps, with refinement intensity tied to control-change transitions and a fallback to target-only generation after two consecutive rejections.
**Limitation:** The paper has no dedicated limitations section, but the text implies thresholds are calibrated on a small set of 20 cases and then fixed, and draft/target models must share a latent space, chunk length, and control interface, with cross-model latent alignment named as future work.
