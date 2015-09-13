import os
from base import *

DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '.daoapp.io', '.gevinzone.com', '.gevinzone.com.']

DEBUG = (os.environ['DEBUG'].lower() == 'true')
ALLOWED_HOSTS = [host.strip() for host in os.environ['ALLOWED_HOSTS'].split(',')]


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db_prod.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        # 'NAME': 'V4HQUqcEA83F9BL1',
        # 'USER': 'u4uf8Gl7bUCnXFQs',
        # 'PASSWORD': 'pcqm8nCvzspDwFBAG',
        # 'HOST': '10.10.26.58',   # Or an IP Address that your DB is hosted on
        # 'PORT': '3306',
        'NAME': os.environ['MYSQL_INSTANCE_NAME'],
        'USER': os.environ['MYSQL_USERNAME'],
        'PASSWORD': os.environ['MYSQL_PASSWORD'],
        'HOST': os.environ['MYSQL_PORT_3306_TCP_ADDR'],
        'PORT': os.environ['MYSQL_PORT_3306_TCP_PORT']
    }
}