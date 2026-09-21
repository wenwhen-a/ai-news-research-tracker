**[B10] ABot-World (ABot-World-0 / ABot-3DWorld-0)**
- **Company:** Alibaba — AMAP/高德 CV Lab, a Gaode/Amap subsidiary team within Alibaba Group **(FLAG: borderline company attribution — subsidiary, a step removed from the "Alibaba" parent brand)**
- **Status:** Public preview (open test portal; gallery browsable without login, creating a new world requires login) · **Released:** 2026-07-16 · **New**
- **Surface:** Web app/interactive demo platform (test portal) + partially open weights/code
- **Primary source:** <https://finance.yahoo.com/technology/ai/articles/alibabas-amap-unveils-abot-world-072100723.html> (syndicated official release text); test portal at <https://abot-world.amap.com>
- **Underlying research:** "ABot-World-0: Infinite Interactive World Rollout on a Single Desktop GPU" (arXiv/HF 2607.19191); "ABot-3DWorld-0: A Universal World Model to Explore Any 3D Space" (arXiv 2607.11673)
- **Availability:** Free test portal at abot-world.amap.com with a public "World Plaza" gallery of 120+ pre-made worlds browsable without login; creating a new world requires logging in. Partial weights/code mirrored on GitHub/Hugging Face; designed to run on a single desktop-class GPU.

**What shipped:** Amap (Alibaba's mapping subsidiary) shipped a public test portal for two interactive world-generation models — ABot-World-0 (video-based interactive worlds) and ABot-3DWorld-0 (3D-Gaussian-Splatting-based persistent spaces) — where visitors upload a reference image and generate an explorable "world" in real time, with rendering latency under 1.5 seconds per the product page.
