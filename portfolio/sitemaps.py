from django.conf import settings
from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .models import Article, Project

LANGS = [code for code, _ in settings.LANGUAGES]


class _BaseSitemap(Sitemap):
    protocol = 'https'

    def location(self, obj):
        raise NotImplementedError

    def items(self):
        # each item is (lang, obj-or-None)
        items = []
        for lang in LANGS:
            items.append((lang, None))
        return items

    def _url(self, loc, priority=0.5, changefreq='weekly'):
        return {'location': loc, 'priority': priority, 'changefreq': changefreq}

    def get_urls(self, page=1, site=None, protocol=None):
        urls = []
        for lang, obj in self.items():
            loc = f'https://mhkaman.com/{lang}{self.location(obj)}'
            urls.append({'location': loc, 'lastmod': getattr(obj, 'updated', None),
                         'priority': 0.8, 'changefreq': 'weekly'})
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


sitemaps = {
    'static': StaticSitemap,
    'projects': ProjectSitemap,
    'articles': ArticleSitemap,
}
