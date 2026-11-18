## Towards Data-Efficient, Real-Time World Models
- **arXiv:** 2611.22497 · https://arxiv.org/abs/2611.22497
- **Submitted:** 2026-11-17
- **Authors:** Raluca Stevenson, David Bignell, Jennifer C. White, Tabish Rashid, Emanuele Aiello, Mariya Hendriksen, Junha Hyung, Sadegh Aliakbarian, Abdelhak Lemkhenter, Marko Tot, Katja Hofmann, Sarah Parisot
- **Qualifying affiliation(s):** Microsoft — Sarah Parisot (listed affiliation "Microsoft, Cambridge, United Kingdom"); paper states "This work was carried out at Microsoft." Katja Hofmann is also a known Microsoft Research (Game Intelligence) lead, though per-author affiliation tags were garbled in the HTML.
- **Categories:** cs.AI
- **Open release:** none found (no code/weights/demo link in abstract or comments)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The authors tackle two barriers to real-time, action-conditioned gameplay world models: slow autoregressive inference and the large data requirements of training. They replace next-token prediction with a two-stage discrete-diffusion scheme using a lightweight refinement transformer that performs iterative masked predictions. The method is built on top of an existing autoregressive world model (Kanervisto et al., 2025).

**Purpose (≤3 sentences):** To make interactive gameplay-generation world models fast enough for real-time play and cheap enough to train that custom/creative use becomes practical, rather than requiring massive datasets and slow inference.

**Breakthrough (≤3 sentences):** The authors report a 79x inference speedup over the autoregressive baseline with only a modest quality trade-off. They also report that a model trained on roughly 28 hours of gameplay data can still produce high-quality, temporally consistent gameplay.

**Tools & method (≤3 sentences):** Two-stage discrete diffusion replacing next-token prediction, with a lightweight refinement transformer doing iterative masked-token predictions on top of an existing autoregressive world-model backbone (Kanervisto et al., 2025).

**Limitation (≤3 sentences):** The authors themselves describe the speedup as coming with a "modest quality trade-off"; no separate limitations section or training-hardware details are given in the abstract/comments.

---

## FailureGen: Scalable Robot Failure Data Generation with World Models
- **arXiv:** 2611.22367 · https://arxiv.org/abs/2611.22367
- **Submitted:** 2026-11-17
- **Authors:** Akul Santhosh, Chaitra Sathe, Aastha Jhunjhunwala
- **Qualifying affiliation(s):** NVIDIA — all three listed authors (HTML affiliation block shows NVIDIA for the author group)
- **Categories:** cs.RO (primary); cs.AI
- **Open release:** none found
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper addresses the scarcity of robot-failure data, which the authors say is "difficult to collect at scale," by generating synthetic failure videos with temporal event annotations. FailureGen reuses action trajectories from recorded real failures and transplants them into new visual contexts using a fine-tuned world model. A visual failure detector trained with the generated data is evaluated as a downstream application.

**Purpose (≤3 sentences):** To scale up the diversity and quantity of labeled robot-failure data for training failure-detection and robot-learning systems, without relying solely on scarce, hand-collected real failure recordings.

**Breakthrough (≤3 sentences):** The authors report that a failure detector trained on real plus generated data reached average precision of 0.51 versus 0.41 with real data alone, and detected 33 of 36 failure intervals versus 28 of 36 with real data alone. They describe this as a "preliminary comparison."

**Tools & method (≤3 sentences):** Four stages: (1) fine-tune an action-conditioned NVIDIA Cosmos world model on successful and failed real executions; (2) identify failure-related donor segments and compatible successful "host" recordings; (3) transfer donor motion into host contexts (with optional spatial offsets) to generate continuous rollouts; (4) annotate and filter generated samples by detected events and visual quality.

**Limitation (≤3 sentences):** The authors flag the headline numbers as coming from a "preliminary comparison" rather than a full evaluation; no dataset names or training/inference hardware are specified in the abstract.

---

## Decoding Without a Decoder: Direct Pixel Prediction from Diffusion Transformers
- **arXiv:** 2611.22287 · https://arxiv.org/abs/2611.22287
- **Submitted:** 2026-11-17
- **Authors:** Hansheng Chen, Shengqu Cai, Jan Ackermann, Rayhan Zirvi, Gordon Wetzstein, Xinchen Yan, Leonidas Guibas
- **Qualifying affiliation(s):** FLAG: borderline — Luma AI (Hansheng Chen and Xinchen Yan are listed with "Affiliation: Luma AI" in the HTML author block; other authors are listed with Stanford University / Caltech)
- **Categories:** cs.CV
- **Open release:** project page — https://hanshengchen.com/dwd (no code/weights listed)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** Latent diffusion models normally need a separate decoder to turn denoised latents into pixels, adding complexity and inference cost. The authors propose "Decoding Without a Decoder" (DWD), which finetunes a diffusion transformer so a linear head directly predicts final pixels, while a separate denoising head still drives the sampling trajectory. Only the last few transformer blocks are finetuned.

**Purpose (≤3 sentences):** To remove the standalone pixel decoder from latent/pixel diffusion pipelines in order to cut inference cost and architectural complexity, without sacrificing (and ideally improving) output pixel quality.

**Breakthrough (≤3 sentences):** On Wan video generation, the authors report a 23% reduction in warping error along with reduced detail distortion and flickering. For pixel diffusion image models, they report an ImageNet FID improvement from 1.55 to 1.43, which they describe as a new state of the art among pixel-flow models.

