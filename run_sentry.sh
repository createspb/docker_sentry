#!/bin/bash

exec >> /var/log/start_sentry.sh.log 2>&1
set -x

wait_for_postgres() {
  # Wait for postgres to finish starting up first.
  while [[ ! -e /run/pgsql-after-init.hook ]] ; do
      inotifywait -q -e create /run/ >> /dev/null
  done

}

# TODO: this is not actually needed anymore with new init. Just exit 1 if postgre hook is not there.
wait_for_postgres

exec /usr/local/bin/sentry --config=/etc/sentry.conf.py start