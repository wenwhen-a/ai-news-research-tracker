**[A03] Zing-0.5: Toward Playable Worlds with Real-Time Joint Action and Text Control**
- **arXiv:** 2609.17909 · <https://arxiv.org/abs/2609.17909>
- **Submitted:** 2026-09-15 (v1)
- **Authors:** Mingyang Chen et al.
- **Qualifying affiliation(s):** SeedLeap.ai (all authors) — FLAG: borderline (company not on the core qualifying list; standing unverified)
- **Categories:** cs.CV; cs.LG
- **Open release:** weights | code — <https://huggingface.co/seedleap/zing-0.5,> <https://github.com/seedleap/zing-world-model,> <https://github.com/seedleap/Zing-SGLang;> project page <https://zing.loopit.me/>
- **Shipped counterpart:** none found

**Summary:** The paper presents Zing-0.5, a 5B-parameter autoregressive world model built for "playability," letting users explore generated worlds and influence unfolding events via joint keyboard and real-time text control.
**Purpose:** The authors aim to build an interactive world model where users can both navigate and cause persistent event changes through natural-language instructions, rather than navigation-only control.
**Breakthrough:** The authors report three technical contributions: unified action-and-text conditioning learned jointly with magnitude-aware keyboard inputs and temporally aligned text instructions; event-scale supervision using distribution-matching distillation from a segment-level teacher to a block-level causal student; and four-step generation with context-preserving streaming enabling 832×480 real-time inference at 24 FPS at an estimated $0.009 per stream-minute server cost.
**Tools & method:** Zing-0.5 is a 5B autoregressive world model trained with jointly annotated action-and-text video data, using a segment-level teacher model distilled into a block-level causal student via distribution-matching distillation.
