import os
from base import *

DEBUG = os.environ['DEBUG'] or False
ALLOWED_HOSTS = ['*']
# ALLOWED_HOSTS = ['localhost', '127.0.0.1', '111.222.333.444', 'mywebsite.com']

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db_prod.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'huEa6SbKq9Zf2nFJ',
        'USER': 'u5LhA34TwmuQr0Gb',
        'PASSWORD': 'psba2ZyhOoxwTmGDW',
        'HOST': '10.10.26.58',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
        # 'NAME': os.environ['MYSQL_INSTANCE_NAME'],
        # 'USER': os.environ['MYSQL_USERNAME'],
        # 'PASSWORD': os.environ['MYSQL_PASSWORD'],
        # 'HOST': os.environ['MYSQL_PORT_3306_TCP_ADDR'],
        # 'PORT': os.environ['MYSQL_PORT']
    }
}