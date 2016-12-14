# djangocms-skeletor

**A boilerplate django project with [djangoSHOP](http://www.django-shop.org) already installed, along with some other useful apps.**

---

## Get started

To start a new project:

```bash
$ pip install Django==1.9.12
$ django-admin startproject --template https://github.com/dinoperovic/djangocms-skeletor/archive/master.zip -e py,md,env -n Procfile project_name
$ pip install -r requirements/dev.txt
$ python manage.py migrate
```

Out of the box, this project assumes SASS preprocessor is used to write CSS. To start a SASS compiler with the
development server you can use [Honcho](https://github.com/nickstenning/honcho) wich is already installed. Simply run:

```bash
$ honcho start
```
