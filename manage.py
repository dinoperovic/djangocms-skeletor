#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import sys

import dotenv

dotenv.read_dotenv()


if __name__ == '__main__':
    settings = os.getenv('ENVIRONMENT', 'development')
    assert settings in ['staging', 'production', 'development'], \
        "ENVIRONMENT variable must be set to either staging, production or development."

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', '{{ project_name }}.settings')
    os.environ.setdefault('DJANGO_CONFIGURATION', settings.title())

    from configurations.management import execute_from_command_line

    execute_from_command_line(sys.argv)
