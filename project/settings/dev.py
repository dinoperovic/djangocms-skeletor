# -*- coding: utf-8 -*-
from .base import *  # noqa
import os
import dj_database_url


DEBUG = True
TEMPLATE_DEBUG = DEBUG

MEDIA_ROOT = project_path('media')
STATIC_ROOT = project_path('static')

DATABASES = {'default': dj_database_url.config(
    default='sqlite:///{}'.format(project_path('..', 'dev.db')))}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

CACHES = {
    'default': {'BACKEND': 'django.core.cache.backends.dummy.DummyCache'},
}

# set up Django Debug Toolbar if installed.
if os.environ.get('USE_DEBUG_TOOLBAR', 'true') == 'true':
    try:
        import debug_toolbar  # noqa
        MIDDLEWARE_CLASSES += (
            'debug_toolbar.middleware.DebugToolbarMiddleware',
        )
        INSTALLED_APPS += (
            'debug_toolbar',
        )
        DEBUG_TOOLBAR_CONFIG = {
            'INTERCEPT_REDIRECTS': False,
        }
    except ImportError:
        pass


# Set up django-extensions if installed
try:
    import django_extensions  # noqa
    INSTALLED_APPS += ('django_extensions',)
except ImportError:
    pass
