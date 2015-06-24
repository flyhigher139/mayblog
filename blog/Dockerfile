#
# MAINTAINER        Gevin <flyhigher139@gmail.com>
# DOCKER-VERSION    1.6.2
#
# Dockerizing Ubuntu: Dockerfile for building Ubuntu images
#
FROM       ubuntu:14.04
MAINTAINER Gevin <flyhigher139@gmail.com>

ENV TZ "Asia/Shanghai"
ENV TERM xterm

ADD sources.list /etc/apt/sources.list


RUN apt-get update && apt-get install -y curl wget tar bzip2 unzip vim && \
    apt-get install -y nginx git python-dev python-pip libmysqlclient-dev && \
    apt-get clean all

# RUN pip install supervisor uwsgi -i http://pypi.douban.com/simple

# ADD supervisord.conf /etc/supervisord.conf

# RUN mkdir -p /etc/supervisor.conf.d && \
#     mkdir -p /var/log/supervisor

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY . /usr/src/app
RUN pip install -r /usr/src/app/requirements.txt
# RUN ln -s /usr/src/app/mayblog_nginx.conf /etc/nginx/sites-enabled && \
#     service nginx restart

# RUN python manage.py collectstatic --noinput && python manage.py migrate
RUN /usr/bin/python2.7 manage.py migrate && \
    /usr/bin/python2.7 manage.py createsuperuser --username admin --email admin@gmail.com --noinput


EXPOSE 8000

# ENTRYPOINT ["/bin/bash"]
# CMD ["/bin/bash"]
CMD ["/usr/bin/python2.7", "manage.py", "runserver", "0.0.0.0:8000"]
