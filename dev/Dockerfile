FROM node:17.3-slim

WORKDIR /app

# Python
RUN apt-get update \
    && apt-get install -y curl nkf wget python3-pip graphviz xdg-utils \
    && alias pip=pip3 \
    && alias python=python3
ADD requirements.txt /app/
RUN pip install -r requirements.txt

# Node.js
RUN npm install @nuxtjs/eslint-config-typescript