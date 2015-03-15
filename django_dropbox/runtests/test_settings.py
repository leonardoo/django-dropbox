import os
import sys

import django

DEBUG = True
TEMPLATE_DEBUG = DEBUG

settings_dir = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(settings_dir)

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_ROOT, 'development.db'),
    }
}

# Internationalization
TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True


# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '12345'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
)

#ROOT_URLCONF = 'urls'
#WSGI_APPLICATION = 'demo.wsgi.application'

#TEMPLATE_DIRS = (
#    os.path.join(PROJECT_ROOT, 'templates/'),
#)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    "django_dropbox",
    "django_dropbox.runtests.dbtest",
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# Needed for Storage

DROPBOX_CONSUMER_KEY = '9lyr7cjqblxb2kv'
DROPBOX_CONSUMER_SECRET = '4saauuu6alx0iiz'
DROPBOX_ACCESS_TOKEN = 'vkf07symi6iadqba'
DROPBOX_ACCESS_TOKEN_SECRET = 'rz32iqtxsrfuwko'
#DROPBOX_CONSUMER_KEY = os.environ['DROPBOX_CONSUMER_KEY']
#DROPBOX_CONSUMER_SECRET = os.environ['DROPBOX_CONSUMER_SECRET']
#DROPBOX_ACCESS_TOKEN = os.environ['DROPBOX_ACCESS_TOKEN']
#DROPBOX_ACCESS_TOKEN_SECRET = os.environ['DROPBOX_ACCESS_TOKEN_SECRET']
ACCESS_TYPE = 'app_folder'