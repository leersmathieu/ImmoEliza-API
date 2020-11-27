FROM python:3.7-slim-buster

COPY main.py /opt/app/
COPY model_bin/apart_model.p /opt/app/model_bin/
COPY model_bin/house_model.p /opt/app/model_bin/

COPY requirements.txt /

RUN apt-get update
RUN apt-get clean
RUN apt-get install libgomp1

RUN pip install gunicorn
RUN pip install -r requirements.txt

WORKDIR /opt/app/
CMD python main.py