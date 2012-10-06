# Generated by statirator
import os

# Directories setup
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
BUILD_DIR = os.path.join(ROOT_DIR, 'build')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}


# Site(s) definitions. The Sites will be created when generate is called
# Each site is (domain, language, title). language of None means all
SITES = (
    ('meirkriheli.com', None, 'Meir Kriheli'),
)

SITE_ID = 1

# Local time zone. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Israel'

# Default Language code. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'he'
_ = lambda s: s

LANGUAGES = (
    ('en', _('English')),

    ('he', _('Hebrew')),
)

ROOT_URLCONF = 'conf.urls'

TEMPLATE_DIRS = (
    os.path.join(ROOT_DIR, 'templates'),
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.locale.LocaleMiddleware',
)


TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'statirator.core.context_processors.st_settings'
)

LOCALE_PATHS = (
    os.path.join(ROOT_DIR, 'locale'),
)

# Static files setup
STATIC_URL = '/'
STATIC_ROOT = BUILD_DIR
STATICFILES_DIRS = (
    os.path.join(ROOT_DIR, 'static'),
)

INSTALLED_APPS = (
    'django.contrib.contenttypes',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'django_medusa',
    'taggit',
    'disqus',
    'statirator.core',
    'statirator.blog',
    'statirator.pages',
    'pipeline',
)

MEDUSA_RENDERER_CLASS = "django_medusa.renderers.DiskStaticSiteRenderer"
MEDUSA_MULTITHREAD = False
MEDUSA_DEPLOY_DIR = BUILD_DIR

# Set your Analytics site id in here to enable analytics in pages
GOOGLE_ANALYTICS_ID = 'UA-26475861-1'

# How many posts to show on the index page
POSTS_IN_INDEX = 2

# disqus settings
DISQUS_API_KEY = ''
DISQUS_WEBSITE_SHORTNAME = ''

# django-pipline settings
PIPELINE_YUI_BINARY = '/usr/local/bin/yuicompressor.sh'

PIPELINE_COMPILERS = (
    'pipeline.compilers.less.LessCompiler',
)

PIPELINE_LESS_BINARY = '/usr/bin/lessc'

STATICFILES_STORAGE = 'pipeline.storage.PipelineStorage'

PIPELINE_CSS = {
    'meir': {
        'source_filenames': (
            'css/normalize.css',
            'css/normalize_rtl.css',
            'css/main.css',
            'css/syntax.css',
            'css/font-awesome.less',
            'css/theme.less',
        ),
        'output_filename': 'css/meir.css',
    }
}

PIPELINE_JS = {
    'bundle': {
        'source_filenames': (
            'js/main.js',
            'js/plugins.js',
        ),
        'output_filename': 'js/bundle.js',
    }
}

# Optionally place sensitive settings, which shoulen't be tracked by version
# control (e.g: Secret API keys, etc) in local_settings.py. Make sure to have
# that file ignored.
try:
    from local_settings import *
except ImportError:
    pass
