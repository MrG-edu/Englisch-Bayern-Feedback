# Korrigierter Text im Lehrerstil

Am Ende jeder Korrektur gibst du den Schülertext **noch einmal vollständig** aus, so wie du ihn bekommen hast, mit eingebauten Korrekturen wie von der Lehrkraft:
- Fehler **rot durchgestrichen**, die Verbesserung **darüber**,
- **Fehlerkürzel am Rand**,
- längere Erklärungen als **Kommentar unter dem Text**.

## Was korrigiert wird

- **Nur sprachlich.** Inhalt, Aufbau und Aussage bleiben so, wie die Person sie geschrieben hat. Nichts ergänzen, nichts umstellen, nichts streichen, nur weil es inhaltlich nicht passt. Das steht schon im Feedback oben.
- Erlaubt ist, was die Sprachbewertung betrifft, ohne den Sinn zu ändern: z. B. eine abgeschriebene Stelle in eigene Worte fassen (Ü) oder direkte Rede in indirekte umwandeln.
- Jede Korrektur aus der Tabelle „Sprachliche Korrektur" taucht hier auf, mit demselben Kürzel.
- Absätze und Reihenfolge des Originals bleiben erhalten. Der Text wird nicht geglättet.

## Darstellung A: HTML (bevorzugt)

Nutze diese Form, wenn du in deiner Umgebung eine HTML-Datei, ein Artefakt oder eine Canvas-Vorschau erstellen kannst. Kopiere die Vorlage unten **unverändert** und ersetze nur die drei Kommentare `<!-- AUFGABE -->`, `<!-- TEXT … -->` und `<!-- KOMMENTARE … -->`. Dateiname: `korrektur.html`.

Markiere jede Korrektur im Text mit dem Element `<k>`. Das Skript in der Vorlage macht daraus Durchstreichung, Verbesserung darüber und Randkürzel.

| Fall | Schreibweise | Beispiel |
|---|---|---|
| Ersetzen | `<k v="Verbesserung" z="Kürzel">Original</k>` | `the town <k v="has" z="G">have</k> fast internet` |
| Streichen | `<k v="" z="Kürzel">Original</k>` | `He <k v="" z="G">did</k> went home` |
| Einfügen (z. B. Komma, Artikel) | `<k v="Einfügung" z="Kürzel"></k>` | `First<k v="," z="Z"></k> the author` |
| Mit Kommentar unten | zusätzlich `n="Nummer"` | `<k v="deals with" z="Id" n="1">it is about</k>` |

Regeln:
- Eine Verbesserung über dem Text hat **höchstens vier Wörter**. Ist sie länger, schreibst du über den Text nur `→ ②` (Kommentarnummer als Kreiszahl), setzt `n="2"` und bringst die Verbesserung im Kommentar unten.
- Mehrere Kürzel für eine Stelle trennst du mit Leerzeichen: `z="G Id"`.
- Kommentare nummerierst du in der Reihenfolge des Textes. Die Nummer in `n` entspricht der Position in der Kommentarliste. Höchstens 20 Kommentare, kurze Erklärungen zu einfachen Fehlern brauchen keinen.
- Sonderzeichen im Schülertext: `<` als `&lt;`, `&` als `&amp;`. Anführungszeichen in `v` als `&quot;`.

### Vorlage

