## NOFACE3D: NOise-scheduled Focused Anchoring and Controlled Enhancement for 3D Generation
- **arXiv:** 2610.13050 · https://arxiv.org/abs/2610.13050
- **Submitted:** 2026-10-09
- **Authors:** James Rose, Jingwen Liang, Wenchao Ma, Oren Jacob, Haomiao Jiang
- **Qualifying affiliation(s):** Roblox (listed affiliation in author header, alongside The Pennsylvania State University; exact per-author mapping is unclear in the rendered HTML, but Roblox appears as a real author affiliation, not a citation)
- **Categories:** cs.CV
- **Open release:** none stated; project page only — https://idkcouscous.github.io/NoFACE3D/
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** Image-to-3D generators produce convincing overall shapes but render thin, small, or detail-rich regions soft and under-resolved because fixed-resolution voxel grids sample all surfaces at the same density. NOFACE3D is a training-free, inference-time method built on the frozen TRELLIS.2 generator that re-extracts and refines selected detail-critical submeshes and merges them back into the full asset. It uses flow-based sampling guided by the input image crop and a spatially varying noise schedule that anchors region boundaries during re-generation.
**Purpose (≤3 sentences):** To recover fine geometric and textural detail in generated 3D meshes without retraining the base generator, targeting regions a fixed-resolution grid under-samples.
**Breakthrough (≤3 sentences):** The authors report improved detail fidelity over the TRELLIS.2 baseline on PAniC-3D (FID 33.02 vs. 43.17, DINO 0.812 vs. 0.792) and TexVerse (DINO 0.741 vs. 0.728, FID 64.92 vs. 66.56), plus a GPT-5.6 judged win-share advantage on both. In a 16-reviewer, 1,188-response human study on PAniC-3D, 83.3% of judged ratings favored NOFACE3D over TRELLIS.2.
**Tools & method (≤3 sentences):** Built on TRELLIS.2's sparse voxel representation; evaluated on PAniC-3D (329 artist-paired anime character assets, with a larger 4,892-asset version in the appendix), TexVerse (151 PBR-textured objects), and a new 339-asset benchmark, BigDetail, introduced by the authors. Timing was measured on NVIDIA RTX A6000 and H100 GPUs.
**Limitation (≤3 sentences):** Because it is training-free and built on a frozen generator, the method inherits TRELLIS.2's limits and cannot produce content the base model otherwise can't generate. The authors note printed labels and lettering often remain distorted after refinement, and suggest (without testing) post-training the generator on text-rich data as a possible fix.

## GenIA: Generative Reconstruction with Test-Time Input Alignment
- **arXiv:** 2610.12388 · https://arxiv.org/abs/2610.12388
- **Submitted:** 2026-10-08
- **Authors:** Stefano Esposito, Naama Pearl, Polina Karpikova, Samuel Rota Bulò, Lorenzo Porzi, Peter Kontschieder, Andreas Geiger, Jonathon Luiten
- **Qualifying affiliation(s):** Meta Reality Labs — Samuel Rota Bulò, Lorenzo Porzi, Peter Kontschieder, Jonathon Luiten (other authors are Tübingen AI Center / University of Tübingen)
- **Categories:** cs.CV
- **Open release:** none found
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** Generative 3D models can hallucinate plausible geometry for unseen parts of an object from one or a few views, but their outputs often don't match the observed geometry, appearance, or pose. GenIA steers an existing generative 3D model (SAM3D) at test time, without retraining, by estimating object translation and scale from observed geometry while keeping the model's learned rotation prior, and by refining appearance through attention, multi-view fusion, and rendering-based guidance during denoising. It also supports externally supplied geometry for dynamic (moving/deforming) objects.
**Purpose (≤3 sentences):** To align a frozen generative reconstruction model's output with real observations (pose, scale, appearance) at inference time, improving single/few-view 3D object reconstruction for both static and dynamic objects.
**Breakthrough (≤3 sentences):** The authors report better pose estimation and reconstruction than recent optimization-based, per-frame image-to-3D, and video-to-4D baselines; depth-grounded translation/scale reduce reprojection error by 1.4–2.8x and relative jitter by 2–4x, and ICP halves Chamfer distance on static reconstruction. On their ActionBench tracking metric, GenIA reaches 0.50 versus Any4D's 0.71 and HiMoR's 0.65 (lower reported as better in their table), and leads DAVIS occlusion agreement (0.37) over Lift4D (0.27), though behind HiMoR (0.42).
**Tools & method (≤3 sentences):** Built on top of the SAM3D generative model, with dynamic-object geometry supplied by an external predictor, ActionMesh. Evaluated on GSO-30 (30 rendered objects), CO3D (10 sequences, LaRa protocol), ActionBench (6 Sketchfab-animation scenes created by the authors), and DAVIS (10 monocular video sequences).
**Limitation (≤3 sentences):** Dynamic-object geometry depends on the external ActionMesh predictor rather than being grounded directly in observations, so its errors or misplacements can strongly degrade results; rotation remains largely prior-driven and is corrected only by a noise-sensitive ICP step. The authors note ICP's effect is dataset-dependent (it worsens appearance/reprojection error on DAVIS) and that test-time refinement can lower CLIP-I when it overfits to inaccurate geometry.

