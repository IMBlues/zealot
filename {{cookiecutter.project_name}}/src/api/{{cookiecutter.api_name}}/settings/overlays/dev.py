{%- if cookiecutter.license_header -%}
"""{{cookiecutter.license_header}}"""

{%- endif -%}
from {{cookiecutter.api_name}}.settings import env
from {{cookiecutter.api_name}}.settings.django import *  # noqa
from {{cookiecutter.api_name}}.settings.utils import *  # noqa

DEBUG = True
LOG_LEVEL = env.str("LOG_LEVEL", default="DEBUG")
LOGGING = get_stdout_logging(LOG_LEVEL, "{{cookiecutter.api_name}}")

DATABASES = get_db_config()