FROM python:3.10.7-alpine3.16

COPY requirements.txt /temp/requirements.txt
COPY server /server
WORKDIR /server
EXPOSE 8000

RUN apk add postgresql-client build-base postgresql-dev

RUN pip install -r /temp/requirements.txt

# RUN adduser --disabled-password server-user

# USER service-user