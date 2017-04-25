# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from cms.sitemaps import CMSSitemap
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

sitemaps = {
    'cmspages': CMSSitemap,
}

urlpatterns = [
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}),
]


# Handle static & media files in dev.
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# Add django-debug-toolbar urls.
if getattr(settings, 'DEBUG_TOOLBAR', False):
    import debug_toolbar
    urlpatterns += [url(r'^__debug__/', include(debug_toolbar.urls))]


urlpatterns += i18n_patterns(
    url(r'^admin/', include(admin.site.urls)),
    url(r'^translate/', include('rosetta.urls')),
    url(r'^', include('cms.urls')),
    prefix_default_language=False,
)
