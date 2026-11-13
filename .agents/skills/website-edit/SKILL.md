---
name: website-edit
description: Implementiere Änderungswünsche an Texten, Aufbau, Bildern oder mobilem Design der Mostly Functional Studios Website. Verwenden bei mehrteiligen oder unklar formulierten Website-Änderungen von nicht-technischen Teammitgliedern; nicht für einzelne Tippfehler.
---

# Website edit — Wunsch zu Umsetzung

1. Interpretiere die Nutzerbitte als Produkt-/Designfeedback, nicht als Programmierauftrag. Erkenne Ziel, betroffene Seite und ggf. Desktop/Mobile aus Nachricht oder Screenshot.
2. Suche gezielt nach dem betroffenen Text/Selektor. Öffne nur die nötigen Abschnitte in `site/index.html`, `site/impressum/index.html`, `site/404.html` oder `site/assets/css/styles.css`. Keine Vollinventur.
3. Wenn Text/Tonalität betroffen ist, lies `docs/CONTENT_RULES.md`. Verändere keine nicht angefragten Texte und keine Rechtsangaben.
4. Setze die kleinste verständliche Änderung um; erhalte Corporate Design, Navigation, Mobile, Tastaturbedienbarkeit und `prefers-reduced-motion`.
5. Bei Bild-/Logoänderungen Originalassets unverändert verwenden. Externe Bilder oder neue Informationen nur auf ausdrücklichen Wunsch und mit geeigneter Quelle.
6. Führe `python3 scripts/check_ready.py --draft` aus. Bei CSS-/Layoutänderungen: falls ein Browser verfügbar ist, betroffene Breiten prüfen; andernfalls im Abschluss transparent darauf hinweisen.
7. Antworte in 1–4 kurzen Sätzen auf Deutsch: was sichtbar anders ist, was geprüft wurde, bei Bedarf eine konkrete offene Frage.

**Entscheidungsgrenze:** Unklare Kleinigkeiten selbst sinnvoll lösen. Bei neuen Unternehmensbehauptungen, Rechtsdaten, Preis-/Kontaktangaben, Löschung ganzer Bereiche oder Veröffentlichung nichts erfinden und nötigenfalls einmal nachfragen.
