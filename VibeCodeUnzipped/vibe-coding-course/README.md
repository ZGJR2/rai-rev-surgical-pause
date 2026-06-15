# Vibe Coding for Healthcare Professionals — Course Package

A beginner course (no coding background needed) on using AI "vibe coding" tools to
build useful, practical, **PHI-free** tools for healthcare workflow, learning, and
administrative tasks. Available in **English** and **Spanish**.

## Contents

| Document | English | Spanish |
|---|---|---|
| Syllabus / Programa | [`en/01-syllabus.md`](en/01-syllabus.md) | [`es/01-programa.md`](es/01-programa.md) |
| Week 1 Full Lesson / Semana 1 | [`en/02-week1-lesson.md`](en/02-week1-lesson.md) | [`es/02-semana1-leccion.md`](es/02-semana1-leccion.md) |

### PDF versions (`pdf/`)

- `Vibe-Coding-Syllabus-EN.pdf`
- `Vibe-Coding-Week1-Lesson-EN.pdf`
- `Vibe-Coding-Programa-ES.pdf`
- `Vibe-Coding-Semana1-Leccion-ES.pdf`

## The one rule that matters most

**Never enter real patient information (PHI) into any AI tool.** Build only with
fake / sample data, in the "green zone" (education, public references, personal
admin, dummy-data demos). When real patient data is involved, stop and escalate
to your IT/compliance team. This package is educational and is not legal or
compliance advice.

## Rebuilding the PDFs

```bash
pip install markdown weasyprint
python3 build_pdf.py
```

PDFs are written to `pdf/`. The script converts each markdown file to styled
HTML and then to PDF with WeasyPrint.
