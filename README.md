# Oberstufe Englisch Bayern – Feedback

Ein KI-Skill, der deine englischen Schreibaufgaben in den Jahrgangsstufen 12 und 13 korrigiert, ausgerichtet auf das bayerische Abitur und die Abitur-Operatoren (*outline, analyze, discuss* …).

Der Skill funktioniert mit **Claude** und **ChatGPT**.

## Was der Skill macht – und was nicht

Du schickst deinen Text **einmal** und bekommst die fertige Korrektur in einer Antwort:

✅ ob du die Aufgabe und den Operator erfüllt hast, was inhaltlich fehlt, falsch oder überflüssig ist,
✅ Hinweise zum Aufbau,
✅ **jeden Sprachfehler mit Verbesserung**, Fehlerkürzel und kurzer Erklärung,
✅ Vorschläge für einen besseren Ausdruck,
✅ drei Punkte, auf die du beim nächsten Mal achten solltest,
✅ zum Schluss **deinen Text, korrigiert wie von der Lehrkraft**: Fehler rot durchgestrichen, Verbesserung darüber, Kürzel am Rand, Kommentare darunter. Korrigiert wird dabei nur die Sprache, dein Inhalt bleibt.

So sieht die korrigierte Fassung aus: [Beispiel öffnen](beispiele/outline-beispiel-korrektur.html) (zum Ansehen herunterladen und im Browser öffnen). Die komplette Beispielkorrektur steht in [`beispiele/outline-beispiel.md`](beispiele/outline-beispiel.md).

Das Feedback ist auf Deutsch.

❌ Er schreibt keine eigene Musterlösung, sondern korrigiert **deinen** Text.
❌ Er gibt **keine Note**. Die Bewertung macht deine Lehrkraft.

## Was du brauchst

Füge immer **alle drei Teile** ein:
1. die Aufgabenstellung (wörtlich),
2. den Ausgangstext (bei Bildern oder Statistiken eine kurze Beschreibung),
3. deinen eigenen Text.

Schreib **keine Namen** oder andere persönliche Daten in den Chat.

## Welche Operatoren schon fertig sind

| Operator | Status |
|---|---|
| outline / summarize / sum up | ✅ fertig |
| analyze / examine | ✅ fertig |
| discuss | 🧪 Entwurf, wird noch geprüft |
| alle anderen | allgemeines Feedback zu Inhalt und Sprache, noch ohne eigene Checkliste |

## So benutzt du den Skill

### Variante 1: Claude
1. Lade die Datei [`dist/englisch-bayern-feedback.zip`](dist/englisch-bayern-feedback.zip) herunter (nicht entpacken).
2. Öffne in Claude die Einstellungen und lade die ZIP-Datei bei den **Skills** hoch.
3. Starte einen neuen Chat und füge Aufgabenstellung, Ausgangstext und deinen Text ein.

Claude zeigt die korrigierte Fassung direkt als Seite an, die du auch drucken kannst.

### Variante 2: ChatGPT mit Skills (nur in Business-, Enterprise- und Edu-Konten)
1. Lade dieselbe ZIP-Datei herunter.
2. In ChatGPT: **Skills → Create → Upload** und die ZIP-Datei auswählen.

### Variante 3: Eigener GPT (für Lehrkräfte, damit Schüler ihn per Link nutzen)
1. In ChatGPT einen neuen GPT anlegen.
2. Den Inhalt von [`SKILL.md`](skill/englisch-bayern-feedback/SKILL.md) **ohne** den Kopfbereich zwischen den `---`-Zeilen in das Feld **Instructions** kopieren.
3. Alle Dateien aus [`references/`](skill/englisch-bayern-feedback/references/) als **Knowledge** hochladen.
4. Unter **Capabilities** „Canvas“ aktivieren, damit die korrigierte Fassung als Seite angezeigt werden kann.
5. Den GPT per Link teilen.

In ChatGPT erscheint die korrigierte Fassung im Canvas. Dort auf **Vorschau** tippen. Ohne Canvas kommt sie als einfacher Text mit ~~durchgestrichen~~ und **fett**.

### Variante 4: Einfügen in jeden Chat (funktioniert immer)
1. Öffne [`dist/einfuegen.md`](dist/einfuegen.md) und kopiere den gesamten Text.
2. Füge ihn als erste Nachricht in einen neuen Chat ein (Claude, ChatGPT oder ein anderes Programm).
3. Danach Aufgabenstellung, Ausgangstext und deinen Text schicken.

## Aufbau des Repos

```
skill/englisch-bayern-feedback/
├── SKILL.md                 Hauptanweisungen (unter 8000 Zeichen)
└── references/
    ├── operators/           eine Datei pro Operator
    ├── kriterien/           Kriterien für Inhalt und Sprache
    └── korrekturtext.md     Vorlage für den korrigierten Text im Lehrerstil
beispiele/                   erfundene Beispieltexte mit Musterfeedback
dist/                        fertige Dateien zum Herunterladen
build.py                     erzeugt dist/ neu
```

Nach Änderungen im Ordner `skill/` einmal `python3 build.py` ausführen.

## Quellen

- IQB: *Gemeinsame Abituraufgabenpools der Länder – Englisch, Grundstock von Operatoren* (gilt ab Prüfungsjahr 2027)
- ISB Bayern: Bewertungsraster Profil- und Leistungsstufe / Abiturprüfung, Moderne Fremdsprachen (Stand Juni 2024)
- StMUK: *Schriftliche Prüfungsformen im Unterricht der modernen Fremdsprachen in der Profil- und Leistungsstufe und der Abiturprüfung* (12.06.2023)

Die Kriterien sind in eigenen Worten zusammengefasst. Maßgeblich sind die offiziellen Dokumente beim [ISB](https://www.isb.bayern.de) und im [LehrplanPLUS](https://www.lehrplanplus.bayern.de).

## Hinweis

KI-Feedback kann Fehler übersehen oder sich irren. Im Zweifel gilt, was deine Lehrkraft sagt.

## Lizenz

[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.de): Du darfst den Skill nutzen, teilen und anpassen, solange du die Quelle nennst und Änderungen unter derselben Lizenz weitergibst.
