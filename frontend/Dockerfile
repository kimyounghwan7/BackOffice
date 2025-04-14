FROM node:22.14.0-slim
WORKDIR /usr/src/app
COPY . /usr/src/app/
RUN apt-get update && apt-get install -y bash tzdata
RUN ln -snf /usr/share/zoneinfo/Asia/Seoul /etc/localtime && \
	echo "Asia/Seoul" > /etc/timezone