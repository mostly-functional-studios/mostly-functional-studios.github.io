# Codex-Auftrag: Firmenwebsite für Mostly Functional Studios

Arbeite direkt im **aktuellen, zunächst leeren Verzeichnis**. Erstelle alle benötigten Dateien vollständig und ausführbar. Kein Entwurf, kein Pseudocode. Stelle keine Rückfragen, sofern du mit eindeutig markierten Datenplatzhaltern weiterarbeiten kannst.

## Ziel und Referenzen

Entwickle eine moderne, seriös wirkende, aber bewusst leicht ironische **deutschsprachige Firmenwebsite** für **Mostly Functional Studios**. Sie dient zunächst als offiziell nutzbare Unternehmenspräsenz (auch gegenüber dem Finanzamt) und soll später ohne großen Aufwand per KI gepflegt werden. Orientiere dich visuell an `https://mostly-functional-studios.github.io/privacy/` und den dort verwendeten originalen Markenassets. Corporate Design: beinahe schwarzer Hintergrund, kräftiges Neongrün, cremeweiße Typografie, Retro-Computer-Maskottchen mit pixeligen Augen, technische/spielerische Details. Originales Logo *nicht* neu zeichnen oder stilistisch verändern.

Die vollständigen Originaldateien heißen `mostly functional studios - company logo.jpeg`, `logo-512.png` und `apple-touch-icon.png`. Ein komplett leerer Ordner enthält diese Bilder natürlich nicht: Prüfe zuerst, ob du die originalen Dateien über die genannte öffentliche Datenschutzseite bzw. das dazugehörige öffentliche Repository beziehen kannst. Falls nicht, verwende funktionsfähige lokale, explizit als **temporär** markierte Asset-Platzhalter und dokumentiere knapp die drei einzukopierenden Originaldateien samt Zielpfaden. Niemals erfundene Markenlogos verwenden, keine fremden Bild-CDNs und keine permanenten Remote-Image-Hotlinks. Lege Favicon-Varianten aus dem Original `logo-512.png` an, sobald es verfügbar ist.

## Technologie

- **Nur semantisches HTML5 und modernes CSS**, minimalstes Vanilla JavaScript nur bei echtem funktionalem Bedarf.
- Kein Angular, Nuxt, Next.js, React, Framework, npm, Tailwind, UI-Library, CDN, Tracking, Cookie-Banner ohne Anlass oder externe Webfonts.
- Keine Build-Abhängigkeiten. Veröffentlichung als unveränderte statische Dateien aus `site/`.
- Responsiv für 390 px, 768 px und 1440 px; zugänglich (Semantik, Tastatur, Fokus-Stile, Kontrast, sinnvolle Alt-Texte, `prefers-reduced-motion`).
- Relative lokale Pfade verwenden. Bereits bestehende Datenschutzseite unter `https://mostly-functional-studios.github.io/privacy/` verlinken; deren Eignung für den neuen Firmenauftritt explizit im README als Prüfung markieren.

## Inhalt der Startseite

1. Header mit dem originalen Maskottchen als Icon, Wordmark „Mostly Functional Studios“ und Navigation „Leistungen“, „Studio“, „Kontakt“.
2. Starker Hero mit großer Original-Firmengrafik, Headline **„GAMES. CODE. CONTENT.“**, Unterzeile: Wir entwickeln Spiele, Software und digitale Inhalte; kreativer, pragmatischer Ansatz mit Humor. Primärer CTA zu Leistungen.
3. Leistungsübersicht als drei Karten: **Games & Interactive** (Casual-/Mobile-Games), **Software & Development** (Web-/App-Software, Tools, Komponenten) und **AI & Digital Content** (digitale Medien/KI-gestützte Produktion).
4. Studio-Abschnitt: kleine Experimente, schnelle Prototypen, gute Software, kontinuierliche Verbesserung. Humorvoller Terminal-Baustein „Build ✓ / Run ✓ / Stable ~“.
5. Kontaktabschnitt mit geschäftlicher E-Mail als gut sichtbarem Platzhalter `[[CONTACT_EMAIL]]`. Keine erfundene E-Mail-Adresse, kein Kontaktformular.
6. Footer mit **Impressum**, **Datenschutz** und Rücksprung zur Startseite.
7. Eigenständige `impressum/index.html` und passende `404.html` in derselben Designsprache.

