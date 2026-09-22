"""Lightweight server-side analytics — no third-party services, no raw IPs."""
import hashlib
import re
import secrets

from django.conf import settings

from .models import Visit

# Bot user-agents: recorded pages stay human-traffic (Googlebot etc. skipped)
_BOT_RE = re.compile(
    r'bot|crawler|spider|crawling|slurp|bingpreview|facebookexternalhit|'
    r'whatsapp|telegrambot|twitterbot|linkedinbot|embedly|quora|headless|'
    r'python-requests|curl|wget|axios|postman|uptime|pingdom|gtmetrix', re.I)

_TABLET_RE = re.compile(r'ipad|tablet|kindle|silk', re.I)
_MOBILE_RE = re.compile(r'mobile|iphone|android(?!.*tablet)|iemobile|opera mini', re.I)

_REFERRERS = {
    'google.': 'Google',
    'bing.': 'Bing',
    'duckduckgo.': 'DuckDuckGo',
    'yahoo.': 'Yahoo',
    'linkedin.': 'LinkedIn',
    'github.': 'GitHub',
    't.me': 'Telegram',
    'telegram.': 'Telegram',
    'twitter.': 'X (Twitter)',
    'x.com': 'X (Twitter)',
    'facebook.': 'Facebook',
    'instagram.': 'Instagram',
    'reddit.': 'Reddit',
    'bale.ai': 'Bale',
}


def _referral(source):
    if not source:
        return 'Direct'
    low = source.lower()
    for needle, name in _REFERRERS.items():
        if needle in low:
            return name
    return source[:120]


def _device(ua):
    if _TABLET_RE.search(ua):
        return 'tablet'
    if _MOBILE_RE.search(ua):
        return 'mobile'
    return 'desktop'


def _ip_hash(ip):
    if not ip:
        return ''
    salt = getattr(settings, 'ANALYTICS_SALT', settings.SECRET_KEY)
    return hashlib.sha256(f'{salt}:{ip}'.encode()).hexdigest()[:16]


def _is_bot(user_agent, path):
    if _BOT_RE.search(user_agent or ''):
        return True
    # sitemap/robots/RSS-ish fetches are machines by definition
    return path.startswith('/sitemap') or path == '/robots.txt'


def _session_key(request, response=None):
    """Anonymous per-visitor id in a cookie (no personal data)."""
    key = request.COOKIES.get('kp_vis')
    if key:
        return key, False  # existing
    key = secrets.token_urlsafe(24)[:40]
    if response is not None:
        response.set_cookie('kp_vis', key, max_age=180 * 24 * 3600,
                            samesite='Lax', httponly=True,
                            secure=request.is_secure())
    return key, True  # first visit


def record(request, response, event='pageview', path=''):
    """Attach analytics row + visitor cookie to an outgoing response."""
    ua = (request.META.get('HTTP_USER_AGENT') or '')[:300]
    path = (path or request.path)[:300]
    if _is_bot(ua, path):
        return response
    key, first = _session_key(request, response)
    try:
        Visit.objects.create(
            event=event,
            path=path,
            lang=getattr(request, 'LANGUAGE_CODE', '') or 'en',
            referrer=_referral(request.META.get('HTTP_REFERER', '')),
            device=_device(ua),
            user_agent=ua,
            ip_hash=_ip_hash(request.META.get('HTTP_X_FORWARDED_FOR', '').split(',')[0].strip()
                             or request.META.get('REMOTE_ADDR', '')),
            session_key=key,
        )
    except Exception:
        pass  # analytics must never break the site
    return response


def is_bot(request):
    """Public helper for views that record their own events."""
    return _is_bot(request.META.get('HTTP_USER_AGENT') or '', request.path)
