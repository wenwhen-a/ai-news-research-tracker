# Part A — Papers
Window: last 30 days (2026-08-26 to 2026-09-25). Categories: cs.GR, cs.CV, cs.LG, cs.AI, cs.RO. Retrieval: website fallback (arxiv.org/search; arXiv API returned HTTP 406 for all queries). Qualifying papers: 5 (0 flagged).

---
## OREO: Fidelity Alignment in 3D Generation via On-the-fly Rendering-Editing Optimization
- **arXiv:** 2609.29788 · https://arxiv.org/abs/2609.29788
- **Submitted:** 2026-09-24
- **Authors:** Zhiyuan Ma, Wenbo Hu, Wang Zhao, Pengfei Wang, Ying Shan, Lei Zhang
- **Qualifying affiliation(s):** Tencent — Wenbo Hu, Wang Zhao, Ying Shan listed at Tencent ARC Lab (Zhiyuan Ma is dual-affiliated with Tencent ARC Lab and The Hong Kong Polytechnic University)
- **Categories:** cs.CV, cs.GR
- **Open release:** none stated
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** OREO targets the gap between generated 3D assets and real-world visual fidelity, noting that generated assets "often lack intricate textures and fine-grained details observed in real-world subjects" because 3D training data is far scarcer than 2D imagery. It introduces a render-edit-optimize loop that distills 2D-diffusion-refined renderings back into the 3D generator. The work was accepted to ECCV 2026.

**Purpose (≤3 sentences):** The authors aim to close the fidelity gap without needing more 3D training data, by using a 2D image editor to improve rendered views of a 3D asset and feeding those improvements back into the generator itself.

**Breakthrough (≤3 sentences):** On a 2,396-image Conceptual Design Dataset the authors report OREO reaches 0.7834 CLIP similarity and 0.8065 DINO similarity versus a Trellis baseline's 0.7613 and 0.7916; on Google Scanned Objects the gap narrows (0.7764 vs 0.7722 CLIP). In a 20-participant, 100-example user study, OREO received the highest aggregate preference share at 38%.

**Tools & method (≤3 sentences):** "Reinforced Editing" uses inversion-free image editing that couples source/target flow trajectories to enhance a rendered view while preserving its spatial layout, and a contrastive distillation loss (`L_contrast = ||z⁰-z0+||² - ||z⁰-z0-||²`) treats the edited render as a positive target and the original as negative. Training used batch size 8 across 8 GPUs at 1024×1024 resolution with the Adan optimizer (lr 10⁻⁴); each optimization iteration costs about 2s for the generator update plus roughly 4s for the 9-step editing pass (81% of total time).

**Limitation (≤3 sentences):** The authors report viewpoint drift on face-like objects, where "the 2D editor may rotate the face toward the camera instead of preserving the intended 3D-facing direction," and style shifts inherited from the editor's bias on materials outside its photorealistic training distribution. Occluded surfaces, thin appendages, and sharp material boundaries receive weak supervision, and the method depends on conditional flow-based latent generators, so "improvements may be less consistent" for architectures that decouple geometry from appearance.

---
## From Scattered Gaussians to Structured Maps: Efficient Gaussian Splatting Coding via Dual-phase Morton Sorting
- **arXiv:** 2609.29041 · https://arxiv.org/abs/2609.29041
- **Submitted:** 2026-09-24
- **Authors:** Bolin Chen, Shanzhi Yin, Ru-Ling Liao, Yibo Fan, Yan Ye
- **Qualifying affiliation(s):** Alibaba — Bolin Chen (also Fudan University/Hupan Lab), Ru-Ling Liao and Yan Ye listed at DAMO Academy, Alibaba Group
- **Categories:** cs.MM
- **Open release:** none stated
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper addresses the storage and bandwidth cost of 3D Gaussian Splatting (3DGS), whose unstructured millions-of-primitives representation resists standard video-codec compression. It proposes converting the irregular Gaussian layout into a structured 2D map so block-based codecs like HEVC/VVC can compress it efficiently.

**Purpose (≤3 sentences):** Prior orderings such as PLAS and plain Morton sorting either cost too much to compute or fail to preserve enough spatial coherence once splats are reshaped into a 2D grid; the authors aim for an ordering that is both fast and coherent enough for codec-friendly compression.

