from .base import *
from os import environ
import dj_database_url

##########
APP_ENVIRONMENT = 'prod'
S3_STATIC = False
DEBUG = False
SECRET_KEY = environ.get('SECRET_KEY', get_random_string(50, 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'))
ALLOWED_HOSTS = ['.example.com'] # Replace
WSGI_APPLICATION = 'config.wsgi.prod.application'

##########
# Database setting
DATABASES['default'] = dj_database_url.config(conn_max_age=500)
#DATABASES['default']['ENGINE'] = 'django.contrib.gis.db.backends.postgis'

##########
# Use the cached template loader so template is compiled once and read from
# memory instead of reading from disk on each load.
TEMPLATES[0]['OPTIONS']['loaders'] = [
    ('django.template.loaders.cached.Loader', [
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    ]),
]

##########
# WhiteNoise settings
# See: http://whitenoise.evans.io/en/stable/
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# WHITENOISE_MIDDLEWARE = [
#     'whitenoise.middleware.WhiteNoiseMiddleware',
# ]

##########
# Middleware setting
# See: https://docs.djangoproject.com/en/1.11/topics/http/middleware/
# MIDDLEWARE += WHITENOISE_MIDDLEWARE

# Using S3 for serving static files.
if S3_STATIC:
    AWS_STORAGE_BUCKET_NAME = '<s3 bucket name>'
    AWS_ACCESS_KEY_ID = '<access key id>'
    AWS_SECRET_ACCESS_KEY = '<secret access key>'
    STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    S3_URL = 'http://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
    STATIC_URL = S3_URL