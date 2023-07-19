FROM python:3.9-bullseye as base

ENV APP_HOME /app

RUN apt update
RUN apt upgrade -y

RUN rm -rf /var/cache/apk/*

WORKDIR /app
COPY .. /app

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install --no-cache-dir wheel
RUN pip install --no-cache-dir --force-reinstall -r requirements.txt
RUN pip install --no-cache-dir --force-reinstall -r requirements_test.txt