WICHTIG: Keine erfundenen Referenzen, Kunden, aktiven Spiele, Veröffentlichungen, Auszeichnungen, Adressen, Rechtsformen oder Ansprechpartner. „Mostly Functional Studios“ zunächst als **Marke** darstellen, nicht unbestätigt als bereits eingetragene UG. Keine unnötigen Marketing-Claims.

## Recht und Veröffentlichungssicherheit

- Impressum mit **sichtbaren** Platzhaltern für rechtlichen Anbieter/korrekte Rechtsform, ladungsfähige Anschrift, Vertretungsberechtigten, E-Mail, Telefon und – nur soweit zutreffend – Registergericht/HRB, USt-IdNr./Wirtschafts-IdNr. sowie weitere fallabhängige Angaben.
- An § 5 DDG und gegebenenfalls andere einschlägige Anforderungen erinnern, aber keine rechtliche Prüfung behaupten. Wichtig: Die korrekte Rechtsform hängt vom tatsächlichen Gründungsstatus ab.
- Kein Tracking und keine Cookie-Setzung durch den eigenen Seiten-Code. Für GitHub Pages gilt dennoch, dass beim Hosting IP-Adressen protokolliert werden können. Vor Veröffentlichung die vorhandene Datenschutzerklärung auf Geltung für diese Firmenwebsite überprüfen.
- Markiere den Impressumsentwurf bis zur rechtlichen Prüfung als `data-release-blocker="legal-review"` und lasse den Check ebenfalls blockieren, bis diese Markierung nach Prüfung bewusst entfernt ist.
- Verwende `scripts/check_ready.py` (nur Python-Standardbibliothek) als Release-Guard: fehlende Dateien, lokale kaputte Links und verbliebene `[[...]]`-Platzhalter führen zu Exit-Code 1.
- Zwei Prüfmodi: `python3 scripts/check_ready.py --draft` prüft lokale Links/Assets/Grundstruktur und darf trotz gekennzeichneter, offener Impressumsdaten erfolgreich sein. `python3 scripts/check_ready.py` ist die strenge Release-Prüfung und blockiert bei Platzhaltern/ungeprüftem Impressum. Ein Agent darf niemals Rechtsdaten erfinden oder die Sperre heimlich umgehen.
- `README.md` beschreibt explizit, warum der erste Deploy ohne echte Geschäftsdaten absichtlich fehlschlägt. Niemals heimlich Demo-Impressumsdaten live stellen.

## GitHub Pages

- Bereite `.github/workflows/deploy.yml` für GitHub Actions vor: bei Push auf `main` Release-Guard ausführen und ausschließlich `site/` als Pages-Artefakt veröffentlichen.
- Ziel-Repository: `mostly-functional-studios.github.io` unter der Organisation `mostly-functional-studios`, Ziel-URL `https://mostly-functional-studios.github.io/`.
- Erstelle `.nojekyll`, `robots.txt`, `sitemap.xml`, Manifest, Open-Graph-Tags, Apple-Touch-Icon und Favicons. Keine Secrets.
- Beachte, dass GitHub Pages primär für Projekt-/Organisationsdarstellung vorgesehen ist und nicht als kostenloses Hosting für einen transaktionsorientierten Online-Shop oder SaaS dienen soll; erwähne das in README.

## Agent-Infrastruktur: unbedingt gleichzeitig mit der Website erzeugen

