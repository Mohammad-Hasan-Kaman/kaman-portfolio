"""
Generate a CV / Resume PDF in the requested language.

SINGLE SOURCE OF TRUTH: the content comes from cv_data.py (the user's
original CV file, EN / FA / AR).  Nothing is taken from the database, so
the site's downloadable PDF always matches the original CV word-for-word.

- FA/AR: Vazirmatn font + HarfBuzz shaping via fpdf2's set_text_shaping
- EN: Arial
Layout: colored header band, section rules, keep-together blocks.

Alignment rules (verified with pymupdf measurements):
- Every block starts flush at the left margin (LTR) / right margin (RTL).
- Section titles are always kept together with the first lines of their
  content (no orphan titles, no titles dropped off the page edge).
- Each project/entry block is kept together on one page.

The visual rendering is correct for RTL — fpdf2's shaping engine handles
bidi reordering at the glyph level.  Text extraction tools (pypdf, fitz)
may show logical-order text that looks garbled, but the PDF renders
correctly in any viewer.
"""
from __future__ import annotations

import os
import sys
from io import BytesIO
from typing import TYPE_CHECKING

from fpdf import FPDF

if TYPE_CHECKING:
    from .models import Profile

_BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _BASE not in sys.path:
    sys.path.insert(0, _BASE)

Vazir = os.path.join(_BASE, "static", "fonts", "Vazirmatn-Regular.ttf")
VazirBold = os.path.join(_BASE, "static", "fonts", "Vazirmatn-Bold.ttf")


def _first_existing(*paths):
    """Cross-platform font resolution: Windows Arial on Windows, DejaVu on Linux."""
    for p in paths:
        if p and os.path.exists(p):
            return p
    raise FileNotFoundError(f"No usable font among: {paths}")


Arial = _first_existing(
    "C:/Windows/Fonts/arial.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
)
ArialBold = _first_existing(
    "C:/Windows/Fonts/arialbd.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
)

_HB = {
    "fa": {"direction": "rtl", "script": "arab", "language": "fa"},
    "ar": {"direction": "rtl", "script": "arab", "language": "ar"},
    "en": {"direction": "ltr", "script": "latn", "language": "en"},
}

# Eastern-Arabic digit normalization so FA and AR keep the same numbers.
_FA_DIGITS = str.maketrans("0123456789", "۰۱۲۳۴۵۶۷۸۹")
_AR_DIGITS = str.maketrans("0123456789", "٠١٢٣٤٥٦٧٨٩")

ACCENT = (124, 92, 255)
ACCENT_2 = (0, 140, 200)
TEXT = (23, 26, 46)
SOFT = (90, 96, 128)

# Section titles for Summary / Core Competencies (same as the original CV).
SUMMARY_TITLE = {"en": "Summary", "fa": "خلاصه", "ar": "ملخص"}
CORE_TITLE = {
    "en": "Core Competencies",
    "fa": "شایستگی‌های اصلی",
    "ar": "الكفاءات الأساسية",
}


def _localize(text: str | None, lang: str) -> str:
    """Normalize Latin digits to the script's native digits for FA/AR."""
    if not text:
        return ""
    if lang == "fa":
        return text.translate(_FA_DIGITS)
    if lang == "ar":
        return text.translate(_AR_DIGITS)
    return text


PT2MM = 0.3528  # 1 pt = 0.3528 mm (fpdf2 cell heights are in mm)


