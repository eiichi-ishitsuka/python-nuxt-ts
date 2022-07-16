FROM python:3.9.13-slim-bullseye

WORKDIR /opt/build

ADD backend/requirements.txt /opt/build/
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
