**[B12] NVIDIA ACE Game Agent SDK (beta) and ACE plugins for Unreal Engine 5**
- **Company:** NVIDIA
- **Status:** GA (UE5 plugins) / Public beta (Game Agent SDK) · **Released:** 2026-06-16 · **New**
- **Surface:** SDK / engine plugin
- **Primary source:** https://developer.nvidia.com/blog/build-on-device-ai-companions-with-the-nvidia-ace-game-agent-sdk-and-unreal-engine-5-plugins/
- **Underlying research:** no traceable paper (the post references NVIDIA's open-source Kimodo motion project without an arXiv id; see Part A open releases)
- **Availability:** NVIDIA states "a new suite of NVIDIA ACE plugins is now available" for UE5 and that developers can "download the NVIDIA ACE Game Agent SDK in beta"; on-device inference.

**What shipped:** An on-device conversational-companion pipeline for games: ASR ("nemo-conformer-ctc-120m"), a "Qwen 3.5 4B model" for function calling, and the "Chatterbox Turbo 350M TTS model," packaged as UE5 plugins and an SDK.
**What research it translates:** NVIDIA's ACE digital-human stack repackaged around small open models for local NPC dialogue; NVIDIA also describes Kimodo as "an open source project for promptable, controllable human motion."
**Practical significance:** UE5 developers can add local, non-cloud voice-interactive companions today, per NVIDIA.
**Engineering details:** Referenced against Unreal Engine 5.7; components are swappable open models; hardware requirements are not stated in the post.
**Limitation / caveats:** The SDK itself is labelled beta; no latency or quality figures are given.
