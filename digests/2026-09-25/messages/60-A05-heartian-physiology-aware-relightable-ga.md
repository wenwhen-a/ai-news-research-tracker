**[A05] Heartian: Physiology-Aware Relightable Gaussian Head Avatar**
- **arXiv:** 2609.28539 · <https://arxiv.org/abs/2609.28539>
- **Submitted:** 2026-09-22
- **Authors:** Xiaoyue Fan, Jose Echevarria, Akshay Paruchuri, Kaan Akşit
- **Qualifying affiliation(s):** Adobe — Jose Echevarria listed at Adobe Research (other authors at UCL and Stanford)
- **Categories:** cs.CV, cs.GR
- **Open release:** none stated
- **Shipped counterpart:** none found

**Summary:** Heartian addresses the fact that conventional Gaussian head avatars treat facial appearance as temporally static, ignoring the subtle cardiac-induced skin-color changes (remote photoplethysmography, or rPPG) that a real face exhibits.
**Purpose:** The goal is to make head avatars physiologically plausible — carrying a detectable, non-contact-measurable heartbeat signal — without degrading the avatar's visual reconstruction quality.
**Breakthrough:** The authors report a pooled heart-rate mean absolute error of 0.29 bpm (0.38% MAPE) when reading the signal directly off the avatar's attributes, and 0.97 bpm MAE (1.21% MAPE) when recovering it from rendered video using a motion-augmented TS-CAN model on the MMPD dataset.
**Tools & method:** After training a baseline Gaussian head reconstruction, a second stage optimizes a per-frame albedo modulation on skin-region Gaussians only, combining a two-Gaussian fundamental waveform (capturing systolic/diastolic peaks in cardiac phase) with a lightweight MLP spatial residual conditioned on cardiac phase, beat identity, and position.
**Limitation:** The authors note sensitivity to large initial ground-truth PPG spikes during capture, which introduce visual artifacts, and reduced effectiveness for skin tones with lower green-channel reflectance or under warm/high-intensity LED lighting, since the method modulates the green channel directly.