**Breakthrough (≤3 sentences):** The authors report BD-rate gains of 1.29% (RGB-PSNR), 1.69% (YUV-PSNR) and 3.19% (YUV-SSIM) over a plain-Morton baseline, and 1.15%/0.88%/0.45% over PLAS on the same three metrics. Their sorting step runs in 144.63 ms on average versus PLAS's 18,698.91 ms, while plain Morton sorting alone runs in 24.51 ms.

**Tools & method (≤3 sentences):** The method applies Morton-code (Z-order) sorting to each Gaussian's 3D mean position first, then re-maps that 1D-sorted sequence onto a 2D grid using 2D Morton indexing rather than row-major reshaping, so neighboring 1D indices land on spatially neighboring pixels; the same permutation is applied consistently across position, scale, rotation, opacity, and spherical-harmonics attributes. Experiments used MPEG common test sequences (1F static and NF dynamic scenes) on an NVIDIA Tesla V100 SXM2 32GB with an Intel Xeon Platinum 8163 CPU, inside the GSCodec Studio pipeline with HM 18.0 (HEVC reference software).

**Limitation (≤3 sentences):** The authors note the gains are scene-dependent: "some challenging content, such as gymnast and flowerdance, exhibits noticeable BD-rate losses, likely due to complex motion and highly non-uniform appearance distributions," and state the method's benefit "can vary depending on scene characteristics" rather than being uniform across content types.

---
## OmniFabric: Coherent UV Space Texture Synthesis for 3D Garment Reconstruction
- **arXiv:** 2609.30234 · https://arxiv.org/abs/2609.30234
- **Submitted:** 2026-09-24
- **Authors:** Ding-Jiun Huang, Yuanhao Wang, Cheng Zhang, Hugo Bertiche, Alexandru-Eugen Ichim, Thabo Beeler, Fernando De la Torre
- **Qualifying affiliation(s):** Google — Hugo Bertiche, Alexandru-Eugen Ichim, Thabo Beeler listed at Google (other authors at CMU, University of Washington, Texas A&M)
- **Categories:** cs.CV
- **Open release:** none stated
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** OmniFabric targets automated creation of production-ready 3D garment textures from a single reference image, a task where existing methods "bake environmental illumination and shadows directly into the texture map" or lose global coherence, making the result unsuitable for physical simulation or relighting. The paper was accepted to SIGGRAPH Asia 2026.

**Purpose (≤3 sentences):** The authors aim to produce clean, normalized, sewing-pattern-space texture maps — free of baked lighting — that can be reused across simulation and relighting pipelines, rather than a single fixed-lighting render.

**Breakthrough (≤3 sentences):** On their synthetic test set the authors report LPIPS of 0.092 versus 0.223–0.311 for FabricDiffusion, Paint3D, and Hunyuan3D-2.0, and CLIP-score 0.963 versus 0.890–0.924 for those baselines. In a user study, OmniFabric was ranked 1.09 for overall quality (lower is better, versus 2.10–3.41 for competitors) and scored 4.44/5 on fidelity versus 1.75–3.43.

**Tools & method (≤3 sentences):** A first stage uses Gemini 3 Pro to repose the input garment into a canonical A-pose and Veo 3 to synthesize a 360° rotation, from which four orthogonal views are projected onto unwrapped sewing patterns to build a coarse but globally coherent texture; a second stage trains a LoRA-fine-tuned Diffusion Transformer, conditioned on the coarse texture, a frontal rendering, and a 3D position map, to remove baked shadows and distortions. Training used a single NVIDIA A6000 GPU at 1024×1024 resolution on 30,000 textured sewing patterns derived from 3,000 garments in GarmentCodeData; inference takes roughly 5 minutes per sample, dependent on Gemini server load.

**Limitation (≤3 sentences):** The authors state the method "does not yet explicitly disentangle albedo from shading in a strictly principled, physics-based manner," and that highly reflective or metallic fabrics with strong view-dependent effects remain challenging. Geometric errors from the upstream sewing-pattern prediction cannot be corrected at the texturing stage, and the pipeline relies on closed-source generative models (Gemini/Veo), though the authors note open-source alternatives showed comparable performance in their tests.

