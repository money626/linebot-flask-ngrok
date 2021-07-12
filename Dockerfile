FROM  python:3.8.9-alpine3.13

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN apk update \
    && apk add --no-cache jpeg-dev zlib-dev \
    && apk add --no-cache --virtual .build-deps build-base linux-headers \
    && pip install --no-cache-dir -r requirements.txt
COPY . .
ENV FLASK_APP=main.py

CMD ["flask", "run"]