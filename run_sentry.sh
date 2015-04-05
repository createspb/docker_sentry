#!/bin/bash

exec >> /var/log/start_sentry.sh.log 2>&1
set -x

exec /usr/local/bin/sentry --config=/etc/sentry.conf.py start