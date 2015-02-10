from sentry.conf.server import *

# SENTRY_URL_PREFIX = 'http://sentry.mpn.lc'

SENTRY_ALLOW_REGISTRATION = False
# Set this to false to require authentication
SENTRY_PUBLIC = False
SENTRY_ALLOW_PUBLIC_PROJECTS = False

DATABASES = {
    'default': {
        'ENGINE':   'django.db.backends.postgresql_psycopg2',
        'NAME':     'sentry',
        'USER':     'sentry',
        'PASSWORD': 'sentry',
        'HOST':     '127.0.0.1',
        'PORT':     '5432'
    }
}

SENTRY_KEY = '123dkdslyvBUGWq5bcnW9d1MZQ82qmPZB4pskKS3555fdBfuhySw=='



# You should configure the absolute URI to Sentry.
# It will attempt to guess it if you don't
# but proxies may interfere with this.
# SENTRY_URL_PREFIX = 'http://sentry.example.com'  # No trailing slash!

SENTRY_WEB_HOST = '0.0.0.0'
SENTRY_WEB_PORT = 9000
SENTRY_WEB_OPTIONS = {
    'workers': 3,  # the number of gunicorn workers
}

ALLOWED_HOSTS = '*'
SENTRY_ALLOWED_HOSTS = '*'

# Mail server configuration

# For more information check Django's documentation:
#  https://docs.djangoproject.com/en/1.3/topics/email/#e-mail-backends

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

EMAIL_HOST = 'localhost'
EMAIL_HOST_PASSWORD = ''
EMAIL_HOST_USER = ''
EMAIL_PORT = 25
EMAIL_USE_TLS = False

# http://twitter.com/apps/new
# It's important that input a callback URL, even if its useless.
# We have no idea why, consult Twitter.
TWITTER_CONSUMER_KEY = ''
TWITTER_CONSUMER_SECRET = ''

# http://developers.facebook.com/setup/
FACEBOOK_APP_ID = ''
FACEBOOK_API_SECRET = ''

# http://code.google.com/apis/accounts/docs/OAuth2.html#Registering
GOOGLE_OAUTH2_CLIENT_ID = ''
GOOGLE_OAUTH2_CLIENT_SECRET = ''

# https://github.com/settings/applications/new
GITHUB_APP_ID = ''
GITHUB_API_SECRET = ''

# https://trello.com/1/appKey/generate
TRELLO_API_KEY = ''
TRELLO_API_SECRET = ''



LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler'
        },
        'sentry': {
            'level': 'ERROR',
            'class': 'raven.contrib.django.handlers.SentryHandler',
        },
        'file':{
            'level':'DEBUG',

            'class': 'logging.handlers.RotatingFileHandler',
            'maxBytes': 4196,
            'backupCount': 5,
            'filename': '/var/log/sentry_master.log',
            'mode': 'a',
        },
    },
    'formatters': {
        'client_info': {
            'format': '%(name)s %(levelname)s %(project_slug)s/%(team_slug)s %(message)s'
        }
    },
    'root': {
        'level': 'WARNING',
        'handlers': ['file', 'console', 'sentry'],
    },
    'loggers': {
        'sentry': {
            'level': 'ERROR',
            'handlers': ['file', 'console', 'sentry'],
            'propagate': True,
        },
        'sentry.coreapi': {
            'formatter': 'client_info',
        },
        'sentry.errors': {
            'level': 'ERROR',
            'handlers': ['file', 'console'],
            'propagate': True,
        },
        'static_compiler': {
            'level': 'INFO',
        },
        'django.request': {
            'level': 'ERROR',
            'handlers': ['file', 'console'],
            'propagate': True,
        },
        'toronado.cssutils': {
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

INSTALLED_APPS += (
    'sentry_slack',
)