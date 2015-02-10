FROM phusion/baseimage:0.9.16

MAINTAINER Vladimir Shulyak <vladimir@shulyak.net>

RUN apt-get update
RUN apt-get install -y postgresql postgresql-contrib libpq-dev
RUN apt-get install -y build-essential python-dev python-lxml python-pip
RUN apt-get install -y pwgen inotify-tools


# Sentry and Postrgres service
RUN mkdir /etc/service/postgres
ADD run_postgres.sh /etc/service/postgres/run
RUN chmod 755 /etc/service/postgres/run

RUN mkdir /etc/service/sentry
ADD run_sentry.sh /etc/service/sentry/run
RUN chmod 755 /etc/service/sentry/run


ADD /requirements.txt /var/tmp/requirements.txt
RUN pip install -r /var/tmp/requirements.txt

ADD /sentry.conf.py /etc/sentry.conf.py


#USER postgres
RUN service postgresql start && service postgresql stop

# based on https://github.com/Painted-Fox/docker-postgresql/blob/master/Dockerfile
ADD /first_run.sh /home/first_run.sh
ADD /normal_run.sh /home/normal_run.sh
RUN chmod 755 /home/first_run.sh
RUN chmod 755 /home/normal_run.sh

RUN touch /firstrun

# Cofigure the database to use our data dir.
RUN sed -i -e"s/data_directory =.*$/data_directory = '\/data'/" /etc/postgresql/9.3/main/postgresql.conf
# Allow connections from anywhere.
RUN sed -i -e"s/^#listen_addresses =.*$/listen_addresses = '*'/" /etc/postgresql/9.3/main/postgresql.conf
RUN echo "host    all    all    0.0.0.0/0    md5" >> /etc/postgresql/9.3/main/pg_hba.conf

VOLUME ["/data", "/var/log/postgresql", "/etc/postgresql"]

EXPOSE 9000 5432

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*