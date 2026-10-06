**[A05] Kandinsky 6.0 Video: Foundation Models for Synchronized Video and Audio Generation**
- **arXiv:** 2610.05608 · <https://arxiv.org/abs/2610.05608>
- **Submitted:** 2026-10-04
- **Authors:** Team Kandinsky et al.
- **Qualifying affiliation(s):** Sber (FLAG: borderline) — "Team Kandinsky" contributors are identified in the paper as Sber's Kandinsky Lab, with Cloud.ru (Sber-affiliated cloud infrastructure) also named; individual per-author institution tags were not resolvable from the retrieved text beyond the group-level attribution
- **Categories:** cs.CV, cs.AI, cs.LG, cs.MM
- **Open release:** code (<https://github.com/kandinskylab/kandinsky-6>) | weights (<https://huggingface.co/collections/kandinskylab/kandinsky-60-diffusers>) | demo/project page (<https://kandinskylab.ai>)
- **Shipped counterpart:** none found

**Summary:** Kandinsky 6.0 Video introduces two diffusion foundation models — Lite (3B parameters) and Pro (29B parameters) — for synchronized video and audio generation, producing 5-second clips with synchronized 44 kHz audio including lip-sync across multiple generation modes.
**Purpose:** The authors aim to provide an open foundation model family that jointly generates visually and acoustically synchronized video, rather than video and audio as separate, unsynchronized outputs.
**Breakthrough:** The authors report that the Pro model outperforms its predecessor and performs competitively against comparable systems, built on a dual-stream CrossDiT architecture connecting a pretrained video stream and a newly trained audio stream via bidirectional cross-attention, trained through pretraining, fine-tuning, reinforcement-learning optimization and distillation stages.
**Tools & method:** The model family was developed by Sber's Kandinsky Lab team with infrastructure support from Cloud.ru; the authors release model weights, source code, and a diffusers integration under the MIT license.
