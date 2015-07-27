#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import sys


if __name__ == '__main__':
    if not os.path.exists(os.path.join('project', 'settings', 'local.py')):
        sys.exit('You must configure your local settings in a '
                 '"project/settings/local.py" file.')

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings.local')

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
