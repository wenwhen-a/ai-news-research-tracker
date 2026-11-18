**[A03] FastFrames: Video Generation at Interactive Latency**
- **arXiv:** 2611.23226 · <https://arxiv.org/abs/2611.23226>
- **Submitted:** 2026-11-17
- **Authors:** Gene Chou, Guandao Yang, Fujun Luan, Lars Mescheder, Wei Dong, Stephan Richter, Vladlen Koltun
- **Qualifying affiliation(s):** Apple — Gene Chou (paper states the work was completed during his internship at Apple); Apple is also listed as institution #1 in the paper's affiliation block, and Vladlen Koltun is an Apple researcher.
- **Categories:** cs.CV
- **Open release:** demo (project page: <https://apple-aiml-research.github.io/ml-fastframes/>); no code/weights link found
- **Shipped counterpart:** none found

**Summary:** FastFrames is a family of fast autoregressive video diffusion models built for interactive-latency generation.
**Purpose:** The goal is to make autoregressive video generation fast enough for fluid, real-time interaction (e.g., a user steering a camera or applying physics inputs while video is generated live), which current models are reported to be far too slow for.
**Breakthrough:** The authors report a 1.3B-parameter variant running at 36 ms/frame (28 responses per second) on a single B200 GPU, matching the quality of a state-of-the-art model nearly 8x slower.
**Tools & method:** The core technique is a latency-profiling-driven redesign of an autoregressive video diffusion pipeline, replacing the VAE decoder and the KV-cache update mechanism with lightweight alternatives rather than treating them as fixed costs.
**Limitation:** The abstract does not state explicit limitations, but the reported 14B configuration still requires an 8-GPU (B200) node to reach its stated frame rate.
