## Evolve in Panorama, Render in View: Panoramic World State Evolution for Video World Models
- **arXiv:** 2611.22733 · https://arxiv.org/abs/2611.22733
- **Submitted:** 2026-11-17
- **Authors:** Longtao Jiang, Mingfei Han, Jianmin Bao, Tingjun Dai, Jinjie Wei, Zhiran Zhang, Xin Tao, Zhihui Li, Salman Khan, Xiaojun Chang
- **Qualifying affiliation(s):** Kuaishou Technology (co-author(s); the HTML author block lists "Mohamed bin Zayed University of Artificial Intelligence" and "Kuaishou Technology" as the paper's two affiliations but does not map each name to a specific one)
- **Categories:** cs.CV
- **Open release:** none yet — abstract states "Code, models, and data will be released"

**Summary (≤3 sentences):** PanoEvo is a video world model that keeps content outside the camera's current view evolving by maintaining world state in the latent space of a panoramic video diffusion model, where every direction is represented at every time step. A Perspective Renderer then reads that panoramic latent state via latent-space projection and direction-restricted cross-attention to render sharp perspective views. The authors also built PanoEvo-Data, an event-centric dataset from real 360° videos, to train the model to evolve a scene from a single starting image.
**Purpose (≤3 sentences):** The paper targets a specific failure mode of current video world models: when the camera turns away and returns, unobserved parts of the scene freeze, lose objects, or change appearance because there is no representation for content outside the current view. It aims to give world models a persistent, always-evolving representation of the full surrounding scene.
**Breakthrough (≤3 sentences):** The authors report that PanoEvo achieves the best overall score among 23 publicly evaluated models on WRBench and the highest total score on STEVO-Bench.
**Tools & method (≤3 sentences):** A "Panoramic Evolver" is trained coarse-to-fine as an image-to-panoramic-video diffusion model on the newly built PanoEvo-Data. A separate "Perspective Renderer," built on a perspective video diffusion model, converts the low-resolution panoramic latent state into high-quality rendered views via latent-space projection and direction-restricted cross-attention.
**Limitation (≤3 sentences):** The authors note that directly projected views from the panorama are blurry and show low-quality details or structural errors because each perspective view covers only a small part of the low-resolution panorama — the stated motivation for adding the separate Perspective Renderer. Code, models, and data are announced but not yet released.

---

## Towards Data-Efficient, Real-Time World Models
- **arXiv:** 2611.22497 · https://arxiv.org/abs/2611.22497
- **Submitted:** 2026-11-17
- **Authors:** Raluca Stevenson, David Bignell, Jennifer C. White, Tabish Rashid, Emanuele Aiello, Mariya Hendriksen, Junha Hyung, Sadegh Aliakbarian, Abdelhak Lemkhenter, Marko Tot, Katja Hofmann, Sarah Parisot
- **Qualifying affiliation(s):** Microsoft (Sarah Parisot — Microsoft, Cambridge, UK; the paper's acknowledgments state "This work was carried out at Microsoft"; Katja Hofmann, the arXiv submitter, is also Microsoft Research Cambridge)
- **Categories:** cs.AI
- **Open release:** none mentioned in the abstract

**Summary (≤3 sentences):** This paper targets real-time, data-efficient gameplay world models by replacing next-token prediction with a two-stage discrete-diffusion approach built on top of an existing autoregressive world model (citing Kanervisto et al., 2025). A lightweight refinement transformer performs iterative masked predictions to produce the final frames. The authors show the resulting model can also be trained on a much smaller gameplay dataset than prior state-of-the-art models.
**Purpose (≤3 sentences):** Current state-of-the-art gameplay world models trade inference speed for consistent, high-quality generation, which the authors say makes real-time interactive play and ideation difficult. The large data requirements of these models also make custom training impractical for creative use cases, limiting their adoption.
**Breakthrough (≤3 sentences):** The authors report a 79x inference speed-up over the base autoregressive world model with, in their words, "a modest quality trade-off." They also report the model can be trained to reproduce high-quality, consistent gameplay using a dataset of approximately 28 hours (about one day) of gameplay data.
**Tools & method (≤3 sentences):** The approach builds on an existing autoregressive world model capable of generating consistent, complex sequences over minutes (Kanervisto et al., 2025), and introduces a two-stage discrete-diffusion scheme with a lightweight refinement transformer carrying out iterative masked predictions in place of next-token prediction.
**Limitation (≤3 sentences):** The authors explicitly acknowledge a "modest quality trade-off" that comes with the reported 79x speed-up; the abstract gives no further quantified detail on this trade-off.

---

## FailureGen: Scalable Robot Failure Data Generation with World Models
- **arXiv:** 2611.22367 · https://arxiv.org/abs/2611.22367
- **Submitted:** 2026-11-17
- **Authors:** Akul Santhosh, Chaitra Sathe, Aastha Jhunjhunwala
- **Qualifying affiliation(s):** NVIDIA (all three authors, per the paper's HTML author block)
- **Categories:** cs.RO, cs.AI
- **Open release:** none mentioned in the abstract

**Summary (≤3 sentences):** FailureGen generates synthetic robot failure videos with temporal event annotations by reusing action trajectories from previously recorded failures and transferring them into new, compatible contexts. It fine-tunes an action-conditioned NVIDIA Cosmos world model on both successful and failed real robot executions as the generative backbone. The method is intended to scale up the range of failure scenarios available for robot learning.
**Purpose (≤3 sentences):** Robot failures are difficult to collect at scale, which the authors say limits the diversity of failure scenarios represented in robot learning datasets. FailureGen aims to synthetically expand this failure data by reusing real recorded failures in new situations.
**Breakthrough (≤3 sentences):** The authors report that, in a preliminary comparison, a visual failure detector trained on real plus generated data reaches an average precision of 0.51 versus 0.41 using real data alone, and detects 33 of 36 failure intervals versus 28 of 36 for real-data-only training.
**Tools & method (≤3 sentences):** The four-stage pipeline: (1) fine-tunes an action-conditioned Cosmos world model on successful and failed real executions; (2) annotates source recordings to identify donor failure segments and compatible successful host recordings; (3) transfers donor motion into host contexts, with optional spatial offsets, to generate continuous video rollouts; (4) annotates and filters the generated samples by observed events and visual quality.
**Limitation (≤3 sentences):** The authors describe their validation as "a preliminary comparison" across two implementations with different tasks and robot configurations, indicating the detection-accuracy results are early-stage rather than a broad benchmark.

---

## DreamFAR: Real-Time and Long-Horizon Interaction with Diverse Objects
- **arXiv:** 2611.22001 · https://arxiv.org/abs/2611.22001
- **Submitted:** 2026-11-16
- **Authors:** Yiming Dou, Botao He, Antonio Loquercio, Andrew Owens, Jitendra Malik, Sumedh Anand Sontakke, Ruoshi Liu
- **Qualifying affiliation(s):** Amazon FAR (the paper's HTML author block lists "Amazon FAR" alongside Cornell University, University of Maryland College Park, and University of Pennsylvania as the paper's affiliations, without a stated author-to-institution mapping)
- **Categories:** cs.RO
- **Open release:** code and weights — authors' Reproducibility Statement says they release training/inference code and an interactive demo, plus weights for both the full DreamFAR and an ABC-trained DreamFAR, and their ABC data split with evaluation scripts; project page https://www.yimingdou.com/DreamFAR/

**Summary (≤3 sentences):** DreamFAR is a world model for robot manipulation whose dynamics model is trained from scratch on a large robot-native teleoperation dataset, with no internet-video pretraining. The authors present an architecture and training recipe designed specifically for robot-native data. They report it is significantly smaller than high-performance video generation world models while running at 10 FPS on a commercial GPU.
**Purpose (≤3 sentences):** Existing world models for robot manipulation are either fit to a single environment or cannot simulate long-horizon, contact-rich events, limiting their use as simulators for robot learning. DreamFAR aims to provide a world model that handles real-time, long-horizon interaction with diverse objects.
**Breakthrough (≤3 sentences):** The authors report DreamFAR "significantly outperforms existing models in predicting the long-horizon future" and shows better understanding of contact and causality than larger video generation models, despite its smaller size and 10 FPS runtime on a commercial GPU.
**Tools & method (≤3 sentences):** The dynamics model is trained from scratch on a large-scale robot-native teleoperation dataset (no internet-video pretraining), using an architecture and learning recipe the authors designed for this data regime. Demonstrated applications include policy evaluation and mixed-data co-training.
**Limitation (≤3 sentences):** The abstract does not state explicit residual limitations of DreamFAR itself beyond the gaps in prior models it is designed to address (observed, not stated).

---

## FaceRiff: Data-Efficient Unified Text-to-3D Face Asset Synthesis via Geometric Conditioning
- **arXiv:** 2611.21867 · https://arxiv.org/abs/2611.21867
- **Submitted:** 2026-11-16
- **Authors:** Elly Akhoundi, Mathieu Lamarre, Thibault Goyallon, Patrick Anderson, Étienne Danvoye
- **Qualifying affiliation(s):** Electronic Arts (all five authors, per the paper's HTML author block: EA Vancouver, EA Montréal, EA Toronto)
- **Categories:** cs.CV, cs.AI, cs.GR
- **Open release:** none mentioned in the abstract

**Summary (≤3 sentences):** FaceRiff generates complete 3D face assets — mesh, albedo, and displacement — directly from text prompts in a shared UV space, by adapting a pretrained SDXL image diffusion backbone with task-specific LoRA adapters. UV normal maps are used as geometric conditioning: per-instance normals guide albedo and displacement synthesis, while a dataset-mean normal anchors mesh generation. The method is trained on only 2,049 scans from about 350 identities on a single GPU.
**Purpose (≤3 sentences):** High-resolution facial datasets with consistent UV-mapped geometry, albedo, and physically based displacement are scarce, even though such assets are needed for photorealistic digital-human rendering. The authors aim to produce render-ready 3D face assets without large specialized datasets or per-instance optimization.
**Breakthrough (≤3 sentences):** The authors report FaceRiff updates less than 3% of the SDXL backbone's parameters per task, and that a blind study with 45 industry professionals found it achieves "substantially higher perceived realism" than the DreamFace baseline, approaching that of real captures. They also report greater per-prompt diversity than FaceG2E and DreamFace while preserving prompt alignment and fixed-topology UV consistency.
**Tools & method (≤3 sentences):** The method adapts a pretrained SDXL backbone with task-specific LoRA adapters, using UV normal maps as geometric conditioning for albedo, displacement, and mesh generation. It additionally produces lighting-independent albedo suitable for physically based (PBR) relighting and pore-scale displacement, which the authors say prior text-driven baselines lack.
**Limitation (≤3 sentences):** The authors frame the result as a demonstration that pretrained 2D diffusion priors can be adapted to this task "under limited data" — training used only 2,049 scans from roughly 350 identities, and the method is demonstrated specifically on faces (observed, not stated as a general limitation).

---

# Near-misses
- 2611.22717 · PCRG: Training-Free Pruning and Caching of Reference Tokens for Video Generation · non-qualifying affiliation — the paper's only listed affiliation is "Anorak" (Anorak Games), a UK pre-seed AI startup that raised $5M in November 2026, not a top-tier industry lab comparable to the tracked companies; also arguably off-topic (reference-conditioned video generation/editing acceleration, not specifically 3D/world-models/character-animation/game-engines).
- 2611.22673 · FVScore: Specification-Driven Neuro-Symbolic Video Evaluation · off-topic on closer read — despite a strong Google Cloud AI Research affiliation (Tomas Pfister, Yale Song, Long T. Le, Yiwen Song) plus National University of Singapore (Min-Yen Kan), the paper is a generic video-generation evaluation/scoring framework, not specifically about 3D, world models, character animation, or game engines.
- 2611.22537 · Testing World Models on Actions They Have Never Seen: Held-Out Plans, Forecast Accuracy and Price Rules in Retail · academic only, no industry co-author — sole author Karthik Iyer, with no institutional affiliation stated anywhere on the arXiv page (only a personal email and ORCID).
- 2611.22483 · Manufacturing Differential Sparsity: Planner-Hardware Co-Design for Efficient World Model Planning · academic only, no industry co-author — all five authors are at University of Southern California and Columbia University, per the paper's HTML author block.
- 2611.22287 · Decoding Without a Decoder: Direct Pixel Prediction from Diffusion Transformers · off-topic on closer read — the paper is a general diffusion-model architecture improvement (removing the VAE decoder for direct pixel prediction) demonstrated on Wan video generation and ImageNet text-to-image, not specifically about 3D, world models, character animation, or game engines; affiliation is also borderline (Luma AI, per the HTML author block for Hansheng Chen, with Xinchen Yan noted as "work done while at Luma AI," alongside Caltech and Stanford).

Verification: all 10 leads were checked against their arXiv abstract page (title, v1 date, authors, categories, no withdrawal) and, where an HTML version existed, against the HTML author-affiliation block; all 10 had HTML versions available. No paper in this batch required falling back to "affiliation unverifiable."
