FROM createdigitalspb/py2:1.4

MAINTAINER Vladimir Shulyak <vladimir@shulyak.net>


# Sentry service
RUN mkdir /etc/service/sentry
ADD run_sentry.sh /etc/service/sentry/run
RUN chmod 755 /etc/service/sentry/run

ADD /requirements.txt /var/tmp/requirements.txt
RUN pip install -r /var/tmp/requirements.txt

ADD /sentry.conf.py /etc/sentry.conf.py

EXPOSE 9000

# Clean up
RUN rm -rf /tmp/* /var/tmp/*