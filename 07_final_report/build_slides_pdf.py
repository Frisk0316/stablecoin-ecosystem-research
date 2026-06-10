# -*- coding: utf-8 -*-
"""Build a 16:9 PDF deck from slide_script_v0_3.md using headless Edge.

No third-party dependencies: parses the Markdown speaker script into one
HTML page per slide, then drives Microsoft Edge --print-to-pdf.
"""
import html
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
SRC = HERE / "slide_script_v0_3.md"
HTML_OUT = HERE / "穩定幣研究 — 讀書會投影片 v0.4.1.html"
PDF_OUT = HERE / "穩定幣研究 — 讀書會投影片 v0.4.1.pdf"
EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

MARKERS = ("**Body**", "**Speaker notes**", "**Source claims**",
           "**Key figures**", "**Visual**")


def parse(text):
    pages = []
    cur = None
    section = None
    for raw in text.split("\n"):
        line = raw.rstrip()
        if line.startswith("# Speaker Checklist"):
            break  # internal prep, not part of the deck
        if line.startswith("## Slide "):
            cur = {"kind": "slide", "title": line[len("## Slide "):].strip(),
                   "body": [], "notes": [], "claims": "", "figures": "",
                   "visual": ""}
            pages.append(cur)
            section = None
            continue
        if line.startswith("# "):
            pages.append({"kind": "part", "title": line[2:].strip()})
            cur = None
            section = None
            continue
        if cur is None or cur["kind"] != "slide":
            continue
        if line == "**Body**":
            section = "body"; continue
        if line == "**Speaker notes**":
            section = "notes"; continue
        if line.startswith("**Source claims**"):
            cur["claims"] = line.split(":", 1)[1].strip() if ":" in line else ""
            section = None; continue
        if line.startswith("**Key figures**"):
            cur["figures"] = line.split(":", 1)[1].strip() if ":" in line else ""
            section = None; continue
        if line.startswith("**Visual**"):
            cur["visual"] = line.split(":", 1)[1].strip() if ":" in line else ""
            section = None; continue
        if section == "body" and line.startswith(">"):
            cur["body"].append(line[1:].strip())
        elif section == "notes":
            cur["notes"].append(line)
    return pages


def split_title(t):
    if " / " in t:
        en, zh = t.split(" / ", 1)
        # leading "N -" already stripped; en may still hold the number prefix
        return zh.strip(), en.strip()
    return t.strip(), ""


def esc(s):
    return html.escape(s)


def render_body(body):
    out = []
    for ln in body:
        if ln == "":
            out.append('<div class="spacer"></div>')
        else:
            out.append(f'<div class="bline">{esc(ln)}</div>')
    return "\n".join(out)


def render_notes(notes):
    # collapse blank lines into paragraph breaks
    paras, buf = [], []
    for ln in notes:
        if ln.strip() == "":
            if buf:
                paras.append(" ".join(buf)); buf = []
        else:
            buf.append(ln.strip())
    if buf:
        paras.append(" ".join(buf))
    return "\n".join(f"<p>{esc(p)}</p>" for p in paras)


