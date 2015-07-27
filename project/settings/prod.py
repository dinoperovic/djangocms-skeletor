# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .base import *  # noqa

import os

import dj_database_url


def home_path(*args):
    return os.path.join(os.path.expanduser('~'), *args)


ALLOWED_HOSTS = []

DEBUG = False


# Static, media
MEDIA_ROOT = home_path('public_html', 'media')
STATIC_ROOT = home_path('public_html', 'static')


# Uses DATABASE_URL evironmental variable if set, falls back to default.
DATABASES = {'default': dj_database_url.config(
    default='mysql://<user>:<password>@<host>:<port>/<name>')}


CACHES = {
    'default': {'BACKEND': 'django.core.cache.backends.locmem.LocMemCache'},
}
