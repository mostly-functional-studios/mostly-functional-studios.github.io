# Mostly Functional Studios — Codex project instructions

## Goal and audience
Maintain this German-language static company website. Two of four teammates are non-developers: accept short, informal German change requests as normal task descriptions. Implement reasonable, low-risk interpretations autonomously. Explain outcomes in plain German, without technical jargon.

## Always-on rules
- Keep the stack simple: semantic HTML/CSS; JavaScript only if essential. No framework, npm, external runtime assets or build tooling without an explicit request.
- `site/` is the publishable root; preserve the dark/neon-lime visual identity, official logos, responsive layout, accessibility and existing content unless the user asks otherwise.
- **Minimal scope, minimal tokens:** locate and read only files relevant to the request. Never inventory or dump the full repository by default. Prefer targeted edits, reuse existing CSS; avoid unrelated cleanups and documentation churn.
- No parallel/recursive subagents. Do not write lengthy plans for small edits.
- Never invent company facts, products, clients, legal form, contact information, metrics or awards. Never replace release blockers with fake data.
- No trackers, cookies, external fonts, CDN assets or contact forms without explicit approval and a privacy review.
- Do not commit, push, publish, modify remote settings, install dependencies or request secrets unless explicitly asked. Never assert that a deployment happened without evidence.
- For copy/messaging changes, consult `docs/CONTENT_RULES.md` only if relevant. For design work, preserve existing CSS tokens and assets.

## Choose the smallest workflow
- Typo or one-word fix: edit the obvious file, run the appropriate lightweight check, finish. Do **not** load skills or all docs.
- More involved text, layout, responsive or image changes: use `.agents/skills/website-edit/SKILL.md` if the workflow is useful.
- If asked whether the site is ready to publish, or to prepare a release: use `.agents/skills/website-release/SKILL.md`.
- For missing essential facts (legal identity, addresses, contact data, business claims), do not guess. Ask **one specific question** or leave the affected field unchanged and flag it.

## Verification and response
- After site edits: `python3 scripts/check_ready.py --draft` checks files and links without requiring a completed legal imprint.
- For actual release readiness: `python3 scripts/check_ready.py` must pass; only real, human-verified legal details can clear its release blocker.
- If a browser preview is available, check the affected viewport(s); do not claim a visual check otherwise.
- Finish briefly in German: **Geändert**, **Geprüft**, and only if needed **Noch offen**. No detailed implementation walkthrough unless requested.
