# syntax=docker/dockerfile:1

# Use Ubuntu as base image to closely match live system
FROM ubuntu:22.04

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

# update the package list and install necessary packages
RUN apt update && \
    apt install -y \
    python3 python3-venv python3-pip python3-dev \
    build-essential libcurl4-openssl-dev libssl-dev \
    libjpeg-dev zlib1g-dev \
    git firefox


# install python requirements package
COPY requirements requirements
RUN pip install -r requirements/local.txt

COPY compose/django/start.sh compose/django/start.sh
RUN chmod +x /app/compose/django/start.sh