import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'dev_db.sqlite3'),
    }
}

# Email
# https://docs.djangoproject.com/en/1.8/topics/email/

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
