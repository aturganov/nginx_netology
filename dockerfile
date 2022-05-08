FROM python:3.9
LABEL maintainer "Турганов Артем"

WORKDIR /usr/src/www

COPY . /usr/src/www/  

RUN pip install -r requirements.txt

USER root

EXPOSE 5002