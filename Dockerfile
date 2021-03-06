# pull base image
FROM python:3.10

# set envorenment variables
ENV PYTHONDONTWRITEBYTCODE 1
ENV PYTHONUNBUFFERED 1

# set work directory
RUN mkdir /code
WORKDIR /code

# install dependencies

COPY ./requirements.txt /code/
#RUN apk add gcc
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /code/