---
## Heartian: Physiology-Aware Relightable Gaussian Head Avatar
- **arXiv:** 2609.28539 · https://arxiv.org/abs/2609.28539
- **Submitted:** 2026-09-22
- **Authors:** Xiaoyue Fan, Jose Echevarria, Akshay Paruchuri, Kaan Akşit
- **Qualifying affiliation(s):** Adobe — Jose Echevarria listed at Adobe Research (other authors at UCL and Stanford)
- **Categories:** cs.CV, cs.GR
- **Open release:** none stated
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** Heartian addresses the fact that conventional Gaussian head avatars treat facial appearance as temporally static, ignoring the subtle cardiac-induced skin-color changes (remote photoplethysmography, or rPPG) that a real face exhibits. It builds a relightable Gaussian head avatar, based on HRAvatar, that embeds a recoverable heart-rate signal into per-frame skin-Gaussian albedo.

**Purpose (≤3 sentences):** The goal is to make head avatars physiologically plausible — carrying a detectable, non-contact-measurable heartbeat signal — without degrading the avatar's visual reconstruction quality.

**Breakthrough (≤3 sentences):** The authors report a pooled heart-rate mean absolute error of 0.29 bpm (0.38% MAPE) when reading the signal directly off the avatar's attributes, and 0.97 bpm MAE (1.21% MAPE) when recovering it from rendered video using a motion-augmented TS-CAN model on the MMPD dataset. They report this comes at a cost of only 0.005 dB average PSNR degradation and negligible SSIM/LPIPS change versus the non-physiological baseline reconstruction.

**Tools & method (≤3 sentences):** After training a baseline Gaussian head reconstruction, a second stage optimizes a per-frame albedo modulation on skin-region Gaussians only, combining a two-Gaussian fundamental waveform (capturing systolic/diastolic peaks in cardiac phase) with a lightweight MLP spatial residual conditioned on cardiac phase, beat identity, and position. Evaluation used 152 stationary recordings across UBFC-rPPG (10 subjects), PURE (10 subjects), and MMPD (33 subjects, four lighting conditions), trained on an NVIDIA RTX 4060 in PyTorch for 60 epochs in the second stage.

**Limitation (≤3 sentences):** The authors note sensitivity to large initial ground-truth PPG spikes during capture, which introduce visual artifacts, and reduced effectiveness for skin tones with lower green-channel reflectance or under warm/high-intensity LED lighting, since the method modulates the green channel directly. They also flag frame-level Gaussian jitter that hurts rPPG recovery on some datasets (notably PURE), theoretical phase-drift accumulation across frames, and that the method is an offline, per-recording process rather than real-time.

---
## M-plicits: Neural Implicit Surfaces via Nested Multiscale Residuals
- **arXiv:** 2609.28684 · https://arxiv.org/abs/2609.28684
- **Submitted:** 2026-09-23
- **Authors:** Vinícius da Silva, Isabelle Melo, Matheus Bessa, Guilherme Schardong, Luiz Schirmer, André Araújo, Nuno Gonçalves, Hélio Lopes, Alberto Raposo, Luiz Velho, Tiago Novello
- **Qualifying affiliation(s):** Google — Matheus Bessa and André Araújo listed at Google DeepMind (other authors at PUC-Rio, IMPA, University of Coimbra, Universidade Federal de Santa Maria)
- **Categories:** cs.CV, cs.GR, cs.LG
- **Open release:** none stated
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper targets a tradeoff in neural implicit surface representations for 3D reconstruction from point clouds: single-MLP methods are accurate but slow at inference, while grid-based methods are fast but can overfit noise and limit surface smoothness. M-plicits models the signed distance function as a sum of progressively finer residual SIREN networks trained on narrowing neighborhoods of the surface.

**Purpose (≤3 sentences):** The authors aim for a representation that keeps single-MLP-style smoothness and noise robustness while approaching grid-based methods' rendering and mesh-extraction speed, without the large parameter counts of grid representations.

