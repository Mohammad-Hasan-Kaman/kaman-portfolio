from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def tf(context, obj, field):
    """Trilingual field lookup: returns the current language's field, falling back to English."""
    lang = context.get('LANG', 'en')
    val = getattr(obj, f'{field}_{lang}', '') or getattr(obj, f'{field}_en', '') or ''
    return val


@register.filter
def techs(value):
    """Split a comma-separated tech stack string into a list."""
    return [t.strip() for t in (value or '').split(',') if t.strip()]


@register.filter
def split_lines(value):
    """Split a multiline string into a list of non-empty lines."""
    return [l for l in (value or '').splitlines() if l.strip()]


@register.simple_tag
def category_name(value, t):
    return t['projects'].get(value, value)


@register.simple_tag(takes_context=True)
def skill_label(context, skill):
    """Honest skill level label (tier-based, no percentages)."""
    return skill.tier_label(context.get('LANG', 'en'))


@register.simple_tag(takes_context=True)
def lang_url(context, lang_code):
    """URL of the current path in the given language."""
    from django.urls import translate_url
    request = context['request']
    return translate_url(request.get_full_path(), lang_code)


@register.simple_tag(takes_context=True)
def abs_lang_url(context, lang_code):
    """Absolute URL of the current path in the given language (no query string)."""
    from django.conf import settings
    from django.urls import translate_url
    request = context['request']
    path = translate_url(request.path, lang_code)
    return f'https://{settings.SITE_DOMAIN}{path}'


@register.simple_tag
def total_visits():
    from .models import Visit
    return Visit.objects.count()


@register.simple_tag
def unique_visitors():
    from .models import Visit
    return Visit.objects.values('session_key').distinct().count()


@register.simple_tag
def today_visits():
    from django.utils import timezone
    from .models import Visit
    return Visit.objects.filter(created_at__gte=timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)).count()

def _gregorian_to_jalali(gy, gm, gd):
    g_d_m = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    if gy > 1600:
        jy = 979
        gy -= 1600
    else:
        jy = 0
        gy -= 621
    gy2 = gy + 1 if gm > 2 else gy
    days = (365 * gy) + ((gy2 + 3) // 4) - ((gy2 + 99) // 100) \
        + ((gy2 + 399) // 400) - 80 + gd + g_d_m[gm - 1]
    jy += 33 * (days // 12053)
    days %= 12053
    jy += 4 * (days // 1461)
    days %= 1461
    if days > 365:
        jy += (days - 1) // 365
        days = (days - 1) % 365
    if days < 186:
        jm = 1 + days // 31
        jd = 1 + days % 31
    else:
        jm = 7 + (days - 186) // 30
        jd = 1 + (days - 186) % 30
    return jy, jm, jd


@register.filter
def jalali(value):
    """Format a date/datetime as Jalali YYYY/MM/DD (Persian site dates)."""
    if not value:
        return ''
    jy, jm, jd = _gregorian_to_jalali(value.year, value.month, value.day)
    return f"{jy:04d}/{jm:02d}/{jd:02d}"

