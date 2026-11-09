# Older base image on purpose so Xray also reports OS-level findings.
FROM python:3.9-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /srv

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app

ARG APP_VERSION=dev
ENV APP_VERSION=${APP_VERSION}

EXPOSE 8080
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app.main:app"]
