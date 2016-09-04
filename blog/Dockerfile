# MAINTAINER        Gevin <flyhigher139@gmail.com>
# DOCKER-VERSION    1.6.2
#
# Dockerizing Ubuntu: Dockerfile for building Ubuntu images


FROM       ubuntu:14.04
MAINTAINER Gevin <flyhigher139@gmail.com>

RUN apt-get update && apt-get install -y curl vim && \
    apt-get install -y nginx git python-dev python-pip libpq-dev postgresql-client && \
    apt-get clean all


RUN echo "daemon off;" >> /etc/nginx/nginx.conf

RUN pip install supervisor uwsgi

ADD supervisord.conf /etc/supervisord.conf

RUN mkdir -p /etc/supervisor.conf.d && \
    mkdir -p /var/log/supervisor

RUN mkdir -p /usr/src/app && mkdir -p /var/log/uwsgi
WORKDIR /usr/src/app

ADD requirements.txt /usr/src/app/requirements.txt
RUN pip install -r /usr/src/app/requirements.txt

COPY . /usr/src/app

RUN ln -s /usr/src/app/mayblog_nginx.conf /etc/nginx/sites-enabled


RUN /usr/bin/python2.7 manage.py collectstatic --noinput


EXPOSE 8000


CMD ["/bin/bash", "/usr/src/app/init.sh"]
