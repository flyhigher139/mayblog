import os
from base import *

DEBUG = False
ALLOWED_HOSTS = ['*']
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '111.222.333.444', 'mywebsite.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db_prod.sqlite3'),
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         # 'NAME': 'mayblog',
#         # 'USER': 'root',
#         # 'PASSWORD': 'root_1234',
#         # 'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
#         # 'PORT': '3306',
#         'NAME': os.environ['DB_NAME'],
#         'USER': os.environ['DB_USER'],
#         'PASSWORD': os.environ['DB_PASS'],
#         'HOST': os.environ['DB_SERVICE'],
#         'PORT': os.environ['DB_PORT']
#     }
# }