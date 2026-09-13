**[A24] FaceSnap: Real-Time Personalized Lightstage Facial Performance Capture**
- **arXiv:** 2608.31033 · https://arxiv.org/abs/2608.31033
- **Submitted:** 2026-08-31
- **Authors:** Rukhshanda Hussain, Noé Artru, Emeline Got, Luiz Gustavo Hafemann, Alexandre Messier, Brandon Dearlove, Rafael M. O. Cruz, Abdallah Dib, Eric Granger
- **Qualifying affiliation(s):** Ubisoft (La Forge) — Emeline Got, Luiz Gustavo Hafemann, Alexandre Messier, Brandon Dearlove, Abdallah Dib
- **Categories:** cs.CV
- **Open release:** none (the Multi4D benchmark is announced)
- **Shipped counterpart:** none found

**Summary:** A two-stage framework that amortises expensive lightstage multi-camera sessions into a reusable personalised model, then tracks facial performance in real time from a single camera at 83 fps, with a personalised residual upscaler recovering subject-specific detail. The authors also introduce Multi4D, a benchmark for topology-invariant 4D facial reconstruction.
**Purpose:** Lightstage capture for production digital humans needs costly camera arrays, hours of compute and large storage; the aim is to keep that fidelity while enabling monocular real-time capture after one personalisation step.
**Breakthrough:** The authors report 0.92 mm average point-to-surface error at about 12 ms per frame on an NVIDIA RTX A6000 versus 1.24 mm for Topo4D, LPIPS 0.0497 versus 0.0503 (Topo4D) and 0.0698 (fine-tuned ESRGAN), and roughly 5,000x speedup over Topo4D and 25,000x over production pipelines.
**Tools & method:** A personalised geometry-and-appearance model optimised once from multi-view capture, then a real-time single-camera tracker and upscaler; data from a 24-camera, 60 fps, 4K lightstage (3 subjects) and Multi4D (6 Multiface subjects, about 7,600 frames, 38 views).
**Limitation:** The authors state the dynamic appearance model runs at 512x512 and "may lose fine details such as micro-wrinkles" that offline methods capture.
