from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path
from django.views.generic import RedirectView
from django.views.i18n import set_language

from portfolio.sitemaps import sitemaps

urlpatterns = [
    path('i18n/setlang/', set_language, name='set_language'),
    path('admin/', admin.site.urls),
    path('favicon.ico', RedirectView.as_view(url='/static/img/logo.svg', permanent=False)),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', RedirectView.as_view(url='/static/robots.txt', permanent=True)),
    path('llms.txt', RedirectView.as_view(url='/static/llms.txt', permanent=True)),
    path('llms-full.txt', RedirectView.as_view(url='/static/llms-full.txt', permanent=True)),
]

urlpatterns += i18n_patterns(
    path('', include('portfolio.urls')),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
