FROM python:2.7-slim

RUN pip install gunicorn json-logging-py falcon

COPY logging.conf /logging.conf
COPY gunicorn.conf /gunicorn.conf

COPY simple_api.py /
COPY simple_api.py /var/

EXPOSE 8000

ENTRYPOINT ["/usr/local/bin/gunicorn", "--config", "/gunicorn.conf", "--log-config", "/logging.conf", "-b", ":8000", "simple_api:api"]