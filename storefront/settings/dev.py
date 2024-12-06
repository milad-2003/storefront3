from .common import *


DEBUG = True

SECRET_KEY = config("SECRET_KEY")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': '/home/milad/Files/Codes/Django/storefront3/my.cnf'
        },
    }
}
