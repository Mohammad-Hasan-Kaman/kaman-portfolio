"""Generate updated CV PDFs (EN / FA / AR) from cv_data.py.

Thin wrapper around the site's own generator (portfolio/cv_pdf.py, fpdf2)
so there is exactly ONE rendering engine and ONE content source.
Run:  python generate_cv.py
"""
import os
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kaman_portfolio.settings")

import django  # noqa: E402

django.setup()

from portfolio.cv_pdf import _CvPdf  # noqa: E402
from cv_data import DATA  # noqa: E402

if __name__ == "__main__":
    for lang, d in DATA.items():
        pdf = _CvPdf(lang=lang).build(None, lang)
        out = os.path.join(BASE, "media", "cv", d["file"])
        with open(out, "wb") as f:
            f.write(pdf)
        print("built:", d["file"])
        if lang == "en":
            # The site's cv page also serves a language-suffixed variant.
            alt = os.path.join(BASE, "media", "cv", "Mohammad_Hasan_Kaman_CV_en.pdf")
            with open(alt, "wb") as f:
                f.write(pdf)
            print("built:", "Mohammad_Hasan_Kaman_CV_en.pdf")
    print("ALL DONE")
