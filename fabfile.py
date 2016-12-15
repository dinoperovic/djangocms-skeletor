# -*- coding: utf-8 -*-
from __future__ import unicode_literals, with_statement

import os
from contextlib import contextmanager

from fabric.api import cd, env, prefix, run, task

env.project_path = '~/webapps/{{ project_name }}'
env.virtualenv = '~/virtualenvs/{{ project_name }}'
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


def restart():
    with cd(env.project_path):
        run('touch {{ project_name }}/wsgi.py')


@task
def deploy():
    """Deploy project via git"""
    with cd(env.project_path):
        with virtualenv():
            run('git pull')
            run('pip install -r requirements/production.txt')
            run('python manage.py migrate')
            run('python manage.py collectstatic --noinput')
            run('django-admin makemessages -a')
    restart()
