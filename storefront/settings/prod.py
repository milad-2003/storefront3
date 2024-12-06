from decouple import config
from .common import *


DEBUG = False

SECRET_KEY = config("SECRET_KEY")

ALLOWED_HOSTS = []
