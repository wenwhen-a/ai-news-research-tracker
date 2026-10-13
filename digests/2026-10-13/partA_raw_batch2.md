## UniBRep: Learning Unified Geometry and Topology for Image-conditioned B-Rep Generation
- **arXiv:** 2610.04092 · https://arxiv.org/abs/2610.04092
- **Submitted:** 2026-10-02
- **Authors:** Haiyang Ying, Allen Tu, Jiaye Wu, Tom Goldstein, Matthias Zwicker
- **Qualifying affiliation(s):** Amazon — Jiaye Wu (listed as "Amazon, Bellevue, Washington, USA"); other authors are University of Maryland, College Park
- **Categories:** cs.CV (primary), cs.GR
- **Open release:** none found (no code/demo link in abstract, comments, or HTML)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** UniBRep is a geometry-first framework that adapts a pretrained image-to-3D model to generate CAD B-Rep (boundary representation) solids from a single image. Dual decoder branches jointly produce a feature mesh's geometry and face-separation signal, and a CAD-kernel-based construction pipeline fits surfaces and recovers boundary curves/connectivity to assemble a valid B-Rep. It is evaluated on the DeepCAD benchmark against CADDreamer and the HoLa public demo.

**Purpose (≤3 sentences):** The authors target image-conditioned CAD generation, aiming to directly produce structured, editable B-Rep CAD models (not just meshes) from a single input image. They frame this as unifying geometry prediction and topology recovery in one pipeline rather than treating them as separate stages.

**Breakthrough (≤3 sentences):** The authors report producing valid B-reps for 80.49% of DeepCAD inputs and reducing face Chamfer distance from 0.1096 (CADDreamer) to 0.0345. They also report outperforming the HoLa public demo in a matched comparison, and qualitatively demonstrate generalization to shapes beyond 30 faces, outside the CAD training distribution, and to real photographs.

**Tools & method (≤3 sentences):** The method adapts a pretrained image-to-3D generative model and adds dual decoder branches for geometry and face-separation features, followed by a CAD-kernel construction pipeline that fits surfaces and recovers curves/connectivity. Training and evaluation use the DeepCAD benchmark.

**Limitation (≤3 sentences):** The paper does not state explicit failure-mode limitations beyond reporting the 80.49% valid-B-rep rate (implying ~20% of inputs do not yield a valid B-rep). No further acknowledged limitations were extracted from the abstract/HTML text reviewed.

## Game-Guided Skill Discovery through Self-Play for Playable Agent Control
- **arXiv:** 2609.40137 · https://arxiv.org/abs/2609.40137
- **Submitted:** 2026-09-30
- **Authors:** Seungeun Rho, Jeonghwan Kim, Xue Bin Peng, Sehoon Ha
- **Qualifying affiliation(s):** NVIDIA — Xue Bin Peng (listed as "Simon Fraser University and NVIDIA")
- **Categories:** cs.LG (primary), cs.AI, cs.RO
- **Open release:** demo — https://ggsd-demo.github.io (interactive demo)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper presents Game-Guided Skill Discovery (GGSD), which uses self-play in games to discover a small set of motor skills that a human can control directly, like a video-game character controller. A hierarchical agent competes against past versions of itself; a high-level policy selects among a small discrete skill set, and a skill-conditioned low-level policy executes each behavior. A human can then take over the high-level policy to control the agent with the learned skills.

**Purpose (≤3 sentences):** The authors aim to discover skills that are not just useful for autonomous agents but are directly "playable" by a human, i.e., controllable and composable in real time. They test whether people can combine the discovered skills to solve tasks the system was never trained on.

**Breakthrough (≤3 sentences):** The authors report that skill transitions produce emergent combo behaviors not explicitly trained for. They report results across Ant, Franka-arm, and Unitree G1 (simulated) environments, where human players composed the learned skills to solve unseen tasks such as Maze and CubePush with no additional training.

**Tools & method (≤3 sentences):** The approach combines self-play (agent vs. past selves) with hierarchical reinforcement learning: a discrete high-level skill selector and per-skill low-level policies. An interactive demo lets users try the human-playable control directly.

