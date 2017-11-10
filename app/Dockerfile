FROM ubuntu:16.04

RUN apt-get update && \
            apt-get install -y --no-install-recommends git \
            python3 \
            python3-pip \
            python3-dev \
            python3-setuptools \
            supervisor \
            nginx \
            libmysqlclient-dev \
            unattended-upgrades && \
            pip3 install -U pip setuptools && \
            rm -r /var/lib/apt/lists/*    

RUN pip3 install uwsgi \
      && pip3 install "mysqlclient==1.3.8"


# setup all the config files
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
COPY nginx-app.conf /etc/nginx/sites-available/default
COPY supervisor-app.conf /etc/supervisor/conf.d/

# COPY requirements.txt and RUN pip install BEFORE adding the rest of your code, this will cause Docker's caching mechanism
# to prevent re-installing (all your) dependencies when you made a change a line or two in your app.

COPY app/requirements.txt /home/docker/code/app/
RUN pip3 install -r /home/docker/code/app/requirements.txt

# add (the rest of) our code
COPY . /home/docker/code/

WORKDIR /app

EXPOSE 80
CMD ["supervisord", "-n"]




