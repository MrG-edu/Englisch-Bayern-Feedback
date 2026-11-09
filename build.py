#!/usr/bin/env python3
"""Baut die Download-Dateien im Ordner dist/.

- dist/englisch-bayern-feedback.zip  -> Skill zum Hochladen (Claude, ChatGPT)
- dist/einfuegen.md                             -> alles in einem Text zum Einfügen in jeden Chat

Aufruf im Hauptordner des Repos:  python3 build.py
"""
import re
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SKILL_NAME = "englisch-bayern-feedback"
SKILL_DIR = ROOT / "skill" / SKILL_NAME
DIST = ROOT / "dist"
GPT_LIMIT = 8000  # Zeichengrenze für Anweisungen eines eigenen GPT


def body_of(skill_md: str) -> str:
    """SKILL.md ohne YAML-Frontmatter."""
    return re.sub(r"\A---\n.*?\n---\n", "", skill_md, flags=re.S).strip() + "\n"


def build_zip() -> Path:
    DIST.mkdir(exist_ok=True)
    out = DIST / f"{SKILL_NAME}.zip"
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(SKILL_DIR.rglob("*")):
            if f.is_file() and not f.name.startswith("."):
                z.write(f, Path(SKILL_NAME) / f.relative_to(SKILL_DIR))
    return out


def build_paste() -> Path:
    skill = (SKILL_DIR / "SKILL.md").read_text(encoding="utf-8")
    parts = [
        "Bitte lies die folgenden Anweisungen und halte dich im ganzen Chat daran. "
        "Wo von Dateien wie `outline.md` oder `references/kriterien/…` die Rede ist, "
        "sind die gleichnamigen Abschnitte weiter unten gemeint. "
        "Antworte zuerst nur mit: „Bereit! Schick mir die Aufgabenstellung, den "
        "Ausgangstext und deinen Text.“",
        "",
        "=" * 60,
        "",
        body_of(skill),
    ]
    refs = sorted((SKILL_DIR / "references").rglob("*.md"))
    for ref in refs:
        rel = ref.relative_to(SKILL_DIR)
        parts += ["", "=" * 60, f"DATEI: {rel}  ({ref.name})", "=" * 60, "",
                  ref.read_text(encoding="utf-8").strip(), ""]
    out = DIST / "einfuegen.md"
    out.write_text("\n".join(parts), encoding="utf-8")
    return out


def check_gpt_limit() -> None:
    body = body_of((SKILL_DIR / "SKILL.md").read_text(encoding="utf-8"))
    n = len(body)
    status = "ok" if n <= GPT_LIMIT else "ZU LANG für eigene GPTs"
    print(f"SKILL.md ohne Frontmatter: {n} Zeichen (Grenze {GPT_LIMIT}) -> {status}")
    m = re.search(r"^description: (.*)$", (SKILL_DIR / "SKILL.md").read_text(encoding="utf-8"), flags=re.M)
    d = len(m.group(1)) if m else 0
    print(f"Beschreibung: {d} Zeichen (Grenze 200) -> {'ok' if d <= 200 else 'ZU LANG für den Upload in Claude'}")


if __name__ == "__main__":
    print("ZIP:", build_zip().relative_to(ROOT))
    print("Einfüge-Version:", build_paste().relative_to(ROOT))
    check_gpt_limit()
