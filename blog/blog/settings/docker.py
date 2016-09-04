import os
from base import *

DEBUG = (os.environ['DEBUG'].lower() == 'true')
# DEBUG = False

ALLOWED_HOSTS = [host.strip() for host in os.environ['ALLOWED_HOSTS'].split(',')]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['DB_NAME'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASS'],
        'HOST': os.environ['DB_SERVICE'],
        'PORT': os.environ['DB_PORT']
    }
}