**Limitation (≤3 sentences):** The abstract/HTML reviewed did not state explicit acknowledged limitations; the environments used (Ant, Franka-arm, Unitree G1) appear to be simulated rather than deployed on physical hardware, which bounds the generality of the human-playability claims.

## MegaAvatar: Controllable Talking Avatar Generation
- **arXiv:** 2609.39273 · https://arxiv.org/abs/2609.39273
- **Submitted:** 2026-09-30
- **Authors:** Junyao Gao, Sibo Liu, Weidong Zhang, Cairong Zhao, Jun Zhang
- **Qualifying affiliation(s):** Tencent — Junyao Gao, Sibo Liu, Weidong Zhang (listed as "Affiliation: Tencent"; footnote: "done during Junyao Gao's internship at AIPD, Tencent")
- **Categories:** cs.CV
- **Open release:** none yet — authors state code, dataset, and models "will be released on GitHub" (not yet confirmed live)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** MegaAvatar is a controllable talking-avatar generation framework built on the Wan2.2-TI2V-5B video diffusion model. It adds body/head control via a rendered, encoded SMPL-X driving sequence injected into latent tokens, plus audio and face cross-attention modules for speech-synchronized expression control and identity preservation. An audio-to-SMPL-X model lets the system run from just a reference image and audio, without requiring users to supply motion sequences.

**Purpose (≤3 sentences):** The authors aim to generate talking avatar videos with controllable full-body and head motion, fine-grained expression, and preserved identity, rather than face-only talking-head synthesis. They also target flexibility across resolutions and video lengths.

**Breakthrough (≤3 sentences):** The authors report high-quality results with controllable body and head motion and consistent identity preservation across different resolutions and video lengths. The audio-to-SMPL-X component is reported to remove the need for users to manually supply driving motion sequences.

**Tools & method (≤3 sentences):** Built on Wan2.2-TI2V-5B; adds a lightweight 3D convolutional encoder for dense SMPL-X mesh frames, audio and face cross-attention modules, and an audio-to-SMPL-X motion predictor. Code, dataset, and models are stated to be released on GitHub (not yet verified as live).

**Limitation (≤3 sentences):** The abstract/HTML reviewed did not state explicit acknowledged limitations or quantitative benchmark numbers beyond qualitative claims of "high-quality" and "controllable" results.

## Does Native 3D Texture Generation Necessarily Require 3D Assets for Training?
- **arXiv:** 2609.34621 · https://arxiv.org/abs/2609.34621
- **Submitted:** 2026-09-28
- **Authors:** Jiangshan Wang, Zeqiang Lai, Jiayi Guo, Xin Yang, Xin Huang, Jiarui Chen, Ziheng Ouyang, Chunchao Guo, Xiangyu Yue
- **Qualifying affiliation(s):** Tencent — via "Tencent Hunyuan" affiliation for Jiangshan Wang, Xin Yang, Xin Huang, Jiarui Chen, Ziheng Ouyang
- **Categories:** cs.CV
- **Open release:** code — https://github.com/wangjiangshan0725/Tex-Zero
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper introduces Tex-Zero, a native 3D texture generation framework (VAE + diffusion transformer) trained entirely without 3D asset data. Instead, it converts 2D images into pseudo-3D training samples by placing images on planes in 3D space, randomly rotating and aggregating them into complex shapes. A VAE trained on these samples reconstructs real, unseen 3D assets, and a diffusion transformer conditioned on multi-view images (encoded by the same VAE) generates native 3D textures.

**Purpose (≤3 sentences):** The authors ask whether native 3D texture generation genuinely requires 3D training assets, arguing that fine-grained 2D color/texture information matters more than 3D geometry data, which can instead be synthesized procedurally. They aim to remove the dependency on curated 3D texture datasets.

**Breakthrough (≤3 sentences):** The authors report that Tex-Zero produces high-fidelity textures with fine detail despite being trained using only 2D image data, and that its VAE generalizes to reconstruct real 3D assets never seen in training. This is reported as evidence against the necessity of 3D asset data for native 3D texture generation.

