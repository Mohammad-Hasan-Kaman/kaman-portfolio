# 🌍 Kaman Portfolio — mhkaman.com

> Trilingual personal portfolio (English / فارسی / العربية) for **Mohammad Hasan Kaman**, built with Django 5. Everything on the site — profile, projects, skills, services, testimonials, articles, even UI strings — is editable from the Django admin. Deployed live at **[mhkaman.com](https://mhkaman.com)**.

[![Django](https://img.shields.io/badge/Django-5+-green.svg?logo=django&logoColor=white)](https://django.com)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg?logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/Mohammad-Hasan-Kaman/kaman-portfolio?color=blue)](https://github.com/Mohammad-Hasan-Kaman/kaman-portfolio/releases)
[![Live](https://img.shields.io/badge/Live-mhkaman.com-2ecc71.svg)](https://mhkaman.com)

---

## 🚀 Purpose & Audience

| Audience | How to use |
|----------|------------|
| **Visitors / clients** | Browse the live site — [mhkaman.com](https://mhkaman.com) — in EN, FA or AR. |
| **Developers** | Clone, `pip install -r requirements.txt`, `python manage.py seed_data`, `runserver` — full local copy in under a minute. |

---

## ✨ Key Features (verified in code)

- 🌐 **Trilingual by design:** EN / FA / AR with automatic **RTL layout** for Persian and Arabic — language-prefixed URLs (`/en/`, `/fa/`, `/ar/`), a navbar switcher, and English-first landing via `ForceEnglishDefaultMiddleware` (strips `Accept-Language` so first visits always land on `/en/`).
- 🛠 **Fully admin-driven content:** `Profile`, `Project`, `Skill`, `Service`, `Testimonial`, `Experience`, `Education`, `CvLanguage`, `Article`, `ContactMessage` — plus `SiteText` (every UI string overridable from the admin with EN fallback) and `MarqueeTag` (hero tech-ticker labels).
- 📁 **Project case-study pages:** slug URLs, tech-stack tags, live-demo + repo links, featured/ordered grid, "next project" navigation.
- 📝 **Articles (blog):** trilingual body with EN fallback, emoji card icons, optional covers, publish toggle, detail pages at `/<lang>/articles/<slug>/`.
- 📄 **Trilingual CV generator** (`portfolio/cv_pdf.py` + `cv_data.py`): single source of truth — PDFs in EN/FA/AR rendered with fpdf2, Vazirmatn + HarfBuzz shaping for FA/AR, downloadable per language (`/cv/download/?lang=fa`).
- 📊 **Privacy-friendly analytics:** server-side only — pageviews, CV downloads, contact events, language switches. Salted IP hashes, anonymous `kp_vis` cookie, bot filtering, no third-party trackers. Admin dashboard at `templates/admin/portfolio/visit/dashboard.html`.
- 🎨 **Modern animated UI:** floating gradient orbs, glassmorphism cards, bento project grid, typing effect, scroll-reveal, animated counters, tier-based skill labels (**no fake percentages** — `Skill.tier_label()` returns honest tier text).
- 🌙 **Dark & light themes:** animated toggle, persisted in localStorage, applied before first paint.
- ✉️ **AJAX contact form** (`contact_submit`): stored in DB, shown in admin, optional email notifications.
- 🔍 **SEO built in:** Django sitemap (static/projects/articles × 3 languages), `static/robots.txt`, `static/llms.txt` + `llms-full.txt`.
- ⚙️ **Separate production settings** (`kaman_portfolio/settings_prod.py`): fully env-driven via `.env.example`, fails fast on missing/weak `DJANGO_SECRET_KEY`, HSTS + secure cookies, distinct cookie names (coexists with a second Django site on the same host).

---

## 📥 Installation & Setup

### For visitors

**🌐 [https://mhkaman.com](https://mhkaman.com)** — pick EN / فا / ع from the navbar.

### For developers (local)

```bash
# Clone
git clone https://github.com/Mohammad-Hasan-Kaman/kaman-portfolio.git
cd kaman-portfolio

# Virtual environment (recommended)
python -m venv venv
# Windows: venv\Scripts\activate
# Linux/Mac: source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Database + demo content
python manage.py migrate
python manage.py seed_data        # profile, 9 projects, skills, services, testimonials
python manage.py seed_site_text   # UI strings + marquee tags (idempotent)

# Your own admin account
python manage.py createsuperuser

# Run
python manage.py runserver
```

Open <http://127.0.0.1:8000> (redirects to `/en/`).

> **First run:** create your own admin account with `python manage.py createsuperuser` — never use default credentials in production.

| URL | What |
|-----|------|
| `/en/` · `/fa/` · `/ar/` | The site in each language (FA/AR render RTL) |
| `/en/cv/` | Resume page + per-language PDF download |
| `/en/projects/<slug>/` | Project case-study page |
| `/en/articles/<slug>/` | Article page |
| `/admin/` | Django admin — all content lives here |

### Production (how it runs on the VPS)

```bash
# on the server: copy .env.example -> .env, fill real values
DJANGO_SETTINGS_MODULE=kaman_portfolio.settings_prod gunicorn kaman_portfolio.wsgi
```

`settings_prod.py` enables `ForceEnglishDefaultMiddleware` + `AnalyticsMiddleware`, distinct `kamanportfolio_*` cookie names, `SECURE_SSL_REDIRECT` (nginx terminates TLS), HSTS preload and email notifications for contact messages. `DEBUG` templates/media serving is disabled — nginx serves `staticfiles/` and `media/`.

---

## 🛠 Tech Stack

| Technology | Role |
|------------|------|
| **Django 5** | Web framework (i18n patterns, sitemaps, admin) |
| **Python 3.10+** | Language |
| **SQLite** | Default DB (configurable) |
| **Pillow** | Avatars, project/article covers |
| **fpdf2 + uharfbuzz** | Trilingual CV PDFs (Vazirmatn, RTL shaping) |
| **Zero-dependency `.env` reader** | Env config inside `settings_prod.py` (no extra package) |
| **Vanilla CSS/JS** | Theme variables, RTL-aware responsive layout, typing/reveal/counter/filter animations |
| **gunicorn + nginx** | Production serving (Linux VPS, LE certificate) |

---

## 📝 Demo content

`seed_data` preloads a realistic portfolio in all three languages — 9 projects across 4 categories (`ai`, `web`, `security`, `desktop`), tiered skills, services and testimonials. `seed_site_text` fills admin-editable UI strings and hero marquee tags without overwriting anything you already customized. Run them again anytime; both skip existing data.

---

## 📂 Content management

Everything lives in **Admin →** Profile / Projects / Skills / Services / Testimonials / Experience / Education / CV Languages / Articles / UI Texts / Marquee Tags / Analytics. Every content model carries `_en` / `_fa` / `_ar` fields — empty FA/AR falls back to English via the `tf` template tag. Upload your photo via **Profile → avatar** and a CV file via **Profile → cv file** to unlock the "Download CV" button (or use the built-in generator).

---

## 📝 Project Structure

```
kaman-portfolio/
├── kaman_portfolio/        # settings, prod settings, urls (i18n_patterns), middleware
│   ├── settings.py         # dev settings (DEBUG=True)
│   ├── settings_prod.py    # production: env-driven, HSTS, secure cookies
│   ├── middleware.py       # ForceEnglishDefaultMiddleware
│   └── analytics_mw.py     # AnalyticsMiddleware (pageview/event recorder)
├── portfolio/              # main app
│   ├── models.py           # Profile, Project, Skill, Service, Testimonial,
│   │                       # Experience, Education, CvLanguage, Article,
│   │                       # ContactMessage, SiteText, MarqueeTag, Visit
│   ├── views.py            # home, project/article detail, CV page/download, contact
│   ├── cv_pdf.py           # trilingual CV renderer (SINGLE source: cv_data.py)
│   ├── analytics.py        # salted-hash, bot-filtered event recording
│   ├── sitemaps.py         # static/projects/articles × EN/FA/AR
│   ├── translations.py     # default UI strings (admin SiteText overrides them)
│   ├── context_processors.py  # `t`, `LANG`, `DIR`, `LANGUAGES_LIST`
│   ├── templatetags/portfolio_extras.py  # tf, techs, skill_label, lang_url, …
│   └── management/commands/
│       ├── seed_data.py       # demo profile/projects/skills/services
│       └── seed_site_text.py  # UI strings + marquee tags
├── templates/              # base.html, 404.html, portfolio/*, admin analytics dashboard
├── static/                 # css, js, fonts (Vazirmatn), logo, robots.txt, llms.txt
├── cv_data.py              # THE cv content source (EN/FA/AR)
├── generate_cv.py          # renders media/cv/*.pdf via the site's own engine
├── requirements.txt        # Django, Pillow, fpdf2
└── manage.py
```

> `db.sqlite3`, `media/` and `staticfiles/` are git-ignored — they exist only on the server.

---

## 🤝 Contributing

Found a bug or have an idea? Open an [Issue](https://github.com/Mohammad-Hasan-Kaman/kaman-portfolio/issues). Pull requests are welcome — keep UI strings in `translations.py` trilingual and add admin-editable content as model fields with `_en/_fa/_ar` triplets.

---

## ⭐ Support

If you find this project useful, please give it a **⭐ star**!

[![Stars](https://img.shields.io/github/stars/Mohammad-Hasan-Kaman/kaman-portfolio?style=for-the-badge&logo=github&color=blue)](https://github.com/Mohammad-Hasan-Kaman/kaman-portfolio/stargazers)

---

*Maintained by Mohammad Hasan Kaman · Live at [mhkaman.com](https://mhkaman.com) · Last updated: September 2026*