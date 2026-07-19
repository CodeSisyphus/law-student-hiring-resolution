#!/usr/bin/env python3
"""Regenerate the pamphlet QR code (qr_site.png).

Edit URL below only if the GitHub Pages address changes (for example, if you
publish under a different repository name or a custom domain). After running
this, re-render the pamphlet with render_pamphlet.py so the new QR is embedded.

Requires: pip install "qrcode[pil]"
"""
import qrcode

URL = "https://codesisyphus.github.io/law-student-hiring-resolution/"

qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=12, border=2)
qr.add_data(URL)
qr.make(fit=True)
qr.make_image(fill_color="#12294a", back_color="white").save("qr_site.png")
print("Wrote qr_site.png pointing to:", URL)
