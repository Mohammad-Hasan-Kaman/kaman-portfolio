# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- `hreflang` alternates for English, Persian and Arabic on every page, plus an
  `x-default` link pointing at the English version.
- The CV pages (`/en/cv/`, `/fa/cv/`, `/ar/cv/`) are now listed in
  `sitemap.xml`, and every sitemap entry carries its own language alternates.

### Changed

- The CV was regenerated from `cv_data.py` with the real release tag of every
  public project, the verified stack (Edge WebView2, CustomTkinter, yt-dlp,
  FastAPI, django-allauth, Jalali calendar, SQLite, nginx/gunicorn) and the
  verified test counts (365 offline checks in the translator, 12 named checks
  in the streaming diagnostics toolkit).
- The testimonial section is now titled "Feedback & Collaborators" in all
  three languages: the two cards are feedback from people the author worked
  with, not client endorsements.

### Fixed

- The de-AI restyle (2026-11-16) is recorded here: a single solid accent,
  solid card surfaces, and the removal of gradients, orbs and emoji icons.
  Follow-up fixes from the heavy test and the 2026-11-17 repository audit:
  home project cards show their localized descriptions, light-theme form
  messages are readable, the empty Desktop filter is gone, the CV
  competency bullets align inside their card, article pages declare their
  `markdown` dependency, and the 404 page shows the site branding again.
- Content facts restored: the translator ships 365 offline tests at
  v3.2.3, Agent Stream Doctor is v0.2.2, and the AI Counseling Widget
  is v2.0.0.

### Removed

- Unverifiable claims from the CV: "Bootstrap" and the IDE list
  ("VS Code, PyCharm, Visual Studio").

## [1.0.0] - 2026-09-22

### Added

- First public release of the trilingual Django portfolio running live at
  [mhkaman.com](https://mhkaman.com).
- Three languages — English, Persian and Arabic — with automatic RTL layout and
  language-prefixed URLs (`/en/`, `/fa/`, `/ar/`).
- Fully dynamic content: profile, projects, skills, services, testimonials,
  articles and UI texts are all editable from the admin.
- An educational blog and an admin analytics view.
