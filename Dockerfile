ARG PYTHON_VERSION=3.11.2

FROM python:$PYTHON_VERSION as staging

ENV \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONFAULTHANDLER=1

WORKDIR /app
COPY ./app .

RUN apt-get update -y \
    && apt-get install netcat -y \
    && apt-get install -y --no-install-recommends graphviz \
    && apt-get upgrade -y \
    && rm -rf /var/lib/apt/lists/* \
    && chmod -R 777 . \
    && pip install --upgrade pip \
    && pip install --no-cache-dir -r /app/requirements.txt \
    && pip freeze > /app/requirements.txt


RUN chmod u+x /app/entrypoint.sh