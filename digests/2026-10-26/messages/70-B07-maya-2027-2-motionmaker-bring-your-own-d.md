**[B07] Maya 2027.2 — MotionMaker "Bring Your Own Data" custom motion-model training**
- **Company:** Autodesk (borderline — flagged per tracker rules)
- **Status:** GA · **Released:** 2026-07-22 (same release wave as 3ds Max 2027.2; Maya's own help pages give no explicit date) · **New**
- **Surface:** Studio tool (Maya character-animation feature)
- **Primary source:** <https://help.autodesk.com/cloudhelp/2027/ENU/Maya-WhatsNew/files/GUID-49B18BA5-F029-4395-83B5-8B216DBE5914.htm>
- **Underlying research:** no traceable paper
- **Availability:** Ships in Maya 2027.2, available to Maya subscribers now; MotionMaker is an existing Maya ML motion-generation tool, now extended with a custom-data training workflow.

**What shipped:** Autodesk added "Bring Your Own Data" (BYOD) to MotionMaker in Maya 2027.2, letting users train custom machine-learning motion-generation models from their own animation/mocap data, define custom "standard characters" for those models, and set a model frame rate that is stored with the trained model.
**What research it translates:** This productizes custom-data motion-model training inside Autodesk's existing MotionMaker character-animation tool; Autodesk's documentation names no specific research paper for the BYOD training method.
**Practical significance:** Autodesk states studios can now train and assign their own motion-style models — rather than relying only on Autodesk-provided styles — when assigning action styles to characters, aimed at making MotionMaker's generative locomotion usable with a studio's proprietary animation data.
**Engineering details:** The same 2027.2 update bundles Arnold for Maya 5.6.2, whose release notes state it adds native Gaussian Splat support and improved denoising, plus a USD for Maya 0.37 update with asset-path diagnostics.
