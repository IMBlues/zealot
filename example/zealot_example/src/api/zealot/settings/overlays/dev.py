""""""
from zealot.settings import env
from zealot.settings.django import *  # noqa
from zealot.settings.utils import *  # noqa

DEBUG = True
LOG_LEVEL = env.str("LOG_LEVEL", default="DEBUG")
LOGGING = get_stdout_logging(LOG_LEVEL, "zealot")

DATABASES = get_db_config()