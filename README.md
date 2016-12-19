# djangocms-skeletor

**A boilerplate django project with [djangoSHOP](http://www.django-shop.org) already installed.**

---

## Get started

To start a new project:

```bash
$ pip install Django==1.9.12
$ django-admin startproject --template https://github.com/dinoperovic/djangocms-skeletor/archive/master.zip -e py,md,env project_name
$ cd project_name
$ pip install -r requirements/dev.txt
$ python manage.py migrate
```

This project assumes [SASS](http://sass-lang.com/) preprocessor is used to write CSS. To start a SASS compiler with
the development server you can use [Honcho](https://github.com/nickstenning/honcho) wich is already installed.
Simply run:

```bash
$ honcho start
```

## Deployment

[Fabric](http://www.fabfile.org/) can be used for deployment via git. Edit the `fabfile.py` to update hosts for
**staging** and **production** servers and set paths for *project* and *virtualenv* on the server.
To deploy to a production server you can then run:

```bash
$ fab production deploy
```