## Zebra3D: Efficient Hybrid Foundation Models For Scalable 3D Reconstruction
- **arXiv:** 2610.12727 · https://arxiv.org/abs/2610.12727
- **Submitted:** 2026-10-08
- **Authors:** Utkarsh Saxena, Ruijing Yang, Mehdi Rezagholizadeh, Akash Haridas, Vikram Appia, Emad Barsoum
- **Qualifying affiliation(s):** AMD (Advanced Micro Devices) — all six authors, per the paper's affiliation block. **Flag: BORDERLINE** — AMD is on the borderline/comparable-labs list, not the main qualifying list. Note: the pre-screen's "Tencent" and "Google" flags are **false positives** — the paper's real affiliation is AMD; Tencent and Google appear only as citations to baseline models the authors benchmark against (HunyuanWorld-Mirror is a Tencent model, VGGT/π³ are associated with Google-adjacent prior work), not as author affiliations.
- **Categories:** cs.CV (primary), cs.LG
- **Open release:** none yet; authors state in a Reproducibility Statement that code, configs, custom kernels, and checkpoints "will be" released upon publication, but no link is given in the text read.
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** Feed-forward 3D foundation models (e.g., VGGT, HunyuanWorld-Mirror, π³) reconstruct scenes from unposed images, but their global self-attention scales quadratically with view count, limiting them to modest numbers of views; the authors report attention accounts for 88% of VGGT's runtime at 512 views. Zebra3D converts these pretrained models into hybrids, training-free via closed-form affine fitting, that use linear attention in early layers (found to tolerate approximation) and tile-sparse attention with landmark summaries in middle-to-late layers (found to need more concentrated attention), with optional post-conversion distillation training.
**Purpose (≤3 sentences):** To make existing dense-attention 3D foundation models scale efficiently to much larger numbers of input views without retraining them from scratch.
**Breakthrough (≤3 sentences):** The authors report end-to-end speedups that grow with view count, reaching up to 7.1x at 1,024 views, and after post-conversion training, Zebra3D-VGGT reaches 80.5% RealEstate10K AUC@30 at 94% mean attention sparsity, within 1.1 percentage points of dense VGGT trained under the same schedule. Training-free variants stay close to dense-model accuracy at high sparsity levels across multiple benchmarks (7Scenes, NRGBD, CO3Dv2).
**Tools & method (≤3 sentences):** Applied to three pretrained backbones (VGGT, HunyuanWorld-Mirror, π³); evaluated on 7Scenes, Neural RGB-D, RealEstate10K, CO3Dv2, DTU, and ScanNet-50 (FastVGGT long-sequence protocol), with training using a 20% subset of HunyuanWorld-Mirror data. Training used 8x AMD MI355X GPUs (BF16); single-GPU MI355X for timing.
**Limitation (≤3 sentences):** The authors report no single attention-mixer variant wins on every metric (e.g., Sparse Linear Attention is best on NRGBD while SGA stays competitive on some 7Scenes metrics), and linear-attention conversion is most disruptive in a narrow middle band of layers. Training used at most 16 views per sequence, so results on longer sequences test generalization beyond the trained regime; oracle block selection recovers only part of the teacher's attention mass at a 20% compute budget.

