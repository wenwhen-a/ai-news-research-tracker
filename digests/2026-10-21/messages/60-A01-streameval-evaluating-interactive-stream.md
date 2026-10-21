**[A01] StreamEval: Evaluating Interactive Streaming Video Generation Models**
- **arXiv:** 2610.28402 · <https://arxiv.org/abs/2610.28402>
- **Submitted:** 2026-10-20 (v1)
- **Authors:** Credited collectively on the abstract page as "StreamEval Team"; named in the paper's Contributions section as Jungang Li et al.
- **Qualifying affiliation(s):** NVIDIA — the paper's institutional-logo credit block lists seven affiliations (Tsinghua University, NVIDIA, CMU, UC Berkeley, Princeton, NUS, Reactor); this affiliation is confirmed directly from the primary source (the paper's own affiliation block), not the pre-screen keyword hit, but the HTML rendering does not map any specific named author to NVIDIA individually.
- **Categories:** cs.CV
- **Open release:** leaderboard at <https://streameval.ai>; this is a benchmark paper, no generative model weights are released
- **Shipped counterpart:** none found

**Summary:** As interactive streaming video generation advances, there has been no unified way to evaluate real-time interaction with generated video.
**Purpose:** The benchmark is meant to measure whether streaming video generation models can reliably execute incrementally arriving multimodal requests while preserving state and content, rather than only producing visually convincing frames.
**Breakthrough:** Evaluating 37 models across 300 scripted test cases (15–300s), the authors report that high visual quality and identity retention do not necessarily coincide with reliable request execution or sustained state consistency; the highest task-specific "Following" scores were only 36.90 (among seven avatar-performance models) and 25.93 (text-conditioned world generation), and the highest "Edit Success" score was 15.00 (among three reference-editing models).
