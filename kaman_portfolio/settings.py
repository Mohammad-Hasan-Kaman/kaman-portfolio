"""
Django settings for kaman_portfolio project.
Portfolio of Mohammad Hasan Kaman — multilingual (EN/FA/AR), light/dark themes.
"""
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-kaman-portfolio-change-me-in-production-9f2k7x'

# Distinct cookie names: another Django project (drkaman) also runs on
# 127.0.0.1 and cookies are shared across ports. Without unique names the
# two sites overwrite each other's csrftoken/sessionid and contact-form
# POSTs fail with "CSRF token from POST incorrect" (403).
SESSION_COOKIE_NAME = 'kamanportfolio_sessionid'
CSRF_COOKIE_NAME = 'kamanportfolio_csrftoken'
LANGUAGE_COOKIE_NAME = 'kamanportfolio_language'
DEBUG = True
ALLOWED_HOSTS = ['mhkaman.com', 'www.mhkaman.com', 'localhost', '127.0.0.1', 'testserver']

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
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
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
        'NAME': BASE_DIR / 'db.sqlite3',
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

from django.utils.translation import gettext_lazy as _

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
