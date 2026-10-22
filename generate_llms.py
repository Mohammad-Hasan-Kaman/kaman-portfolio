"""Generate static/llms-full.txt from the live database content.

The file is a machine-readable, plain-text mirror of the site's public
content, used by crawlers and LLM indexers. It is generated from the same
Django models the templates render, so it can never drift from the site.

Run:  python manage.py seed_data && python generate_llms.py
"""
import os
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kaman_portfolio.settings")

import django  # noqa: E402

django.setup()

from portfolio.models import (Article, CvLanguage, Education, Experience,  # noqa: E402
                               MarqueeTag, Profile, Project, Service, Skill,
                               Testimonial)
from portfolio.views import MARQUEE_TAGS  # noqa: E402

SITE = "https://mhkaman.com"


def _tags():
    tags = list(MarqueeTag.objects.values_list("label", flat=True))
    return tags or MARQUEE_TAGS


def build() -> str:
    p = Profile.objects.first()
    out = []
    add = out.append

    add("# mhkaman.com — Full Content for LLMs")
    add("")
    add("> This is the machine-readable full-content version of https://mhkaman.com")
    add("> (see llms.txt for the index). Content below is generated from the live")
    add("> database that renders the site. Persian and Arabic versions exist at")
    add("> /fa/ and /ar/ with identical structure.")
    add("")

    # ------------------------------------------------------------------ home
    add(f"# PAGE: Home ({SITE}/en/)")
    add("")
    add(f"{p.name_en} — {p.role_en}")
    add(f"📍 Based in {p.location_en} · 📧 {p.email}")
    add("")
    add(p.about_en)
    add("")
    add(p.tagline_en)
    add("")
    add(f"{p.years_experience}+ Years Building Software · "
        f"{p.projects_completed} Projects Delivered · "
        f"{Project.objects.exclude(repo_url='').count()} Open-Source Repos")
    add("")
    add("## Tech tag marquee")
    add("")
    add(", ".join(_tags()))
    add("")
    add("## Skills")
    add("")
    for s in Skill.objects.all():
        add(f"{s.icon} {s.name}")
    add("")
    add("## Featured projects")
    add("")
    for pr in Project.objects.filter(featured=True):
        add(f"{pr.icon} {pr.title_en}")
        add(pr.description_en)
        add(pr.tech_stack)
        add(f"Case study: {SITE}/en/projects/{pr.slug}/")
        if pr.repo_url:
            add(f"Source code: {pr.repo_url}")
        if pr.live_url:
            add(f"Live: {pr.live_url}")
        add("")
    add("## More projects")
    add("")
    for pr in Project.objects.filter(featured=False):
        add(f"{pr.icon} {pr.title_en}")
        add(pr.description_en)
        add(pr.tech_stack)
        add(f"Case study: {SITE}/en/projects/{pr.slug}/")
        if pr.repo_url:
            add(f"Source code: {pr.repo_url}")
        if pr.live_url:
            add(f"Live: {pr.live_url}")
        add("")
    add("## Articles")
    add("")
    for a in Article.objects.filter(published=True):
        add(f"{a.icon} {a.title_en}")
        add(a.excerpt_en)
        add(f"Read: {SITE}/en/articles/{a.slug}/")
        add("")
    add("## Services")
    add("")
    for s in Service.objects.all():
        add(f"{s.icon} {s.title_en}")
        add(s.description_en)
        add("")
    add("## Testimonials")
    add("")
    for t in Testimonial.objects.all():
        add(f"“{t.text_en}”")
        add(f"— {t.name}, {t.role_en}")
        add("")
    add("## Contact")
    add("")
    add(f"📧 Email: {p.email}")
    add(f"✈️ Telegram: {p.telegram.rsplit('/', 1)[-1]}")
    add(f"💼 LinkedIn: {p.linkedin}")
    add(f"🐙 GitHub: {p.github.rsplit('/', 1)[-1]}")
    add(f"🌐 Website: {SITE}")
    add("")

    # -------------------------------------------------------------------- cv
    add(f"# PAGE: CV ({SITE}/en/cv/)")
    add("")
    add(f"{p.name_en} — {p.role_en}")
    add(f"📍 Based in {p.location_en} · 📧 {p.email}")
    if p.cv_file:
        add("⬇ Download CV (PDF): " + f"{SITE}{p.cv_file.url}")
    add("")
    add("## Summary")
    add("")
    add(p.summary_en)
    add("")
    add("## Core Competencies")
    add("")
    add(p.core_competencies_en)
    add("")
    add("## Professional Projects")
    add("")
    for e in Experience.objects.all():
        add(f"{e.title_en} — {e.period_en} — {e.org_en}")
        add(e.description_en)
        add("")
    add("## Selected Projects")
    add("")
    for pr in Project.objects.all():
        add(f"{pr.icon} {pr.title_en} — {pr.tech_stack}")
        add("")
    add("## Education")
    add("")
    for e in Education.objects.all():
        add(f"{e.degree_en} — {e.period_en}")
        add(e.details_en)
        add("")
    add("## Languages")
    add("")
    for l in CvLanguage.objects.all():
        add(f"{l.name_en} — {l.level_en}")
    add("")
    add("## Contact Information")
    add("")
    add(f"📧 Email: {p.email}")
    add(f"✈️ Telegram: {p.telegram.rsplit('/', 1)[-1]}")
    add(f"💼 LinkedIn: {p.linkedin.rstrip('/').rsplit('/', 1)[-1]}")
    add(f"🐙 GitHub: {p.github.rsplit('/', 1)[-1]}")
    add(f"✖️ X (Twitter): {p.twitter.rsplit('/', 1)[-1]}")
    add("")
    add("---")
    add("")
    add("Last updated: 2026-10-22. Owner: Mohammad Hasan Kaman "
        "(mohammadhasankaman@gmail.com).")
    return "\n".join(out) + "\n"


if __name__ == "__main__":
    target = os.path.join(BASE, "static", "llms-full.txt")
    with open(target, "w", encoding="utf-8") as f:
        f.write(build())
    print("written:", target, os.path.getsize(target), "bytes")
