FROM python:3.9-alpine

COPY requirements.txt /temp/requirements.txt
COPY ./hardware_store /hardware_store
WORKDIR /hardware_store
EXPOSE 8000

RUN pip install -r /temp/requirements.txt

RUN adduser --disabled-password user

USER user

