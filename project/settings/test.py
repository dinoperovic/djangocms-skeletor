# -*- coding: utf-8 -*-
from .base import *  # noqa
import os


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}


CACHES = {
    'default': {'BACKEND': 'django.core.cache.backends.dummy.DummyCache'},
}


INSTALLED_APPS += ('django_nose', )
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
PROJECT_APPS = [app for app in INSTALLED_APPS
                if os.path.exists(project_path('apps', app))]
if PROJECT_APPS:
    NOSE_ARGS = ['--cover-package=' + ','.join(PROJECT_APPS)]


PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
)
