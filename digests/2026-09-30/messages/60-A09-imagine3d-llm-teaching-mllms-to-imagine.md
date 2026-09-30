**[A09] Imagine3D-LLM: Teaching MLLMs to Imagine 3D Scenes Before Answering**
- **arXiv:** 2609.38177 · <https://arxiv.org/abs/2609.38177>
- **Submitted:** 2026-09-29 (v1)
- **Authors:** Jaewoo Jung, Hyeonseo Yu, Honggyu An, Jisang Han, Mungyeom Kim, Minkyeong Jeon, Heeseong Shin, WonJun Moon, Federico Tombari, Daniel Barath, Marc Pollefeys, Seungryong Kim, Sunghwan Hong
- **Qualifying affiliation(s):** Google — Federico Tombari (rest of team is KAIST AI / ETH Zürich / ETH AI Center)
- **Categories:** cs.CV; cs.CL
- **Open release:** none (project page cvlab-kaist.github.io/Imagine3D-LLM lists code as "Coming Soon")
- **Shipped counterpart:** none found

**Summary:** The paper trains multimodal LLMs to build a compact 3D scene representation before answering spatial questions, rather than reasoning directly over raw pixels.
**Purpose:** MLLMs are weak at 3D spatial reasoning because they rely on pixel-level detail rather than an internal spatial model.
**Breakthrough:** The authors report that "learning to reconstruct propagates 3D-aware signals throughout the model," yielding consistent improvements over baselines on spatial reasoning and 3D understanding tasks.
**Tools & method:** Learnable Gaussian summary tokens are decoded into a 3D Gaussian Splatting (3DGS) scene representation with photometric reconstruction as the supervisory signal, optionally distilled from a pretrained compact Gaussian teacher.
**Limitation (≤3 sentences, authors' own):** Training efficiency is a stated limitation: without the pretrained Gaussian teacher, the model needs substantially more training steps to reach comparable performance.