## No Distillation Needed: Single-Pass Real-Time Talking Heads via Acausal Noise Shaping
- **arXiv:** 2610.11070 · https://arxiv.org/abs/2610.11070
- **Submitted:** 2026-10-08
- **Authors:** Yu Han, Dejan Markovic, Alexander Richard, Wojciech Zielonka, Akshay Venkatesh, Cheng-hsin Wuu, Michael Zollhoefer
- **Qualifying affiliation(s):** Meta Reality Labs — all authors
- **Categories:** cs.CV
- **Open release:** none stated; project page with supplemental videos — https://wojciechzielonka.com/facegan/
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** Real-time audio-driven facial animation for avatars must generate each output frame from only the audio received so far (streaming/causal), but diffusion models — the current state of the art — need many network passes per frame, which is a poor fit for this setting. The authors argue facial motion is low-dimensional enough for a single-pass GAN, and that a causal generator fed independent per-step noise cannot suppress output in a frequency band without also losing step-to-step variation. Their model, FaceGAN, resolves this by shaping the noise path non-causally (sampling future noise in advance since it's synthetic) while keeping the audio-to-expression path itself causal.
**Purpose (≤3 sentences):** To produce real-time, streaming, single-pass audio-driven facial animation (expression + head pose) without the multi-step inference cost of diffusion-based talking-head methods or the need for offline distillation.
**Breakthrough (≤3 sentences):** The authors report FaceGAN achieves the best Sync Score (0.8767) among compared methods (Fallingwater, DiffPoseTalk, MemoryTalker, ARTalk) and competitive FED/FPD, while running at 43.3 ms per frame (12.1x real time) on a single H200, with time-to-first-frame of 83 ms versus 4.20 s for ARTalk. A 19-participant, 684-comparison user study found FaceGAN preferred on lip sync (50.5%) and naturalness (57.1%) pooled against baselines.
**Tools & method (≤3 sentences):** Trained and evaluated on a dataset from Chu et al. (2026) of 34,906 clips from 832 subjects (469.6 hours), with 784 training / 48 test identities and a fixed 64-clip held-out test set; training used 8x NVIDIA H200 GPUs, with single-H200 latency benchmarking.
**Limitation (≤3 sentences):** FaceGAN is not best on every metric — ARTalk scores better on FPD and Similarity, DiffPoseTalk on FED — and an ablation shows a fully causal variant (zero lookahead) or a causal noise stack both reduce expression/pose quality and diversity. The model outputs expression/pose coefficients rather than pixels (so photorealistic video needs an external renderer the authors don't provide), is not conditioned on speaker identity or style, and the authors acknowledge deepfake-misuse risk that the output format only partly mitigates.

## GHARP: Real-time Gaussian Head Animation from Large-scale Reconstruction Prior
- **arXiv:** 2610.10945 · https://arxiv.org/abs/2610.10945
- **Submitted:** 2026-10-07
- **Authors:** Ali Benlalah, Sepehr Johari, Patricia Vitoria, Armin Kappeler, Artem Sevastopolsky, Alexander Jung, Gabriele Fanelli, Kevin Mader, Manuel Breitenstein, Claudia Plüss, Jan Rüegg, Simon Biland, Thomas Etterlin, Dmitry Kostiaev, Mathias Deschler, Brian Amberg, Sebastian Martin
- **Qualifying affiliation(s):** Apple — all 17 authors
- **Categories:** cs.CV (primary), cs.LG
- **Open release:** none found
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** GHARP animates 3D human heads in real time from a few input images plus a driving expression signal, splitting the task into an offline per-subject identity stage (building geometry/appearance) and a lightweight runtime animation stage suited to mobile devices. Animation happens in the latent space of a pretrained large-scale reconstruction prior ("HeadsUp"), fusing multiple input views into a compact canonical Gaussian representation. A body-alignment network (BAN) corrects for body pose/clothing mismatches that expression codes don't capture, reducing blur and temporal flicker.
**Purpose (≤3 sentences):** To achieve real-time, high-fidelity, mobile-capable 3D Gaussian head animation that is both faster and higher-quality than prior reconstruction-prior-based methods.
**Breakthrough (≤3 sentences):** The authors report state-of-the-art quality on Ava-256 with 13x faster runtime and 8x fewer Gaussians than compared methods; their body-alignment variant (Ours+BAN) reduces body temporal instability to σ_body^t 0.7 versus 18.8 (Avat3r) and 22.9 (FastGHA). Animation runs at 1.18 ms (851 FPS) on an H100 regardless of view count, and 5.1 ms (196 FPS) on an iPhone 17 Pro GPU, versus much slower comparable methods (e.g., FastGHA 17.6–66.9 ms on iPhone depending on view count).
**Tools & method (≤3 sentences):** Built on the "HeadsUp" large-scale reconstruction prior trained on studio data (10k subjects, with a 1k-subject ablation); evaluated on Ava-256 and an in-the-wild iPhone 15 video with ARKit-extracted expression codes. Benchmarked on NVIDIA A100/H100 and iPhone 17 Pro GPU/ANE hardware.
**Limitation (≤3 sentences):** The HeadsUp prior was trained on studio data with specific camera configurations/focal lenses, and the authors say adapting it to more diverse capture settings is future work. A narrow frozen-body blend leaves a neck seam on mouth opening, while a wider blend alters chin shape and reduces expression fidelity; a weaker (1k-subject) prior lowers reconstruction quality though animation fidelity stays above baselines.

## MeshOctave: Vertex Split-and-Rewire Cascades for Native Mesh Generation
- **arXiv:** 2609.38985 · https://arxiv.org/abs/2609.38985
- **Submitted:** 2026-09-30
- **Authors:** Junkai Lin, Tianhao Zhao, Hang Long, Huipeng Guo, Jielei Zhang, Youjia Zhang, Jiale Xu, Wenbing Li, Rendong Liang, Jozef Hladký, Matthias Nießner, Yuanming Hu, Wei Yang
- **Qualifying affiliation(s):** Meshy AI (several authors, including the corresponding-adjacent "Project Leader" marker and a footnote stating one author's contribution "was done while interning at Meshy AI"). **Flag: BORDERLINE** — Meshy AI is a 3D-generation startup, not on the main tracked-company list (other co-authors: Huazhong University of Science and Technology, Technical University of Munich, and an independent researcher).
- **Categories:** cs.CV
- **Open release:** none stated; project page only — https://maymhappy.github.io/MeshOctave/
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** Current artist-style mesh generation methods either generate connectivity tokens one at a time (slow) or rely on heuristic connectivity decoders. MeshOctave defines levels of detail via dyadic spatial grid resolutions: a coarsening step merges vertices sharing a voxel cell, and a reverse "split-and-rewire" step decides which sub-vertices to create per coarse face and resolves connectivity via discrete structural tokens. Because these operations work per-face without serialization, generation parallelizes within each scale and handles variable mesh length and adaptive resolution.
**Purpose (≤3 sentences):** To generate artist-quality 3D meshes natively (with proper topology/connectivity) faster and more faithfully than token-by-token autoregressive or heuristic-decoder approaches.
**Breakthrough (≤3 sentences):** The authors report MeshOctave beats all compared autoregressive, next-scale, and flow-matching baselines on every metric in their main comparison (CD-L2 0.0392 vs. 0.0406 for the strongest baseline; Hausdorff distance 0.0645 vs. 0.0665; normal consistency 0.8478 vs. 0.8333). Generation takes about 8s per scale (20 diffusion steps) and about 90s across all 10 scales, roughly independent of face count.
**Tools & method (≤3 sentences):** A scale-conditioned masked discrete diffusion model trained on ~350K meshes filtered from Objaverse and Toys4K (up to 15K faces); evaluated on 300 meshes from ObjaverseXL/Toys4K plus 200 meshes generated by large 3D generative models. Training used 8x NVIDIA H800 80GB GPUs over 7 days; baselines (VertexRegen, ARMesh) were retrained from scratch on a separate 200K-mesh set.
**Limitation (≤3 sentences):** Sequential generation across scales has higher latency than single-scale flow matching, and because the method has no backtracking, coarse topological errors can propagate to finer scales. Thin features confined to a single voxel are handled via degenerate zero-area faces — described by the authors as a workaround rather than a full solution — and the authors list diffusion distillation and bidirectional topology revision as future work.

## Considering Context: When World Models Need Context Encoders
- **arXiv:** 2610.06651 · https://arxiv.org/abs/2610.06651
- **Submitted:** 2026-10-05
- **Authors:** Oleg Smirnov, Sofiane Ennadir, John Pertoft, Bjartur Hjaltason, Sara Karimi
- **Qualifying affiliation(s):** Microsoft — King AI Labs, Microsoft Gaming (all five authors; Sara Karimi also lists KTH Royal Institute of Technology)
- **Categories:** cs.LG
- **Open release:** code — anonymous reference codebase at https://anonymous.4open.science/r/considering_context/ (source, configs, protocols)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** Model-based reinforcement learning commonly assumes an agent cannot infer the latent context governing environment dynamics from its own experience, so systems supply that context externally (e.g., to a world model like DreamerV3). The authors introduce "predictive sufficiency," decomposing how much context access improves next-step prediction into a part recoverable from history, a residual that truly requires ground-truth context, and error added by a finite learned model. They test this across discrete/continuous diagnostic environments and standard RL benchmarks.
**Purpose (≤3 sentences):** To determine when and how much context-aware mechanisms (e.g., explicit context encoders) actually help model-based RL world models, versus when an agent's own learned state already implicitly captures the needed information.
**Breakthrough (≤3 sentences):** The authors report that predictive headroom from context does not simply follow the environment's MDP class — in some settings, agent behavior already implicitly identifies context so context-aware mechanisms add nothing (e.g., near-zero headroom for DreamerV3, DALI-S, and cRSSM-D on their "identifiable" CARL DMC Walker Walk setting), while in a "hard" setting the learned state captures only part of the available headroom (e.g., LILAC-style shows 3.49 ± 0.68 headroom with 0.73 ± 0.29 residual gain). They propose a practical criterion for matching contextual mechanisms to available information, estimable from an ordinary trained agent without needing a reference policy.
**Tools & method (≤3 sentences):** Evaluated on MiniGrid Empty-8x8 (Wind/Resistance variants), a custom Point-Mass-Attractor environment, CARL DMC Walker Walk (identifiable and "hard" settings), RWRL Walker (non-i.i.d. parameter drift), and a linear-Gaussian calibration environment with a hidden Markov regime; compared methods include DreamerV3, DALI-S, LILAC-style, and cRSSM-D. Compute: single 24GB NVIDIA L4 GPU runs (~9 hours per 10^6 steps).
**Limitation (≤3 sentences):** The authors note their estimates are properties of a closed loop — each method's own visitation shapes what information it can access — and they deliberately avoid a shared reference policy, leaving cross-visitation comparisons (e.g., paired counterfactual resets) to future work. Estimates are conservatively biased upward (finite-sample error can inflate apparent headroom), and the calibration attenuation ratio is characterized only on one calibration environment, with no claim it transfers elsewhere.

## PixReenact: Pixel-Conditioned Causal Video Diffusion for Streaming Head-Avatar Reenactment
- **arXiv:** 2610.05233 · https://arxiv.org/abs/2610.05233
- **Submitted:** 2026-10-04
- **Authors:** Gavriel Habib, Dvir Samuel, Or Shimshi, Rami Ben-Ari
- **Qualifying affiliation(s):** NVIDIA — Dvir Samuel (other authors: OriginAI, Israel). Real author affiliation confirmed in the paper's own header, not a GPU-hardware mention or project-host artifact.
- **Categories:** cs.CV
- **Open release:** none stated; project page only — https://gavriel-habib.github.io/pixreenact/
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** PixReenact is a streaming system that animates a reference face using a live driving video, operating directly on encoded image frames rather than specialized identity/motion features extracted by external models (which the authors argue inherits those extractors' errors). Training uses pseudo cross-identity pairs and corrective objectives to disentangle "who someone looks like" from "how they move," plus long self-rollouts with dual-teacher distillation to reduce drift over streaming use. A 4-step distilled student model emits four frames per update.
**Purpose (≤3 sentences):** To enable robust, low-latency, streaming head-avatar reenactment that stays stable over long sessions and handles extreme viewpoints, occlusions, and strong expressions better than prior feature-extractor-based pipelines.
**Breakthrough (≤3 sentences):** The authors report strong gains over PersonaLive on identity preservation under extreme conditions (ID 0.727 vs. 0.472) and especially on self-reenactment fidelity (TalkingHead-1KH PSNR 37.48 vs. 19.55, FVD 8.2 vs. 199.4; VFHQ-Test FVD 5.5 vs. 83.8). The 4-step student model runs at a mean latency of 239 ms per 4-frame chunk (16.74 FPS) on a single H200.
**Tools & method (≤3 sentences):** Trained with pseudo cross-identity pairs and dual-teacher distillation; evaluated on CelebV-HQ (extreme-condition drivers), FFHQ (references), TalkingHead-1KH, VFHQ-Test, NeRSemble (15 held-out subjects), and HDTF/self-collected YouTube videos for long-horizon streaming tests. Teacher training used 44 NVIDIA H200 GPUs, final student training 4 H200s.
**Limitation (≤3 sentences):** The authors note PixReenact is slower per-chunk than the PersonaLive baseline (238.9 ms vs. 211.1 ms, 16.74 vs. 18.95 FPS), and fewer denoising steps (3- or 2-NFE) cut latency further but visibly degrade motion and distribution quality. They also flag that their motion metrics (AED/APD, based on SMIRK) are sensitive to occlusion/extreme pose, and that FVD can be insensitive to temporal corruption, so quality claims need to be read across multiple metrics together; failure modes are shown in a figure but not detailed in text.

# Near-misses
- 2610.11322 · USDCraft: Geometrically Grounded Programmatic Modeling of Articulated 3D Assets for Simulation · Real NVIDIA affiliation confirmed (one author's work "conducted during an internship at NVIDIA," plus NTU/PKU co-authors), but the paper is categorized cs.RO and its stated purpose is real-to-sim-to-real robot manipulation, not 3D content/game-asset creation — dropped as robotics-unrelated-to-games despite 3D-asset-generation keyword overlap.
- (Google flag on 2610.12727 Zebra3D) · Confirmed false positive — "Google" and the initially flagged "Tencent" both trace to citations of baseline models (VGGT/π³, HunyuanWorld-Mirror) the paper benchmarks against, not to author affiliations. The paper's real industry affiliation is AMD (all authors), kept as a borderline pass — see main entry above.
