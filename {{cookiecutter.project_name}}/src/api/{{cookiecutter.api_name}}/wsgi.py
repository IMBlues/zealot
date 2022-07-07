{%- if cookiecutter.license_header -%}
"""{{cookiecutter.license_header}}"""

{%- endif -%}
import os

from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', '{{cookiecutter.api_name}}.settings.overlays.prod')

application = WhiteNoise(get_wsgi_application())
