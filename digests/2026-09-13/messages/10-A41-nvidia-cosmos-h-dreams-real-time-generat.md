**[A41] NVIDIA Cosmos-H-Dreams: Real-Time Generative Physics Simulation for Surgical Robotics**
- **arXiv:** 2608.24199 · https://arxiv.org/abs/2608.24199
- **Submitted:** 2026-08-25
- **Authors:** Javier Gamazo Tejero et al.
- **Qualifying affiliation(s):** NVIDIA — Javier Gamazo Tejero, Lukas Zbinden, Keyur Sheth, Raghavendra K M, Nadim Daher, Mahdi Azizian, Sean D. Huver (co-authors at CMR Surgical)
- **Categories:** cs.RO
- **Open release:** weights and code (https://github.com/isaac-for-healthcare/Cosmos-H-Dreams; https://huggingface.co/nvidia/Cosmos-H-Dreams; https://huggingface.co/nvidia/Cosmos-H-Surgical-Simulator)
- **Shipped counterpart:** none found

**Summary:** A real-time surgical world-model system combining an action-conditioned generative model, a teacher-to-student distillation recipe and a deployment stack on the NVIDIA FlashDreams streaming-inference library, built on Cosmos-H-Surgical-Simulator fine-tuned on the Open-H-Embodiment corpus.
**Purpose:** An interactive generative simulator for surgical robotics, since animal and cadaver labs are costly and classical simulators struggle with photorealism and deformable tissue.
**Breakthrough:** The authors report the distilled student streams at roughly 160 inference FPS on one NVIDIA RTX PRO 6000 Blackwell GPU and call it "the first interactive surgical world model supporting live human and policy control"; distillation raises FVD from 170.1 to 265.4 and LPIPS from 0.086 to 0.121 relative to the teacher.
**Tools & method:** Control via browser keyboard over WebRTC, a Meta Quest over WebXR, CMR Surgical's Versius console and learned policies; Self Forcing distillation to a causal few-step student.
**Limitation:** The authors state the real-time regime "carries a measurable fidelity cost," that "scenes with thin, self-interacting structures degrade most," and that the student sometimes hallucinates suture thread geometry where it folds or crosses.
