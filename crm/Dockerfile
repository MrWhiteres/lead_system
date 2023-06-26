FROM python:3.11.4-alpine3.18

WORKDIR ./crm

EXPOSE 8000

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . .

RUN pip install --no-cache-dir -r requirements.txt
RUN apk add postgresql-client build-base postgresql-dev
RUN adduser --disabled-password --no-create-home backend-user

USER backend-user

