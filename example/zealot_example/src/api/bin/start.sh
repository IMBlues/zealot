#!/bin/bash

LISTEN_PORT="${PORT:=8000}"
if [ "$RUN_MIGRATE" -eq 1 ]; then
    echo "Migrate database..."
    python manage.py migrate --noinput
fi

python manage.py collectstatic --noinput

gunicorn zealot.wsgi -w 8 --threads 2 --max-requests 1024 --max-requests-jitter 50 -b :$LISTEN_PORT --access-logfile - --error-logfile - --access-logformat '[%(h)s] %({request_id}i)s %(u)s %(t)s "%(r)s" %(s)s %(D)s %(b)s "%(f)s" "%(a)s"'