class _CvPdf(FPDF):
    """CV PDF with proper text shaping, wrapping and page-break control."""

    def __init__(self, lang: str = "en"):
        self.lang = lang
        self.is_rtl = lang in ("fa", "ar")
        self._hb = _HB.get(lang, _HB["en"])
        super().__init__(orientation="P", unit="mm", format="A4")
        self.add_font("Vazir", "", Vazir)
        self.add_font("Vazir", "B", VazirBold)
        self.add_font("Arial", "", Arial)
        self.add_font("Arial", "B", ArialBold)
        self.set_auto_page_break(auto=True, margin=11)
        self.set_text_shaping(use_shaping_engine=True, **self._hb)
        self.set_margins(11, 10, 11)

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------
    def _font(self) -> str:
        return "Vazir" if self.is_rtl else "Arial"

    def _align(self) -> str:
        return "R" if self.is_rtl else "L"

    def _content_width(self) -> float:
        return self.w - self.l_margin - self.r_margin

    def _ensure_space(self, needed: float):
        """Start a new page if `needed` mm do not fit (keep-together)."""
        if self.get_y() + needed > self.page_break_trigger:
            self.add_page()

    def _est_lines(self, txt: str, size: float) -> int:
        """Estimate wrapped line count for txt at the given font size."""
        if not txt:
            return 0
        avail = self._content_width()
        self.set_font(self._font(), "", size)
        space_w = self.get_string_width(" ")
        lines, cur = 1, 0.0
        for word in txt.split():
            w_w = self.get_string_width(word)
            if cur > 0 and cur + space_w + w_w > avail:
                lines += 1
                cur = w_w
            else:
                cur += (space_w if cur > 0 else 0) + w_w
        return lines

    def _write(self, txt: str, size: float = 10, bold: bool = False,
               color: tuple = TEXT, line_h: float | None = None):
        """Write a wrapped paragraph with a sane line height."""
        if not txt or not txt.strip():
            return
        self.set_font(self._font(), "B" if bold else "", size)
        self.set_text_color(*color)
        lh = line_h if line_h is not None else size * 1.27 * PT2MM
        self.set_x(self.l_margin)
        self.multi_cell(w=0, h=lh, text=txt.strip(), align=self._align())
        # fpdf2 leaves x at the right edge of the cell by default - reset it
        # so the next cell / section title always starts at the left margin.
        self.set_x(self.l_margin)

    def _section_title(self, title: str):
        """Section heading with a rule, kept together with what follows."""
        self._ensure_space(12)
        self.set_font(self._font(), "B", 11)
        self.set_text_color(*ACCENT)
        display_title = title.upper() if not self.is_rtl else title
        self.set_x(self.l_margin)
        self.cell(w=0, h=5.5, text=display_title,
                  align=self._align(), new_x="LMARGIN", new_y="NEXT")
        yy = self.get_y() + 0.5
        self.set_line_width(0.4)
        if self.is_rtl:
            self.set_draw_color(*ACCENT)
            self.line(self.w - self.r_margin - 20, yy, self.w - self.r_margin, yy)
            self.set_draw_color(*ACCENT_2)
            self.set_line_width(0.25)
            self.line(self.l_margin, yy, self.w - self.r_margin - 22, yy)
        else:
            self.set_draw_color(*ACCENT)
            self.line(self.l_margin, yy, self.l_margin + 20, yy)
            self.set_draw_color(*ACCENT_2)
            self.set_line_width(0.25)
            self.line(self.l_margin + 22, yy, self.w - self.r_margin, yy)
        self.set_y(self.get_y() + 1.6)

    def _header_band(self, d: dict, lang: str):
        """Compact colored header band + contact lines (from cv_data)."""
        band_h = 26
        self.set_fill_color(*ACCENT)
        self.rect(0, 0, self.w, band_h, style="F")
        self.set_y(4)
        self._write(d["name"], size=17, bold=True, color=(255, 255, 255), line_h=8)
        self._write(_localize(d["role"], lang), size=10,
                    color=(230, 230, 245), line_h=5)

        # Contact info — two lines (contact | links), straight from cv_data
        self.set_y(band_h + 2)
        self.set_font(self._font(), "", 7)
        self.set_text_color(*SOFT)
        if d.get("contact"):
            self.set_x(self.l_margin)
            self.multi_cell(w=0, h=3.5, text=d["contact"], align=self._align())
        if d.get("links"):
            self.set_x(self.l_margin)
            self.multi_cell(w=0, h=3.5, text=d["links"], align=self._align())
        self.ln(1)
        self.set_x(self.l_margin)

    # ------------------------------------------------------------------
    # Main build — content straight from cv_data.DATA[lang]
    # ------------------------------------------------------------------
    def build(self, profile: "Profile", lang: str) -> bytes:
        from cv_data import DATA

        d = DATA.get(lang) or DATA["en"]

        self.add_page()
        self._header_band(d, lang)

        # ---- Summary ----
        summary = _localize(d.get("summary", ""), lang)
        if summary:
            self._ensure_space(9 + self._est_lines(summary, 8.5) * 4.0)
            self._section_title(SUMMARY_TITLE.get(lang, SUMMARY_TITLE["en"]))
            self._write(summary, size=8.5, color=SOFT)
            self.ln(0.5)

        # ---- Core Competencies ----
        core = d.get("core") or []
        if core:
            self._ensure_space(9 + len(core) * 4.0)
            self._section_title(CORE_TITLE.get(lang, CORE_TITLE["en"]))
            for line in core:
                self._write(f"• {_localize(line, lang)}", size=8.5, color=SOFT)
            self.ln(0.5)

        # ---- Sections from cv_data (Projects / Skills / Education / Languages) ----
        for title, items in d.get("sections") or []:
            if not items:
                continue
            # Keep the section title together with its FIRST entry (no orphan
            # titles); long sections then flow with per-entry keep-together.
            first = items[0]
            first_h = (self._est_lines(_localize(first[0], lang), 9.5) * 4.3
                       + (3.6 if _localize(first[1], lang) else 0)
                       + self._est_lines(_localize(first[2], lang), 8.5) * 4.0)
            self._ensure_space(12 + first_h + 1.5)
            self._section_title(title)

            for head, meta, body in items:
                head = _localize(head, lang)
                meta = _localize(meta, lang)
                body = _localize(body, lang)
                block_h = (self._est_lines(head, 9.5) * 4.3
                           + (3.6 if meta else 0)
                           + self._est_lines(body, 8.5) * 4.0)
                self._ensure_space(block_h + 1.5)

                self._write(head, size=9.5, bold=True, color=TEXT)
                if meta:
                    self._write(meta, size=8, color=ACCENT_2)
                if body:
                    self._write(body, size=8.5, color=SOFT)
                self.ln(1.2)

        # ---- Footer (disable auto-break so it lands on current page) ----
        self.set_auto_page_break(auto=False)
        self.set_y(self.h - 10)
        self.set_font(self._font(), "", 6.5)
        self.set_text_color(150, 150, 150)
        w = self._content_width()
        self.cell(w=w, h=4, text=f"{d.get('name', '')}  |  mhkaman.com", align="C")

        buf = BytesIO()
        self.output(buf)
        return buf.getvalue()
