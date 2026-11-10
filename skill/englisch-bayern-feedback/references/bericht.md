# Bericht als HTML-Seite

Der Bericht ist **eine** HTML-Seite für alle Teilaufgaben. Sie zeigt pro Teilaufgabe den Gesamteindruck, das Profil als Grafik, ein Diagramm der Fehlerarten, Stärken und Schwächen, alle Korrekturen und den korrigierten Text im Lehrerstil, darüber eine ausklappbare Liste aller Korrekturzeichen. Dateiname: `korrektur.html`.

## So füllst du die Vorlage

Kopiere die Vorlage unten **unverändert**. Du änderst nur zwei Stellen:
1. das JSON im Block `<script type="application/json" id="daten">`,
2. den Kommentar `<!-- KORRIGIERTE TEXTE … -->`: an seine Stelle kommt pro Teilaufgabe ein `<template id="text-1">`, `<template id="text-2">` … mit dem korrigierten Text.

Das Skript in der Vorlage baut daraus die ganze Seite, die Grafiken, das Fehlerdiagramm und die Liste der Korrekturzeichen. Die Fehler zählt es selbst aus der Liste `fehler`, Wellenlinien und Wiederholungen aus dem korrigierten Text.

### Das JSON

```json
{
  "massstab": "Q13 · eA · Ziel C1",
  "aufgaben": [
    {
      "nummer": "B.1",
      "operator": "outline",
      "aufgabe": "Aufgabenstellung wörtlich",
      "gesamteindruck": "Zwei, drei Sätze.",
      "profil": [
        {"bereich": "Aufgabenerfüllung", "stufe": 2, "kommentar": "Ein kurzer Satz."},
        {"bereich": "Inhalt", "stufe": 3, "kommentar": "…"},
        {"bereich": "Aufbau", "stufe": 2, "kommentar": "…"},
        {"bereich": "Sprachrichtigkeit", "stufe": 2, "kommentar": "…"},
        {"bereich": "Wortschatz & Ausdruck", "stufe": 2, "kommentar": "…"},
        {"bereich": "Satzbau & Verknüpfungen", "stufe": 3, "kommentar": "…"}
      ],
      "staerken": ["…", "…"],
      "schwaechen": ["…", "…"],
      "inhalt": {"gut": ["…"], "fehlt": ["…"], "falsch": ["…"], "ueberfluessig": ["…"]},
      "aufbau": ["…", "…"],
      "fehler": [
        {"original": "the town have", "verbesserung": "the town has", "kuerzel": "gr", "erklaerung": "…"}
      ],
      "ausdruck": [{"original": "…", "vorschlag": "…"}],
      "naechstesMal": ["…", "…", "…"],
      "kommentare": ["Kommentar ① zum korrigierten Text", "Kommentar ②"]
    }
  ]
}
```

Regeln für das JSON:
- **Maßstab:** Jahrgangsstufe, Kurs und Zielniveau nach `kriterien/niveau.md`, z. B. `"Q12 · gA · Ziel B2"`. Ohne Angabe: `"Abitur · B2/C1 (keine Angabe zu Jahrgangsstufe und Kurs)"`.
- **Gültiges JSON:** doppelte Anführungszeichen um alle Texte. Anführungszeichen **im** Text als `\"`. Keine Kommas nach dem letzten Element.
- **Profil:** immer genau diese sechs Bereiche in dieser Reihenfolge. `stufe` ist 1, 2, 3 oder 4 (1 Baustelle, 2 ausbaufähig, 3 solide, 4 Stärke).
- **Korrekturzeichen** wie in SKILL.md, klein geschrieben. Mehrere Zeichen für eine Stelle mit Leerzeichen trennen: `"gr voc"`. Die Zeichen `~` und `x` sind keine Fehler und gehören **nicht** in `fehler`, sondern in `ausdruck`.
- Leere Listen sind erlaubt (`"falsch": []`), dann fällt der Abschnitt weg.
- Kurze Hervorhebungen mit `<i>…</i>` sind in allen Texten erlaubt, sonst kein HTML.

### Der korrigierte Text

Gib den Schülertext **vollständig** wieder, so wie du ihn bekommen hast, jeder Absatz in `<p>…</p>`. Korrigiert wird **nur die Sprache**. Inhalt, Aufbau und Aussage bleiben unverändert, auch wenn sie inhaltlich falsch sind. Das steht schon im Bericht oben. Erlaubt ist, was die Sprachbewertung betrifft, ohne den Sinn zu ändern, z. B. eine abgeschriebene Stelle in eigene Worte fassen (Ü) oder direkte in indirekte Rede umwandeln.

