FROM python:3.11

USER root

RUN apt-get -y update && apt-get -y install sudo

RUN adduser --disabled-password --gecos '' docker

USER docker

WORKDIR /home/docker

RUN mkdir -p .local/bin 

ENV PATH=$PATH:/home/docker/.local/bin

ENV MYCONFIG='.env.ini'

COPY django/requirements/requirements.txt .

RUN python3 -m pip install -r requirements.txt

WORKDIR app

COPY project_settings/ .

USER root

RUN chown -R docker.docker *

USER docker

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

