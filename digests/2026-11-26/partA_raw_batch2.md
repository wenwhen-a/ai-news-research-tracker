## LiveRelight: Sub-Second Global Illumination Editing for Gaussian Interiors
- **arXiv:** 2611.34226 · https://arxiv.org/abs/2611.34226
- **Submitted:** 2026-11-25 (v1)
- **Authors:** Noah Rothenberger, Dor Verbin, Serge Belongie, Bernhard Kerbl
- **Qualifying affiliation(s):** Google DeepMind — Dor Verbin (other authors: University of Copenhagen)
- **Categories:** cs.CV
- **Open release:** none found
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** LiveRelight is a hybrid relighting method for 3D-Gaussian-splatting reconstructions of indoor scenes that supports sub-second edits to direct and indirect illumination, including changes to emission and surface reflectance, without re-running per-edit optimization. It precomputes geometric light exchange once, then evaluates direct illumination on 2D Gaussians while propagating diffuse interreflection via sparse radiosity on a triangle-mesh proxy, transferring the result back onto the reconstruction. The authors report about 5 dB higher PSNR than prior path-traced editing baselines across eight synthetic relighting conditions, with editing latency cut by up to three orders of magnitude.
**Purpose (≤3 sentences):** The paper targets interactive, physically based relighting of Gaussian-splatting reconstructions of interiors, a setting where existing path-traced or neural relighting pipelines require costly recomputation for every lighting edit. It aims to let users change lights and materials and see global illumination update in well under a second.
**Breakthrough (≤3 sentences):** The authors state their key insight is to precompute geometric light exchange rather than precomputed illumination responses, decoupling the expensive light-transport geometry from the editable emission/reflectance parameters. They report this yields roughly 5 dB higher PSNR than prior path-traced editing approaches and up to a 1000x reduction in editing latency across eight synthetic test scenes.
**Tools & method (≤3 sentences):** The method combines a 2D Gaussian splatting representation for direct illumination with a sparse radiosity solve on an extracted triangle-mesh proxy for diffuse interreflection, transferring results back onto the Gaussian reconstruction. Evaluation uses eight synthetic relighting scenarios compared against path-traced references; no additional hardware/dataset details were available from the fetched pages.
**Limitation (≤3 sentences):** (observed, not stated) The reported evaluation covers only eight synthetic scenes, so real-world capture performance is not directly demonstrated; the radiosity approximation targets diffuse interreflection, suggesting more complex glossy/specular indirect transport may not be fully captured. No explicit limitations section was found in the material retrieved.

---

## DeltaRAE: Derivative Tokenization for Long Video Generation
- **arXiv:** 2611.33886 · https://arxiv.org/abs/2611.33886
- **Submitted:** 2026-11-25 (v1)
- **Authors:** Mingzhuo Yu, Shengcao Cao, Chengzhi Mao, Yong Cheng, Di Jiang, Lijun Yu
- **Qualifying affiliation(s):** Google — Mingzhuo Yu, Di Jiang; Google DeepMind — Shengcao Cao, Yong Cheng, Lijun Yu (Chengzhi Mao: Rutgers University)
- **Categories:** cs.CV
- **Open release:** none found
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** DeltaRAE is a causal video "representation autoencoder" that fully encodes periodic anchor frames and represents all other frames with only a handful of tokens each via derivative ("delta") tokenization, leaning on a frozen pretrained image encoder. The authors report it is competitive with state-of-the-art video tokenizers on UCF-101 and Kinetics-600, roughly halves tokenizer GFLOPs on 16-frame clips, and represents one minute of video with 18.8x fewer tokens than baselines.
**Purpose (≤3 sentences):** The paper addresses the token-efficiency bottleneck in generating long videos, since standard tokenizers spend tokens on every frame and make minute-long generation computationally expensive. DeltaRAE aims to compress redundant temporal information so a diffusion transformer can generate much longer videos within a fixed token/compute budget.
**Breakthrough (≤3 sentences):** The authors report that a diffusion transformer trained end-to-end on DeltaRAE's latents can generate a full minute of coherent video, which they attribute to the derivative tokenization built on a frozen pretrained image encoder. They note this as evidence the approach enables long-horizon generation beyond what comparable token budgets otherwise allow.
**Tools & method (≤3 sentences):** The method periodically encodes full "anchor" frames and compact delta tokens for intermediate frames, using a frozen pretrained image encoder; it is evaluated on the UCF-101 and Kinetics-600 video benchmarks and trained end-to-end on one-minute video clips.
**Limitation (≤3 sentences):** The authors report a specific failure mode: without the pretrained image encoder, a generator trained at the same token budget collapses (loses coherence) within about 15 seconds in most test videos, indicating the method's long-horizon gains depend on that frozen-encoder component.

---

