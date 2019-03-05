# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from cms.sitemaps import CMSSitemap
from django.conf import settings
from django.urls import include, path
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

sitemaps = {
    'cmspages': CMSSitemap,
}

urlpatterns = [
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
]


# Handle static & media files in dev.
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# Add django-debug-toolbar urls.
if getattr(settings, 'DEBUG_TOOLBAR', False):
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]


urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('translate/', include('rosetta.urls')),
    path('', include('cms.urls')),
    prefix_default_language=False,
)
