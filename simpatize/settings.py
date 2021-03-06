"""
Django settings for simpatize project.

Generated by 'django-admin startproject' using Django 1.8.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'llzv8^@$yd-lc3hjt4b&z11*-@)#n35qr$ycgcd=rb5_=olle8'

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'simpatize',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'simpatize.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "simpatize")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'simpatize.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

database_config = {}

if 'DYNO' in os.environ:
    database_config["NAME"] = "d2q78f1dsq37lg"
    database_config["USER"] = "jrgqcedhpbwvxx"
    database_config["PASSWORD"] = "AgBv45XHA7iEybJ9rb0cdoHPNo"
    database_config["HOST"] = "ec2-54-225-194-162.compute-1.amazonaws.com"
    database_config["PORT"] = "5432"
else:
    database_config["NAME"] = "simpatize"
    database_config["USER"] = "dev"
    database_config["PASSWORD"] = "1234"
    database_config["HOST"] = "localhost"
    database_config["PORT"] = ""

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': database_config["NAME"],
        'USER': database_config["USER"],
        'PASSWORD': database_config["PASSWORD"],
        'HOST': database_config["HOST"],
        'PORT': database_config["PORT"]
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# Google Places API key

GOOGLE_PLACES_API_KEY = "AIzaSyAfZcyrKMHxsidSpMsUcwLlOWbLsVZS0W4"
