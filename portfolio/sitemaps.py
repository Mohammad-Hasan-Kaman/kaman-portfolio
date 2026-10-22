from django.conf import settings
from django.contrib.sitemaps import Sitemap

from .models import Article, Project

LANGS = [code for code, _ in settings.LANGUAGES]
DEFAULT_LANG = settings.LANGUAGE_CODE if settings.LANGUAGE_CODE in LANGS else LANGS[0]
SITE_DOMAIN = getattr(settings, 'SITE_DOMAIN', 'mhkaman.com')


class _BaseSitemap(Sitemap):
    """One entry per language, with hreflang alternates for every URL.

    The domain is taken from the incoming request (nginx forwards the real
    Host header) and falls back to ``settings.SITE_DOMAIN`` so the sitemap
    never advertises an IP or a local port.
    """

    protocol = 'https'
    priority = 0.8
    changefreq = 'weekly'

    def location(self, obj):
        raise NotImplementedError

    def items(self):
        # each item is (lang, obj-or-None)
        return [(lang, None) for lang in LANGS]

    def _domain(self, site):
        """Always advertise the public domain.

        ``site.domain`` is the raw request host (or ``testserver`` in tests),
        which would leak local hosts into the sitemap, so the configured
        ``SITE_DOMAIN`` is the single source of truth.
        """
        return SITE_DOMAIN

    def get_urls(self, page=1, site=None, protocol=None):
        protocol = protocol or self.get_protocol()
        domain = self._domain(site)
        urls = []
        for lang, obj in self.items():
            path = self.location(obj)
            alternates = [
                {'location': f'{protocol}://{domain}/{alt}{path}', 'lang_code': alt}
                for alt in LANGS
            ]
            alternates.append({
                'location': f'{protocol}://{domain}/{DEFAULT_LANG}{path}',
                'lang_code': 'x-default',
            })
            urls.append({
                'location': f'{protocol}://{domain}/{lang}{path}',
                'lastmod': getattr(obj, 'updated', None),
                'priority': str(self.priority),
                'changefreq': self.changefreq,
                'alternates': alternates,
            })
        return urls


class StaticSitemap(_BaseSitemap):
    def location(self, obj):
        return '/'


class ProjectSitemap(_BaseSitemap):
    def items(self):
        return [(lang, p) for lang in LANGS for p in Project.objects.all()]

    def location(self, obj):
        return f'/projects/{obj.slug}/'


class ArticleSitemap(_BaseSitemap):
    def items(self):
        return [(lang, a) for lang in LANGS for a in Article.objects.filter(published=True)]

    def location(self, obj):
        return f'/articles/{obj.slug}/'


class CvSitemap(_BaseSitemap):
    """The CV pages, in every language."""

    priority = 0.6

    def location(self, obj):
        return '/cv/'


sitemaps = {
    'static': StaticSitemap,
    'projects': ProjectSitemap,
    'articles': ArticleSitemap,
    'cv': CvSitemap,
}
