## SplashSplat: Reconstructing Splashing Liquids from Real-World Multi-View Videos
- **arXiv:** 2609.20818 · https://arxiv.org/abs/2609.20818
- **Submitted:** 2026-09-17
- **Authors:** Peiyu Liu, Dingxi Zhang, Federico Tombari, Marc Pollefeys, Christina Tsalicoglou, Daniel Barath
- **Qualifying affiliation(s):** Google — Peiyu Liu, Dingxi Zhang, Federico Tombari, Christina Tsalicoglou (Peiyu Liu also lists EPFL; Marc Pollefeys and Daniel Barath list ETH Zurich/EPFL)
- **Categories:** cs.CV, cs.GR
- **Open release:** none yet — the authors' GitHub repo (github.com/Niko-creater/Splashsplat) exists but the paper states the reconstruction code "will be released there"; not yet populated as of this check.
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** The paper presents SplashSplat, a method for reconstructing dynamic, splashing liquids (from coherent streams to violent splashes) from real-world multi-view video, plus a new 20-scene benchmark captured with seven synchronized 4K cameras at 60 fps. It targets a gap the authors identify in prior work, which focuses on smoke or static liquid states rather than dynamic free-surface liquid motion.

**Purpose (≤3 sentences):** Existing reconstruction methods struggle with liquid surfaces because they are weakly textured with view-dependent appearance, form and vanish as thin structures within frames, and have unobservable interior motion. The authors built a dedicated benchmark and method to address dynamic free-surface liquid reconstruction, which they state is unsolved by prior smoke- or static-liquid-focused approaches.

**Breakthrough (≤3 sentences):** The authors report SplashSplat "outperforms state-of-the-art dynamic Gaussian splatting methods on real captures and on a synthetic benchmark, with physically more plausible motion and a lower training cost." On their real benchmark, they report PSNR 20.13 vs. 18.92, LPIPS 0.0806 vs. 0.0898, and a density-deviation physical-plausibility metric of 219.9 vs. 1005.1, compared against a 4D-Scaffold-GS baseline. Training took 37.8 minutes with 5.31 GiB peak memory on a single NVIDIA V100-32GB GPU, the lowest among compared methods per the paper.

**Tools & method (≤3 sentences):** The pipeline fuses multi-view masks into per-frame signed distance fields (SDFs), fits a coarse velocity field between consecutive SDFs via level-set transport, and advects Lagrangian carriers through a forecast-correct-resample loop that decodes them into local Gaussians for differentiable rendering — applying physical structure "only where observations constrain it." Evaluation uses the authors' new SplashSplat benchmark (20 real scenes) and the existing synthetic NeuroFluid benchmark; training hardware was a single NVIDIA V100-32GB GPU.

**Limitation (≤3 sentences):** The authors state the method reconstructs the liquid from silhouettes, so transient structures such as impact bubbles and foam are missed. They also note the fitted velocity field is kinematic — consistent with the observed interface but not enforcing a momentum balance.

## LYRIC: Language-Driven Physics-Based Character Control for Contact-Rich Whole-Body Object Interaction
- **arXiv:** 2609.19688 · https://arxiv.org/abs/2609.19688
- **Submitted:** 2026-09-17
- **Authors:** Zeyu Han, Zichong Meng, Julian Tanke, Minami Matsumoto, Sergey Bashkirov, Yingruo Fan, Selim Engin, Dongseok Shim, Takashi Shibuya, Yuki Mitsufuji, Huaizu Jiang
- **Qualifying affiliation(s):** Sony — Julian Tanke (Sony AI America), Minami Matsumoto and Sergey Bashkirov (Sony Interactive Entertainment), Yingruo Fan and Selim Engin (Sony Corporation of America), Dongseok Shim and Takashi Shibuya (Sony Group Corporation), Yuki Mitsufuji (Sony Corporation of America); other authors (Zeyu Han, Zichong Meng, Huaizu Jiang) list Northeastern University
- **Categories:** cs.RO, cs.GR
- **Open release:** none found
- **Shipped counterpart:** none found

**Summary (≤3 sentences):** LYRIC is a generative flow-matching controller that lets physics-simulated humanoid characters perform contact-rich, whole-body object interactions (manipulation combined with locomotion) from a free-form language instruction and a sparse terminal object goal. It is trained and evaluated on the OMOMO motion-capture dataset (4,890 sequences, 17 subjects, 13 objects).

**Purpose (≤3 sentences):** The authors target combining manipulation with locomotion in physics simulation while handling imperfect motion-capture references and maintaining stable hand-object contact — a combination they say prior physics-based character controllers do not jointly solve.

**Breakthrough (≤3 sentences):** The authors report their tracking policy reaches 64.3% success vs. 53.2% for an InterMimic baseline, that a unified tracker achieves 76.5% success on the full OMOMO dataset, and that their text-conditioned controller reaches 90.3% task success on a held-out split, outperforming kinematic-planner baselines (74.2% success).

**Tools & method (≤3 sentences):** The method uses a three-stage pipeline: Stage I trains a tracking policy with geometry-conditioned grasp rewards adapted to local object thickness and relaxed reference tracking during contact; Stage II trains a factorized controller — a trajectory planner predicting object/root trajectories and an action generator, both via conditional flow matching; Stage III post-tunes the action generator on-policy using the planner's predicted trajectories as intermediate supervision. Training used eight NVIDIA H100 GPUs on the OMOMO dataset.

**Limitation (≤3 sentences):** The paper's provided text does not state explicit limitations; evaluation is confined to the OMOMO dataset and the approach depends on the quality of the underlying motion-capture references (observed, not stated).

# Near-misses
- 2609.20034 · Astronex-World 1.0: Real-Time Interactive World Model Foundation · authors list "Astronex Robotics" and "Nanjing University of Information Science and Technology" — no tracked-company author; NVIDIA appears only as GPU hardware (two NVIDIA L20 GPUs) and as the source of the "NVIDIA PhysicalAI" training dataset, not as an author affiliation, so it does not clear the Part A gate.
