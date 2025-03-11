# Dockerfile

# pull the official docker image -> check if version still good
FROM python:3.10.7-slim

ARG ENVIRONMENT

# set env variables

ENV ENVIRONMENT=${ENVIRONMENT} \
    POETRY_VERSION=1.3.1 \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    PIP_NO_CACHE_DIR=off \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

COPY . /app

RUN apt-get update -y && apt-get install -y gcc

# System deps:
RUN pip install "poetry==$POETRY_VERSION"

# set work directory
WORKDIR /app

# Project initialization:
RUN poetry config virtualenvs.create false &&  \
    poetry install --no-interaction --no-ansi && \
    adduser --disabled-password appuser

USER appuser
