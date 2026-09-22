"""Seed SiteText rows (UI strings) and MarqueeTag rows from code defaults.

Run:  python manage.py seed_site_text
Idempotent: creates missing rows, fills empty translations,
never overwrites values that were already edited in the admin.
"""
from django.core.management.base import BaseCommand

from portfolio.models import MarqueeTag, SiteText
from portfolio.translations import STRINGS
from portfolio.views import MARQUEE_TAGS

LABELS = {
    'nav': 'Top menu links',
    'hero': 'Homepage hero section',
    'about': 'About section',
    'skills': 'Skills section',
    'projects': 'Projects section',
    'articles': 'Articles section',
    'services': 'Services section',
    'testimonials': 'Testimonials section',
    'contact': 'Contact section & form',
    'footer': 'Page footer',
    'stats': 'Hero stat labels',
    'misc': 'Miscellaneous (theme, language, scroll hint)',
    'cv': 'Resume page',
}


def flatten(prefix, node, out):
    for key, val in node.items():
        dotted = f'{prefix}.{key}' if prefix else key
        if isinstance(val, dict):
            flatten(dotted, val, out)
        elif isinstance(val, str):
            out[dotted] = val


class Command(BaseCommand):
    help = 'Create SiteText/MarqueeTag rows from code defaults (no overwrites).'

    def handle(self, *args, **options):
        flats = {}
        for lang in ('en', 'fa', 'ar'):
            flat = {}
            flatten('', STRINGS[lang], flat)
            flats[lang] = flat

        all_keys = sorted(set().union(*[set(f) for f in flats.values()]))
        created = 0
        filled = 0
        for key in all_keys:
            label = LABELS.get(key.split('.')[0], key.split('.')[0])
            obj, was_created = SiteText.objects.get_or_create(
                key=key,
                defaults={
                    'value_en': flats['en'].get(key, ''),
                    'value_fa': flats['fa'].get(key, ''),
                    'value_ar': flats['ar'].get(key, ''),
                    'label': label,
                },
            )
            if was_created:
                created += 1
                continue
            # fill translations that were missing, keep admin edits intact
            changed = False
            for lang in ('en', 'fa', 'ar'):
                if not getattr(obj, f'value_{lang}') and flats[lang].get(key):
                    setattr(obj, f'value_{lang}', flats[lang][key])
                    changed = True
            if changed:
                obj.save()
                filled += 1

        tag_created = 0
        for i, tag in enumerate(MARQUEE_TAGS):
            _, was_created = MarqueeTag.objects.get_or_create(
                label=tag, defaults={'order': i})
            if was_created:
                tag_created += 1

        self.stdout.write(self.style.SUCCESS(
            f'SiteText created: {created}, translations filled: {filled} '
            f'(total {SiteText.objects.count()}), '
            f'MarqueeTag created: {tag_created} (total {MarqueeTag.objects.count()})'))