## VivaWorld: Long-Horizon Video World Model With Compositional 3D Priors
- **arXiv:** 2611.33591 · https://arxiv.org/abs/2611.33591
- **Submitted:** 2026-11-25 (v1)
- **Authors:** Ying Jiang, Donglai Xiang, Anita Hu, Masha Shugrina
- **Qualifying affiliation(s):** NVIDIA — all authors
- **Categories:** cs.CV
- **Open release:** demo (project page: https://research.nvidia.com/labs/sil/projects/vivaworld/); no code/weights found
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** VivaWorld generates long, geometry- and view-consistent videos from a single input image with accurate camera control, aimed at long-horizon world exploration. It combines reconstructed point clouds (preserving the observed scene) with generated textured meshes that complete object geometry over full 360° views, then conditions a video generation model on this compositional 3D representation through a control adapter.
**Purpose (≤3 sentences):** The paper targets long-horizon, controllable scene exploration and novel-view synthesis from a single image, a setting where pure video generation models tend to drift in geometry and camera pose over long rollouts. The stated goal is to support controllable novel-view synthesis, long-horizon scene exploration, and "physical AI" applications.
**Breakthrough (≤3 sentences):** The authors report state-of-the-art visual quality and camera-control accuracy versus prior methods, which they attribute to removing disconnected floating geometry fragments and to a hybrid camera embedding that blends scene-level and object-anchored ray encodings to keep generated video grounded in the compositional 3D scene.
**Tools & method (≤3 sentences):** The pipeline reconstructs point clouds from the input image, generates textured meshes to complete occluded/unseen object geometry across 360°, and feeds a hybrid (scene- plus object-anchored) camera-ray embedding into a video diffusion model via a control adapter; a project page with demo material is hosted at research.nvidia.com.
**Limitation (≤3 sentences):** (observed, not stated) The fetched abstract states no explicit quantitative limitations or failure cases. Because the approach depends on mesh-completion and point-cloud reconstruction quality, behavior under heavy occlusion or sparse initial observation is not characterized in the material retrieved.

---

## DreamTour: Layout Steering for Training-Free World Exploration
- **arXiv:** 2611.33378 · https://arxiv.org/abs/2611.33378
- **Submitted:** 2026-11-24 (v1)
- **Authors:** Srikumar Sastry, Meher Gitika Karumuri, Chenqi Li, Sarosij Bose, Mellon Zhang, Allen Tu, Ziyang Long, Yen-Liang Lin, Alexander Schwing, Nathan Jacobs
- **Qualifying affiliation(s):** Amazon — Srikumar Sastry, Allen Tu (paper states the work was completed during an internship at Amazon)
- **Categories:** cs.CV
- **Open release:** none found
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** DreamTour is a training-free method that turns a single image into a long, camera-controllable video "tour" of the implied 3D scene. It first uses an image inpainting model to outpaint the scene beyond the original frame, renders that extended scene along the desired camera path to build spatial guidance, then steers video-diffusion latents toward that guidance with a "Layout Steering" step using decaying low-frequency corrections.
**Purpose (≤3 sentences):** The paper targets precise camera-motion control for single-image-to-video "world exploration," a setting where existing video generators often drift off the intended camera path or lose scene consistency. It pursues this without any additional model training.
**Breakthrough (≤3 sentences):** The authors report improved directional accuracy and travel-distance calibration on VBench, and stronger camera control plus scene consistency on WorldScore, while keeping video quality competitive with prior methods — achieved training-free rather than through additional fine-tuning.
**Tools & method (≤3 sentences):** The method chains an image inpainting/outpainting model with camera-path rendering to build spatial guidance, applies "Layout Steering" (decaying low-frequency latent corrections) to align video-diffusion latents to that guidance, and for longer tours generates video in chained segments that re-derive guidance from the previous segment's last frame. It is evaluated on the VBench and WorldScore benchmarks.
**Limitation (≤3 sentences):** (observed, not stated) The retrieved abstract states no explicit limitations. As a training-free, inpainting-dependent pipeline, output plausibly depends on the inpainting model's ability to plausibly extend unseen regions of the scene, though this is not directly discussed in the fetched material.

# Near-misses
- 2611.34261 · TORE: Token-Wise Taylor Order Selection via Decomposed Residual Error Estimation for Diffusion Acceleration · affiliation unverifiable, no HTML version (arxiv.org/html/2611.34261 returned 404; "Google" regex hit not confirmable from abs page, likely a Google Scholar link)
- 2611.33761 · ScanAR: Parallel Row-Scan Decoding for Efficient Image Generation in Unified Autoregressive Models · off-topic (general efficiency method for autoregressive image generation decoding, benchmarked on ImageNet/GenEval, not specifically 3D/world-model/character/game); real affiliation is Xiaomi Robotics (borderline), not Google — the "Google" regex hit was not found in the author block
- 2611.33734 · (title on page: "DualCast: Dual-Image Conditioned Diffusion Transformers for Digital Human E-Commerce Video Generation"; the page's actual abstract describes an unrelated system, "GameWeaver," for game camera-trajectory/video generation — an arXiv metadata mismatch) · no qualifying industry co-author, purely academic (all authors affiliated with Zhejiang University); "Google" regex hit not found in affiliation block
- 2611.33650 · Linear-Time Online Visual Geometry Transformer with Hybrid Architecture (LinearVGGT) · no qualifying industry co-author, purely academic (all authors affiliated with UNITES Lab, University of North Carolina at Chapel Hill); "Google" regex hit not found in affiliation block
- 2611.33407 · An Adversarial Multi-Agent Pursuit Game for Locomotor Agility Pretraining · no qualifying industry co-author, purely academic (all authors affiliated with Loyola University Chicago); "Kuaishou" regex hit not found in affiliation or acknowledgments block

Verification pass: each of the above papers was re-checked against its arXiv abstract page (title, authors, v1 date, categories) and, where an HTML version existed, the author affiliation block near the top of the HTML paper (not the abs-page regex snippet). Passing papers were confirmed to have at least one author affiliation reading as a qualified-company employee in the actual paper text, and to be genuinely on-topic (3D / world models / character animation / game engines) from the abstract content, not keyword overlap alone.
