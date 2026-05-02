FROM docker.arvancloud.ir/python:3.11.0-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY requirements.txt /app/

RUN pip install -i https://mirror-pypi.runflare.com/simple --no-cache-dir --upgrade --upgrade pip
RUN pip install -i https://mirror-pypi.runflare.com/simple --no-cache-dir --upgrade -r requirements.txt

COPY ./core /app/

CMD python3 manage.py runserver 0.0.0.0:8000
