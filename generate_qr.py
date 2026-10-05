"""Generate the QR codes that point to the website.

Usage:
    pip install segno
    python qr/generate_qr.py                      # uses the default URL below
    python qr/generate_qr.py https://example.com  # or pass a different URL

Outputs (in this folder):
    qr-code.svg        Vector. Best for resumes, business cards, and anything printed.
    qr-code.png        High-res PNG (1800px). For LinkedIn, slides, or Canva.
    qr-code-small.png  450px. For email signatures or quick sharing.
"""

import sys
from pathlib import Path

import segno

DEFAULT_URL = "https://niko2421.github.io/NikolasMorris-Website/"
OUT = Path(__file__).resolve().parent

# Brand color for the dark modules. Keep it DARK on a WHITE background:
# low contrast and inverted (light-on-dark) codes fail on many phone cameras.
DARK = "#1f4e8c"
LIGHT = "#ffffff"


def main() -> None:
    url = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_URL

    # Error correction "q" (~25% recoverable) holds up when the code is
    # printed small, slightly smudged, or scanned at an angle.
    qr = segno.make(url, error="q", micro=False)

    # border=4 is the "quiet zone" the QR spec requires. Don't crop it off.
    qr.save(OUT / "qr-code.svg", scale=10, border=4, dark=DARK, light=LIGHT)
    qr.save(OUT / "qr-code.png", scale=40, border=4, dark=DARK, light=LIGHT)
    qr.save(OUT / "qr-code-small.png", scale=10, border=4, dark=DARK, light=LIGHT)

    print(f"QR codes for {url}")
    print(f"  version {qr.version}, error correction {qr.error}, {qr.symbol_size(border=0)[0]}x{qr.symbol_size(border=0)[0]} modules")
    print(f"  written to {OUT}")


if __name__ == "__main__":
    main()
