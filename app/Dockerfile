FROM grahamdumpleton/mod-wsgi-docker:python-3.5

RUN apt-get update && \
            apt-get install -y --no-install-recommends git \
            python-pip \
            python-dev \
            supervisor \
            libmysqlclient-dev \
            unattended-upgrades && \
            rm -r /var/lib/apt/lists/*

ADD . /app

ADD requirements.txt /app/requirements.txt
RUN cd /app && pip install -r /app/requirements.txt

RUN pip install --upgrade pip \ 
      && pip install "django==1.11" \ 
      && pip install "mysqlclient==1.3.8" \
      && pip install "kafka-python<=1.0" \
      && pip install "elasticsearch<3.0"

EXPOSE 8002

WORKDIR /app

CMD ["sh", "./start.sh"]