# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os

from configurations import Configuration, values


def _(s): return s

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Common(Configuration):
    """
    Common project settings.
    """
    SECRET_KEY = values.SecretValue()

    DEBUG = values.BooleanValue(False)

    SITE_ID = 1

    # Application definition.
    INSTALLED_APPS = [
        'djangocms_admin_style',
        'admin_shortcuts',
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django.contrib.sites',
        'django.contrib.sitemaps',
        'cms',
        'mptt',
        'menus',
        'sekizai',
        'reversion',
        'treebeard',
        'djangocms_text_ckeditor',
        'filer',
        'easy_thumbnails',
        'cmsplugin_filer_file',
        'cmsplugin_filer_folder',
        'cmsplugin_filer_image',
        'cmsplugin_filer_link',
        'cmsplugin_filer_teaser',
        'cmsplugin_filer_video',
        'compressor',
        'parler',
        'rosetta',
    ]

    MIDDLEWARE = [
        'django.middleware.cache.UpdateCacheMiddleware',
        'htmlmin.middleware.HtmlMinifyMiddleware',
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'django.contrib.sites.middleware.CurrentSiteMiddleware',
        'cms.middleware.page.CurrentPageMiddleware',
        'cms.middleware.user.CurrentUserMiddleware',
        'cms.middleware.toolbar.ToolbarMiddleware',
        'cms.middleware.language.LanguageCookieMiddleware',
        'cms.middleware.utils.ApphookReloadMiddleware',
        'solid_i18n.middleware.SolidLocaleMiddleware',
        'django.middleware.cache.FetchFromCacheMiddleware',
        'htmlmin.middleware.MarkRequestMiddleware',
    ]

    ROOT_URLCONF = 'project.urls'

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(BASE_DIR, 'templates')],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                    'django.core.context_processors.i18n',
                    'django.core.context_processors.media',
                    'django.core.context_processors.static',
                    'django.core.context_processors.tz',
                    'cms.context_processors.cms_settings',
                    'sekizai.context_processors.sekizai',
                ],
            },
        },
    ]

    WSGI_APPLICATION = 'project.wsgi.application'

    DATABASES = values.DatabaseURLValue('sqlite:///{}'.format(os.path.join(BASE_DIR, 'db.sqlite3')))

    # Authentication
    AUTH_PASSWORD_VALIDATORS = [
        {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
        {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
        {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
        {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
    ]

    # Internationalization
    LANGUAGE_CODE = 'en'
    LANGUAGES = [('en', 'English')]
    TIME_ZONE = 'UTC'
    USE_I18N = True
    USE_L10N = True
    USE_TZ = True
    LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale')]

    # Static files
    STATIC_URL = '/static/'
    MEDIA_URL = '/media/'
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
    STATICFILES_FINDERS = [
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
        'compressor.finders.CompressorFinder',
    ]

    # parler
    PARLER_LANGUAGES = {None: tuple({'code': x[0]} for x in LANGUAGES)}

    # compressor
    COMPRESS_CSS_FILTERS = [
        'compressor.filters.css_default.CssAbsoluteFilter',
        'compressor.filters.cssmin.CSSMinFilter',
    ]

    # htmlmin
    EXCLUDE_FROM_MINIFYING = [r'^admin/', r'^translate/']

    # rosetta
    SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'
    ROSETTA_STORAGE_CLASS = 'rosetta.storage.SessionRosettaStorage'
    ROSETTA_SHOW_AT_ADMIN_PANEL = True

    # admin_shortcuts
    ADMIN_SHORTCUTS_SETTINGS = {
        'hide_app_list': False,
        'open_new_window': False,
    }
    ADMIN_SHORTCUTS = [
        {'shortcuts': [
            {'url': '/', 'open_new_window': True},
            {'url_name': 'admin:cms_page_changelist', 'title': _('Pages')},
            {'url_name': 'admin:filer_folder_changelist', 'title': _('Files')},
            {'url_name': 'admin:auth_user_changelist', 'title': _('Users')}
        ]},
    ]

    # cms
    CMS_SEO_FIELDS = True
    CMS_HIDE_UNTRANSLATED = True
    CMS_REDIRECTS = True
    CMS_TEMPLATES = [
        ('default.html', _('Default')),
    ]
    CMS_PLACEHOLDER_CONF = {
        'content': {
            'plugins': [
                'TextPlugin',
                'FilerFilePlugin',
                'FilerFolderPlugin',
                'FilerImagePlugin',
                'FilerTeaserPlugin',
                'FilerVideoPlugin',
            ],
            'text_only_plugins': ['FilerLinkPlugin'],
            'name': _('Content'),
        },
    }

    # djangocms_text_ckeditor
    CKEDITOR_SETTINGS = {
        'language': 'en',
        'toolbar_CMS': [
            ['Undo', 'Redo'],
            ['cmsplugins', '-', 'ShowBlocks'],
            ['Format', 'Styles'],
            ['PasteText', 'PasteFromWord'],
            ['Maximize', ''],
            '/',
            ['Bold', 'Italic', 'Underline', '-', 'RemoveFormat'],
            ['Link', 'Unlink'],
            ['JustifyLeft', 'JustifyCenter', 'JustifyRight'],
            ['Table', 'HorizontalRule'],
            ['NumberedList', 'BulletedList', '-', 'Blockquote'],
            ['Source']
        ],
        'skin': 'moono',
    }
    TEXT_SAVE_IMAGE_FUNCTION = 'cmsplugin_filer_image.integrations.ckeditor.create_image_plugin'

    # filer
    FILER_ALLOW_REGULAR_USERS_TO_ADD_ROOT_FOLDERS = True

    # easy_thumbnails
    THUMBNAIL_HIGH_RESOLUTION = True
    THUMBNAIL_PROCESSORS = (
        'easy_thumbnails.processors.colorspace',
        'easy_thumbnails.processors.autocrop',
        'filer.thumbnail_processors.scale_and_crop_with_subject_location',
        'easy_thumbnails.processors.filters',
    )


class Development(Common):
    """
    The in-development settings.
    """
    ALLOWED_HOSTS = ['*']

    INTERNAL_IPS = ['127.0.0.1']

    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

    INSTALLED_APPS = Common.INSTALLED_APPS + [
        'debug_toolbar',
        'django_extensions',
    ]

    MIDDLEWARE = ['debug_toolbar.middleware.DebugToolbarMiddleware'] + Common.MIDDLEWARE

    CACHES = {'default': {'BACKEND': 'django.core.cache.backends.dummy.DummyCache'}}

    # Static files
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

    # debug_toolbar
    DEBUG_TOOLBAR_CONFIG = {'INTERCEPT_REDIRECTS': False}


class Staging(Common):
    """
    The in-staging settings.
    """
    ALLOWED_HOSTS = []

    CACHES = {'default': {'BACKEND': 'django.core.cache.backends.locmem.LocMemCache'}}

    # Static, media
    MEDIA_ROOT = os.path.join(os.path.expanduser('~'), 'public', 'media')
    STATIC_ROOT = os.path.join(os.path.expanduser('~'), 'public', 'static')

    # Security
    SESSION_COOKIE_SECURE = values.BooleanValue(True)
    SECURE_BROWSER_XSS_FILTER = values.BooleanValue(True)
    SECURE_CONTENT_TYPE_NOSNIFF = values.BooleanValue(True)
    SECURE_HSTS_INCLUDE_SUBDOMAINS = values.BooleanValue(True)
    SECURE_HSTS_SECONDS = values.IntegerValue(31536000)
    SECURE_REDIRECT_EXEMPT = values.ListValue([])
    SECURE_SSL_HOST = values.Value(None)
    SECURE_SSL_REDIRECT = values.BooleanValue(True)
    SECURE_PROXY_SSL_HEADER = values.TupleValue(('HTTP_X_FORWARDED_PROTO', 'https'))


class Production(Staging):
    """
    The in-production settings.
    """
