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

CELERY_BROKER_URL = 'redis://localhost:6380/1'

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        # Here we use database 2, becuase database 1 is already used for the message broker
        "LOCATION": "redis://127.0.0.1:6380/2",
        # Setting the default timeout for the cache to 10 minutes
        "TIMEOUT": 10 * 60,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}
