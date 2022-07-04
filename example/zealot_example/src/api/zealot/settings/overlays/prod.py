""""""
from zealot.settings import env
from zealot.settings.django import *  # noqa
from zealot.settings.utils import *  # noqa

DEBUG = False
ALLOWED_HOSTS = ['*']
LOG_LEVEL = env.str("LOG_LEVEL", default="INFO")
LOGGING = get_stdout_logging(LOG_LEVEL, "zealot")

DB_PREFIX = env.str("DB_PREFIX", default="DB")
DATABASES = get_db_config(DB_PREFIX)
