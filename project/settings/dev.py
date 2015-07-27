# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .base import *  # noqa

import dj_database_url


ALLOWED_HOSTS = ['localhost']

DEBUG = True


# Uses DATABASE_URL evironmental variable to configure the db.
DATABASES = {'default': dj_database_url.config(
    default='sqlite:///%s' % project_path('..', 'dev.db'))}


# Static, media
MEDIA_ROOT = project_path('media')
STATIC_ROOT = project_path('static')


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


CACHES = {
    'default': {'BACKEND': 'django.core.cache.backends.dummy.DummyCache'},
}


# set up django-debug-toolbar if enabled.
if env_setting('USE_DEBUG_TOOLBAR') == 'true':
    MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware', )
    INSTALLED_APPS += ('debug_toolbar', )
    DEBUG_TOOLBAR_CONFIG = {'INTERCEPT_REDIRECTS': False}


# add django-extensions to apps
INSTALLED_APPS += ('django_extensions', )
