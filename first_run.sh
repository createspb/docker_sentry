
exec >> /var/log/first_run.sh.log 2>&1
set -x

SENTRY_USER=${SENTRY_USER:-super}
SENTRY_PASS=${SENTRY_PASS:-$(pwgen -s -1 16)}

pre_start_action() {

  # test if DATA_DIR has content
  if [[ ! "$(ls -A $DATA_DIR)" ]]; then
      echo "Initializing PostgreSQL at $DATA_DIR"

      # Copy the data that we generated within the container to the empty DATA_DIR.
      cp -R /var/lib/postgresql/9.3/main/* $DATA_DIR
  fi

  # Ensure postgres owns the DATA_DIR
  chown -R postgres $DATA_DIR
  # Ensure we have the right permissions set on the DATA_DIR
  chmod -R 700 $DATA_DIR
}

post_start_action() {
    su postgres sh -c "createdb sentry"
    su postgres sh -c "createuser --no-createdb --encrypted --no-createrole --no-superuser sentry"
    su postgres sh -c "psql -c \"ALTER USER sentry WITH PASSWORD 'sentry';\" "
    su postgres sh -c "psql -c \"GRANT ALL PRIVILEGES ON DATABASE sentry to sentry;\" "
    sentry --config=/etc/sentry.conf.py upgrade --noinput

    echo "Sentry pass is: $PASS"
    echo "from sentry.models.user import User;  User.objects.create_superuser('$SENTRY_USER', 'admin@admin.moc', '$SENTRY_PASS')" | /usr/local/bin/sentry --config=/etc/sentry.conf.py shell

    touch /run/pgsql-after-init.hook

    touch /data/is_bootstrapped
}