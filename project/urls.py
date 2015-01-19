# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sites.models import Site
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.utils.html import mark_safe
from django.utils.translation import ugettext_lazy as _

try:
    from solid_i18n.urls import solid_i18n_patterns as i18n_patterns
except ImportError:
    from django.conf.urls.i18n import i18n_patterns


# Set admin site header.
site = Site.objects.get_current()
admin.site.site_header = _('%s administration' % site.name)


urlpatterns = patterns(
    '',
    url(r'^jsi18n/(?P<packages>\S+?)/$',
        'django.views.i18n.javascript_catalog'),
)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += i18n_patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^translate/', include('rosetta.urls')),
    url(r'^', include('cms.urls')),
)