Jede Korrektur markierst du mit dem Element `<k>`:

| Fall | Schreibweise | Beispiel |
|---|---|---|
| Ersetzen | `<k v="Verbesserung" z="Zeichen">Original</k>` | `the town <k v="has" z="gr">have</k> fast internet` |
| Streichen | `<k v="" z="Zeichen">Original</k>` | `He <k v="" z="gr">did</k> went home` |
| Einfügen (z. B. Komma, Artikel) | `<k v="Einfügung" z="Zeichen"></k>` | `First<k v="," z="p"></k> the author` |
| Mit Kommentar unten | zusätzlich `n="Nummer"` | `<k v="deals with" z="voc" n="1">it is about</k>` |
| Wellenlinie (gerade noch akzeptabel) | `<k v="Vorschlag" z="~">Original</k>` | `young people <k v="revitalize" z="~">make better</k>` |
| Wortwiederholung | `<k v="" z="x">Wort</k>` | `In the past <k v="" z="x">young people</k> left` |

- Jede Korrektur aus `fehler` taucht im Text auf, mit demselben Zeichen. Wellenlinie und Wiederholung streichen nichts durch, sie markieren nur.
- Eine Verbesserung über dem Text hat **höchstens vier Wörter**. Ist sie länger, schreibst du in `v` nur `→ ②` (Kommentarnummer als Kreiszahl ①–⑳), setzt `n="2"` und bringst die Verbesserung in `kommentare`.
- `n` ist die Position in der Liste `kommentare`. Nummeriere in der Reihenfolge des Textes. Einfache Fehler brauchen keinen Kommentar.
- Im Template: `<` im Schülertext als `&lt;`, `&` als `&amp;`, Anführungszeichen in `v` als `&quot;`.

Beispiel für eine Teilaufgabe:

```html
<template id="text-1">
<p>In the article "Small Towns, Big Comeback" by Laura Bennett <k v="deals with" z="voc" n="1">it is about</k> young people.</p>
<p>First<k v="," z="p"></k> the author <k v="explains" z="t">explained</k> that …</p>
</template>
```

## Vorlage

