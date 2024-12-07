import dj_database_url
from .common import *


DEBUG = False

SECRET_KEY = config("SECRET_KEY")

ALLOWED_HOSTS = []

DATABASES = {
    'default': dj_database_url.config() # This function looks for an environment variable called DATABASE_URL, read it, parse that connection string and return a dictionary that we can use here
}

# Here in production, we are using a single redis database both as a message broker and cache
# We have to pay more money in order to have two separate redis databases
REDIS_URL = os.environ['REDIS_URL']

CELERY_BROKER_URL = REDIS_URL

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        # Here we use database 2, becuase database 1 is already used for the message broker
        "LOCATION": REDIS_URL,
        # Setting the default timeout for the cache to 10 minutes
        "TIMEOUT": 10 * 60,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

EMAIL_HOST = os.environ['MAILGUN_SMTP_SERVER']
EMAIL_HOST_USER = os.environ['MAILGUN_SMTP_LOGIN']
EMAIL_HOST_PASSWORD = os.environ['MAILGUN_SMTP_PASSWORD']
EMAIL_PORT = os.environ['MAILGUN_SMTP_PORT']
