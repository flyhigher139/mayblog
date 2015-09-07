import os
from base import *

# DEBUG = os.environ['DEBUG']
DEBUG = False

ALLOWED_HOSTS = [host.strip() for host in os.environ['ALLOWED_HOSTS'].split(',')]

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db_prod.sqlite3'),
#     }
# }

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': os.environ['MYSQL_DATABASE'],
    #     'USER': os.environ['MYSQL_USER'],
    #     'PASSWORD': os.environ['MYSQL_PASSWORD'],
    #     'HOST': os.environ['MYSQL_HOST'],
    #     'PORT': os.environ['MYSQL_PORT']
    # }

    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['DB_NAME'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASS'],
        'HOST': os.environ['DB_SERVICE'],
        'PORT': os.environ['DB_PORT']
    }
}
