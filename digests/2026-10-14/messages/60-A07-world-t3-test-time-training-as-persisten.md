**[A07] World-T3: Test-Time Training as Persistent Memory for Real-Time Video World Models**
- **arXiv:** 2610.17434 · <https://arxiv.org/abs/2610.17434>
- **Submitted:** 2026-10-12
- **Authors:** Junyi Wu, Zekun Li, Chenhongyi Yang, Chen Guo, Lingchen Yang, Yongan Zhang, Xinyi Zhang, Hongbing Hu, Bartek Rymkowski, Srinath Sridhar, Yan Yan, Xijie Huang
- **Qualifying affiliation(s):** Meta — Junyi Wu, Zekun Li, Chenhongyi Yang, Chen Guo, Lingchen Yang, Yongan Zhang, Xinyi Zhang, Hongbing Hu, Bartek Rymkowski, Xijie Huang (all Meta Reality Labs, several with joint academic appointments at UIC/Brown)
- **Categories:** cs.CV (primary); cs.AI; cs.MM
- **Open release:** none found (project page only: adreamwu.github.io/World-T3/, no code/weights link)
- **Shipped counterpart:** none found

**Summary:** World-T3 is a camera-controlled, autoregressive video world model that stores past observations in dedicated test-time-trained model parameters rather than a growing context window, so memory and per-step compute stay constant as rollouts lengthen.
**Purpose:** Long-horizon interactive video world models need to "remember" previously seen parts of a scene when the camera revisits them, but standard approaches either truncate context or grow memory/compute unboundedly.
**Breakthrough:** The authors report that a recursive-least-squares update, keyed by camera pose, consolidates observations into persistent "fast weights" inside the generator.
**Tools & method:** Built on Wan2.2-TI2V-5B and trained on a curated 908K-clip corpus (601K base + 307K revisit-augmented, mixing real footage and game-engine renders with ground-truth poses), using camera poses from 3D foundation models such as VGGT-Ω.
**Limitation:** The authors state the method depends on external camera-pose estimators, which can drift under weak texture or fast motion and misalign the pose-keyed memory retrieval, with errors compounding over long horizons.