**Kontext:** Vier Personen arbeiten am Projekt; zwei davon sind keine Entwickler. Auch diese beiden müssen Codex mit einem Satz in normaler deutscher Alltagssprache bitten können, eine Überschrift, einen Text, ein Bild, Abstände oder das responsive Design zu korrigieren. Codex soll selbstständig die betroffenen Stellen finden, die kleinstmögliche Änderung implementieren und ohne Fachjargon erklären, was passiert ist. Ziel ist **geringer Aufwand und niedriger Tokenverbrauch bei jeder späteren Änderung**.

Erzeuge deshalb mit der Website **vollständig ausgefüllte, echte Projektdateien** (keine leeren Vorlagen):

```text
AGENTS.md
.agents/skills/website-edit/SKILL.md
.agents/skills/website-release/SKILL.md
docs/CONTENT_RULES.md
docs/TEAM_GUIDE.md
```

### 1. Root-AGENTS.md: knapp, immer aktiv

Halte die Datei möglichst unter 100 Zeilen. Schreibe konkrete, überprüfbare Regeln:
- Die Zielgruppe sind auch zwei nicht-technische Teammitglieder. Umgangssprachliche Anweisungen wie „das wirkt zu groß" oder „mach den Text freundlicher" als echte Änderungsaufträge verstehen; die technische Umsetzung übernimmt Codex.
- Nur die betroffenen Dateien/Abschnitte suchen und lesen; keine rekursive Vollinventur, keine riesigen Datei-Dumps, keine pauschale Lektüre aller Dokumente. Kein paralleler oder rekursiver Subagent. Keine großen Pläne für Kleinigkeiten.
- Kleine Änderungen selbstständig ohne Rückfragen erledigen; bei rechtlichen Daten, neuen Unternehmensfakten, Preisen, Namen, Adressen oder Veröffentlichung fehlende Angaben nicht erfinden. Wenn zwingend erforderlich, **genau eine konkrete Rückfrage** stellen.
- Keine ungerechtfertigten Refactorings, Rewrites, Features, Dependencies, Frameworks oder Designwechsel. Nur relevanten HTML-/CSS-Bereich ändern. Logo und Branding schützen.
- Keine Commits, Pushes, Deployments, externen Dienste oder Geheimniszugriffe ohne ausdrückliche Anweisung.
- Datenschutz, Accessibility, Mobile und interne Links erhalten.
- Für kleine Tippfehler **keine Skills/Regeldokumente zusätzlich lesen**. Für größere/mehrteilige Website-Änderungen auf `website-edit` verweisen. Bei Release-Fragen auf `website-release` verweisen. `docs/CONTENT_RULES.md` nur für Texte/Design öffnen, wenn relevant.
- Zum Abschluss `python3 scripts/check_ready.py --draft` und bei Bedarf gezielte visuelle Kontrolle; bei Release explizit ohne `--draft`. Fehlende Browserprüfung transparent benennen.
- Ergebnisbericht **kurz und auf Deutsch**, idealerweise „Geändert / Geprüft / Noch offen"; nicht mit technischem Jargon überfrachten.

### 2. Zwei schlanke, bedarfsabhängige Codex-Skills

Lege Skills in der von Codex verwendeten projektlokalen Struktur `.agents/skills/<name>/SKILL.md` ab. Jede `SKILL.md` beginnt mit korrektem YAML-Frontmatter mit `name` und präziser, triggerorientierter `description`. Jeder Skill ist **kurz** (idealerweise weniger als 60 Zeilen), fokussiert auf seinen Workflow und darf nicht sämtliche globalen Regeln duplizieren.

**`website-edit`** – für mehrteilige oder vage Wünsche an Texte, Seitenabschnitte, Logos, Abstände, Farben und mobile Darstellung:
1. Absicht aus Nutzertext, ggf. Screenshot und betroffener Ansicht erschließen.
2. Nur betroffene HTML-/CSS-Stellen lesen.
3. Falls Tonalität betroffen, `docs/CONTENT_RULES.md` lesen.
4. Minimalen Patch umsetzen, Desktop/Mobil/A11y schützen.
5. Entwurfscheck ausführen; visuellen Check nur als erfolgt melden, wenn wirklich ausgeführt.
6. Kurz und verständlich berichten.
Ein einzelner Tippfehler braucht diesen Skill **nicht**.

