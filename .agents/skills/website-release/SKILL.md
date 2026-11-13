---
name: website-release
description: Prüfe vor der Veröffentlichung der Mostly Functional Studios Website Impressum, Datenschutz-Hinweise, Linkintegrität, Assets und GitHub-Pages-Bereitschaft. Verwenden bei Anfragen wie „ist die Seite bereit?", „prüfe den Release" oder „veröffentlichen".
---

# Website release — Prüfen statt erraten

1. Lies nur `README.md`, `.github/workflows/deploy.yml` und die betroffenen Impressums-/Datenschutzstellen.
2. Prüfe interne Links und Assets. Dokumentiere reale Blocker. Entferne **niemals** Platzhalter oder `data-release-blocker` ohne inhaltliche Prüfung.
3. Prüfe, ob geschäftliche Identität, Vertretung, ladungsfähige Anschrift und Kontaktmöglichkeiten von einem Menschen als richtig bestätigt wurden. Keine rechtliche Freigabe simulieren.
4. Weise darauf hin, dass die bestehende Datenschutzseite `/privacy/` die neue Firmenwebsite und deren Hosting erfassen muss; ihre Eignung ist nicht allein aus einem Link ableitbar.
5. Prüfe die Änderung visuell und funktional, sofern die nötigen Werkzeuge verfügbar sind. Sage klar, was nicht geprüft werden konnte.
6. Gib eine kurze, priorisierte Checkliste auf Deutsch zurück: bereit / blockiert mit konkretem Grund. **Kein automatisches Commit, Push oder Deployment.** Nur bei ausdrücklichem Auftrag und erfüllten Voraussetzungen tätig werden.
