**[A03] No Distillation Needed: Single-Pass Real-Time Talking Heads via Acausal Noise Shaping**
- **arXiv:** 2610.11070 · <https://arxiv.org/abs/2610.11070>
- **Submitted:** 2026-10-08
- **Authors:** Yu Han, Dejan Markovic, Alexander Richard, Wojciech Zielonka, Akshay Venkatesh, Cheng-hsin Wuu, Michael Zollhoefer
- **Qualifying affiliation(s):** Meta Reality Labs — all authors
- **Categories:** cs.CV
- **Open release:** none stated; project page with supplemental videos — <https://wojciechzielonka.com/facegan/>
- **Shipped counterpart:** none found

**Summary:** Real-time audio-driven facial animation for avatars must generate each output frame from only the audio received so far (streaming/causal), but diffusion models — the current state of the art — need many network passes per frame, which is a poor fit for this setting.
**Purpose:** To produce real-time, streaming, single-pass audio-driven facial animation (expression + head pose) without the multi-step inference cost of diffusion-based talking-head methods or the need for offline distillation.
**Breakthrough:** The authors report FaceGAN achieves the best Sync Score (0.8767) among compared methods (Fallingwater, DiffPoseTalk, MemoryTalker, ARTalk) and competitive FED/FPD, while running at 43.3 ms per frame (12.1x real time) on a single H200, with time-to-first-frame of 83 ms versus 4.20 s for ARTalk.
**Tools & method:** Trained and evaluated on a dataset from Chu et al. (2026) of 34,906 clips from 832 subjects (469.6 hours), with 784 training / 48 test identities and a fixed 64-clip held-out test set; training used 8x NVIDIA H200 GPUs, with single-H200 latency benchmarking.
**Limitation:** FaceGAN is not best on every metric — ARTalk scores better on FPD and Similarity, DiffPoseTalk on FED — and an ablation shows a fully causal variant (zero lookahead) or a causal noise stack both reduce expression/pose quality and diversity.
