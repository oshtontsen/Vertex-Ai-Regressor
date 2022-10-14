FROM python:3.7-slim

WORKDIR /app

COPY . /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

CMD gunicorn --bind 0.0.0.0:5005 --timeout=150 app:app -w 5

EXPOSE 5005