**Breakthrough (≤3 sentences):** On the Stanford and Thingi32 benchmarks, their fine configuration reports the best median Chamfer Distance (1.87E-05) and best IoU (0.867) at 246,627 parameters, versus a coarse configuration's 17,153 parameters; real-time rendering reaches 180 FPS (coarse) and 35–43 FPS (fine) at 512² resolution, with up to 5× faster mesh extraction than a SIREN baseline. Under 1% vertex-noise perturbation, their fine model's mean Chamfer Distance (3.36E-05) stays far below Instant-NGP's (2.80E-04) and BACON's (1.68E-03).

**Tools & method (≤3 sentences):** The SDF is expressed as a base network plus successively finer residuals (f₃ = f₁ + r₁ + r₂) at increasing SIREN frequencies (ω₀ = 30/45/100), where each residual is trained only within a narrow, adaptively sized band around the previous level's zero-set — "each residual mᵢ is supervised only within this δᵢ-neighborhood" — rather than over the full domain. Inference uses multiscale sphere tracing (coarse levels first, fine levels near the surface), adaptive marching cubes, and GEMM-based analytical normal computation instead of autodifferentiation; experiments ran on an NVIDIA RTX 5090 (32GB) over the Stanford (Armadillo, Dragon, Lucy, Thai Statue) and Thingi32 (200 of 10,000 models) datasets.

**Limitation (≤3 sentences):** The authors state the smoothness prior "prevents very sharp edges," trading the highest-frequency micro-detail for faithful global geometry, and that the adaptive band-width formula (a max over neighborhood errors) "is sensitive to isolated outlier points," for which they suggest quantile-based alternatives as future work. Blob artifacts appear on some Thingi32 shapes with disconnected components or non-watertight surfaces that violate the method's SDF assumptions.

# Near-misses
- 2609.29092 · DAWN: Noise-Robust Quadruped Parkour via Depth-Denoising World Models · purely academic — all five authors affiliated with Korea University of Technology and Education; the "Intel" screen match did not correspond to any author affiliation.
- 2609.29171 · Representation World Model: Learning States, Transition and Executable Plans in Representation · affiliation unverifiable — no HTML version exists (404); the abstract page lists ten authors with no affiliations, and per policy no PDF fallback was used.
- 2609.28654 · Training Object Permanence in World Models · no qualifying affiliation — all 34 authors are university-affiliated (CMU, Johns Hopkins, UCSD/UCLA/Berkeley, Columbia, Stanford, and others); "Amazon" appears only in the acknowledgements as AWS Trainium compute-credit support, not as an author affiliation.
- 2609.29644 · Markerless Multi-Modal Autonomous Robotic Inspection of Large Space Structures · off-topic — NeRF-based 3D reconstruction applied to orbital/space-structure inspection, not a game, 3D-asset, character-animation, or engine application; the "borderline" company screen match was not pursued given the topic mismatch.
- 2609.29983 · From Interests to Semantic IDs: Retrieval-Grounded Credit Assignment for Generative Recommendation · off-topic — a generative recommender-systems paper (explicitly an excluded topic), evaluated on Amazon Reviews e-commerce data, unrelated to games/3D/animation/engines.
- 2609.29669 · Do World Models Make Better Robots? A Survey of Evaluation Benchmarks for Predictive Embodied Intelligence · off-topic / affiliation disclaimed — Vinija Jain (Meta) and Aman Chadha (Apple) are listed, but the paper states the authors "contributed to this work independently of their roles and employment," and its topic (general VLA-vs-world-model robot benchmarking) is not games/3D/character-animation/engine-specific.
- 2606.03159 · NVIDIA OmniDreams: Real-Time Generative World Model for Closed-Loop Autonomous Vehicle Simulation · out of window — v1 was submitted 2026-06-02, well before the 2026-08-26 cutoff; only a September revision (v3) surfaced it in the site-scan's recent-activity listing.

Verification: each of the five qualifying papers' arXiv abstract page (v1 submission date, title, authors, categories, no withdrawal notice) and HTML page (author affiliation block, confirming the qualifying company) were fetched and cross-checked directly against the primary source; a second read of each HTML page's method/results/limitations sections was done to populate the five objective blocks above. This is the double-verification pass for today's run.
