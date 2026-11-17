**[A05] DuoFlow: Towards Synchronized Speech and Motion Generation with Fine-Grained Control**
- **arXiv:** 2611.21530 · <https://arxiv.org/abs/2611.21530>
- **Submitted:** 2026-11-16 (v1)
- **Authors:** Jun Dong et al.
- **Qualifying affiliation(s):** Tencent — Di Kang, Linchao Bao (other co-authors at Tsinghua University)
- **Categories:** cs.CV
- **Open release:** none — only a project page (<https://jundong-dev.github.io/DuoFlow-project-page/>) is mentioned; no code or weights release stated
- **Shipped counterpart:** none found

**Summary:** Existing joint speech-motion generation models only implicitly condition on transcript semantics or speech features, giving little explicit control over motion hierarchy, body parts, or vocal style.
**Purpose:** To give embodied-speaker generation (synchronized voice + body motion) fine-grained, explicit control over vocal style and motion at the body-part/hierarchy level, rather than only implicit control via text or speech embeddings.
**Breakthrough:** The authors report DuoFlow achieves 4.71% word error rate and 0.94 speaker similarity versus 6.12%/0.80 for a CosyVoice2+MambaTalk cascade baseline, and 87.43%/90.40% pairing accuracy at two granularity levels versus the next-best baseline's 61.37%/62.68% (Motion-Omni).
**Tools & method:** DuoFlow uses a dual-stream latent flow transformer with a shared noise level and a unified second-based temporal coordinate, modality-specific residual connectors to inject hierarchical conditions, layer-wise bidirectional cross-modal attention, and a monotonic phoneme pathway with CTC supervision for speech-motion temporal alignment; it was trained on the new MotionSpeech dataset (34,950 clips, ~125.2 hours) using 8×A100 GPUs per stage.
