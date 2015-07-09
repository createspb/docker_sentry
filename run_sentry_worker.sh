#!/bin/bash

exec >> /var/log/start_sentry.sh.log 2>&1
set -x

setuser www-data /usr/local/bin/sentry --config=/etc/sentry.conf.py celery worker -B