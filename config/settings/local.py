"""
Settings locales — desarrollo.
"""
from .base import *  # noqa
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.environ.get(
    'SECRET_KEY',
    'django-insecure-dev-key-change-in-production-000000000000'
)

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '0.0.0.0']

# Usa PostgreSQL si hay env vars de Docker; SQLite si no.
if os.environ.get('DB_HOST'):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ.get('DB_NAME', 'portfolio'),
            'USER': os.environ.get('DB_USER', 'portfolio_user'),
            'PASSWORD': os.environ.get('DB_PASSWORD', 'portfolio_pass'),
            'HOST': os.environ.get('DB_HOST', 'db'),
            'PORT': os.environ.get('DB_PORT', '5432'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',  # noqa: F405
        }
    }

# En local mostramos emails en consola
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
