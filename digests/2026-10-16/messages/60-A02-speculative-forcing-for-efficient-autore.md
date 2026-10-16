**[A02] Speculative Forcing for Efficient Autoregressive Video Generation**
- **arXiv:** 2610.22347 · <https://arxiv.org/abs/2610.22347>
- **Submitted:** 2026-10-15 (v1, 17:57:01 UTC)
- **Authors:** Hyunwook Choi et al.
- **Qualifying affiliation(s):** NAVER AI Lab — Dongyoon Han, Sangdoo Yun (Hyunwook Choi did the work during a NAVER AI Lab internship; Seungryong Kim is KAIST AI). **FLAG: borderline** (NAVER AI Lab is not on the default qualified-company list; it is South Korea's largest internet/tech company and runs an established industry AI research lab, included here per the skill's "comparable top-tier lab, flag if unsure" rule). Note: the screening lead expected an NVIDIA co-author — this is **not confirmed**; NVIDIA appears only in the reference list (a cited world-simulation paper) and as the GPU used for benchmarking (one NVIDIA H100), not as an author affiliation.
- **Categories:** cs.CV
- **Open release:** demo/project page only (speculative-forcing.github.io); no code repository found
- **Shipped counterpart:** none found

**Summary:** The paper addresses inefficiency in few-step autoregressive video generators, which run every token through the full denoising schedule even after that token's content has effectively converged.
**Purpose:** Few-step autoregressive video diffusion models are already more efficient than full diffusion, but the paper argues they still waste computation by denoising every token to the same fixed depth regardless of how quickly it has stabilized.
**Breakthrough:** On LongLive (5-second videos) the authors report their learned verifier reaches a VBench-style total score of 83.21 (vs. 83.08 for the 4-step baseline) at 41.74 FPS (vs. 26.40 FPS), using about 1.68 mean denoising steps per token.
