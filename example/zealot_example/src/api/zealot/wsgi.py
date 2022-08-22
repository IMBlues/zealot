import os

from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise
import faulthandler

# 开启后可以更有效地捕获 Gunicorn worker timeout 问题的堆栈信息
# https://stackoverflow.com/questions/57167240/is-it-possible-to-get-a-stack-trace-when-a-gunicorn-worker-hits-a-timeout
faulthandler.enable()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'zealot.settings.overlays.prod')

application = WhiteNoise(get_wsgi_application())
