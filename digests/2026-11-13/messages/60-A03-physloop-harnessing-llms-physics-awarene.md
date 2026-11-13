**[A03] PhysLoop: Harnessing LLMs' Physics Awareness for Self-Improving Video Generation Models**
- **arXiv:** 2611.16748 · <https://arxiv.org/abs/2611.16748>
- **Submitted:** 2026-11-12
- **Authors:** Yuxuan Chen et al.
- **Qualifying affiliation(s):** ByteDance Seed (listed among the paper's affiliations; exact per-author mapping not recoverable from the HTML, affiliation fields were blank — other listed affiliations: Peking University, UC Santa Barbara, MIT, Universität Hamburg, Hangzhou Normal University)
- **Categories:** cs.CV (primary), cs.AI
- **Open release:** code + dataset — github.com/DAGroup-PKU/PhysLoop; authors say they release the 100K-video PhysLoop-100K set, PhysLoop-Gen/PhysLoop-Repair eval sets, and "generation tools" (no model weights mentioned)
- **Shipped counterpart:** none found (uses third-party models Seedance 2.5, GPT-6 Astra, Claude Opus 5 as components, not claimed as a new shipped product)

**Summary:** PhysLoop is a harness in which an LLM agent writes a physics task/scene program that Unreal Engine (with Taichi/Genesis support) simulates, a verifier checks the simulated result, and a video model (Seedance 2.5 by default) renders appearance on top — building a training/repair pipeline for physically-grounded video generation.
**Purpose:** Video generation models often produce visually realistic but physically implausible motion.
**Breakthrough:** The authors report 85% task success on PhysLoop-Gen (100 generation tasks) versus 73% for standalone Seedance 2.5, and 86% success on PhysLoop-Repair (50 repair tasks) versus 19.33% for the best standalone baseline.
**Tools & method:** Simulation ran on a Mac mini (Apple M4, 10-core, 16 GB) with Unreal Engine 5.7, producing 1080p/24fps output after appearance refinement; combined generation time is estimated at 7–12 minutes per task.
