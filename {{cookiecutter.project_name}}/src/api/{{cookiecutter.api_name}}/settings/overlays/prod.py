"""{{cookiecutter.license_header}}"""
from {{cookiecutter.api_name}}.settings import env
from {{cookiecutter.api_name}}.settings.django import *  # noqa
from {{cookiecutter.api_name}}.settings.utils import *  # noqa

DEBUG = False
ALLOWED_HOSTS = ['*']
LOG_LEVEL = env.str("LOG_LEVEL", default="INFO")
LOGGING = get_stdout_logging(LOG_LEVEL, "{{cookiecutter.api_name}}")

DB_PREFIX = env.str("DB_PREFIX", default="DB")
DATABASES = get_db_config(DB_PREFIX)
