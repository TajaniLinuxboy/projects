FROM python:3.11

USER root

COPY Requirements/NonPython/requirements.txt .

RUN apt-get -y update && \
    apt-get -y install sudo && \
    xargs -a requirements.txt apt-get -y -m install


WORKDIR home

RUN adduser --disabled-password --gecos '' docker

USER docker

WORKDIR /home/docker

ENV MYCONFIG='.env.ini'

RUN mkdir -p .local/bin

ENV PATH=$PATH:/home/docker/.local/bin

COPY Requirements/Python/requirements.txt .

RUN python3 -m pip install -r requirements.txt

COPY django_backend/project_settings .

USER root

RUN chown -R docker.docker *

USER docker

RUN python manage.py makemigrations 

RUN python manage.py migrate

CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000" ]