# Kaman.dev — Personal Portfolio

A dynamic, trilingual (English / فارسی / العربية) portfolio website for **Mohammad Hasan Kaman**, built with Django 5.

## ✨ Features

- **Fully dynamic** — every piece of content (profile, projects, skills, services, testimonials, messages) is editable from the Django admin at `/admin/`
- **3 languages** — English, Persian and Arabic with automatic **RTL layout** for FA/AR (switcher in the navbar, language-prefixed URLs: `/en/`, `/fa/`, `/ar/`)
- **Dark & Light themes** — animated toggle, saved in localStorage, applied before first paint (no flash)
- **Modern animated design** — floating gradient orbs, glassmorphism cards, bento-style project grid, typing effect, scroll-reveal animations, animated counters, animated skill bars, project category filters, live-project badges
- **Project pages** — case-study pages with tech stack, live demo + source links, and "next project" navigation
- **AJAX contact form** — messages are stored in the database and shown in the admin

## 🚀 Quick start

```bash
cd kaman-portfolio
python manage.py runserver
```

Then open <http://127.0.0.1:8000> (redirects to `/en/`).

| URL | Description |
|---|---|
| `/en/` | English site |
| `/fa/` | Persian site (RTL) |
| `/ar/` | Arabic site (RTL) |
| `/admin/` | Django admin |

> **First run:** create your own admin account with `python manage.py createsuperuser` — never use default credentials in production.

## 📝 Articles (blog)

Add articles from **Admin → Articles**:
- Title / excerpt / full body each in EN / FA / AR (empty FA/AR falls back to English)
- Optional cover image and an emoji icon for the card
- **Published** checkbox controls visibility; separate paragraphs with a blank line
- Articles appear in the "Articles" section on the home page and get their own page at `/en/articles/<slug>/`

## 🔒 Confidential projects (private / client work)

Removed — use the Articles section instead for write-ups that cannot include source code.

## 🛠 Management commands

```bash
python manage.py seed_data      # preload profile, 9 projects, skills, services, testimonials (skips existing data)
python manage.py createsuperuser
```

## 📁 Structure

```
kaman-portfolio/
├── kaman_portfolio/        # project settings & urls (i18n_patterns)
├── portfolio/              # main app
│   ├── models.py           # Profile, Project, Skill, Service, Testimonial, ContactMessage (trilingual fields)
│   ├── translations.py     # UI strings for EN/FA/AR
│   ├── context_processors.py
│   ├── templatetags/portfolio_extras.py   # tf (trilingual lookup), lang_url, techs
│   ├── management/commands/seed_data.py
│   └── admin.py            # rich admin with trilingual fieldsets
├── templates/              # base.html, portfolio/home.html, portfolio/project_detail.html
├── static/css/style.css    # theme variables (dark/light), RTL-aware, responsive
├── static/js/main.js       # typing, reveals, counters, filters, AJAX form
└── media/                  # uploads (avatar, project images, CV)
```

## 🌐 Content editing

Everything lives in **Admin →** Profile / Projects / Skills / Services / Testimonials. Each has `_en`, `_fa`, `_ar` fields — if a translation is empty, the English text is shown as fallback. Add your real photo via **Profile → avatar** and your CV via **Profile → cv file** to unlock the "Download CV" button.

## 🔒 Production notes

- Set a real `SECRET_KEY` and `DEBUG = False` in `kaman_portfolio/settings.py`
- Set `ALLOWED_HOSTS` to your domain
- Run `python manage.py collectstatic` and serve via nginx + gunicorn
