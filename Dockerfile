FROM python:2.7

ENV PYTHONUNBUFFERED 1

RUN pip install -U pip 3to2

RUN mkdir -p /code/
WORKDIR /code

ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt --no-cache-dir

ENV DOCKER 1

EXPOSE 8000