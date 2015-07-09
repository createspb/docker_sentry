FROM createdigitalspb/py2:1.4

MAINTAINER Vladimir Shulyak <vladimir@shulyak.net>


# Sentry service
RUN mkdir /etc/service/sentry && mkdir /etc/service/sentry_worker
ADD run_sentry.sh /etc/service/sentry/run
ADD run_sentry_worker.sh /etc/service/sentry_worker/run
RUN chmod 755 /etc/service/sentry/run && chmod 755 /etc/service/sentry_worker/run

ADD /requirements.txt /var/tmp/requirements.txt
RUN pip install -r /var/tmp/requirements.txt

ADD /sentry.conf.py /etc/sentry.conf.py

RUN mkdir /var/log/sentry
RUN chown www-data:www-data /var/log/sentry

EXPOSE 9000

# Clean up
RUN rm -rf /tmp/* /var/tmp/*