# djangocms-skeletor

**A boilerplate django project with [djangoCMS](https://www.django-cms.org) already installed.**

---

## Get started

To start a new project:

```bash
$ pip install Django==1.11.9
$ django-admin startproject --template https://github.com/dinoperovic/djangocms-skeletor/archive/master.zip -e py,md,env,json project_name
$ cd project_name
$ pip install -r requirements/dev.txt
$ python manage.py migrate
```

This project assumes use of [Webpack](https://webpack.js.org/) to bundle and manage your static files. To start watching static files
with Webpack along with Django development server you can use [Honcho](https://github.com/nickstenning/honcho) wich is already installed.
Simply run:

```bash
$ honcho start
```

## Configuration

Settings is managed by the [django-configurations](https://github.com/jazzband/django-configurations) project.
This allows you to configure the settings using environment variables. For example setting `DJANGO_MEDIA_ROOT='/path/to/media'`
as an environment variable will affect the Django `MEDIA_ROOT` setting.

The required settings are `ENVIRONMENT` which is either `development`, `stagging` or `production`. And ``DJANGO_SECRET_KEY``
that comes included in `.env` file when first starting a new project.

Read more about this project on [ReadTheDocs](https://django-configurations.readthedocs.io).

#### Dotenv

A [django-dotenv](https://github.com/jpadilla/django-dotenv) project is included to enable setting environment variables
through the `.env` file in your project root. This file will be downloaded when starting a new project but is included
in the `.gitignore` file. It should be unique for each of the enviromnents you install your project in.


## Deployment

To prepare static files from Webpack for deployment, simply run:

```bash
$ npm run build
```

This will generate an output in `static/bundles/` directory so that it gets included when running `collectstatic` from Django.

[Fabric](http://www.fabfile.org/) can be used for deployment via git. Edit the `fabfile.py` to update hosts for
**staging** and **production** servers and set paths for *project* and *virtualenv* on the server.
To deploy to a production server you can then run:

```bash
$ fab production deploy
```
