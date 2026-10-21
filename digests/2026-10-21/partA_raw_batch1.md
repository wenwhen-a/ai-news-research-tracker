---
## Joints, Camera, Action! Co-Generating 3D Motion and Video for Arbitrary Rigs
- **arXiv:** 2610.28632 · https://arxiv.org/abs/2610.28632
- **Submitted:** Tue, 20 Oct 2026 17:59:56 UTC (v1)
- **Authors:** Noam Rotstein, Yoad Tewel, Chen Tessler, Haggai Maron, Gal Chechik, Or Litany, Yoni Kasten, Yuval Atzmon
- **Qualifying affiliation(s):** NVIDIA — all eight authors carry an NVIDIA affiliation marker in the paper's author block; several also hold secondary academic affiliations (Technion — Rotstein, Maron, Litany, Kasten; Bar-Ilan University — Chechik)
- **Categories:** cs.CV (primary); cs.AI, cs.GR, cs.LG, cs.RO (cross-listed)
- **Open release:** project page only (https://research.nvidia.com/labs/par/projects/jca/); no code or weights stated
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** Video generation models produce realistic motion, but that motion stays in pixels and cannot easily be reused as replayable 3D animation in a 3D scene. The authors present a model that directly co-generates video and 3D motion for any supplied rig, along with a camera that registers the motion to the scene.

**Purpose (≤3 sentences):** The goal is to let a single system turn a text or video prompt into replayable 3D motion for arbitrary skeletons — not just humans — correctly placed in its 3D scene, rather than only generating pixel-level video.

**Breakthrough (≤3 sentences):** The authors report that keeping 3D motion in a separate model connected to a pretrained video backbone via a small set of cross-attention layers lets the system learn skeleton motion from motion-only data; their evaluations state the model animates diverse rigs from text more faithfully than video-first pipelines and that its motion responds to the surrounding scene.

**Tools & method (≤3 sentences):** The model builds on the Wan2.2 I2V-A14B video backbone and a generative video editor ("Bernini") used to place animated 3D assets from Objaverse/Objaverse-XL into matching scenes, producing the authors' own "Objaverse in Video" dataset and, combined with human and robot video, nearly 200K training pairs. Evaluation uses the Puppeteer test set and HumanML3D.

**Limitation (≤3 sentences):** The authors state that their alignment procedure assumes a static camera at inference time, that the model does not represent 3D scene geometry so it cannot enforce contact or prevent penetration, and that each clip animates only a single rig, with training rigs skewed heavily toward bipedal characters.

---
## SceneRig: An Agentic System for Simulation-Ready 3D Scene Reconstruction from Single Images
- **arXiv:** 2610.28585 · https://arxiv.org/abs/2610.28585
- **Submitted:** Tue, 20 Oct 2026 17:39:42 UTC (v1); accepted at the CoRL 2026 Agentic Robotics Workshop per the abstract page
- **Authors:** Rundong Luo, Yunong Liu, Di Cao, Matthew Tancik, Shyamal Buch, Colton Stearns, Wenqi Xian
- **Qualifying affiliation(s):** Luma AI — the paper's affiliation block lists "Luma AI" and "Cornell University," with a footnote "Work done during an internship at Luma AI," confirming at least one author is Luma AI-affiliated (individual author-to-institution mapping was not resolvable from the extracted HTML). **FLAG: borderline** — Luma AI is not on the tracked-company list; it is a well-known applied-AI company for generative 3D/video (Genie, Dream Machine/Ray2). Kept per the skill's "when unsure, flag rather than drop" rule, for a human to judge.
- **Categories:** cs.RO (primary); cs.AI, cs.CV
- **Open release:** none stated
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** Simulation is valuable for robotics, but building diverse, simulation-ready 3D scenes at scale is difficult, and single-image reconstruction alone does not guarantee objects are correctly identified, placed, and physically grounded. SceneRig is an agentic system that turns a single image into an editable, simulation-ready 3D scene.

**Purpose (≤3 sentences):** The authors aim to produce 3D scenes from a single image that are not just visually plausible but physically stable and behave correctly under robot manipulation, addressing what they describe as frequent object misplacement from post-hoc physics settling in prior methods.

**Breakthrough (≤3 sentences):** The authors report that SceneRig improves instance segmentation, object-level appearance, and 3D placement while keeping reconstructed scenes physically stable, and that its scenes predict real-robot policy outcomes more accurately than their baseline and more reliably support replay of recorded manipulations without trajectory adaptation.

**Tools & method (≤3 sentences):** SceneRig combines geometric, visual, and physical tools to reconstruct a scene, then runs an agent through edit-and-validate loops inside a physics simulator to reach physical stability. The paper names RoboDojo, RoboLab, and SimFoundry among its experimental setups.

**Limitation (≤3 sentences):** The authors' discussion states that "complex room scenes remain challenging due to occlusion, depth ambiguity, and frequent contacts."

---
## OverSeer: Multi-Agent World Models Beyond What Agents See
- **arXiv:** 2610.28554 · https://arxiv.org/abs/2610.28554
- **Submitted:** Tue, 20 Oct 2026 17:17:59 UTC (v1)
- **Authors:** Runjia Li, Kam Woh Ng, Minghao Chen, Junlin Han, Jianyuan Wang, Zhaochong An, Juan-Manuel Perez-Rua, Andrea Vedaldi, Shikun Liu
- **Qualifying affiliation(s):** Meta (Meta AI) — Li, Ng, Han, Wang, An, Perez-Rua, Vedaldi, and Liu are listed with a Meta AI affiliation (Li, Han, Wang, and Vedaldi also list University of Oxford); Chen is listed with University of Oxford only
- **Categories:** cs.CV
- **Open release:** none stated
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** Video world models are hard to extend to multiple agents because each agent needs its own video stream, and those streams must stay consistent over time and with each other. OverSeer adds fixed auxiliary camera views alongside each agent's egocentric view to act as a proxy for a world-centric representation.

**Purpose (≤3 sentences):** The aim is to improve temporal and cross-agent consistency in multi-agent world models without requiring each agent's egocentric view alone to carry the full world state.

**Breakthrough (≤3 sentences):** The authors report that because the auxiliary views are fixed in space, changes in them map directly to localized changes in world state, and that experiments in Minecraft and Doom show improved world and agent consistency versus their baseline; qualitative results on real-world multi-camera captures are presented as evidence the approach is not tied to game engines.

**Tools & method (≤3 sentences):** The redundant, largely static auxiliary views are compressed with a delta-VAE that encodes only changes relative to a static reference image, reducing the token count needed to process them; per the appendix, the model was trained with a batch size of 64 across 64 NVIDIA GB300 GPUs. Evaluation uses the Replay dataset, the Solaris engine, and Freedoom maps.

**Limitation (≤3 sentences):** The authors' "Limitations and Future Work" appendix states that OverSeer's benefits depend on auxiliary coverage, and that fast-changing scenes such as Doom can lose consistency under aggressive residual compression.

---
## Latent Bridge: From Video Latents to 3D Geometry via Feature Alignment
- **arXiv:** 2610.28521 · https://arxiv.org/abs/2610.28521
- **Submitted:** Tue, 20 Oct 2026 16:57:49 UTC (v1)
- **Authors:** Shuai Zhang, Zhanpeng Ouyang, Zhengqing Chen, Ruohong Mei, Shaoyu Chen, Weiqiang Ren, Hui Sun, Qian Zhang, Wenyu Liu, Xinggang Wang
- **Qualifying affiliation(s):** Horizon Robotics — the paper gives one joint affiliation block ("Huazhong University of Science and Technology, Horizon Robotics") without mapping individual authors to either institution. **FLAG: borderline** — Horizon Robotics is not on the tracked-company list; it is a Chinese autonomous-driving/robotics AI chip and software company (publicly listed), kept here per the skill's "when unsure, flag rather than drop" rule for a human to judge as a possibly comparable industry lab.
- **Categories:** cs.CV
- **Open release:** code at https://github.com/hustvl/Latent-Bridge (per the abstract page link)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** Video generation and feed-forward 3D reconstruction normally use separate representations, requiring RGB decoding and re-encoding to recover geometry from generated video latents. Latent Bridge instead connects video generative latent spaces directly to geometric feature spaces to predict 3D geometry from the latents.

**Purpose (≤3 sentences):** The goal is a reusable, interface between video generation and 3D reconstruction that avoids a separate decode-then-reconstruct pipeline for each generative backbone.

**Breakthrough (≤3 sentences):** The authors report that one trained bridge transfers across image-to-video and text-to-video generation within the same latent space without retraining, and that on Co3Dv2 and WildRGB-D it gives competitive geometric reconstruction quality with faster latent-to-geometry decoding than decode-then-reconstruct baselines.

**Tools & method (≤3 sentences):** The authors build representation-specific bridges for the Wan2.1 and V-RAE video-latent spaces, trained via feature distillation on RGB video while the video encoder and geometry model stay frozen, requiring no ground-truth geometry. The Wan2.1 bridge was trained on NVIDIA RTX PRO 6000 then RTX 5090 GPUs and the V-RAE bridge on 16 RTX PRO 6000 GPUs, evaluated against DL3DV, WildRGB-D, CO3Dv2, RealEstate10K, and Waymo data.

**Limitation (≤3 sentences):** The authors state in their appendix that the bridge depends on a pretrained geometry model and "cannot be expected to correct the teacher's geometric errors," and that it does not automatically correct inconsistencies in generated video, so it "cannot guarantee the reconstruction of a coherent 3D scene."

---
## StreamEval: Evaluating Interactive Streaming Video Generation Models
- **arXiv:** 2610.28402 · https://arxiv.org/abs/2610.28402
- **Submitted:** Tue, 20 Oct 2026 15:47:43 UTC (v1)
- **Authors:** Credited collectively on the abstract page as "StreamEval Team"; named in the paper's Contributions section as Jungang Li, Ziqi Huang, Tian Ye, Haocheng Xi, Yuezhou Hu, Kai Jiang, Zhifei Li, Yichuan Wang, Shuo Yang, Zhiqiu Lin, Zian Zheng, Alberto Taiuti, Jintao Zhang
- **Qualifying affiliation(s):** NVIDIA — the paper's institutional-logo credit block lists seven affiliations (Tsinghua University, NVIDIA, CMU, UC Berkeley, Princeton, NUS, Reactor); this affiliation is confirmed directly from the primary source (the paper's own affiliation block), not the pre-screen keyword hit, but the HTML rendering does not map any specific named author to NVIDIA individually.
- **Categories:** cs.CV
- **Open release:** leaderboard at https://streameval.ai; this is a benchmark paper, no generative model weights are released
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** As interactive streaming video generation advances, there has been no unified way to evaluate real-time interaction with generated video. The authors introduce StreamEval, a benchmark spanning five tasks: avatar dialogue, avatar performance, world generation, instruction editing, and reference editing.

