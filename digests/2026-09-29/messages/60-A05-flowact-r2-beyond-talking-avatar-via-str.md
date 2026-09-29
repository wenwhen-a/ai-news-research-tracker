**[A05] FlowAct-R2: Beyond Talking Avatar via Streaming Multimodal References and Proactive Agent Planning**
- **arXiv:** 2609.35728 · <https://arxiv.org/abs/2609.35728>
- **Submitted:** 2026-09-28
- **Authors:** Ziyao Huang, Zhengkun Rong, Shiyang Qin, Shuang Liang, Wentao Hu, Yuxuan Luo, Yuan Zhang, Mingyuan Gao
- **Qualifying affiliation(s):** ByteDance Intelligent Creation — all authors
- **Categories:** cs.CV
- **Open release:** demo (Hugging Face Space: <https://huggingface.co/spaces/ProAudience/FlowAct-R2);> project page: <https://bone-11.github.io/Flowact-R2/;> no code repo or weights found
- **Shipped counterpart:** none found

**Summary:** FlowAct-R2 is a streaming talking-avatar system that adapts a video generation backbone (Seedance 2.0 Mini) to accept continuously changing multimodal references (image/audio/video) alongside a "Proactive Interaction Agent" that plans and schedules behavior in real time.
**Purpose:** The authors state that prior talking-avatar systems are "confined to a single scenario" and struggle with dynamically changing image, audio, and video references while preserving identity and temporal continuity.
**Breakthrough:** The authors report gains over Vidu-S1 of "+54.76% for video quality" and "+40.48% for real-time interaction" (GSB scores), with support for real-time 720p generation and hour-scale streaming.
**Tools & method:** The method builds a Streaming Multimodal Reference Diffusion Transformer on the Seedance 2.0 Mini backbone, paired with a two-stage Proactive Interaction Agent (offline planning, online scheduling).
**Limitation:** Not stated explicitly beyond framing prior single-scenario systems as the gap being addressed; no separate limitations section was found in the fetched content.
