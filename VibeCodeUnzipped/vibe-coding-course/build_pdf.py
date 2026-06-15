#!/usr/bin/env python3
"""Convert the course markdown files into styled HTML and PDF.

Usage:  python3 build_pdf.py
Requires: python `markdown` and `weasyprint` packages.
"""
import os
import sys
import markdown
from weasyprint import HTML

HERE = os.path.dirname(os.path.abspath(__file__))
PDF_DIR = os.path.join(HERE, "pdf")

# (source markdown, output base name)
FILES = [
    ("en/01-syllabus.md", "Vibe-Coding-Syllabus-EN"),
    ("en/02-week1-lesson.md", "Vibe-Coding-Week1-Lesson-EN"),
    ("es/01-programa.md", "Vibe-Coding-Programa-ES"),
    ("es/02-semana1-leccion.md", "Vibe-Coding-Semana1-Leccion-ES"),
]

CSS = """
@page { margin: 2cm; }
body { font-family: 'Liberation Sans', Arial, sans-serif; font-size: 11pt;
       line-height: 1.5; color: #1a1a1a; max-width: 100%; }
h1 { color: #0b5394; font-size: 22pt; border-bottom: 3px solid #0b5394;
     padding-bottom: 6px; margin-top: 0; }
h2 { color: #0b5394; font-size: 16pt; margin-top: 22px;
     border-bottom: 1px solid #cfe0f2; padding-bottom: 3px; }
h3 { color: #1f6fb2; font-size: 13pt; margin-top: 16px; }
p, li { font-size: 11pt; }
em { color: #444; }
strong { color: #111; }
a { color: #0b5394; text-decoration: none; word-break: break-all; }
table { border-collapse: collapse; width: 100%; margin: 12px 0; }
th, td { border: 1px solid #b9c9da; padding: 6px 9px; text-align: left;
         vertical-align: top; font-size: 10pt; }
th { background: #e8f0fa; color: #0b5394; }
tr:nth-child(even) td { background: #f6f9fd; }
code { background: #eef2f6; padding: 1px 4px; border-radius: 3px;
       font-family: 'Liberation Mono', 'Courier New', monospace; font-size: 9.5pt; }
pre { background: #f4f6f8; border: 1px solid #d6dde4; border-left: 4px solid #0b5394;
      padding: 10px 12px; border-radius: 4px; overflow-x: auto; }
pre code { background: none; padding: 0; font-size: 9pt; line-height: 1.35; }
blockquote { border-left: 4px solid #5b9bd5; background: #f3f8fd; margin: 12px 0;
             padding: 8px 14px; color: #2a2a2a; }
hr { border: none; border-top: 1px solid #cfd8e0; margin: 20px 0; }
ul, ol { margin: 8px 0 8px 4px; }
"""

EXTS = ["tables", "fenced_code", "sane_lists", "nl2br"]


def build_html(md_path, out_base):
    with open(md_path, encoding="utf-8") as f:
        text = f.read()
    body = markdown.markdown(text, extensions=EXTS)
    html = (
        "<!DOCTYPE html><html><head><meta charset='utf-8'>"
        f"<style>{CSS}</style></head><body>{body}</body></html>"
    )
    html_path = os.path.join(PDF_DIR, out_base + ".html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)
    return html_path


def to_pdf(html_path, pdf_path):
    HTML(filename=html_path).write_pdf(pdf_path)


def main():
    os.makedirs(PDF_DIR, exist_ok=True)
    for md_rel, out_base in FILES:
        md_path = os.path.join(HERE, md_rel)
        html_path = build_html(md_path, out_base)
        pdf_path = os.path.join(PDF_DIR, out_base + ".pdf")
        to_pdf(html_path, pdf_path)
        ok = os.path.exists(pdf_path)
        print(f"{'OK ' if ok else 'FAIL'} {out_base}.pdf")
        if not ok:
            sys.exit(1)


if __name__ == "__main__":
    main()
