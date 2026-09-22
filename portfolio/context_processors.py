from .translations import STRINGS
from .models import SiteText


def site_context(request):
    lang = request.LANGUAGE_CODE if request.LANGUAGE_CODE in STRINGS else 'en'
    base = dict(STRINGS[lang])

    # Apply admin-edited UI texts (one query, cached per request set)
    overrides = {
        s.key: getattr(s, f'value_{lang}', '') or s.value_en
        for s in SiteText.objects.all()
    }
    for key, value in overrides.items():
        parts = key.split('.')
        node = base
        for p in parts[:-1]:
            if not isinstance(node.get(p), dict):
                node[p] = {}
            node = node[p]
        node[parts[-1]] = value

    return {
        't': base,
        'LANG': lang,
        'DIR': STRINGS[lang]['dir'],
        'LANGUAGES_LIST': [
            {'code': 'en', 'label': 'EN', 'name': 'English'},
            {'code': 'fa', 'label': 'فا', 'name': 'فارسی'},
            {'code': 'ar', 'label': 'ع', 'name': 'العربية'},
        ],
    }
