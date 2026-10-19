## Persistent Planar Memory for Video World Models
- **arXiv:** 2610.23795 · https://arxiv.org/abs/2610.23795
- **Submitted:** 2026-10-16 (v1)
- **Authors:** Yuze He, Bin Tan, Zelin Gao, Yujun Shen, Yong-Jin Liu, Nan Xue, Yinghao Xu
- **Qualifying affiliation(s):** Ant Group — Bin Tan, Zelin Gao, Yujun Shen, Nan Xue, Yinghao Xu (He and Liu are Tsinghua University). FLAG: borderline — screen matched "Alibaba," but the actual industry affiliation is Ant Group (a separate fintech/AI affiliate), which is on the borderline-company watch list.
- **Categories:** cs.CV
- **Open release:** none (project page only, https://hyzcluster.github.io/ppmem; no code/weights release stated)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** PPMem is a video world model that maintains a persistent, compact 3D memory built from plane primitives rather than point clouds, enabling long, geometrically consistent video generation under large camera motion. It extends a video diffusion transformer with a planar-prediction head and a Depth Token Fusion module so each generated chunk both contributes to and is conditioned by an accumulating scene-wide plane pool.
**Purpose (≤3 sentences):** The paper targets the need for video world model memory that is simultaneously compact, geometrically explicit, consistent across viewpoints, and able to update as new content is generated — properties the authors say prior point-cloud, surfel, TSDF, or frame-retrieval memories only partially satisfy.
**Breakthrough (≤3 sentences):** The authors report PPMem outperforms the point-cloud-based baseline Gen3C on DL3DV and RealEstate10K (e.g., PSNR 16.99 vs 15.74, LPIPS 0.335 vs 0.474 at N=49 on DL3DV), keeps a ~0.27 DINOv2-similarity lead over the next-best method at frame 300 in ~350-frame rollouts, and uses roughly 5 MB of memory for a full scene versus 1.7 GiB for an equivalent point cloud.
**Tools & method (≤3 sentences):** Built on the Wan 2.2 TI2V 5B diffusion transformer, PPMem regresses 7-parameter plane primitives per ~25-frame chunk and merges them into a pool via occlusion deletion, quality-based deduplication, and forward-looking pruning, training in two stages (video fine-tuning, then frozen-backbone geometry LoRA) on DL3DV and RealEstate10K.
**Limitation (≤3 sentences):** The authors state PPMem favors structured scenes with good planar priors and may under-represent highly organic environments compared to point-based methods, and extreme out-of-training camera trajectories can degrade quality. The frozen two-stage design means video and geometry are not jointly optimized end-to-end, and dynamic scenes/open-world scaling are left as future work.

## Agentic Physics-Grounded Video Generation via Memory-Augmented In-Context Reasoning
- **arXiv:** 2610.23677 · https://arxiv.org/abs/2610.23677
- **Submitted:** 2026-10-16 (v1)
- **Authors:** Xikang Guan, Shaocong Yang, Yanqi Bao, Can Wang, Zheng Gu, Zhengqing Chen, Kai Chen, Jing Huo, Yang Gao
- **Qualifying affiliation(s):** Horizon Robotics — Yanqi Bao, Zhengqing Chen (other authors are from Nanjing University, University of Hong Kong, Shenzhen University). FLAG: borderline — Horizon Robotics is a major Chinese autonomous-driving AI/chip company not on the explicit qualified list; kept per the "comparable-standing industry lab" allowance.
- **Categories:** cs.CV
- **Open release:** none (project page only, https://xxkkxxx.github.io/PhysRepair-Website/; no code/weights release stated)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** PhysRepair reframes physics-grounded video generation as "generate-diagnose-repair" rather than enforcing physics only before generation, using an agent to find and fix implausible dynamics after a video is produced via targeted local regeneration.
**Purpose (≤3 sentences):** It targets the failure mode where pre-generation physics guidance narrows motion diversity yet still misses physically invalid events — incorrect contact, forces, or material behavior — that only become visible after generation.
**Breakthrough (≤3 sentences):** On the Physics-IQ Verified benchmark (198 instances across solid mechanics, fluids, optics, thermodynamics, and magnetism), the authors report PhysRepair reaches a Physics-IQ score of 43.6 versus 42.7 for the strongest baseline (Cosmos3-Super-Image2Video) and 39.8 for its own unrepaired base generator, with spatiotemporal IoU rising from 22.8 to 34.7 after repair.
**Tools & method (≤3 sentences):** The system builds a spatiotemporal causal graph to localize the first invalid physical state and its causally affected descendants, restricts regeneration to just those states, and combines short-term working memory with retrieved long-term repair memory (experience-augmented in-context learning), running on a frozen MiniMax H3 generator with SAM 2, tracking, optical flow, depth tools, PyBullet/Blender simulation, and GPT-6-Astra for diagnosis and planning.
**Limitation (≤3 sentences):** The authors note that performance depends on the capability of the multimodal language model used as the repair agent, with weaker backbones giving less reliable repairs, and that the iterative repair process adds inference cost relative to single-pass generation.

## FlexPart: Text-Controlled Semantics-Aware 3D Part Segmentation at Flexible Granularity
- **arXiv:** 2610.23659 · https://arxiv.org/abs/2610.23659
- **Submitted:** 2026-10-16 (v1)
- **Authors:** Yiqun Zhao, Jiachen Xu, Yihao Zhi, Yunfei Zhao, Zibo Zhao, Xintong Han, Chunchao Guo, Shenghua Gao
- **Qualifying affiliation(s):** Tencent Hunyuan — Jiachen Xu, Yunfei Zhao, Zibo Zhao, Xintong Han, Chunchao Guo (others are University of Hong Kong / CUHK-Shenzhen)
- **Categories:** cs.CV
- **Open release:** none (project page only, https://zhao-yiqun.github.io/flexpart/; builds on open-source Hunyuan3D 2.1 as a base dependency, but states no own code/weights release)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** FlexPart segments 3D meshes into parts chosen and described by the user in free text, at whatever granularity the prompt implies, rather than following one fixed artist partition.
**Purpose (≤3 sentences):** It addresses the lack of 3D part datasets and controls that support multiple valid granularities and semantic (rather than purely geometric or click-based) part selection, framed as "what you ask for is what you get."
**Breakthrough (≤3 sentences):** The authors report their model beats the strongest baseline by 15% mIoU on PartObjaverse-Tiny even when that baseline uses ground-truth guidance, by 22% average mIoU on their new FlexPartBench, and by 35% IoU over the strongest click-based baseline on selective segmentation.
**Tools & method (≤3 sentences):** A VLM (Gemini) pipeline mines artist-authored components from HY3D-Bench into multi-granularity, text-labeled training data; a text-conditioned dual-stream DiT with a frozen Qwen3-VL-4B text encoder predicts a continuous part-identity field (6-bit codes per face) via flow matching, trained with background-dropping augmentation, with a frozen planner VLM able to fill in part descriptions from renderings at inference.
**Limitation (≤3 sentences):** The authors report that part boundaries can remain unresolved between similar or overlapping parts, and that location clauses may fail to disambiguate repeated or symmetric components (e.g., merging two of a ship's five sails). They also note the model can assign incorrect identifiers even to otherwise correctly located regions.

## TriFold: Folding irregular 3D Gaussians into structured latents for 3D Scene Generation
- **arXiv:** 2610.23050 · https://arxiv.org/abs/2610.23050
- **Submitted:** 2026-10-16 (v1)
- **Authors:** Yun Wang, Chiyu Wang, Fan Jiang, Ziyu Zhu, Zhaoxu Sun, Guangchi Fang, Mu Xu, Dapeng Wu
- **Qualifying affiliation(s):** Alibaba Group (AMAP) — Chiyu Wang, Fan Jiang, Ziyu Zhu, Zhaoxu Sun, Mu Xu (Yun Wang interned at AMAP; Wang and Wu are City University of Hong Kong)
- **Categories:** cs.CV
- **Open release:** none (project page only, https://fantasy-amap.github.io/TriFold; no code/weights release stated)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** TriFold is a variational autoencoder that folds the irregular, variable-count primitives of a 3D Gaussian Splatting scene into a fixed-size triplane latent, enabling standard latent generative modeling over 3DGS scenes.
**Purpose (≤3 sentences):** It addresses the mismatch between 3DGS scenes' irregular, variable-length Gaussian sets and the fixed-shape tensors latent generative models require, where prior fixed-budget, voxel, or field-based approaches struggle with density variation or high-frequency attributes.
**Breakthrough (≤3 sentences):** The authors report a 5.15 dB PSNR gain in reconstruction over the GaussianGPT baseline (26.55 vs 21.40 dB, with lower LPIPS and Chamfer Distance) on InteriorGS and the Aria Synthetic Environments subset of SceneSplat-49K, and demonstrate point-cloud-conditioned and single-image amodal scene generation via a trained latent flow-matching model.
**Tools & method (≤3 sentences):** A modified Point Transformer V3 encoder with learned per-cell queries projects Gaussians onto three planes with sparse cross-plane attention and a variational bottleneck; a DETR-style set decoder with optimal-transport matching reconstructs variable Gaussian counts per voxel, trained on AMD MI308X GPUs with occupancy, OT-center, rendering, and phantom-voxel losses.
**Limitation (≤3 sentences):** An appendix limitations note states reconstructions "are not flawless," with sparsely observed regions near scene boundaries appearing less sharp than ground truth. The authors also note single-image-conditioned completions in unobserved regions may plausibly differ from the true reference scene.

## ESC: Escaping 2D Diffusion Ambiguity with Geometric Constraints for Consistent Novel View Synthesis
- **arXiv:** 2610.23732 · https://arxiv.org/abs/2610.23732
- **Submitted:** 2026-10-14 (v1)
- **Authors:** Ge Ya Luo, Daniel Severo, Brian Karrer, Christopher Pal, Adriana Romero-Soriano, Michal Drozdzal
- **Qualifying affiliation(s):** Meta (FAIR) — Daniel Severo, Brian Karrer, Michal Drozdzal, Adriana Romero-Soriano (joint last author); Ge Ya Luo's work was done at Meta. Pal is Mila/Polytechnique Montréal.
- **Categories:** cs.CV
- **Open release:** none found
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** ESC targets single-image novel view synthesis under large camera changes, where 2D diffusion models can produce plausible but geometrically invalid views that standard 2D or pose metrics fail to catch.
**Purpose (≤3 sentences):** It aims to improve the 3D consistency of generated novel views by resolving the depth/geometry ambiguity inherent in purely 2D diffusion-based view synthesis.
**Breakthrough (≤3 sentences):** The authors report that jointly generating RGB and depth, combined with their Projection Consistency Constraint (PCC) used for best-of-N selection (ESC-PCC-BoN), improves consistency over their own base model on DL3DV, RealEstate10K, and Tanks & Temples (e.g., DL3DV LPIPS 0.4340 vs 0.4448, PCC 0.2257 vs 0.2448). They also report PCC computed from predicted depth correlates with PCC from reference DA3 depth at Pearson r = 0.955.
**Tools & method (≤3 sentences):** Built on a Qwen MM-DiT backbone with LoRA adaptation and a Ray ControlNet for pose conditioning, ESC concatenates depth tokens with image tokens to jointly predict target RGB and depth from a source image, its depth map, and Plücker ray maps for source and target cameras, trained on a DL3DV/RealEstate10K mixture.
**Limitation (≤3 sentences):** The authors note off-the-shelf DA3 depth is noisy even in consistent scenes, and that best-of-N selection scales compute roughly linearly with N without being compute-matched against single-sample baselines. They also note PSNR/SSIM — on which baselines like LagerNVS score higher — may penalize plausible but pixel-misaligned generations.

# Near-misses
- 2610.23722 · Beyond Large Language Models: A Mental World Model Framework for Mental Modeling, Simulation, Evolution, and Interpretability · off-topic: cognitive-science / Theory-of-Mind mental-modeling framework, not a 3D/visual/game-relevant world model; sole-author paper with no HTML version available to verify any industry affiliation.
- 2610.23622 · Foundation-Model-Driven 3D Scene Graphs for Mobile Manipulation · off-topic: robotics/mobile-manipulation application (MIT-led, cs.RO) — scene graphs built for robot navigation and grasping, not for 3D content generation, world models, or games.
- 2610.23423 · Momentum: Persistent Dynamics for Video World Models · no industry affiliation: all six authors are academic (INSAIT/Sofia University, Harvard, University of Ulm, TUM, MCML); no qualifying company found despite the regex hit.
- 2610.23334 · LAW: Unifying Language, Action, and World Modeling for Agentic Physical Intelligence · no industry affiliation: all 20 authors are affiliated only with Peking University and the Beijing Innovation Center of Humanoid Robotics (a research institute, not a qualified company); the "Google" screen match appears to be a false positive.
- 2610.22708 · GlobeBench: Evaluating Text-Based World Model Capabilities for Scalable Environment Simulations · off-topic: purely text-based LLM environment-simulation benchmark (cs.AI/cs.CL), not 3D/visual/game-engine-relevant; also no HTML version available to verify affiliation.
- 2610.22450 · DriveWorld3D: Evidence Constrained 3D World Modeling and Generative Simulation for Real-World Autonomous Driving · affiliation unverifiable (no HTML version) — the abstract page gives only a partial, truncated author list ("Wei Wang and 6 other authors") with no stated institutional affiliations.
