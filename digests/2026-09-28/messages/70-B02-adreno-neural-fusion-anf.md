**[B02] Adreno Neural Fusion (ANF)**
- **Company:** Qualcomm
- **Status:** GA · **Released:** 2026-09-22 (expanded at Snapdragon Summit; SDK public on GitHub) · **New**
- **Surface:** GPU rendering SDK — native Vulkan integration, Unreal Engine 5 plugin, Unity 6.6+ support
- **Primary source:** <https://www.qualcomm.com/developer/blog/2026/09/introducing-adreno-neural-fusion-sdk-for-snapdragon-mobile-platforms>
- **Underlying research:** no traceable paper (Qualcomm cites no arXiv paper or research post for ANF's specific method)
- **Availability:** Requires Snapdragon 8 Elite Gen 6 / Extreme Gen 6 silicon (new "Adreno matrix core" hardware); first commercial phones (e.g. Xiaomi 18 Pro Max) shipped 2026-09-23. SDK, docs and samples are public on GitHub with no developer waitlist. Qualcomm names 20+ partner titles (Diablo Immortal, Honkai: Star Rail, Monster Hunter Outlanders, Naraka: Bladepoint Mobile, War Thunder Mobile, and others).

**What shipped:** Qualcomm shipped Adreno Neural Fusion (ANF), an AI rendering pipeline unifying neural super resolution and frame generation, running on new "Adreno matrix core" AI-dedicated GPU cores paired with 18MB of on-chip memory.
**What research it translates:** ANF applies temporal-accumulation upscaling and frame-interpolation techniques — sub-pixel camera jitter, motion-vector-guided reprojection, depth-based disocclusion handling — conceptually similar to NVIDIA DLSS, AMD FSR and Intel XeSS, run through Qualcomm's own trained models.
**Practical significance:** Qualcomm states ANF lets titles "render at half resolution and generate half as many real frames but deliver full-resolution output at double the submitted frame rate." Because it ships as plugins for both Unreal Engine 5 and Unity 6.6+, Qualcomm says studios can adopt it "without custom implementations." Adoption depends on new Gen 6 silicon reaching consumers, which only began 2026-09-23.
