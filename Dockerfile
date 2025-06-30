FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt /app
RUN pip install --upgarde pip -r requirements.txt

COPY . /app

EXPOSE 5000
