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

PROJECT_SOURCE_DIR = Path(os.path.dirname(os.path.dirname(BASE_DIR)))

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "dist",
            PROJECT_SOURCE_DIR / "ui/dist",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]