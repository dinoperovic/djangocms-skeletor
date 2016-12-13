#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import sys

import dotenv

dotenv.read_dotenv()


if __name__ == '__main__':
    ENVIRONMENT = os.getenv('ENVIRONMENT')

    if ENVIRONMENT == 'STAGING':
        settings = 'staging'
    elif ENVIRONMENT == 'PRODUCTION':
        settings = 'production'
    else:
        settings = 'development'

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
    os.environ.setdefault('DJANGO_CONFIGURATION', settings.title())

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
