# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os

import dotenv
from configurations.wsgi import get_wsgi_application

try:
    dotenv.read_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))
except Exception as e:
    print(e)


settings = os.getenv('ENVIRONMENT', 'development')
assert settings in ['staging', 'production', 'development'], \
    "ENVIRONMENT variable must be set to either staging, production or development."

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
os.environ.setdefault('DJANGO_CONFIGURATION', settings.title())

application = get_wsgi_application()
