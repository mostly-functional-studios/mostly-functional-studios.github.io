# Mostly Functional Studios — Corporate Website

Static, dependency-free German-language studio website using the official brand artwork. Built for GitHub Pages with basic accessibility and privacy-conscious defaults.

## Website einfach mit Codex bearbeiten

**Für alle im Team – auch ohne Programmierkenntnisse:** [Kurzanleitung mit Beispielen](docs/TEAM_GUIDE.md). Beschreibt Codex den Änderungswunsch in normalem Deutsch, gern mit Screenshot. Codex soll den kleinsten sinnvollen Eingriff durchführen, testen und verständlich berichten.

Projektregeln: `AGENTS.md`. Bei Bedarf werden die Skills `website-edit` (Inhalte/Design) und `website-release` (Veröffentlichungsprüfung) aus `.agents/skills/` verwendet; Tonalität und Markenregeln stehen in `docs/CONTENT_RULES.md`. Für einen Tippfehler müssen keine zusätzlichen Skills geladen werden.

## Run locally

```sh
python3 -m http.server 8080 --directory site
```

Open http://localhost:8080/.

## Publish to GitHub Pages

1. Create the **public** repository `mostly-functional-studios.github.io` in the `mostly-functional-studios` GitHub organization (or adapt canonical/sitemap paths to another repository). Using this repository name yields `https://mostly-functional-studios.github.io/`.
2. **Before your first deployment**, replace all `[[UPPERCASE_PLACEHOLDERS]]` in `site/index.html` and `site/impressum/index.html` with verified corporate details. If a conditional registration or ID does not exist, remove the corresponding optional line/section instead of publishing `n/a` text or fictional data.
3. Remove the yellow **ENTWURF** banner (`data-release-blocker`) from the imprint **only after** verifying the final business notice. It deliberately blocks a production deployment.
4. Independently verify the company's legal trading name, current legal form, authorized representative, complete **ladungsfähige** address, email and an immediately usable contact option. Check if registry information, VAT or business ID and further mandatory disclosures apply. Do not publish personal tax numbers.
5. Check the existing [privacy page](https://mostly-functional-studios.github.io/privacy/): it may cover games/apps and need to be extended for this new corporate site and its GitHub Pages hosting logs. This repository itself loads no third-party resources, does not use tracking scripts or cookies, and does not include a contact form.
6. Commit and push to `main`. Enable **Settings → Pages → Build and deployment → Source: GitHub Actions**. Workflow `.github/workflows/deploy.yml` validates placeholders/assets before publishing.
7. If the company name or repository host changes, update `canonical`, `og:url`, `og:image`, sitemap and robots.txt.

## Verify

```sh
python3 scripts/check_ready.py --draft   # Everyday edits: links/assets, legal fields may remain open
python3 scripts/check_ready.py           # Publication: ALL legal/contact fields must be complete
```

The strict check **intentionally fails** until real legal/contact data is supplied. This is a release safety feature, not an installation error.

## Project structure

```
site/
  index.html                Company landing page
  impressum/index.html      Business imprint (draft until filled)
  404.html                  Custom error page
  assets/css/styles.css     Single shared design system
  assets/img/               Official logos and derived favicon files
  robots.txt
  sitemap.xml
  site.webmanifest
scripts/check_ready.py      No-dependencies release guard
.github/workflows/deploy.yml
AGENTS.md                   Short, always-on Codex instructions
.agents/skills/website-edit/SKILL.md     Editing workflow
.agents/skills/website-release/SKILL.md  Release-readiness workflow
docs/CONTENT_RULES.md      Brand/editorial rules (read only when relevant)
docs/TEAM_GUIDE.md         Plain-language guide for teammates
```

## Maintenance philosophy

Ask your coding agent for targeted edits. Avoid adding a framework until the website genuinely requires rich interactivity, a large content collection, i18n, or dynamic applications. GitHub Pages does not support PHP or a private backend. GitHub Pages also has **commercial-use restrictions**: it is primarily a project/organization showcase host, not a free host for a transactional online business or SaaS. Re-evaluate hosting if that use changes.

## Legal note

The imprint is an implementation scaffold, **not a legally validated final notice**. The business must review all mandatory disclosures and applicable data-protection notices before going live.
