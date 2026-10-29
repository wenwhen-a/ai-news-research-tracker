**[B01] NVIDIA ACE — Nemotron 3.5 Bolt E4B (4GB) via the In-Game Inferencing (IGI) SDK**
- **Company:** NVIDIA
- **Status:** GA · **Released:** 2026-10-27 · **New**
- **Surface:** on-device AI model + SDK (ACE / In-Game Inferencing SDK) for AI game characters
- **Primary source:** <https://developer.nvidia.com/blog/nvidia-rtx-spark-powers-neural-rendering-and-ai-characters-in-games/>
- **Underlying research:** arXiv 2610.33039, "Nemotron 3.5 Bolt 74B-A9B 24GB: A Hybrid Vision-Language Model for Local AI" — same Nemotron 3.5 Bolt model family; the paper documents the 74B-A9B 24GB variant, not the shipped E4B 4GB variant specifically
- **Availability:** Free download via the IGI SDK; runs locally on GeForce RTX and RTX Spark; no waitlist stated

**What shipped:** NVIDIA states Nemotron 3.5 Bolt E4B 4GB "is now available" to developers via the In-Game Inferencing (IGI) SDK, a small on-device LLM described as "purpose-built to power richer, faster in-game character interactions" that runs locally on GeForce RTX and RTX Spark hardware.
**What research it translates:** The Nemotron 3.5 Bolt family (arXiv 2610.33039) is a hybrid Mamba-Transformer vision-language model derived from Nemotron 3.5 Super VL 120B-A12B, using "Star Elastic compression with 2-bit Quantization-Aware Distillation" to fit memory-constrained local deployment; the shipped E4B 4GB variant is a smaller sibling of the exact size the paper benchmarks.
**Practical significance:** NVIDIA states the model offers "~40% higher average quality against our prior model on relevant benchmarks," with multi-turn tool use, configurable reasoning, a 64k context window, and support for 35 languages — letting developers run NPC dialogue/reasoning on-device instead of via a cloud round-trip.
