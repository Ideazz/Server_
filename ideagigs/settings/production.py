from .base import *
import os



DEBUG= True

DATABASES = {
     'default': {

        'NAME': 'dio',
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'USER': 'dio',
        'PASSWORD': '',
        'HOST' : 'localhost',
        'PORT' :'5432',
    }
}
