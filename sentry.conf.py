import os
from decouple import config
from sentry.conf.server import *

# better set these
SENTRY_URL_PREFIX = config('SENTRY_URL_PREFIX', default=None)
SENTRY_ADMIN_EMAIL = config('SENTRY_ADMIN_EMAIL', default=None)
SENTRY_KEY = config('SENTRY_KEY')


SENTRY_ALLOW_REGISTRATION = config('SENTRY_ALLOW_REGISTRATION ', default=False, cast=bool)

# Set this to false to require authentication
SENTRY_PUBLIC = False
SENTRY_ALLOW_PUBLIC_PROJECTS = False

DATABASES = {
    'default': {
        'ENGINE':   'django.db.backends.postgresql_psycopg2',
        'NAME':     os.environ.get('POSTGRESQL_NAME'),
        'USER':     os.environ.get('POSTGRESQL_USER'),
        'PASSWORD': os.environ.get('POSTGRESQL_PASS'),
        'HOST':     os.environ.get('DB_PORT_5432_TCP_ADDR'),
        'PORT':     os.environ.get('DB_PORT_5432_TCP_PORT')
    }
}

SENTRY_CACHE = 'sentry.cache.django.DjangoCache'


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

AWS_SES_REGION_NAME = 'eu-west-1'
AWS_SES_REGION_ENDPOINT = 'email.eu-west-1.amazonaws.com'

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')

EMAIL_BACKEND = 'django_ses.SESBackend'
SERVER_EMAIL = config('SERVER_EMAIL', default=None)
DEFAULT_FROM_EMAIL = config('SERVER_EMAIL', default=None)


# http://twitter.com/apps/new
# It's important that input a callback URL, even if its useless.
# We have no idea why, consult Twitter.
TWITTER_CONSUMER_KEY = ''
TWITTER_CONSUMER_SECRET = ''

# http://developers.facebook.com/setup/
FACEBOOK_APP_ID = ''
FACEBOOK_API_SECRET = ''

# http://code.google.com/apis/accounts/docs/OAuth2.html#Registering
GOOGLE_OAUTH2_CLIENT_ID = os.environ.get('GOOGLE_OAUTH2_CLIENT_ID', '')
GOOGLE_OAUTH2_CLIENT_SECRET = os.environ.get('GOOGLE_OAUTH2_CLIENT_SECRET', '')

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
            'level': 'WARNING',
            'handlers': ['file', 'console', 'sentry'],
            'propagate': True,
        },
        'sentry.coreapi': {
            'formatter': 'client_info',
        },
        'sentry.errors': {
            'level': 'WARNING',
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