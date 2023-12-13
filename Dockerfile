FROM python:3.10.8-slim-buster

RUN apt-get update && apt-get upgrade -y \
    && apt-get install -y git

WORKDIR /Auto-search-tamil-bot

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

CMD ["/bin/bash", "start.sh"]
