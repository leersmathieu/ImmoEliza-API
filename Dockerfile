FROM python:3.7-slim-buster

COPY main.py /opt/app/
COPY requirements.txt /

RUN apt-get update
RUN apt-get clean

RUN pip install gunicorn
RUN pip install -r requirements.txt

WORKDIR /opt/app/
CMD python main.py