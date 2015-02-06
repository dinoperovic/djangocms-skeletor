MANAGE=python manage.py
SETTINGS=--settings=project.settings.test

FLAKE8_OPTS=--exclude=.git,migrations --max-complexity=10

.PHONY: all test coverage clean lint ensure_virtualenv local-settings \
	reqs/dev reqs/test reqs/prod dev-setup test-setup dev-update \
	prod-update update runs shell restart deploy messages compass-watch

all: coverage

test:
	$(MANAGE) test --where=. --where=project/apps $(SETTINGS) --with-xunit -s

coverage:
	$(MANAGE) test --where=. --where=project/apps $(SETTINGS) \
		--with-xcoverage --with-xunit --cover-html  --cover-erase

clean:
	rm -rf .coverage cover nosetests.xml coverage.xml
	rm -rf project/static/CACHE
	find . -name '*.pyc' -exec rm '{}' ';'

lint:
	flake8 $(FLAKE8_OPTS) .

ensure_virtualenv:
	@if [ -z $$VIRTUAL_ENV ]; then \
		echo "Please run me inside virtualenv.";  \
		exit 1; \
	fi

local-settings:
	@if [ ! -f project/settings/local.py ]; then \
		echo '# -*- coding: utf-8 -*-\nfrom .dev import *  # noqa' \
		> project/settings/local.py; \
		echo "Created project/settings/local.py"; \
		else \
			echo "project/settings/local.py already exists"; \
	fi

reqs/dev: ensure_virtualenv
	pip install -r requirements/dev.txt

reqs/test: ensure_virtualenv
	pip install -r requirements/test.txt

reqs/prod: ensure_virtualenv
	pip install -r requirements/prod.txt

dev-setup: ensure_virtualenv reqs/dev
	$(MAKE) local-settings
	$(MAKE) update

test-setup: ensure_virtualenv reqs/test
	$(MAKE) update

dev-update: ensure_virtualenv reqs/dev
	$(MAKE) update

prod-update: ensure_virtualenv reqs/prod
	$(MAKE) update
	$(MANAGE) collectstatic --noinput

update: ensure_virtualenv
	$(MAKE) clean
	$(MANAGE) migrate

runs: ensure_virtualenv
	$(MANAGE) runserver_plus

shell: ensure_virtualenv
	$(MANAGE) shell_plus

restart:
	touch project/wsgi.py

deploy: ensure_virtualenv
	git pull
	$(MAKE) prod-update
	$(MAKE) restart

messages:
	cd project && django-admin makemessages -a

sass-watch:
	cd project/staticfiles/site && sass --watch sass:css