**Purpose (≤3 sentences):** The benchmark is meant to measure whether streaming video generation models can reliably execute incrementally arriving multimodal requests while preserving state and content, rather than only producing visually convincing frames.

**Breakthrough (≤3 sentences):** Evaluating 37 models across 300 scripted test cases (15–300s), the authors report that high visual quality and identity retention do not necessarily coincide with reliable request execution or sustained state consistency; the highest task-specific "Following" scores were only 36.90 (among seven avatar-performance models) and 25.93 (text-conditioned world generation), and the highest "Edit Success" score was 15.00 (among three reference-editing models).

**Tools & method (≤3 sentences):** The benchmark scores four dimensions (task execution, state consistency, visual fidelity, audiovisual coordination) via ten task-specific metrics on a 0–100 scale; test assets were constructed using GPT-Image-2, Qwen-Image, Qwen3.5-Omni, Qwen3.8-Max, and Qwen3-ASR, plus footage from Wikimedia Commons, NASA, and Blender Studio.

**Limitation (≤3 sentences):** The paper has no section titled "Limitations"; the closest stated text, in the conclusion, points to future extensions covering "broader identities and environments" and future work on human pairwise judgments.

# Near-misses

- 2610.28628 · Learning Adaptable Dexterous Skills via Hybrid Dexterous Mimicking (AdaDex) · Off-topic: a generic dexterous-hand manipulation/RL paper (functional grasping, in-hand reorientation, throw-and-catch) with no world-model, 3D-content, or game-engine relevance, despite a verified NVIDIA affiliation for two of eight authors (Yufei Ye, Umar Iqbal; remaining authors are Carnegie Mellon University or unlisted/"Project Lead").
- 2610.28480 · SuperMimic: Scaling Humanoid Whole-Body Control with One Differentiable World Model · Affiliation unverifiable: no arXiv HTML version exists for this id (confirmed HTTP 404 at both arxiv.org/html/2610.28480 and .../2610.28480v1); per task instructions no PDF fallback was used, so the author affiliations (likely UC Berkeley-heavy by author roster: Pieter Abbeel, Koushil Sreenath, Roberto Horowitz) could not be checked against the primary source, even though the paper is clearly on-topic (differentiable world model for humanoid whole-body control, accepted as a CoRL 2026 Oral).
- 2610.28351 · RayCo4D: Ray-Conditioned Continuous Motion Model for Monocular 4D Dynamic Reconstruction · No qualifying affiliation: the paper's own author/affiliation footnotes (extracted from its LaTeX source, since the rendered HTML omits the author block) list only academic institutions — Southern University of Science and Technology, Fudan University, East China University of Science and Technology, Beijing Technology and Business University, and Shenzhen Institutes of Advanced Technology (Chinese Academy of Sciences). The pre-screen's "NVIDIA" hit was a false positive from the "NVIDIA Dynamic Scene Dataset," a third-party benchmark the paper evaluates against, not an author affiliation.

**Verification statement:** All 8 candidates were checked against their arXiv abstract pages (title, authors, v1 date, categories, withdrawal status) and, where available, their arXiv HTML full text (author/affiliation block, acknowledgments, limitations). For 2610.28402 and 2610.28351, the rendered HTML's author/affiliation block was incomplete or missing, so the paper's own LaTeX source (e-print) was additionally checked to resolve the affiliation question from the primary source. For 2610.28480, no HTML version exists and no PDF fallback was used, so it is recorded as a near-miss. All five included papers' v1 submissions are dated 20 Oct 2026 (within the 30-day window ending 2026-10-21), none are withdrawn, and each has at least one author-stated qualifying-company affiliation read directly from the paper (two flagged as borderline companies: Horizon Robotics and Luma AI, per the skill's gate rule for comparable-but-unlisted labs). This is a double-verification pass: every included paper's affiliation, date, and topic claim above was re-checked against the primary-source text quoted during retrieval before this file was written.
