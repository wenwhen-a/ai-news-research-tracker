**[B09] Seedance 2.5**
- **Company:** ByteDance (Seed team; served via Volcano Engine/BytePlus ARK and the Jimeng/Doubao consumer apps)
- **Status:** GA (consumer surface); API access listed "coming soon" at launch · **Released:** 2026-07-31 · **New**
- **Surface:** Consumer app (Jimeng/即梦, Doubao Pro) + cloud API (Volcano Engine ARK/BytePlus ModelArk)
- **Primary source:** <https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5>
- **Underlying research:** "Seedance 2.0: Advancing Video Generation for World Complexity" (arXiv:2604.14148) — base architecture; no dedicated 2.5 paper found
- **Availability:** Live now on Jimeng web and Doubao Pro; API rollout via BytePlus ModelArk announced as imminent at launch.

**What shipped:** ByteDance's Seed team shipped Seedance 2.5, a video-generation model producing a single continuous 30-second clip (up from 15s in 2.0), accepting up to 30 images/10 video clips/10 audio clips as reference material in one pass, and adding timestamp-level regional editing of a generated clip.
**What research it translates:** It extends the unified multimodal audio-video joint-generation architecture from Seedance 2.0 (arXiv:2604.14148); the blog post attributes the duration and reference-budget gains to that base architecture rather than a new method, and no separate 2.5 technical report was found.
**Practical significance:** ByteDance states the model targets professional short-form production (ads, education, drama) needing multi-shot continuity and localized edits without full regeneration — its first consumer/API-facing model to push single-pass generation to a full 30 seconds with in-place region editing.
**Engineering details:** Reference budget is up to 30 images + 10 video clips + 10 audio clips per generation, with claimed multi-round extension for multi-minute output.