**Tools & method (≤3 sentences):** Finetune only the last few blocks of a pretrained diffusion transformer; add a linear DWD head trained with pixel-quality losses to directly output pixels, while anchoring the existing denoising head close to its pretrained behavior to preserve the sampling trajectory. Evaluated on Wan (video) and on pixel/latent image diffusion models (ImageNet, text-to-image).

**Limitation (≤3 sentences):** Neither the abstract nor the comments state explicit limitations; code and weights are not released, only a project page.

---

## DreamFAR: Real-Time and Long-Horizon Interaction with Diverse Objects
- **arXiv:** 2611.22001 · https://arxiv.org/abs/2611.22001
- **Submitted:** 2026-11-16
- **Authors:** Yiming Dou, Botao He, Antonio Loquercio, Andrew Owens, Jitendra Malik, Sumedh Anand Sontakke, Ruoshi Liu
- **Qualifying affiliation(s):** Amazon — the paper's affiliation block lists "Amazon FAR" (Amazon's Frontier AI & Robotics team, confirmed as a real Amazon research group via amazon.jobs listings) alongside Cornell University, University of Maryland College Park, and University of Pennsylvania; per-author mapping was not separable in the HTML.
- **Categories:** cs.RO
- **Open release:** project page — https://www.yimingdou.com/DreamFAR/ (no code/weights released yet per abstract/comments)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** Existing robot-manipulation world models either overfit to a single environment or fail to simulate long-horizon, contact-rich interactions. DreamFAR is trained from scratch on a large robot-native teleoperation dataset, without internet-video pretraining, and is reported to be much smaller than leading video-generation-based world models while better capturing contact and causality. It runs at 10 FPS on a commercial GPU.

**Purpose (≤3 sentences):** To build a world model for robot manipulation that generalizes across diverse objects and long, contact-rich interactions in real time, usable for policy evaluation and for mixed real/generated data co-training.

**Breakthrough (≤3 sentences):** The authors report that DreamFAR outperforms existing world models at predicting long-horizon futures despite its smaller size, and demonstrate its use both for evaluating policies and for co-training with mixed real and generated data.

**Tools & method (≤3 sentences):** A dynamics model trained from scratch (no internet-video pretraining) on a large robot-native teleoperation dataset, with an architecture and training recipe tailored to robot-native data; runs at 10 FPS on a commercial GPU.

**Limitation (≤3 sentences):** The abstract and comments state no explicit limitations; the training dataset is described only as "a large robot-native teleoperation dataset" without being named, and training hardware is not specified (only inference hardware, "a commercial GPU").

---

## FaceRiff: Data-Efficient Unified Text-to-3D Face Asset Synthesis via Geometric Conditioning
- **arXiv:** 2611.21867 · https://arxiv.org/abs/2611.21867
- **Submitted:** 2026-11-16
- **Authors:** Elly Akhoundi, Mathieu Lamarre, Thibault Goyallon, Patrick Anderson, Étienne Danvoye
- **Qualifying affiliation(s):** Electronic Arts — all five authors (HTML affiliation block lists "Electronic Arts, Vancouver/Montréal/Toronto, Canada" for each)
- **Categories:** cs.CV (primary); cs.AI; cs.GR
- **Open release:** none found
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** FaceRiff generates complete 3D face assets — mesh, albedo, and displacement — from text prompts in a shared UV space. It adapts a pretrained SDXL diffusion backbone with task-specific LoRA adapters, using UV normal maps as geometric conditioning. It is trained on a relatively small scan dataset and updates only a small fraction of backbone parameters.

**Purpose (≤3 sentences):** To address the scarcity of high-resolution facial datasets with consistent UV-mapped geometry, albedo, and physically-based displacement, and to produce diverse, production-usable 3D face assets from text without large specialized datasets or per-instance optimization.

**Breakthrough (≤3 sentences):** The authors report greater per-prompt diversity than prior methods FaceG2E and DreamFace while preserving prompt alignment and UV consistency, plus lighting-independent albedo suitable for PBR relighting and pore-scale displacement. A blind study with 45 industry professionals rated FaceRiff's perceived realism substantially higher than DreamFace's and approaching real face captures.

**Tools & method (≤3 sentences):** Pretrained SDXL backbone adapted with task-specific LoRA adapters (updating under 3% of backbone parameters per task); UV normal maps provide geometric conditioning, with per-instance normals guiding albedo/displacement and a dataset-mean normal anchoring mesh generation. Trained on 2,049 scans from about 350 identities on a single GPU, requiring no per-instance optimization. Accepted to SIGGRAPH Asia 2026.

**Limitation (≤3 sentences):** No explicit limitations are stated in the abstract or comments; the GPU model used for training is not specified, and the scan dataset is not named.

---

# Near-misses
- 2611.22537 · Testing World Models on Actions They Have Never Seen: Held-Out Plans, Forecast Accuracy and Price Rules in Retail · off-topic (retail price/promotion forecasting application of "world models," not 3D/world-sim/animation/game-engine topic) and single academic author (Karthik Iyer), no qualifying co-author
- 2611.22483 · Manufacturing Differential Sparsity: Planner-Hardware Co-Design for Efficient World Model Planning · no industry co-author (all authors listed with University of Southern California or Columbia University affiliations)
- 2611.21907 · REEL: Brain-Guided Video Generation and Selection by Reranking Encoder Embeddings with Linear probes · off-topic (fMRI brain-signal-to-video decoding/neuroscience application, not genuinely a 3D/world-model/animation/game-engine paper); all authors appear academic (no qualifying co-author found)
