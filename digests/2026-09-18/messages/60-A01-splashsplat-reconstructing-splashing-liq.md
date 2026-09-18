**[A01] SplashSplat: Reconstructing Splashing Liquids from Real-World Multi-View Videos**
- **arXiv:** 2609.20818 · <https://arxiv.org/abs/2609.20818>
- **Submitted:** 2026-09-17
- **Authors:** Peiyu Liu et al.
- **Qualifying affiliation(s):** Google — Peiyu Liu, Dingxi Zhang, Federico Tombari, Christina Tsalicoglou (Peiyu Liu also lists EPFL; Marc Pollefeys and Daniel Barath list ETH Zurich/EPFL)
- **Categories:** cs.CV, cs.GR
- **Open release:** none yet — the authors' GitHub repo (github.com/Niko-creater/Splashsplat) exists but the paper states the reconstruction code "will be released there"; not yet populated as of this check.
- **Shipped counterpart:** none found

**Summary:** The paper presents SplashSplat, a method for reconstructing dynamic, splashing liquids (from coherent streams to violent splashes) from real-world multi-view video, plus a new 20-scene benchmark captured with seven synchronized 4K cameras at 60 fps.
**Purpose:** Existing reconstruction methods struggle with liquid surfaces because they are weakly textured with view-dependent appearance, form and vanish as thin structures within frames, and have unobservable interior motion.
**Breakthrough:** The authors report SplashSplat "outperforms state-of-the-art dynamic Gaussian splatting methods on real captures and on a synthetic benchmark, with physically more plausible motion and a lower training cost." On their real benchmark, they report PSNR 20.13 vs. 18.92, LPIPS 0.0806 vs. 0.0898, and a density-deviation physical-plausibility metric of 219.9 vs. 1005.1, compared against a 4D-Scaffold-GS baseline.
