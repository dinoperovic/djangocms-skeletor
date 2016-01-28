# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import sys


_ = lambda s: s


PROJECT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))


def project_path(*args):
    return os.path.join(PROJECT_DIR, *args)


def env_setting(key, default=''):
    return os.environ.get(key, default)


# Insert apps dir into sys path
sys.path.insert(0, project_path('apps'))


SITE_ID = 1
ADMINS = [('Admin', 'admin@example.com')]
MANAGERS = ADMINS
DEFAULT_FROM_EMAIL = 'webmaster@localhost'
SERVER_EMAIL = DEFAULT_FROM_EMAIL


def ensure_secret_key_file():
    secret_path = project_path('settings', 'secret.py')
    if not os.path.exists(secret_path):
        from django.utils.crypto import get_random_string
        secret_key = get_random_string(
            50, 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)')
        with open(secret_path, 'w') as f:
            f.write('# -*- coding: utf-8 -*-\n\n')
            f.write('SECRET_KEY = ' + repr(secret_key) + '\n')


ensure_secret_key_file()
from secret import SECRET_KEY  # noqa


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
    'social.apps.django_app.default',
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
    'utils',
]


MIGRATION_MODULES = {
    'cmsplugin_filer_file': 'cmsplugin_filer_file.migrations_django',
    'cmsplugin_filer_folder': 'cmsplugin_filer_folder.migrations_django',
    'cmsplugin_filer_link': 'cmsplugin_filer_link.migrations_django',
    'cmsplugin_filer_image': 'cmsplugin_filer_image.migrations_django',
    'cmsplugin_filer_teaser': 'cmsplugin_filer_teaser.migrations_django',
    'cmsplugin_filer_video': 'cmsplugin_filer_video.migrations_django',
}


MIDDLEWARE_CLASSES = [
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'htmlmin.middleware.HtmlMinifyMiddleware',
    'htmlmin.middleware.MarkRequestMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware',
    'social.apps.django_app.middleware.SocialAuthExceptionMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
    'cms.middleware.utils.ApphookReloadMiddleware',
    'solid_i18n.middleware.SolidLocaleMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
]


# urls, application
ROOT_URLCONF = 'project.urls'
WSGI_APPLICATION = 'project.wsgi.application'


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.'
             'UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.'
             'MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.'
             'CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.'
             'NumericPasswordValidator'},
]


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [project_path('templates')],
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
                'social.apps.django_app.context_processors.backends',
                'social.apps.django_app.context_processors.login_redirect',
                'cms.context_processors.cms_settings',
                'sekizai.context_processors.sekizai',
            ],
        },
    },
]


# Internationalization
LANGUAGE_CODE = 'en'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
LOCALE_PATHS = [project_path('locale')]
LANGUAGES = [
    ('en', _('English')),
]


# Static, media
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATICFILES_DIRS = [project_path('staticfiles')]
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
]


# parler
PARLER_LANGUAGES = {
    1: tuple({'code': x[0]} for x in LANGUAGES),
}


# auth, social
LOGIN_REDIRECT_URL = '/admin/'
LOGIN_URL = '/admin/login/'
LOGOUT_URL = '/admin/logout/'
AUTHENTICATION_BACKENDS = [
    'social.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
]
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = ''
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = ''


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
        {'url_name': 'admin:auth_user_changelist', 'title': _('Users')}]},
]


# cms
CMS_SEO_FIELDS = True
CMS_HIDE_UNTRANSLATED = True
CMS_REDIRECTS = True
CMS_TEMPLATES = [
    ('default.html', _('Default')),
]
CMS_PLACEHOLDER_CONF = {
    'body': {
        'plugins': [
            'TextPlugin',
            'FilerFilePlugin',
            'FilerFolderPlugin',
            'FilerImagePlugin',
            'FilerTeaserPlugin',
            'FilerVideoPlugin',
        ],
        'text_only_plugins': ['FilerLinkPlugin'],
        'name': _('Body'),
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
TEXT_SAVE_IMAGE_FUNCTION = \
    'cmsplugin_filer_image.integrations.ckeditor.create_image_plugin'


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
