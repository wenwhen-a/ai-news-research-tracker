**[A54] Generalized Audio-Driven Synthesis of Precise Drummer Motion**
- **arXiv:** 2608.19055 · https://arxiv.org/abs/2608.19055
- **Submitted:** 2026-08-19
- **Authors:** Álvaro G. Iñesta, Mattia Ryffel, Amit H. Bermano, Robert W. Sumner, Martin Guay
- **Qualifying affiliation(s):** Disney Research|Studios — Álvaro G. Iñesta, Mattia Ryffel, Robert W. Sumner, Martin Guay; FLAG: borderline (not on the tracked list)
- **Categories:** cs.CV, cs.GR, cs.SD
- **Open release:** none
- **Shipped counterpart:** none found

**Summary:** A diffusion framework that synthesises drumming motion from audio with a dual-objective loss separating body-movement accuracy from stick-tip precision, plus two new metrics, Impact Point Deviation and Percussive Alignment Score; the paper won the Best Paper Award at SCA 2026.
**Purpose:** Music-driven character animation where high-acceleration drumming must stay precisely synchronised with audio.
**Breakthrough:** The authors report Impact Point Deviation falling from 8.4 cm (rotations-only baseline) to 1.9 cm, a Percussive Alignment Score of 0.82 versus 0.68 (baseline) and 0.91 (ground truth), and 92.8% preference over the baseline in a 22-participant study.
**Tools & method:** More than 3.5 hours (1,518,450 frames) of professional drumming captured at 120 Hz on a Roland TD-25KV with nine OptiTrack cameras, augmented to over 25,000 sequences; trained about 48 hours on an NVIDIA RTX 3090.
**Limitation:** The authors state the method needs isolated drum audio (polyphonic music requires stem separation) and assumes a fixed drum-kit layout.
