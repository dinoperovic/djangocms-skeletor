# djangocms-skeletor

**A boilerplate django project with [djangoCMS](https://www.django-cms.org) already installed.**

---

## Get started

Make make sure you have [pipenv](https://docs.pipenv.org/) installed. Then inside your `virtualenv` run:

```bash
pip install Django==1.11.15
django-admin startproject --template https://github.com/dinoperovic/djangocms-skeletor/archive/master.zip -e py,md,env,json project_name
cd project_name
npm install
pipenv install --dev
pipenv run python manage.py migrate
```

This project assumes use of [Webpack](https://webpack.js.org/) to bundle and manage your static files. To start watching static files with Webpack along with Django development server you can use [Honcho](https://github.com/nickstenning/honcho) which is already installed. Simply run:

```bash
honcho start
```

Both **Django** and **Webpack** development servers are configured to run without local host restrictions, which means you can immediately access your site with other devices on the same local network by navigating to `http://<local_ip_address>:8000`.


## Configuration

Settings is managed by the [django-configurations](https://github.com/jazzband/django-configurations) project. This allows you to configure the settings using environment variables. For example setting `DJANGO_MEDIA_ROOT='/path/to/media'` as an environment variable will affect the Django `MEDIA_ROOT` setting.

The required settings are `ENVIRONMENT` which is either `development`, `stagging` or `production`. And ``DJANGO_SECRET_KEY`` that comes included in `.env` file when first starting a new project.

Read more about this project on [ReadTheDocs](https://django-configurations.readthedocs.io).

#### Dotenv

A [python-dotenv](https://github.com/theskumar/python-dotenv) project is included to enable setting environment variables through the `.env` file in your project root. This file will be downloaded when starting a new project but is included in the `.gitignore` file. It should be unique for each of the enviromnents you install your project in.

## Webpack

A basic webpack config is provided to handle common static file types. Out of the box you can start writing **SASS/SCSS** by importing files in your `assets/js/main.js` file.

[PostCSS](http://postcss.org/) is configured to process all CSS files with some default plugins including [autoprefixer](https://github.com/postcss/autoprefixer) to handle vendor prefixes automatically. Edit the `postcss.config.js` file to add and configure more plugins.

[Babel](https://babeljs.io/) compiler is used so that next-gen JavaScript can be used as well.

For seamless integration with Django — [django-webpack-loader](https://github.com/ezhome/django-webpack-loader) project is used.

Read more about configuring [Webpack](https://webpack.js.org/configuration/).

## Deployment

To prepare static files from Webpack for deployment, simply run:

```bash
npm run build
```

This will generate an output in `static/bundles/` directory so that it gets included when running `collectstatic` from Django.

[Fabric](http://www.fabfile.org/) is included with a blank `fabfile.py` file.