```html
<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Rückmeldung zu deinem Text</title>
<style>
  :root {
    color-scheme: light;
    --papier: #f4f1ea; --blatt: #fffefb; --linie: #e4dfd3; --linie-stark: #cfc8b8;
    --ink: #1d1c1a; --ink-2: #55524b; --ink-3: #85817a;
    --akzent: #2a78d6; --akzent-hell: #e3eefb; --leer: #e8e4da;
    --rot: #c8102e; --rot-hell: #fdecee; --gruen: #0f7a3d; --gruen-hell: #e8f5ec; --amber-hell: #fdf3e1; --amber: #8a5a00;
    --radius: 14px;
  }
  * { box-sizing: border-box; }
  body { margin: 0; background: var(--papier); color: var(--ink); font: 16px/1.55 system-ui, -apple-system, "Segoe UI", Roboto, sans-serif; }
  .wrap { max-width: 920px; margin: 0 auto; padding: 32px 20px 64px; }
  header.kopf { margin-bottom: 24px; }
  .kicker { font-size: 13px; letter-spacing: .02em; color: var(--ink-3); margin: 0 0 6px; }
  h1 { font-size: 30px; line-height: 1.15; margin: 0 0 10px; letter-spacing: -.01em; }
  .hinweis { font-size: 14px; color: var(--ink-2); margin: 0; }
  .massstab { display: inline-block; font-size: 13px; font-weight: 600; color: var(--ink-2); background: var(--blatt); border: 1px solid var(--linie); border-radius: 999px; padding: 3px 12px; margin: 0 0 10px; }
  nav.sprung { display: flex; gap: 8px; flex-wrap: wrap; margin-top: 16px; }
  nav.sprung a { font-size: 14px; text-decoration: none; color: var(--ink); background: var(--blatt); border: 1px solid var(--linie); border-radius: 999px; padding: 5px 12px; }
  section.aufgabe { background: var(--blatt); border: 1px solid var(--linie); border-radius: var(--radius); padding: 28px; margin-bottom: 28px; box-shadow: 0 1px 2px rgba(40,30,10,.04); }
  .aufg-kopf { display: flex; gap: 12px; align-items: baseline; flex-wrap: wrap; margin-bottom: 6px; }
  .nr { font-weight: 700; font-size: 22px; }
  .chip { font-size: 13px; font-weight: 600; color: var(--akzent); background: var(--akzent-hell); border-radius: 999px; padding: 3px 10px; }
  .aufg-text { font-style: italic; color: var(--ink-2); margin: 0 0 18px; }
  .eindruck { font-size: 18px; line-height: 1.5; margin: 0 0 24px; padding-left: 14px; border-left: 3px solid var(--akzent); }
  h2 { font-size: 17px; margin: 30px 0 12px; display: flex; align-items: center; gap: 8px; }
  h2 .zahl { display: inline-grid; place-items: center; width: 24px; height: 24px; border-radius: 50%; background: var(--ink); color: #fff; font-size: 13px; }
  .grid2 { display: grid; grid-template-columns: 1.15fr 1fr; gap: 20px; }
  .karte { border: 1px solid var(--linie); border-radius: 12px; padding: 18px; background: #fff; }
  .karte h3 { margin: 0 0 4px; font-size: 15px; }
  .karte .unter { margin: 0 0 14px; font-size: 13px; color: var(--ink-3); }
  /* Profil */
  .profil-zeile { display: grid; grid-template-columns: 150px 1fr; gap: 4px 12px; align-items: center; padding: 8px 0; border-top: 1px solid var(--linie); position: relative; }
  .profil-zeile:first-of-type { border-top: 0; }
  .bereich { font-size: 14px; font-weight: 600; }
  .meter { display: flex; align-items: center; gap: 10px; }
  .pips { display: flex; gap: 2px; }
  .pip { width: 30px; height: 10px; background: var(--leer); }
  .pip:first-child { border-radius: 4px 0 0 4px; } .pip:last-child { border-radius: 0 4px 4px 0; }
  .pip.an { background: var(--akzent); }
  .stufe { font-size: 13px; color: var(--ink-2); white-space: nowrap; }
  .pkomm { grid-column: 2; font-size: 13px; color: var(--ink-2); line-height: 1.4; }
  /* Fehlerdiagramm */
  .balken-zeile { display: grid; grid-template-columns: 190px 1fr 28px; gap: 10px; align-items: center; height: 30px; position: relative; cursor: default; }
  .bk { font-size: 14px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; } .bk b { display: inline-block; min-width: 66px; }
  .spur { height: 14px; position: relative; }
  .balken { height: 14px; background: var(--akzent); border-radius: 0 4px 4px 0; min-width: 4px; }
  .wert { font-size: 13px; color: var(--ink-2); font-variant-numeric: tabular-nums; text-align: right; }
  .balken-zeile:hover .balken { filter: brightness(.9); }
  .tip { position: absolute; left: 200px; top: -30px; background: var(--ink); color: #fff; font-size: 12px; padding: 4px 8px; border-radius: 6px; white-space: nowrap; opacity: 0; pointer-events: none; transition: opacity .12s; z-index: 2; }
  .balken-zeile:hover .tip, .balken-zeile:focus .tip { opacity: 1; }
  .leer-hinweis { font-size: 14px; color: var(--ink-2); }
  details.tabelle { margin-top: 10px; font-size: 13px; color: var(--ink-2); }
  details.tabelle table { margin-top: 6px; }
  /* Stärken / Schwächen */
  .sw { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-top: 20px; }
  .sw .karte { padding: 16px 18px; }
  .sw ul { margin: 0; padding-left: 0; list-style: none; }
  .sw li { padding: 6px 0 6px 28px; position: relative; font-size: 15px; }
  .sw li::before { position: absolute; left: 0; top: 6px; width: 20px; height: 20px; border-radius: 50%; display: grid; place-items: center; font-size: 12px; font-weight: 700; }
  .staerken { background: var(--gruen-hell); border-color: #cfe7d7; }
  .staerken h3 { color: var(--gruen); }
  .staerken li::before { content: "✓"; background: var(--gruen); color: #fff; }
  .schwaechen { background: var(--amber-hell); border-color: #f1dfbd; }
  .schwaechen h3 { color: var(--amber); }
  .schwaechen li::before { content: "!"; background: var(--amber); color: #fff; }
  /* Inhalt */
  .gruppe { margin: 0 0 12px; }
  .label { display: inline-block; font-size: 12px; font-weight: 700; padding: 2px 8px; border-radius: 6px; margin-bottom: 4px; }
  .l-fehlt { background: var(--rot-hell); color: var(--rot); }
  .l-falsch { background: var(--rot-hell); color: var(--rot); }
  .l-ueber { background: var(--amber-hell); color: var(--amber); }
  .l-gut { background: var(--gruen-hell); color: var(--gruen); }
  .gruppe ul, .liste { margin: 4px 0 0; padding-left: 20px; }
  .gruppe li, .liste li { margin-bottom: 4px; }
  /* Tabelle */
  table { width: 100%; border-collapse: collapse; font-size: 14px; }
  th { text-align: left; font-size: 12px; color: var(--ink-3); font-weight: 600; padding: 6px 8px; border-bottom: 1px solid var(--linie-stark); }
  td { padding: 8px; border-bottom: 1px solid var(--linie); vertical-align: top; }
  td.orig { color: var(--rot); text-decoration: line-through; text-decoration-thickness: 1px; }
  td.verb { color: var(--gruen); font-weight: 600; }
  td.kz { font-weight: 700; white-space: nowrap; }
  td.n { color: var(--ink-3); font-variant-numeric: tabular-nums; }
  .tab-scroll { overflow-x: auto; }
  /* Ausdruck */
  .ausdruck li { margin-bottom: 8px; }
  .ausdruck .alt { color: var(--ink-3); }
  .ausdruck .pfeil { color: var(--akzent); font-weight: 700; margin: 0 6px; }
  .ausdruck .neu { font-weight: 600; }
  /* Nächstes Mal */
  ol.schritte { list-style: none; padding: 0; margin: 0; counter-reset: s; display: grid; gap: 10px; }
  ol.schritte li { counter-increment: s; background: var(--akzent-hell); border-radius: 10px; padding: 12px 14px 12px 48px; position: relative; }
  ol.schritte li::before { content: counter(s); position: absolute; left: 14px; top: 11px; width: 24px; height: 24px; border-radius: 50%; background: var(--akzent); color: #fff; display: grid; place-items: center; font-weight: 700; font-size: 13px; }
  /* Korrigierter Text */
  .blatt { position: relative; padding: 18px 124px 8px 22px; background: #fff; border: 1px solid var(--linie); border-radius: 12px; font-family: Georgia, "Times New Roman", serif; }
  .blatt::after { content: ""; position: absolute; top: 0; bottom: 0; right: 108px; border-right: 1.5px solid var(--rot); opacity: .7; }
  .blatt p { font-size: 17px; line-height: 3; margin: 0 0 14px; }
  .korr del { color: var(--rot); text-decoration-color: var(--rot); text-decoration-thickness: 1.5px; }
  .korr rt { color: var(--rot); font-family: system-ui, sans-serif; font-size: 13px; font-weight: 600; white-space: nowrap; }
  .korr ruby { ruby-align: center; }
  .korr .einf { color: var(--rot); font-weight: bold; }
  .korr .wellig { text-decoration: underline wavy var(--rot); text-decoration-thickness: 1.5px; text-underline-offset: 4px; }
  .korr .wdh { border-bottom: 1.5px solid var(--rot); }
  .korr .wdh-x { color: var(--rot); font-family: system-ui, sans-serif; font-size: 13px; font-weight: 700; vertical-align: sub; margin-left: 1px; }
  .rand { position: absolute; right: 10px; width: 92px; color: var(--rot); font-family: system-ui, sans-serif; font-weight: 600; font-size: 13px; line-height: 1.3; padding-top: 14px; }
  details.legende { margin: 0 0 14px; border: 1px solid var(--linie); border-radius: 12px; background: #fff; }
  details.legende summary { cursor: pointer; padding: 10px 14px; font-weight: 600; font-size: 14px; list-style: none; display: flex; align-items: center; gap: 8px; }
  details.legende summary::-webkit-details-marker { display: none; }
  details.legende summary::before { content: "▸"; color: var(--rot); transition: transform .15s; }
  details.legende[open] summary::before { transform: rotate(90deg); }
  details.legende summary .hint { font-weight: 400; color: var(--ink-3); font-size: 13px; }
  .leg-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 4px 24px; padding: 4px 14px 14px; }
  .leg-gruppe h4 { margin: 10px 0 4px; font-size: 12px; color: var(--ink-3); font-weight: 600; letter-spacing: .02em; }
  .leg-zeile { display: grid; grid-template-columns: 64px 1fr auto; gap: 8px; align-items: baseline; padding: 4px 0; border-top: 1px solid var(--linie); font-size: 13px; }
  .leg-zeile .lz { color: var(--rot); font-weight: 700; font-family: system-ui, sans-serif; }
  .leg-zeile .lb { color: var(--ink); }
  .leg-zeile .lb i { color: var(--ink-3); }
  .leg-zeile .ln { font-size: 12px; font-weight: 700; color: #fff; background: var(--rot); border-radius: 999px; padding: 0 7px; }
  .leg-zeile.aus { opacity: .55; }
  @media (max-width: 720px) { .leg-grid { grid-template-columns: 1fr; } }
  ol.kommentare { padding-left: 22px; }
  ol.kommentare li { margin-bottom: 6px; }
  ol.kommentare li::marker { color: var(--rot); font-weight: 700; }
  footer { font-size: 13px; color: var(--ink-3); text-align: center; margin-top: 8px; }
  footer p { margin: 4px 0; }
  .fehler-daten { background: var(--rot-hell); color: var(--rot); padding: 16px; border-radius: 12px; }
  @media (max-width: 720px) {
    .wrap { padding: 20px 12px 48px; } section.aufgabe { padding: 18px; }
    .grid2, .sw { grid-template-columns: 1fr; }
    .profil-zeile { grid-template-columns: 1fr; } .pkomm { grid-column: 1; }
    .blatt { padding-right: 66px; } .blatt::after { right: 56px; } .balken-zeile { grid-template-columns: 170px 1fr 24px; } .tip { left: 178px; } .rand { width: 48px; right: 4px; font-size: 12px; }
    h1 { font-size: 24px; }
  }
  @media print {
    body { background: #fff; } nav.sprung { display: none; }
    section.aufgabe { box-shadow: none; break-inside: auto; border: 0; padding: 0; }
    .karte, .blatt, ol.schritte li { break-inside: avoid; }
  }
</style>
</head>
<body>
<div class="wrap">
  <header class="kopf">
    <p class="kicker">Englisch · Oberstufe · Rückmeldung</p>
    <h1>Rückmeldung zu deinem Text</h1>
    <p class="massstab" id="massstab" hidden></p>
    <p class="hinweis">Keine Note – die Bewertung macht deine Lehrkraft. KI-Feedback kann sich irren.</p>
    <nav class="sprung" id="sprung"></nav>
  </header>
  <main id="inhalt"></main>
  <footer>
    <p>Erstellt mit dem Skill „Englisch Bayern Feedback“ · Keine Note – die Bewertung macht deine Lehrkraft.</p>
  </footer>
</div>

<!-- DATEN: hier das JSON einsetzen -->
<script type="application/json" id="daten">
{"aufgaben": []}
</script>

<!-- KORRIGIERTE TEXTE: pro Aufgabe ein <template id="text-1">, <template id="text-2"> … -->

<script>
(function () {
  var KZ = { ref: "Textbezug", sp: "Rechtschreibung", voc: "Wortwahl", wo: "Wortstellung", prep: "Präposition", t: "Zeitform", gr: "Grammatik", p: "Zeichensetzung", reg: "Register", coll: "Umgangssprache", slang: "Slang / vulgär", exp: "Ausdruck", meaning: "Sinnfehler", cop: "übernommen", cit: "Zitierweise" };
  var STUFEN = { 1: "Baustelle", 2: "ausbaufähig", 3: "solide", 4: "Stärke" };
  var KREIS = "①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳";
  var LEGENDE = [
    ["Grammatik und Form", [["gr", "Grammatikfehler", "He work on a farm."], ["t", "falsche Zeitform", "Yesterday I haven't done my homework."], ["wo", "falsche Wortstellung", "I have been never there before."], ["prep", "falsche Präposition", "I was looking on him."], ["sp", "Rechtschreibfehler", "intresting"], ["p", "Fehler in der Zeichensetzung", "The man, who I saw, must be …"]]],
    ["Wortwahl und Stil", [["voc", "falsches Wort für diesen Zusammenhang", "He put on the radio. (switch on)"], ["reg", "unpassende Sprachebene / Register", "The dude came at me."], ["coll", "zu lässige Umgangssprache", "The guy was kinda mad."], ["slang", "heftiger Slang / Vulgärsprache", ""], ["exp", "Bedeutung nicht mehr erkennbar", ""]]],
    ["Bezug und Inhalt", [["ref", "Textbezug ist nicht klar", ""], ["meaning", "nicht nachvollziehbar, Sinnfehler", ""], ["cop", "wörtlich aus dem Ausgangstext übernommen", ""], ["cit", "Zitierweise / Zeilenangabe falsch", "line 12 → (l. 12)"]]],
    ["Hinweise, keine Fehler", [["~~", "Wellenlinie: gerade noch akzeptabel", ""], ["x", "Wortwiederholung", ""]]]
  ];
  function legende(zaehl) {
    var d = el("details", "legende");
    var genutzt = Object.keys(zaehl).length;
    d.innerHTML = "<summary>Korrekturzeichen <span class=\"hint\">– " + (genutzt ? genutzt + " davon kommen in deinem Text vor" : "alle Zeichen") + "</span></summary>";
    var g = el("div", "leg-grid");
    LEGENDE.forEach(function (gr) {
      var box = el("div", "leg-gruppe"); box.appendChild(el("h4", null, gr[0]));
      gr[1].forEach(function (z) {
        var n = zaehl[z[0]] || 0, zl = el("div", "leg-zeile" + (n ? "" : " aus"));
        zl.appendChild(el("span", "lz", z[0]));
        var lb = el("span", "lb"); lb.textContent = z[1]; if (z[2]) { var i = document.createElement("i"); i.textContent = " – " + z[2]; lb.appendChild(i); } zl.appendChild(lb);
        zl.appendChild(n ? el("span", "ln", n + "×") : el("span"));
        box.appendChild(zl);
      });
      g.appendChild(box);
    });
    d.appendChild(g); return d;
  }

  var main = document.getElementById("inhalt"), nav = document.getElementById("sprung");
  function el(tag, cls, html) { var e = document.createElement(tag); if (cls) e.className = cls; if (html != null) e.innerHTML = html; return e; }
  function liste(arr, cls) { var ul = el("ul", cls); (arr || []).forEach(function (t) { ul.appendChild(el("li", null, t)); }); return ul; }
  function h2(nr, text) { return el("h2", null, (nr ? '<span class="zahl">' + nr + "</span>" : "") + text); }

  var daten;
  try { daten = JSON.parse(document.getElementById("daten").textContent); }
  catch (e) { main.appendChild(el("div", "fehler-daten", "Die Daten dieses Berichts konnten nicht gelesen werden. Bitte die Korrektur noch einmal anfordern.")); return; }
  if (daten.massstab) { var ms = document.getElementById("massstab"); ms.textContent = "Maßstab: " + daten.massstab; ms.hidden = false; }

  (daten.aufgaben || []).forEach(function (a, i) {
    var idx = i + 1, sec = el("section", "aufgabe"); sec.id = "aufgabe-" + idx;
    var titel = a.nummer ? "Aufgabe " + a.nummer : "Aufgabe " + idx;
    if ((daten.aufgaben || []).length > 1) { var l = el("a", null, titel); l.href = "#" + sec.id; nav.appendChild(l); }
    var kopf = el("div", "aufg-kopf"); kopf.appendChild(el("span", "nr", titel)); if (a.operator) kopf.appendChild(el("span", "chip", a.operator)); sec.appendChild(kopf);
    if (a.aufgabe) sec.appendChild(el("p", "aufg-text", a.aufgabe));
    if (a.gesamteindruck) sec.appendChild(el("p", "eindruck", a.gesamteindruck));

    // Profil + Fehlerdiagramm
    var g = el("div", "grid2");
    var kp = el("div", "karte"); kp.appendChild(el("h3", null, "Dein Profil")); kp.appendChild(el("p", "unter", "Wo deine Stärken und Baustellen liegen – keine Note"));
    (a.profil || []).forEach(function (p) {
      var z = el("div", "profil-zeile"); z.appendChild(el("div", "bereich", p.bereich));
      var m = el("div", "meter"), pips = el("div", "pips"); pips.setAttribute("role", "img"); pips.setAttribute("aria-label", p.bereich + ": " + (STUFEN[p.stufe] || ""));
      for (var s = 1; s <= 4; s++) pips.appendChild(el("span", "pip" + (s <= p.stufe ? " an" : "")));
      m.appendChild(pips); m.appendChild(el("span", "stufe", STUFEN[p.stufe] || "")); z.appendChild(m);
      if (p.kommentar) z.appendChild(el("div", "pkomm", p.kommentar));
      kp.appendChild(z);
    });
    g.appendChild(kp);

    var kf = el("div", "karte"); kf.appendChild(el("h3", null, "Fehler nach Art"));
    var zaehl = {}, gesamt = 0;
    (a.fehler || []).forEach(function (f) { String(f.kuerzel || "").split(/[\s,]+/).filter(function (k) { return k && k !== "~" && k !== "x"; }).forEach(function (k) { zaehl[k] = (zaehl[k] || 0) + 1; gesamt++; }); });
    var arten = Object.keys(zaehl).sort(function (x, y) { return zaehl[y] - zaehl[x]; });
    kf.appendChild(el("p", "unter", (a.fehler || []).length + " markierte Stellen · häufigste Fehlerart zuerst"));
    if (!arten.length) kf.appendChild(el("p", "leer-hinweis", "Keine Sprachfehler markiert."));
    var max = arten.length ? zaehl[arten[0]] : 1, tab = "<table><tr><th>Zeichen</th><th>Fehlerart</th><th>Anzahl</th></tr>";
    arten.forEach(function (k) {
      var z = el("div", "balken-zeile"); z.tabIndex = 0;
      z.appendChild(el("span", "bk", "<b>" + k + "</b> " + (KZ[k] || "")));
      var sp = el("div", "spur"), b = el("div", "balken"); b.style.width = (zaehl[k] / max * 100) + "%"; sp.appendChild(b); z.appendChild(sp);
      z.appendChild(el("span", "wert", String(zaehl[k])));
      z.appendChild(el("span", "tip", (KZ[k] || k) + ": " + zaehl[k] + "×"));
      kf.appendChild(z);
      tab += "<tr><td>" + k + "</td><td>" + (KZ[k] || k) + "</td><td>" + zaehl[k] + "</td></tr>";
    });
    if (arten.length) { var d = el("details", "tabelle"); d.innerHTML = "<summary>Als Tabelle</summary>" + tab + "</table>"; kf.appendChild(d); }
    g.appendChild(kf); sec.appendChild(g);

    var sw = el("div", "sw");
    var ks = el("div", "karte staerken"); ks.appendChild(el("h3", null, "Das kannst du schon")); ks.appendChild(liste(a.staerken)); sw.appendChild(ks);
    var kw = el("div", "karte schwaechen"); kw.appendChild(el("h3", null, "Hier lohnt sich Üben")); kw.appendChild(liste(a.schwaechen)); sw.appendChild(kw);
    sec.appendChild(sw);

    // 1 Inhalt
    sec.appendChild(h2(1, "Aufgabe und Inhalt"));
    var inh = a.inhalt || {};
    [["gut", "l-gut", "Gelungen"], ["fehlt", "l-fehlt", "Fehlt"], ["falsch", "l-falsch", "Falsch wiedergegeben"], ["ueberfluessig", "l-ueber", "Überflüssig"]].forEach(function (t) {
      if (inh[t[0]] && inh[t[0]].length) { var gr = el("div", "gruppe"); gr.appendChild(el("span", "label " + t[1], t[2])); gr.appendChild(liste(inh[t[0]])); sec.appendChild(gr); }
    });
    // 2 Aufbau
    sec.appendChild(h2(2, "Aufbau")); sec.appendChild(liste(a.aufbau, "liste"));
    // 3 Sprache
    sec.appendChild(h2(3, "Sprachliche Korrektur"));
    var t = "<table><tr><th>Nr.</th><th>Original</th><th>Verbesserung</th><th>Zeichen</th><th>Erklärung</th></tr>";
    (a.fehler || []).forEach(function (f, j) { t += '<tr><td class="n">' + (j + 1) + '</td><td class="orig">' + (f.original || "") + '</td><td class="verb">' + (f.verbesserung || "–") + '</td><td class="kz">' + (f.kuerzel || "") + "</td><td>" + (f.erklaerung || "") + "</td></tr>"; });
    var ts = el("div", "tab-scroll", t + "</table>"); sec.appendChild(ts);
    // 4 Ausdruck
    if (a.ausdruck && a.ausdruck.length) {
      sec.appendChild(h2(4, "Ausdruck verbessern"));
      var ul = el("ul", "liste ausdruck");
      a.ausdruck.forEach(function (x) { ul.appendChild(el("li", null, '<span class="alt">' + x.original + '</span><span class="pfeil">→</span><span class="neu">' + x.vorschlag + "</span>")); });
      sec.appendChild(ul);
    }
    // 5 Nächstes Mal
    sec.appendChild(h2(5, "Darauf achtest du beim nächsten Mal"));
    var ol = el("ol", "schritte"); (a.naechstesMal || []).forEach(function (x) { ol.appendChild(el("li", null, x)); }); sec.appendChild(ol);
    // 6 Korrigierter Text
    var tpl = document.getElementById("text-" + idx);
    if (tpl) {
      sec.appendChild(h2(6, "Dein korrigierter Text"));
      var blatt = el("div", "blatt"); blatt.appendChild(tpl.content.cloneNode(true));
      var zz = {}; Object.keys(zaehl).forEach(function (c) { zz[c] = zaehl[c]; });
      blatt.querySelectorAll("k").forEach(function (k) { String(k.getAttribute("z") || "").split(/\s+/).forEach(function (c) { if (c === "~" || c === "x") { c = c === "~" ? "~~" : "x"; zz[c] = (zz[c] || 0) + 1; } }); });
      sec.appendChild(legende(zz));
      blatt.querySelectorAll("k").forEach(function (k) {
        var orig = k.innerHTML, v = k.getAttribute("v") || "", z = k.getAttribute("z") || "", n = k.getAttribute("n");
        var s = el("span", "korr");
        if (z === "~") { s.innerHTML = '<ruby><span class="wellig"></span><rt></rt></ruby>'; s.querySelector(".wellig").innerHTML = orig; z = "~~"; }
        else if (z === "x") { s.innerHTML = '<ruby><span class="wdh"></span><rt></rt></ruby><span class="wdh-x">ⓧ</span>'; s.querySelector(".wdh").innerHTML = orig; }
        else if (orig.trim() === "") { s.innerHTML = '<ruby><span class="einf">‸</span><rt></rt></ruby>'; }
        else { s.innerHTML = "<ruby><del></del><rt></rt></ruby>"; s.querySelector("del").innerHTML = orig; }
        s.querySelector("rt").textContent = v;
        var r = el("span", "rand"); r.textContent = z + (n ? " " + (KREIS[+n - 1] || "(" + n + ")") : ""); s.appendChild(r);
        k.replaceWith(s);
      });
      sec.appendChild(blatt);
      if (a.kommentare && a.kommentare.length) { sec.appendChild(el("h3", null, "Kommentare")); var ok = el("ol", "kommentare"); a.kommentare.forEach(function (x) { ok.appendChild(el("li", null, x)); }); sec.appendChild(ok); }
    }
    main.appendChild(sec);
  });

  function rand() {
    document.querySelectorAll(".blatt").forEach(function (blatt) {
      var prev = null;
      blatt.querySelectorAll(".rand").forEach(function (r) { r.style.display = ""; if (r.dataset.t) r.textContent = r.dataset.t; else r.dataset.t = r.textContent; });
      blatt.querySelectorAll(".rand").forEach(function (r) { if (prev && Math.abs(r.offsetTop - prev.offsetTop) < 8) { prev.textContent += " " + r.textContent; r.style.display = "none"; } else prev = r; });
    });
  }
  rand(); window.addEventListener("resize", rand);
})();
</script>
</body>
</html>
```

## Ohne HTML

Kannst du keine HTML-Datei und keine Vorschau anzeigen, gib den Bericht als Markdown aus, in derselben Reihenfolge:
- **Maßstab** als erste Zeile: *Maßstab: Q13 · eA · Ziel C1*
- **Profil** als Tabelle: Bereich | Stufe | Kommentar, Stufe als Punkte: ●●●● Stärke, ●●●○ solide, ●●○○ ausbaufähig, ●○○○ Baustelle.
- **Fehler nach Art** als Zeile: *voc 3 · p 3 · t 2 · …*
- **Stärken** mit ✓, **Schwächen** mit !
- **Sprachliche Korrektur** als Tabelle: Nr. | Original | Verbesserung | Zeichen | Erklärung
- **Korrigierter Text:** Ersetzen `~~have~~ **has** ⟨gr⟩`, Streichen `~~did~~ ⟨gr⟩`, Einfügen `First **,** ⟨p⟩ the author`, Wellenlinie `_make better_ (revitalize) ⟨~⟩`, Wiederholung `young people ⟨x⟩`, Kommentar `⟨voc ①⟩` mit nummerierter Liste darunter. Absätze bleiben erhalten.
