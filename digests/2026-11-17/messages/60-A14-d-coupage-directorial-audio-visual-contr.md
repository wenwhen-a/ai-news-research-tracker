**[A14] Découpage: Directorial Audio-Visual Control for Long Multi-Shot Video Generation**
- **arXiv:** 2611.18866 · <https://arxiv.org/abs/2611.18866>
- **Submitted:** 2026-11-13 (v1)
- **Authors:** Yifan Wang et al.
- **Qualifying affiliation(s):** Ant Group (affiliation listed for the author group alongside HKUST and Zhejiang University; the HTML rendering lost the footnote markers linking individual names to institutions, so the specific Ant Group author(s) could not be individually confirmed); FLAG: borderline — Ant Group
- **Categories:** cs.AI (cross-listed cs.SD)
- **Open release:** demo — project page <https://wyf0824.github.io/decoupage/> (authors state code will be released "upon publication," no link yet)
- **Shipped counterpart:** none found

**Summary:** DECOUPAGE is a screenplay-driven framework for generating long, multi-shot, multi-character videos with synchronized but independently-timed audio and visual tracks, addressing cinematic effects like dialogue that bridges across cuts (J-/L-cuts) and deliberate silences.
**Purpose:** Existing audio-visual generative frameworks couple visual and audio timing by default and lack mechanisms to coordinate independent visual/acoustic timing over long, multi-shot narratives, causing them to hallucinate speech during intended silences or drive mouth movement on off-screen/silent listeners.
**Breakthrough:** On their 15-second benchmark the authors report Cut F1 of 0.99 versus 0.28 for the strongest baseline (MiniMax-H3), word error rate of 4.59% versus 10.23%, containment of 93.01% versus 41.95%, and silence leakage of 1.12% (best overall).
**Tools & method:** The system fine-tunes the LTX-2.3 Base joint audio-video diffusion backbone with LoRA (rank 32), adding dual-schedule temporal cross-attention and a directorial lip-sync mechanism that selectively decouples speech conditioning from visual facial dynamics during off-screen dialogue.