**Tools & method (≤3 sentences):** Method: synthetic 3D training samples built from planar-projected 2D images with random rotation/aggregation; a VAE trained on these samples; a diffusion transformer trained on the same data with multi-view image conditioning via the VAE encoder. Code is released on GitHub.

**Limitation (≤3 sentences):** The abstract/HTML reviewed did not list explicit acknowledged limitations beyond the core claim being about texture fidelity; no quantitative benchmark comparisons were surfaced in the sections reviewed.

## ReFM: Semantic-Aware Refinement Flow Model for Motion Retargeting
- **arXiv:** 2609.32068 · https://arxiv.org/abs/2609.32068
- **Submitted:** 2026-09-25
- **Authors:** Jingxiang Qu, Lucie Taglienti, Evan Atherton
- **Qualifying affiliation(s):** Autodesk (borderline/comparable company, flagged) — Lucie Taglienti and Evan Atherton listed under "Affiliation: Autodesk Research"; Jingxiang Qu's work was conducted "during an internship at Autodesk" under their mentorship
- **Categories:** cs.CV (primary), cs.AI, cs.GR
- **Open release:** none found
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** ReFM addresses motion retargeting — transferring motion between characters with different skeletons — by treating it as progressive refinement rather than single-pass regression or direct copying of source motion. It uses an SO(3) canonicalizer to remove global-orientation variation and a contrastively pretrained cross-character semantic encoder, then applies a learned flow to refine an initial target motion guided by semantic consistency, physical plausibility, temporal coherence, and minimal modification.

**Purpose (≤3 sentences):** The authors argue existing retargeting methods carry over artifacts from mismatched character proportions when copying source motion as initialization, and that single-pass regression is too restrictive for this underdetermined problem. ReFM aims to be source-mesh-agnostic and work with various initializations, including direct copying and industry tools.

**Breakthrough (≤3 sentences):** The authors report that ReFM works as a refinement layer compatible with different initializations, including both direct motion copying and Autodesk HumanIK (an industry-standard full-body IK retargeting system), improving on both. Specific quantitative benchmark numbers were not surfaced in the abstract text reviewed.

**Tools & method (≤3 sentences):** Core components: an SO(3) canonicalizer for orientation normalization, a contrastively pretrained cross-character semantic encoder, and a learned flow-based refinement model conditioned on semantic/physical/temporal objectives. Compared against direct copying and Autodesk HumanIK as initialization baselines.

**Limitation (≤3 sentences):** The abstract/HTML reviewed did not state explicit acknowledged limitations; no quantitative results or dataset details beyond the method description were extracted.

# Near-misses
- 2610.02388 · Octrees as an Explicit 3D Language (OctLLM) · False positive: all authors are Peking University or independent researchers; the only "Meta" mentions are a citation "(Meta AI, 2023)" and a Llama 2 reference entry, not an author affiliation.
- 2609.37181 · EgoHumanoid-V2: Human-to-Humanoid Transfer of Coordinated Whole-Body Skills for Loco-Manipulation · Real Alibaba Group affiliation confirmed (internship at Alibaba Token Hub), but topic is physical humanoid robot loco-manipulation/sim-to-real transfer (cs.RO), not character/avatar animation — off-topic per scope rules.
- 2609.37831 · ReCaVSR: One-Step Streaming Diffusion Video Super-Resolution with Recycled Latents and Learned Cache Routing · False positive: "NVIDIA" appears only as GPU hardware ("a single NVIDIA A100-80GB"), all authors are University of Science and Technology of China; also off-topic (video super-resolution, not 3D/world models/character animation/game engines).
- 2609.38172 · Counterfactual Video Generation Enables Scalable Humanoid Loco-Manipulation (PRISM) · Real Amazon FAR affiliation confirmed for all 9 authors, but topic is physical humanoid robot loco-manipulation deployed on real robot hardware (cs.RO primary), not character/avatar animation — off-topic per scope rules despite using video generation.
