"""
Local settings for mutualcoin project.

- Run in Debug mode

- Use mailhog for emails
"""

from .base import *  # noqa

# DEBUG
# ------------------------------------------------------------------------------
DEBUG = env.bool('DJANGO_DEBUG', default=True)
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

# SECRET CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key only used for development and testing.
SECRET_KEY = env('DJANGO_SECRET_KEY', default='&p#doYet`FNw.HKBZB3|NELmoT|Frn1NpxJI~:!#~P]$ba[:<E')

# Mail settings
# ------------------------------------------------------------------------------

# EMAIL_PORT = 1025

# EMAIL_HOST = 'localhost'
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_BACKEND = "sendgrid_backend.SendgridBackend"
SENDGRID_API_KEY = "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"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = env('DJANGO_DEFAULT_FROM_EMAIL',
                         default='Mutualcoin <noreply@mutualcoin.fund>')
SENDGRID_SANDBOX_MODE_IN_DEBUG = False



# CACHING
# ------------------------------------------------------------------------------
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': ''
    }
}

# django-debug-toolbar
# ------------------------------------------------------------------------------
MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]
INSTALLED_APPS += ['debug_toolbar', ]

INTERNAL_IPS = ['127.0.0.1', '10.0.2.2', '*']

DEBUG_TOOLBAR_CONFIG = {
    'DISABLE_PANELS': [
        'debug_toolbar.panels.redirects.RedirectsPanel',
    ],
    'SHOW_TEMPLATE_CONTEXT': True,
}

# django-extensions
# ------------------------------------------------------------------------------
INSTALLED_APPS += ['django_extensions', ]

# TESTING
# ------------------------------------------------------------------------------
TEST_RUNNER = 'django.test.runner.DiscoverRunner'

# 3rd party library settings
# ------------------------------------------------------------------------------
URL_FRONT = 'http://localhost:8082/src/#/'
