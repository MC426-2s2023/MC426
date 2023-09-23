FROM python:3.8

ENV PYTHONUNBUFFERED 1

RUN mkdir /projeto_mc426

WORKDIR /projeto_mc426

RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY ../projeto_mc426/requirements.txt /projeto_mc426/

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

COPY ../projeto_mc426/ /projeto_mc426/