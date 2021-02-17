'''Use this for development'''

from .base import *

ALLOWED_HOSTS += ['127.0.0.1']
DEBUG = True

WSGI_APPLICATION = 'home.wsgi.dev.application'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ecomm_platform',
        'USER': 'ecomm_admin',
        'PASSWORD': 'Terse@123',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

CORS_ORIGIN_WHITELIST = (
    'http://localhost:3000',
)