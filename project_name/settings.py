# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os

from configurations import Configuration, values


def _(s): return s


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Common(Configuration):
    """
    Common project settings
    """
    SECRET_KEY = values.SecretValue()
    SITE_ID = values.IntegerValue(1)

    # Application definition
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
        'treebeard',
        'filer',
        'easy_thumbnails',
        'djangocms_text_ckeditor',
        'djangocms_link',
        'djangocms_picture',
        'djangocms_file',
        'djangocms_snippet',
        'djangocms_style',
        'djangocms_video',
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
        'django.middleware.locale.LocaleMiddleware',
        'django.contrib.sites.middleware.CurrentSiteMiddleware',
        'cms.middleware.page.CurrentPageMiddleware',
        'cms.middleware.user.CurrentUserMiddleware',
        'cms.middleware.toolbar.ToolbarMiddleware',
        'cms.middleware.language.LanguageCookieMiddleware',
        'cms.middleware.utils.ApphookReloadMiddleware',
        'django.middleware.cache.FetchFromCacheMiddleware',
        'htmlmin.middleware.MarkRequestMiddleware',
    ]

    ROOT_URLCONF = '{{ project_name }}.urls'

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(BASE_DIR, 'templates')],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.template.context_processors.i18n',
                    'django.template.context_processors.media',
                    'django.template.context_processors.static',
                    'django.template.context_processors.tz',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                    'cms.context_processors.cms_settings',
                    'sekizai.context_processors.sekizai',
                ],
            },
        },
    ]

    WSGI_APPLICATION = '{{ project_name }}.wsgi.application'

    DATABASES = values.DatabaseURLValue('sqlite:///{}'.format(os.path.join(BASE_DIR, 'db.sqlite3')))

    CACHES = values.CacheURLValue('locmem://')

    # Authentication
    AUTH_PASSWORD_VALIDATORS = [
        {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
        {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
        {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
        {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
    ]

    # Email
    ADMINS = []
    MANAGERS = []
    EMAIL = values.EmailURLValue('console://')
    DEFAULT_FROM_EMAIL = 'webmaster@localhost'
    SERVER_EMAIL = 'root@localhost'

    # Internationalization
    LANGUAGE_CODE = 'en'
    LANGUAGES = [('en', 'English')]
    TIME_ZONE = 'UTC'
    USE_I18N = True
    USE_L10N = True
    USE_TZ = True
    LOCALE_PATHS = values.ListValue([os.path.join(BASE_DIR, 'locale')])

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
    PARLER_LANGUAGES = {1: tuple({'code': x[0]} for x in LANGUAGES)}

    # compressor
    COMPRESS_CSS_FILTERS = [
        'compressor.filters.css_default.CssAbsoluteFilter',
        'compressor.filters.cssmin.CSSMinFilter',
    ]

    # htmlmin
    EXCLUDE_FROM_MINIFYING = [r'^admin/', r'^translate/']

    # rosetta
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
                'LinkPlugin',
                'PicturePlugin',
                'FilePlugin',
                'SnippetPlugin',
                'StylePlugin',
                'VideoPlayerPlugin',
            ],
            'name': _('Content'),
        },
    }

    # easy_thumbnails
    THUMBNAIL_HIGH_RESOLUTION = True
    THUMBNAIL_PROCESSORS = (
        'easy_thumbnails.processors.colorspace',
        'easy_thumbnails.processors.autocrop',
        'filer.thumbnail_processors.scale_and_crop_with_subject_location',
        'easy_thumbnails.processors.filters',
    )

    # filer
    FILER_ALLOW_REGULAR_USERS_TO_ADD_ROOT_FOLDERS = True

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


class Development(Common):
    """
    The in-development settings
    """
    DEBUG = values.BooleanValue(True)
    ALLOWED_HOSTS = ['*']
    INTERNAL_IPS = ['127.0.0.1']

    INSTALLED_APPS = Common.INSTALLED_APPS + ['django_extensions']

    # Static files
    MEDIA_ROOT = values.PathValue(os.path.join(BASE_DIR, 'public/media'), check_exists=False)
    STATIC_ROOT = values.PathValue(os.path.join(BASE_DIR, 'public/static'), check_exists=False)

    # debug_toolbar
    DEBUG_TOOLBAR = values.BooleanValue(DEBUG)

    @classmethod
    def post_setup(cls):
        super(Development, cls).post_setup()
        # Activate django-debug-toolbar
        if cls.DEBUG_TOOLBAR:
            cls.INSTALLED_APPS += ['debug_toolbar']
            cls.MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']


class Staging(Common):
    """
    The in-staging settings
    """
    DEBUG = values.BooleanValue(False)
    ALLOWED_HOSTS = values.ListValue([])

    # Static files
    MEDIA_ROOT = values.PathValue('~/public/media')
    STATIC_ROOT = values.PathValue('~/public/static')

    # Security
    SESSION_COOKIE_SECURE = values.BooleanValue(True)
    CSRF_COOKIE_SECURE = values.BooleanValue(True)
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
    The in-production settings
    """
