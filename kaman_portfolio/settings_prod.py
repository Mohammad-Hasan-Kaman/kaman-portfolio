"""
Production settings for the kaman-portfolio deployment.

Local development keeps using kaman_portfolio/settings.py (DEBUG=True).
On the VPS run with:  DJANGO_SETTINGS_MODULE=kaman_portfolio.settings_prod
or pass --settings explicitly to gunicorn/wsgi.

Everything environment-driven: copy .env.example to .env on the server and
fill in real values. Fails fast if a required secret is missing.
"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


def env(name: str, default: str = '') -> str:
    value = os.environ.get(name, default)
    # support .env-style fallback file next to manage.py (no extra deps)
    if value == '' and not name.startswith('.'):
        env_file = BASE_DIR / '.env'
        if env_file.exists():
            for line in env_file.read_text(encoding='utf-8').splitlines():
                line = line.strip()
                if line.startswith(f'{name}='):
                    return line.split('=', 1)[1].strip().strip('"\'')
    return value


SECRET_KEY = env('DJANGO_SECRET_KEY')
if not SECRET_KEY or len(SECRET_KEY) < 50 or 'insecure' in SECRET_KEY:
    raise RuntimeError(
        'DJANGO_SECRET_KEY missing/weak — generate one with: '
        'python -c "import secrets; print(secrets.token_urlsafe(64))"')

DEBUG = env('DJANGO_DEBUG', 'False').lower() in ('1', 'true', 'yes')

ALLOWED_HOSTS = [h.strip() for h in env(
    'DJANGO_ALLOWED_HOSTS', 'mhkaman.com,www.mhkaman.com').split(',') if h.strip()]

CSRF_TRUSTED_ORIGINS = [o.strip() for o in env(
    'DJANGO_CSRF_TRUSTED_ORIGINS', 'https://mhkaman.com,https://www.mhkaman.com').split(',') if o.strip()]

# Distinct cookie names (two Django sites share 127.0.0.1 locally; on the
# VPS they share the domain with drkaman — unique names prevent collisions).
SESSION_COOKIE_NAME = 'kamanportfolio_sessionid'
CSRF_COOKIE_NAME = 'kamanportfolio_csrftoken'
LANGUAGE_COOKIE_NAME = 'kamanportfolio_language'

# HTTPS-only cookies + HSTS (nginx terminates TLS on the VPS)
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
# default True; when no cert yet, .env sets DJANGO_SSL_REDIRECT=False temporarily
SECURE_SSL_REDIRECT = env('DJANGO_SSL_REDIRECT', 'True').lower() in ('1', 'true', 'yes')
# Trust nginx's proto header so requests through the reverse proxy are seen as https
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_HSTS_SECONDS = int(env('DJANGO_HSTS_SECONDS', '31536000'))
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_REFERRER_POLICY = 'same-origin'
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'portfolio',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'kaman_portfolio.middleware.ForceEnglishDefaultMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'kaman_portfolio.analytics_mw.AnalyticsMiddleware',
]

ROOT_URLCONF = 'kaman_portfolio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'portfolio.context_processors.site_context',
            ],
        },
    },
]

WSGI_APPLICATION = 'kaman_portfolio.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / env('DJANGO_DB_NAME', 'db.sqlite3'),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en'
TIME_ZONE = 'Europe/Berlin'
USE_I18N = True
USE_TZ = True

from django.utils.translation import gettext_lazy as _  # noqa: E402

LANGUAGES = [
    ('en', _('English')),
    ('fa', _('Persian')),
    ('ar', _('Arabic')),
]

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# --- Contact-form email notifications (optional but recommended) ---
# Set these on the server to receive visitor messages by email as well;
# they are always stored in the admin regardless.
DEFAULT_FROM_EMAIL = env('DJANGO_DEFAULT_FROM_EMAIL', 'portfolio@mhkaman.com')
EMAIL_HOST = env('DJANGO_EMAIL_HOST', '')
EMAIL_PORT = int(env('DJANGO_EMAIL_PORT', '587'))
EMAIL_HOST_USER = env('DJANGO_EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = env('DJANGO_EMAIL_HOST_PASSWORD', '')
EMAIL_USE_TLS = env('DJANGO_EMAIL_USE_TLS', 'True').lower() in ('1', 'true', 'yes')
# Notify this address about new contact messages:
SERVER_EMAIL = env('DJANGO_SERVER_EMAIL', DEFAULT_FROM_EMAIL)
ADMINS = [(env('DJANGO_ADMIN_NAME', 'Mohammad Hasan'), env('DJANGO_ADMIN_EMAIL', ''))] \
    if env('DJANGO_ADMIN_EMAIL', '') else []
