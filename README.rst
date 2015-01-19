{{ project_name }} (`{{ domain_name }}`_)
=============================

Django website.

Quickstart
----------
Run inside `virtualenv`:

.. code:: python

    git clone git@bitbucket.org:{{ username }}/{{ domain_name }}.git {{ domain_name }}
    cd {{ domain_name }}
    make dev-setup

Start server with:

.. code:: python

    make runs

Run tests with:

.. code:: python

    make test

Open shell with:

.. code:: python

    make shell


.. _{{ domain_name }}: http://{{ domain_name }}
