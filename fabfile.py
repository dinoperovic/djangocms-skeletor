# -*- coding: utf-8 -*-
from __future__ import unicode_literals, with_statement

import os
from contextlib import contextmanager

from fabric.api import cd, env, prefix, run, task

env.project_path = '/path/to/webapps/{{ project_name }}'
env.virtualenv = '/path/to/virtualenvs/{{ project_name }}'
env.hosts = []


@task
def staging():
    env.hosts = ['user@staging-server']
    env.environment = 'staging'


@task
def production():
    env.hosts = ['user@production-server']
    env.environment = 'production'


@contextmanager
def virtualenv():
    with prefix('source {0}'.format(os.path.join(env.virtualenv, 'bin/activate'))):
        yield


@task
def deploy():
    """Deploy project via git"""
    with cd(env.project_path):
        with virtualenv():
            run('git pull')
            run('pip install -r requirements/production.txt')
            run('python manage.py migrate')
            run('python manage.py collectstatic --noinput')
            run('touch {{ project_name }}/wsgi.py')
