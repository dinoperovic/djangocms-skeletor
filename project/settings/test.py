# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .base import *  # noqa

import os


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}


# Static, media
MEDIA_ROOT = project_path('media')
STATIC_ROOT = project_path('static')


CACHES = {
    'default': {'BACKEND': 'django.core.cache.backends.dummy.DummyCache'},
}


# Setup django-nose as test runner
INSTALLED_APPS += ('django_nose', )
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
PROJECT_APPS = [app for app in INSTALLED_APPS
                if os.path.exists(project_path('apps', app))]
if PROJECT_APPS:
    NOSE_ARGS = ['--cover-package=' + ','.join(PROJECT_APPS)]


PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
)
