#!/usr/bin/env python3
"""Render pamphlet.html to a print-ready A4 PDF.

pamphlet.html references qr_site.png by relative path, so run this from inside
this folder (both files must sit together). Output is Pamphlet.pdf; copy it up
to the conference folder as "2 - Pamphlet - A4 color (print this).pdf" to replace
the current one.

Requires: pip install weasyprint
(WeasyPrint needs system libraries pango and cairo; on macOS: brew install pango)
"""
from weasyprint import HTML

HTML("pamphlet.html").write_pdf("Pamphlet.pdf")
print("Wrote Pamphlet.pdf")
