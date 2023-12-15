FROM python:3.10.13-slim-buster

RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y git && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt /requirements.txt
WORKDIR /

RUN pip3 install --no-cache-dir -U pip && \
    pip3 install --no-cache-dir -U -r requirements.txt

RUN mkdir /Auto-search-tamil-bot
WORKDIR /Auto-search-tamil-bot

COPY start.sh /start.sh
CMD ["/bin/bash", "/start.sh"]
