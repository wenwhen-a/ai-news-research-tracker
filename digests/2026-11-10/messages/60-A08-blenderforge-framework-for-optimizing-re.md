**[A08] BlenderFORGE: Framework for Optimizing Reactive 3D-Graphics Editing Ability of MLLMs**
- **arXiv:** 2611.10768 · <https://arxiv.org/abs/2611.10768>
- **Submitted:** 2026-11-07
- **Authors:** Zilin Guo et al.
- **Qualifying affiliation(s):** SenseTime Research — Yichen Liu, Yuxin Guo, Jingcheng Ni, Lewei Lu, Zehuan Wu (FLAG: borderline — SenseTime is not on the primary company list but is a comparable top-tier industrial AI lab)
- **Categories:** cs.AI
- **Open release:** code, weights, demo — <https://github.com/SenseTime-FVG/BlenderFORGE> (release includes data-generation/training/sandbox/evaluation code, test set, fine-tuned model weights, and a demo.zip of multi-turn conversations; some documentation items noted as "planned")
- **Shipped counterpart:** none found

**Summary:** BlenderFORGE is a training framework for open-weight multimodal LLM agents that edit 3D scenes in Blender by generating Blender Python (bpy) code.
**Purpose:** The authors aim to improve MLLM agents' ability to perform "reactive" 3D-graphics editing in Blender — iteratively adjusting a scene toward a goal rendering — rather than one-shot scene generation.
**Breakthrough:** The authors report a perturbation-based data-generation pipeline plus an isolated Blender sandbox enabling deterministic execution and automatic reward computation, combined with a two-stage SFT-then-RL training recipe.
**Tools & method:** The framework targets Blender's bpy API across four task families (placement, shape-key, lighting, materials), using 3D-FRONT/3D-FUTURE assets (not redistributed), a two-stage supervised fine-tuning + reinforcement learning pipeline, and Qwen3-VL-8B / Qwen3.5-9B backbones with VLM-based judging of edits.
