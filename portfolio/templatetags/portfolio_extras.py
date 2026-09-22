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
