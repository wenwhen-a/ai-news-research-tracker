**[B05 · Update] Seedance 2.5 API (BytePlus ModelArk)**
- **Company:** ByteDance/TikTok
- **Status:** GA (API) · **Released:** documentation current as of 2026-10-17 · **Update**
- **Surface:** Cloud API (BytePlus ModelArk), in addition to the existing Dreamina/Jimeng consumer app
- **Primary source:** <https://docs.byteplus.com/en/docs/ModelArk/seedance-2-5> ; <https://ai.byteplus.com/en/activity/seedance2-5>
- **Underlying research:** no traceable paper found for Seedance 2.5 specifically (builds on ByteDance Seed's prior Seedance 1.0/2.0 line)
- **Availability:** Documented under BytePlus ModelArk's "Video generation" API section, with Light/Production/Premium plans valid for 3 months before switching to pay-as-you-go per-token billing. This is new since the original 2026-09-21 entry, which noted the API as "coming soon."

**What shipped:** Update since 2026-09-21: Seedance 2.5, previously GA only as a consumer feature (Dreamina/Jimeng/CapCut) with its API marked "coming soon," now has live BytePlus ModelArk API documentation (tutorial + prompt guide, last updated 2026-10-17) and an active pricing/plan page with per-token and pay-as-you-go billing.
**What research it translates:** No underlying arXiv paper specific to Seedance 2.5 was located; it builds on ByteDance Seed's prior Seedance video-generation line rather than a newly published paper.
**Practical significance:** This moves Seedance 2.5 from "consumer app only" to "developer-integrable," letting third-party products call 30-second audio-video generation programmatically rather than only through Dreamina/Jimeng.
**Engineering details:** Access is documented as part of ModelArk's "Video generation" section alongside a Seedance 2.0 tutorial, with usage "offsets" billed at up to ~1:1.8 across resolutions and input modes once a plan is exhausted.
