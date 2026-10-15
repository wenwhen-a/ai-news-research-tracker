**[A07] Kandinsky S2V 1.0: Audio-Driven Avatar Video Generation**
- **arXiv:** 2610.19290 · <https://arxiv.org/abs/2610.19290>
- **Submitted:** 2026-10-13
- **Authors:** Nikolay Semenov, Artem Riabinin, Sergey Bassenko, Anna Averchenkova, Julia Agafonova, Anastasia Aliaskina, Kirill Kozlov, Lev Novitskiy, Nikita Samsonov, Nikolai Gerasimenko, Denis Dimitrov
- **Qualifying affiliation(s):** Kandinsky Lab (Sber) — all authors; FLAG: borderline — Kandinsky Lab
- **Categories:** cs.CV
- **Open release:** code, model checkpoints, and a diffusers integration, released under the MIT license (per abstract); no specific repo URL found in the page text
- **Shipped counterpart:** none found

**Summary:** Kandinsky S2V 1.0 is an open family of speech-to-video models (a 2B "Lite" and a 21B "Pro" variant) that generate long-form 25 FPS video of a person speaking, driven by a reference image, a speech waveform, and a text prompt.
**Purpose:** The goal is controllable, audio-driven human/avatar animation that stays consistent with speech over long video durations, rather than short clips.
**Breakthrough:** The authors report that in a human side-by-side evaluation, the Pro model performed comparably to or better than an open-source baseline and two commercial models, and was preferred specifically for lip sync.
**Tools & method:** Text and audio conditioning is handled by a Qwen2.5-Omni model, combined with a reference-aware visual memory for identity/appearance consistency; the models are trained on 1.17M single-speaker clips, and the release includes code, checkpoints, and a diffusers integration under the MIT license.
**Limitation:** The training data is limited to single-speaker clips captioned only in English and Russian, which may constrain generalization to other languages or multi-speaker scenes; the retrieved text does not state additional failure modes.
