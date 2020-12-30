from .base import *
from os import environ
from django.utils.crypto import get_random_string
import dj_database_url

##########
APP_ENVIRONMENT = 'heroku'
DEBUG = False
SECRET_KEY = environ.get('SECRET_KEY', get_random_string(50, 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'))
ALLOWED_HOSTS = ['.herokuapp.com'] # Replace
WSGI_APPLICATION = 'config.wsgi.prod.heroku'

##########
DATABASES = {
    'default': dj_database_url.config()
}

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
