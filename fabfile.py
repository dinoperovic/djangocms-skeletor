# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from invoke import task


@task
def info(c):
    """
    Read Fabric docs on "http://www.fabfile.org/".
    """
    print('Read Fabric docs on "http://www.fabfile.org/".')
