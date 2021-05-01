from . import *

SECRET_KEY = env('SECRET_KEY')
DEBUG = False
ALLOWED_HOSTS = ['134.209.92.2']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWD'),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
