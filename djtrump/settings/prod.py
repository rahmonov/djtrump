from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'djtrumpprod',
        'USER': 'postgres',
        'PORT': '5432',
    }
}
