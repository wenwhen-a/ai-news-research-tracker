**[A08] World Models Need a Physical Registry: Learning Internal Predictive States for Physically Plausible World Models**
- **arXiv:** 2610.16365 · <https://arxiv.org/abs/2610.16365>
- **Submitted:** 2026-10-12
- **Authors:** Shinseong Kim, Jaeseok Jeong, Jianlong Fu, Youngjung Uh
- **Qualifying affiliation(s):** Microsoft — Shinseong Kim (joint Yonsei/Microsoft Research Asia), Jianlong Fu (Microsoft Research Asia)
- **Categories:** cs.AI (ACM classes I.2.10, I.4.8)
- **Open release:** none found (project page only: grainsack.github.io/physical-registry/)
- **Shipped counterpart:** none found

**Summary:** The paper introduces the Physical Registry, a set of temporally grounded registry slots inside a video diffusion transformer that hold an explicit, readable predictive-dynamics state separate from appearance tokens.
**Purpose:** Current video world models encode appearance and dynamics jointly in standard tokens, giving no distinct, readable state for learning or auditing predicted physical evolution.
**Breakthrough:** The authors report Physical Registry improves vanilla fine-tuning by 9.9/8.7 points on Physics-IQ I2V/V2V, the largest gain among interfaces compared (vs. REPA, cross-attention, AdaLN, joint generation).
**Tools & method:** Registry slots are initialized from an observation-conditioned forecast, co-evolve with video tokens, and receive future-representation supervision from a frozen V-JEPA 2.1 ViT-g encoder.
**Limitation:** The authors report instruction-following scores on WorldModelBench decrease slightly for Cosmos v2.5 and WAN TI2V-5B even as physical adherence improves, and sampling cost rises to 1.55–1.67× per step.
