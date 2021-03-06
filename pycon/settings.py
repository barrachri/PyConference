"""
Django settings for pycon project.

Generated by 'django-admin startproject' using Django 1.8.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.utils.translation import ugettext_lazy as _

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@c$5x7sb-iaid*k8(&rg5mgo9ld4k*@8!k-7p%uq%t6%okk^q$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['']


# Application definition

INSTALLED_APPS = (
# The Django sites framework is required
    'django.contrib.sites',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    #'allauth.socialaccount.providers.facebook',
    #'allauth.socialaccount.providers.github',

    'grappelli',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'pycon.core',
    'pycon.home',
    'pycon.about',
    'pycon.tickets',
    'pycon.schedule',
    'pycon.slides',
    'pycon.sponsors',
    'pycon.conduct',
    'pycon.volunteers',

    'django_markup',
    'django_medusa',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'pycon.urls'

TEMPLATES = [
     {
         'BACKEND': 'django.template.backends.django.DjangoTemplates',
         'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
         ],
         'APP_DIRS': True,
         'OPTIONS': {
             'context_processors': [
                 'django.core.context_processors.debug',
                 'django.core.context_processors.request',
                 'django.contrib.auth.context_processors.auth',
                 'django.core.context_processors.i18n',
                 'django.core.context_processors.media',
                 'django.core.context_processors.static',
                 'django.core.context_processors.csrf',
                 'django.contrib.messages.context_processors.messages',
             ],
         },
     },
 ]

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

SITE_ID = 1

WSGI_APPLICATION = 'pycon.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# allauth configuration
# http://django-allauth.readthedocs.org/

ACCOUNT_USER_MODEL_USERNAME_FIELD = 'username'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_SIGNUP_FORM_CLASS = 'pycon.core.forms.SignupForm'

# Email
# https://docs.djangoproject.com/en/1.8/topics/email/

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-ca'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES = (
    ('fr', _('French')),
    ('en', _('English')),
)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = ''
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

#-------------------------------------------------------------------------------
# PyCon settings
#-------------------------------------------------------------------------------

SLIDE_WIDTH = 1024
SLIDE_HEIGHT = 768

WEBKIT2PNG_PATH = '/usr/local/bin/webkit2png'

#-------------------------------------------------------------------------------
# localsettings.py
#-------------------------------------------------------------------------------

try:
    from pycon.localsettings import *
except ImportError:
    pass

#-------------------------------------------------------------------------------
# settings_conference.py
#-------------------------------------------------------------------------------

try:
    from pycon.settings_conference import *
except ImportError:
    pass