**`website-release`** – für „können wir veröffentlichen?", „Release prüfen", „GitHub Pages vorbereiten":
1. Strengere Prüfung `python3 scripts/check_ready.py` ausführen.
2. Nicht bestätigte Unternehmensdaten, Impressum/Datenschutz und fehlende Assets als Blocker melden.
3. Legal-Review-Sperre nie automatisch entfernen; keine fiktiven Angaben einsetzen.
4. Veröffentlichung nur auf ausdrücklichen Wunsch und unter erfüllten Voraussetzungen. Keine ungefragten Remote-Aktionen.

**Wichtig:** Keine zusätzliche Sammlung von dutzenden Skills anlegen. Keine `.codex/rules/*.rules` für Inhalts-/Redaktionsrichtlinien benutzen: Die Redaktionsregeln gehören in `AGENTS.md` und `docs/CONTENT_RULES.md`, nicht in Shell-Ausführungsregeln. Keine eigenen Rollen-/Subagenten-Dateien erzeugen.

### 3. Redaktionsregeln (`docs/CONTENT_RULES.md`)

Kurz dokumentieren: deutscher, freundlicher, seriöser Ton mit leichtem Entwicklerhumor; Corporate Design Schwarz/Neongrün/Off-White; offizielles Logo unverändert; kurze, konkrete Texte; keine erfundenen Referenzen/Firmendaten; nicht ungefragt Impressum/Datenschutz bearbeiten; mobile Zugänglichkeit wahren. Diese Datei wird **nur bei Bedarf** gelesen.

### 4. Anleitung für Nicht-Entwickler (`docs/TEAM_GUIDE.md`)

Eine einfache deutschsprachige Seite **ohne Entwickler-Vokabular** mit 4–6 kopierbaren Beispielen wie:
- „Auf dem Handy ist das Logo zu groß, am Desktop soll alles bleiben."
- „Mach den Text unter Software & Development kürzer und lockerer."
- „Der Kontakt-Button ist zu klein. Mach ihn auf Smartphones leichter anklickbar."
- „Die Überschrift gefällt mir nicht. Gib ihr einen professionelleren Ton."
- „Prüfe, ob wir veröffentlichen dürfen, aber veröffentliche noch nichts."
Erkläre knapp, dass Ort + Problem + Wunsch genügen; Screenshots sind hilfreich. Die Teammitglieder müssen keine Dateinamen, Befehle oder CSS-Klassen kennen. Mach deutlich, dass echte Geschäfts-/Rechtsangaben von Menschen kommen müssen.

### 5. README und Tests anpassen

Verlinke `docs/TEAM_GUIDE.md` prominent aus `README.md`, dokumentiere beide Skills sowie den Unterschied zwischen `--draft` und Release-Check. Halte den Check deterministisch und ohne externe Abhängigkeiten. Der Entwurfscheck darf den rechtlichen Release-Guard **nicht** umgehen oder verändern. Teste beide Modi: Entwurfscheck erfolgreich bei korrekter Datei-/Linkstruktur; Release-Check absichtlich fehlgeschlagen bei echten noch fehlenden Pflichtangaben.

## Abschluss

Implementiere alles im aktuellen leeren Ordner. Teste den Projektaufbau, die Link- und Asset-Prüfung und die vorhandenen Breakpoints soweit möglich. Gib dann **nur eine kurze deutsche Zusammenfassung**: was angelegt wurde, wie man die Seite lokal betrachtet, wie Nicht-Entwickler Änderungen anfordern, was vor der ersten Veröffentlichung noch mit echten Daten auszufüllen ist. Keine Veröffentlichung ohne explizite Freigabe.
