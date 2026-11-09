# Part A — Papers
Window: last 30 days (2026-10-10 to 2026-11-09). Categories: cs.GR, cs.CV, cs.LG, cs.AI, cs.RO. Retrieval: API (arxiv_fetch.py; 600 in-window candidates fetched; affiliation screen via local schema adapter, scripts/ untouched). Qualifying papers: 3 (0 flagged).

---
## Video-Coder: Reinforcing Agentic Coding for Video Generation
- **arXiv:** 2611.09894 · https://arxiv.org/abs/2611.09894
- **Submitted:** 2026-11-06
- **Authors:** Chaoyang Wang, Sicheng Gao, Junan Hu, Kunyang Li, Dongyang Chen, Yiyang Zhou, Huaxiu Yao, Yong Jae Lee, Radu Timofte, Yuzhang Shang
- **Qualifying affiliation(s):** Microsoft — Junan Hu (Microsoft Research); other co-authors are University of Central Florida, University of Würzburg, Tsinghua University, UNC-Chapel Hill, UW–Madison
- **Categories:** cs.CV
- **Open release:** code + weights (GitHub: https://github.com/CYWang735/Video-Coder; Hugging Face: https://huggingface.co/Video-Coder)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The authors introduce Video-Coder, a video-generation agent that writes and executes code to construct a dynamic 3D scene ("Draft Video") providing structure and motion signals to downstream video generators, rather than generating pixels directly. It is trained with supervised fine-tuning followed by agentic reinforcement learning combining execution-based and video-based rewards, with an annealing schedule that shifts reliance from the execution reward to the video reward over training.

**Purpose (≤3 sentences):** Current video generators struggle to produce precise spatial structure, coherent motion dynamics, and controllable scene composition. The authors aim to give a video-generation agent an intermediate, code-constructed 3D representation to condition on, instead of relying purely on learned pixel-space dynamics.

**Breakthrough (≤3 sentences):** The authors report Video-Coder improves about 7 points on PhyGenBench and about 24 points on VBench-2.0 compared with MiniMax-H3 (their stated baseline). Gains are smaller when the Draft Video conditions a different downstream generator (OmniWeaving): PhyGenBench rises only from 0.48 to 0.51, by the authors' own account.

**Tools & method (≤3 sentences):** Training data: Video-Coder-SFT-6k and Video-Coder-RL-2k (prompt sources include captions from InternVid, OpenVid-1M, and MiraData); the paper's later sections cite SFT-10k/RL-4k instead, an internal inconsistency in the text. The model (Video-Coder-9B) is trained on 8 NVIDIA H100 GPUs over about 3 days; RL rollouts used MiniMax-H3 deployed on 16 H100 GPUs. Evaluation benchmarks: PhyGenBench and VBench-2.0.

**Limitation (≤3 sentences):** The authors state Video-Coder's Material score (75.02%) trails CogVideoX-1.5 (83.19%) because material appearance and response are not encoded in the white-model Draft Video. The pipeline excludes prompts relying on fine-grained appearance or human facial expressions. The paper has no dedicated limitations section; the dataset-size inconsistency (6k/2k vs. 10k/4k) is noted here as observed, not stated.

---
## Left-Right-Consistent Iterative Stereo Matching via Cross-Injection
- **arXiv:** 2611.09458 · https://arxiv.org/abs/2611.09458
- **Submitted:** 2026-11-06
- **Authors:** Manuel Knott, Diogo Luvizon, Daniel Scharstein, Elias Vansteenkiste
- **Qualifying affiliation(s):** Meta — all four authors listed under Meta Reality Labs
- **Categories:** cs.CV
- **Open release:** code (https://github.com/facebookresearch/stereo_crossinjection); S2M2 checkpoints at https://github.com/junhong-3dv/s2m2 (models used for the Middlebury SOTA numbers are not released, per the paper)
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper proposes cross-injection (CI), a lightweight add-on for iterative refinement-based stereo-matching models that produces mutually consistent left- and right-view disparity maps from a single pass, rather than two independent passes that often disagree. CI feeds the signed left-right inconsistency into every refinement step as an extra input, and can be attached to any pretrained left-only iterative model.

**Purpose (≤3 sentences):** Applications such as per-eye AR/VR rendering, novel view synthesis, and two-view depth fusion need both left and right disparity maps that agree with each other. The common workaround — rerunning the model on the flipped, swapped pair — yields two separate predictions that often conflict, especially on transparent surfaces, textureless regions, and occlusion boundaries.

**Breakthrough (≤3 sentences):** The authors report CI "more than halves" left-right disagreement on the Booster benchmark for FoundationStereo, across five evaluation benchmarks (Middlebury, ETH3D, KITTI-12, KITTI-15, Booster) not seen during training. Applied to two state-of-the-art models, CI also lowers single-view disparity error, per the authors, so it helps even when only left disparity is required.

**Tools & method (≤3 sentences):** FoundationStereo fine-tuning used a subset of the FoundationStereo Dataset, SceneFlow, FallingThings, Virtual KITTI 2, and Sintel (bf16, effective batch 128, 32 H100 GPUs, 50k steps); S2M2 fine-tuning used a similar mix with DrivingStereo instead of Sintel (fp32, effective batch 128 on 32 GPUs, 4,000 optimizer updates). Inference timing is measured on a single A100-SXM4-80GB GPU at 480×640, fp32, batch size 1.

**Limitation (≤3 sentences):** CI assumes a RAFT-style iterative refinement stage and does not apply to single-shot cost-volume regressors, per the authors. They note slower early convergence (the consistency term is unreliable early in training), runtime that grows with iteration count (two passes recomputed each step), and a smearing failure mode on KITTI-15 thin vertical structures that CI "amplifies" relative to standard FoundationStereo; S2M2-L also shows a 0.7-point regression on Booster BP-2.

---
## Dynamic GPU Voxel Grids and Voxel-sequential Processing in NanoVDB
- **arXiv:** 2611.08665 · https://arxiv.org/abs/2611.08665
- **Submitted:** 2026-11-05
- **Authors:** Eftychios Sifakis, Francis Williams, Christopher Horvath, Rohan Sawhney, Mark Harris, Jonathan Swartz, Ken Museth
- **Qualifying affiliation(s):** NVIDIA — Francis Williams, Christopher Horvath, Rohan Sawhney, Mark Harris, Jonathan Swartz, Ken Museth (six of seven authors); Eftychios Sifakis is also affiliated with University of Wisconsin-Madison
- **Categories:** cs.GR (primary), cs.CV, cs.DC
- **Open release:** code (NanoVDB/VoxelBlockManager changes open-sourced in the Academy Software Foundation's OpenVDB repo: https://github.com/AcademySoftwareFoundation/openvdb; reconstruction code in https://github.com/openvdb/fvdb-core)
- **Shipped counterpart:** none found (NanoVDB is used inside NVIDIA Omniverse/OpenVDB tooling, but no dated product release tied to this paper's specific operators was found)

**Summary (≤3 sentences):** The paper extends NanoVDB, NVIDIA's GPU sparse-volume data structure, with dynamic topology operators (morphological dilation, grid merging, pruning, cross-resolution coarsening/refinement) that rebuild grids of hundreds of millions of voxels in milliseconds using bit-parallel algorithms, removing NanoVDB's prior read-only constraint. It also introduces a voxel-sequential access paradigm that streams active voxels as a flat linear sequence so stencil-based GPU operators can approach peak memory bandwidth without tree traversal.

**Purpose (≤3 sentences):** NanoVDB had been effectively read-only once built, limiting its use for workloads that need to dynamically rebuild or restructure sparse volumetric grids (e.g., 3D reconstruction, simulation, voxelization) at interactive rates. The authors aim to make large sparse-volume grids mutable on the GPU without sacrificing the memory-bandwidth efficiency NanoVDB is designed for.

**Breakthrough (≤3 sentences):** On a single 48 GB RTX 6000 Ada GPU, the authors report their mesh-voxelization method reaching about 9.88 billion active voxels at 0.001 voxel size on a 2.8-million-triangle test mesh, compared against OpenVDB's meshToUDF. They report the dynamic topology operators rebuilding grids with hundreds of millions of voxels "in a few milliseconds," and compare 3D-reconstruction results (TSDF/ESDF/occupancy integration on Mai City LiDAR, Replica RGB-D, KITTI Odometry, and 7-Scenes) against nvblox, Open3D, and VDBFusion.

**Tools & method (≤3 sentences):** Fluid-simulation benchmarks use microbenchmarks from a fire simulation (WENO5 narrow-band reinitialization, dilate/prune operators), compared against accessor-based and rebuild-based NanoVDB approaches and OpenVDB's host implementation. Benchmark hardware named in the main text is a single 48 GB RTX 6000 Ada GPU for the scale-ceiling (Table 1) results; the paper references a full hardware configuration in an appendix not covered by this verification pass.

**Limitation (≤3 sentences):** The authors state morphological erosion is not implemented ("we have yet to implement its inverse operator"). They note memory-bound workloads "would struggle to see substantial benefits" from the voxel-sequential approach, that cross-resolution operators are not exercised end-to-end by any of the paper's applications, and that scratchpad bookkeeping allocates roughly 16 MB per candidate root tile, which could hurt performance on very small domains.

# Near-misses
- 2611.09625 · Encoding Memory in World Models with Test-Time Model-Based Reinforcement Learning · screen hit was "DeepMind Control" (a benchmark suite name), not an author affiliation; no qualifying industry co-author found on manual check.
- 2611.09355 · HiMEM: Hippocampus-Inspired Memory Consolidation, Pruning, and Composition for Vision-Language-Action Models in 3D Scenes · screen hits on "Meta" were all instances of "meta-feature"/"meta-semantic" (generic ML terminology), not Meta the company; no qualifying affiliation found.
- 2611.08814 · It Takes Two to Tangram: Multi-Agent Object Centric Reinforcement Learning for Assembly · NVIDIA mention is an acknowledged hardware donation (Academic Grant Program), not an author affiliation; purely academic (TU Darmstadt) paper — does not qualify.
- 2611.08795 · MotionDecipher: LLM-Assisted Clinical Interpretation of Human Motion Signals for Efficient Gait Analysis · screen hits on "Meta" were instances of "Meta Feature Selector"/"Meta Feature Vector" (method components), not Meta the company; no qualifying affiliation found.

Double-verification: all three qualifying papers' abstract pages and HTML author-affiliation blocks were fetched and cross-checked directly (not via sub-agent); dates, affiliations, and all quoted figures/claims were confirmed against the paper text before inclusion.
