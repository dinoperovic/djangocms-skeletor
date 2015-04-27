# -*- coding: utf-8 -*-
import os
import sys


_ = lambda s: s

PROJECT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
PROJECT_NAME = os.path.basename(PROJECT_DIR)


def project_path(*args):
    return os.path.join(PROJECT_DIR, *args)


# Add apps directory to system path.
sys.path.insert(0, project_path('apps'))


SITE_ID = 1

ADMINS = (
    # ('Admin', 'admin@example.com'),
)
MANAGERS = ADMINS

DEFAULT_FROM_EMAIL = 'webmaster@localhost'
SERVER_EMAIL = DEFAULT_FROM_EMAIL

# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
LANGUAGE_CODE = 'en'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

LANGUAGES = (
    ('en', _('English')),
)

LOCALE_PATHS = (
    project_path('locale'),
)

STATIC_ROOT = project_path('static')
STATIC_URL = '/static/'

MEDIA_ROOT = project_path('media')
MEDIA_URL = '/media/'

ADMIN_MEDIA_PREFIX = '/static/admin/'

STATICFILES_DIRS = (
    project_path('staticfiles'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)


def ensure_secret_key_file():
    secret_path = project_path('settings', 'secret.py')
    if not os.path.exists(secret_path):
        from django.utils.crypto import get_random_string
        secret_key = get_random_string(
            50, 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)')
        with open(secret_path, 'w') as f:
            f.write('# -*- coding: utf-8 -*-\n')
            f.write('SECRET_KEY = ' + repr(secret_key) + '\n')

ensure_secret_key_file()
from secret import SECRET_KEY  # noqa


TEMPLATE_DIRS = (
    project_path('templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    # 'social.apps.django_app.context_processors.backends',
    # 'social.apps.django_app.context_processors.login_redirect',
    'cms.context_processors.cms_settings',
    'sekizai.context_processors.sekizai',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.gzip.GZipMiddleware',
    'htmlmin.middleware.HtmlMinifyMiddleware',
    'htmlmin.middleware.MarkRequestMiddleware',
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
)


# Use solid_i18n urls if installed.
try:
    import solid_i18n  # noqa
    MIDDLEWARE_CLASSES += ('solid_i18n.middleware.SolidLocaleMiddleware',)
except ImportError:
    MIDDLEWARE_CLASSES += ('django.middleware.locale.LocaleMiddleware',)


ROOT_URLCONF = PROJECT_NAME + '.urls'
WSGI_APPLICATION = PROJECT_NAME + '.wsgi.application'

INSTALLED_APPS = (
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
    'djangocms_link',
    'filer',
    'easy_thumbnails',
    # 'cmsplugin_filer_file',
    # 'cmsplugin_filer_folder',
    # 'cmsplugin_filer_image',
    # 'cmsplugin_filer_teaser',
    # 'cmsplugin_filer_video',
    'compressor',
    'parler',
    'rosetta',
    'utils',
)

# Set apps correct migrations path.
MIGRATION_MODULES = {
    'cms': 'cms.migrations_django',
    'filer': 'filer.migrations_django',
    'cmsplugin_filer_file': 'cmsplugin_filer_file.migrations_django',
    'cmsplugin_filer_folder': 'cmsplugin_filer_folder.migrations_django',
    'cmsplugin_filer_image': 'cmsplugin_filer_image.migrations_django',
    'cmsplugin_filer_teaser': 'cmsplugin_filer_teaser.migrations_django',
    'cmsplugin_filer_video': 'cmsplugin_filer_video.migrations_django',
    'djangocms_link': 'djangocms_link.migrations_django',
    'djangocms_text_ckeditor': 'djangocms_text_ckeditor.migrations_django',
}


# parler
PARLER_LANGUAGES = {
    1: tuple({'code': x[0]} for x in LANGUAGES),
}


# auth, social
LOGIN_REDIRECT_URL = '/admin/'
LOGIN_URL = '/admin/login/'
LOGOUT_URL = '/admin/logout/'
AUTHENTICATION_BACKENDS = (
    'social.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = ''
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = ''


# compressor
COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter',
]

# htmlmin
EXCLUDE_FROM_MINIFYING = (r'^admin/', r'^translate/')


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

CMS_TEMPLATES = (
    ('default.html', _('Default')),
)

CMS_PLACEHOLDER_CONF = {
    'body': {
        'plugins': [
            'TextPlugin',
            # 'FilerFilePlugin',
            # 'FilerFolderPlugin',
            # 'FilerImagePlugin',
            # 'FilerTeaserPlugin',
            # 'FilerVideoPlugin',
        ],
        'text_only_plugins': ['LinkPlugin'],
        'name': _('Body'),
    },
}


# djangocms_text_ckeditor
CKEDITOR_SETTINGS = {
    'language': 'en',
    'skin': 'moono',
    'toolbar': 'CMS',
}


# filer
FILER_ALLOW_REGULAR_USERS_TO_ADD_ROOT_FOLDERS = True
TEXT_SAVE_IMAGE_FUNCTION = (
    'cmsplugin_filer_image.integrations.ckeditor.create_image_plugin')


# easy_thumbnails
THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    # 'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)
