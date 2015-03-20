# -*- coding: utf-8 -*-
"""
WSGI config for project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import sys
import os
from os.path import dirname, abspath, realpath

# Add working directory to system path.
sys.path.append(abspath(dirname(dirname(realpath(__file__)))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
