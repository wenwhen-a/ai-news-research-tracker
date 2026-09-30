**[A12] LEGO-Anything: Coding Agents for 3D Scene Reconstruction**
- **arXiv:** 2609.36380 · <https://arxiv.org/abs/2609.36380>
- **Submitted:** 2026-09-28
- **Authors:** Xirui Li et al.
- **Qualifying affiliation(s):** AWS (Amazon) — Peng Shi, Mingwen Dong, Sheng Zhang, Zhuoyan Xu, Dongkyu Lee, Shuaichen Chang, Yi Xiang, Lin Pan, Jiarong Jiang; Xirui Li is at University of Maryland, College Park, with the work done during an AWS internship
- **Categories:** cs.CV
- **Open release:** none (project page only: <https://lego-anything.com>; no explicit code/weights release mentioned in the fetched text, though the Harbor evaluation framework is referenced)
- **Shipped counterpart:** none found

**Summary:** LEGO-Anything reframes single-image 3D scene reconstruction as an "Image-to-Code" problem, where general-purpose coding agents iteratively write, execute, and refine Blender programs that render and are compared against the input image, producing an editable, queryable 3D scene as executable code rather than a fixed 3D output.
**Purpose:** The goal is to move beyond fixed-format 3D reconstruction outputs toward an inspectable, editable scene representation (Blender code) built through iterative agentic refinement guided by visual comparison to the source image.
**Breakthrough:** The authors report their best-performing coding agent, GPT-6-astra, scores 53.4% indoor and 39.6% outdoor on LEGO-Bench, and identify three recurring failure modes: weak scene initialization, regressive edits during iteration, and unreliable self-evaluation.
**Tools & method:** The benchmark uses the LychSim simulator with Fab assets (443 registered assets across 8 environments), evaluated through the Harbor Framework with Blender 5.0.1 and Blender-MCP, testing GPT-6 (astra/sol/luna) and GPT-5.6 model families via a Codex-style coding-agent harness.