```html
<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Korrigierter Text</title>
<style>
  body { margin: 0; background: #f3f1ec; font-family: Georgia, "Times New Roman", serif; color: #1a1a1a; }
  .seite { max-width: 820px; margin: 24px auto; background: #fff; padding: 36px 40px 40px; box-shadow: 0 1px 4px rgba(0,0,0,.12); }
  h1 { font-size: 20px; margin: 0 0 4px; font-family: system-ui, sans-serif; }
  .aufgabe { font-size: 14px; color: #555; margin: 0 0 24px; font-family: system-ui, sans-serif; }
  .blatt { position: relative; padding-right: 96px; }
  .blatt::after { content: ""; position: absolute; top: 0; bottom: 0; right: 84px; border-right: 1.5px solid #d33; }
  .blatt p { font-size: 17px; line-height: 3; margin: 0 0 18px; }
  .korr del { color: #d00; text-decoration-color: #d00; text-decoration-thickness: 1.5px; }
  .korr rt { color: #d00; font-size: 14px; ruby-position: over; white-space: nowrap; }
  .korr ruby { ruby-align: center; }
  .korr .einf { color: #d00; font-weight: bold; }
  .rand { position: absolute; right: 0; width: 76px; color: #d00; font-size: 15px; line-height: 1.3; padding-top: 14px; }
  h2 { font-size: 16px; font-family: system-ui, sans-serif; margin: 28px 0 8px; }
  .kommentare li { font-size: 15px; line-height: 1.5; margin-bottom: 6px; }
  .kommentare li::marker { color: #d00; font-weight: bold; }
  .legende { font-size: 13px; color: #555; font-family: system-ui, sans-serif; margin-top: 24px; border-top: 1px solid #ddd; padding-top: 10px; }
  @media (max-width: 600px) { .seite { padding: 20px 14px; } .blatt { padding-right: 64px; } .blatt::after { right: 56px; } .rand { width: 52px; font-size: 13px; } }
  @media print { body { background: #fff; } .seite { box-shadow: none; margin: 0; } }
</style>
</head>
<body>
<div class="seite">
  <h1>Korrigierter Text</h1>
  <p class="aufgabe">Aufgabe: <!-- AUFGABE --></p>

  <div class="blatt">
    <!-- TEXT: jeder Absatz in <p>, Korrekturen mit <k> -->
  </div>

  <h2>Kommentare</h2>
  <ol class="kommentare">
    <!-- KOMMENTARE: <li>…</li>, Nummern passen zu n="…" im Text -->
  </ol>

  <p class="legende">G Grammatik · T Zeitform · W Wort · Id Germanismus · Sb Satzbau · R Rechtschreibung · Z Zeichensetzung · St Stil · A Ausdruck · Ü übernommen · Zi Zitierweise</p>
</div>
<script>
(function () {
  var nums = "①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳";
  var blatt = document.querySelector(".blatt");
  blatt.querySelectorAll("k").forEach(function (k) {
    var orig = k.innerHTML, v = k.getAttribute("v") || "", z = k.getAttribute("z") || "", n = k.getAttribute("n");
    var s = document.createElement("span"); s.className = "korr";
    if (orig.trim() === "") {
      s.innerHTML = '<ruby><span class="einf">‸</span><rt></rt></ruby>';
    } else {
      s.innerHTML = "<ruby><del></del><rt></rt></ruby>";
      s.querySelector("del").innerHTML = orig;
    }
    s.querySelector("rt").textContent = v;
    var r = document.createElement("span"); r.className = "rand";
    r.textContent = z + (n ? " " + (nums[+n - 1] || "(" + n + ")") : "");
    s.appendChild(r);
    k.replaceWith(s);
  });
  function merge() {
    var prev = null;
    blatt.querySelectorAll(".rand").forEach(function (r) {
      r.style.display = ""; if (r.dataset.t) { r.textContent = r.dataset.t; } else { r.dataset.t = r.textContent; }
    });
    blatt.querySelectorAll(".rand").forEach(function (r) {
      if (prev && Math.abs(r.offsetTop - prev.offsetTop) < 8) {
        prev.textContent += " " + r.textContent; r.style.display = "none";
      } else { prev = r; }
    });
  }
  merge(); window.addEventListener("resize", merge);
})();
</script>
</body>
</html>
```

## Darstellung B: ohne HTML

Kannst du keine HTML-Datei und keine Vorschau anzeigen (z. B. in einer App ohne Canvas), gib den Text in Markdown aus:
- Ersetzen: `~~have~~ **has** ⟨G⟩`
- Streichen: `He ~~did~~ ⟨G⟩ went home`
- Einfügen: `First **,** ⟨Z⟩ the author`
- Kommentar: `⟨Id ①⟩` und darunter eine nummerierte Liste mit den Kommentaren.

Absätze bleiben erhalten, zwischen den Absätzen steht eine Leerzeile.