CSS = """
@page { size: 13.333in 7.5in; margin: 0; }
* { box-sizing: border-box; }
body { margin: 0; font-family: "Microsoft JhengHei","PingFang TC","Noto Sans CJK TC",sans-serif; }
.slide { width: 13.333in; height: 7.5in; page-break-after: always; position: relative;
         padding: 0.55in 0.7in 0.45in 0.7in; overflow: hidden; background: #ffffff; color: #1c2733; }
.slide:last-child { page-break-after: auto; }
.tag { font-size: 12px; letter-spacing: 2px; color: #2e6ca4; font-weight: 700; text-transform: uppercase; }
.tag .num { color: #9aa7b4; margin-left: 10px; font-weight: 600; }
h1 { font-size: 34px; margin: 6px 0 2px 0; color: #14334f; line-height: 1.2; }
.en { font-size: 14px; color: #7d8a97; margin: 0 0 14px 0; font-weight: 600; }
.rule { height: 4px; width: 70px; background: #2e6ca4; margin: 10px 0 18px 0; border-radius: 2px; }
.body { font-size: 22px; line-height: 1.5; color: #21303f; }
.bline { margin: 2px 0; }
.spacer { height: 12px; }
.notes { position: absolute; left: 0.7in; right: 0.7in; bottom: 0.85in;
         border-left: 3px solid #cdd8e2; padding: 4px 0 4px 12px; }
.notes .lbl { font-size: 10px; color: #9aa7b4; font-weight: 700; letter-spacing: 1px; }
.notes p { font-size: 10.5px; line-height: 1.35; color: #5d6b78; margin: 2px 0; }
.foot { position: absolute; left: 0.7in; right: 0.7in; bottom: 0.3in;
        font-size: 9.5px; color: #aab4bf; border-top: 1px solid #e6ebf0; padding-top: 4px; }
.foot b { color: #7d8a97; }
/* part divider */
.part { display: flex; flex-direction: column; justify-content: center; align-items: flex-start;
        background: #14334f; color: #ffffff; }
.part .pk { font-size: 16px; letter-spacing: 4px; color: #7fb1dd; font-weight: 700; }
.part h1 { font-size: 48px; color: #ffffff; margin-top: 8px; }
.part .pr { height: 5px; width: 120px; background: #2e6ca4; margin-top: 16px; border-radius: 2px; }
.cover { background: #14334f; color: #fff; justify-content: center; }
"""


def render(pages):
    parts_seen = 0
    slides_html = []
    for p in pages:
        if p["kind"] == "part":
            parts_seen += 1
            pk, ph = (p["title"].split(" - ", 1) + [""])[:2]
            slides_html.append(
                f'<div class="slide part"><div class="pk">{esc(pk)}</div>'
                f'<h1>{esc(ph or pk)}</h1><div class="pr"></div></div>')
            continue
        zh, en = split_title(p["title"])
        # slide number is the leading token of en/zh title line
        num = ""
        # title came in as "36 - Taiwan... / 台灣..."; recover number
        head = p["title"].split(" - ", 1)
        if len(head) == 2 and head[0].strip().isdigit():
            num = head[0].strip()
            zh, en = split_title(head[1])
        meta = []
        if p["visual"]:
            meta.append(f'圖示 {esc(p["visual"])}')
        if p["figures"]:
            meta.append(f'關鍵數據 {esc(p["figures"])}')
        foot_bits = []
        if p["claims"]:
            foot_bits.append(f'<b>Source claims</b> {esc(p["claims"])}')
        if meta:
            foot_bits.append(" &nbsp;|&nbsp; ".join(meta))
        foot = '<div class="foot">' + " &nbsp;|&nbsp; ".join(foot_bits) + "</div>" if foot_bits else ""
        notes = ""
        if p["notes"]:
            notes = (f'<div class="notes"><div class="lbl">講者備註 SPEAKER NOTES</div>'
                     f'{render_notes(p["notes"])}</div>')
        en_html = f'<div class="en">{esc(en)}</div>' if en else ""
        slides_html.append(
            f'<div class="slide"><div class="tag">Slide<span class="num">{esc(num)}</span></div>'
            f'<h1>{esc(zh)}</h1>{en_html}<div class="rule"></div>'
            f'<div class="body">{render_body(p["body"])}</div>'
            f'{notes}{foot}</div>')
    return ("<!doctype html><html lang='zh-Hant'><head><meta charset='utf-8'>"
            f"<style>{CSS}</style></head><body>" + "\n".join(slides_html) +
            "</body></html>")


def main():
    pages = parse(SRC.read_text(encoding="utf-8"))
    HTML_OUT.write_text(render(pages), encoding="utf-8")
    n_slides = sum(1 for p in pages if p["kind"] == "slide")
    print(f"Parsed {n_slides} slides, {len(pages)} total pages -> {HTML_OUT.name}")
    if not pathlib.Path(EDGE).exists():
        print("Edge not found; HTML written but PDF not generated.", file=sys.stderr)
        return 1
    if PDF_OUT.exists():
        PDF_OUT.unlink()
    cmd = [EDGE, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
           f"--print-to-pdf={PDF_OUT}", HTML_OUT.as_uri()]
    subprocess.run(cmd, check=True, timeout=180)
    if PDF_OUT.exists():
        print(f"PDF written: {PDF_OUT.name} ({PDF_OUT.stat().st_size} bytes)")
        return 0
    print("Edge ran but no PDF produced.", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
