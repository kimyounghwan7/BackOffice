FROM node:22.14.0-alpine
WORKDIR /usr/src/app
COPY . /usr/src/app/
RUN apk update && apk add bash
RUN apk add tzdata
RUN ln -snf /usr/share/zoneinfo/Asia/Seoul /etc/localtime