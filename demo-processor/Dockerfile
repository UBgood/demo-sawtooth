FROM ubuntu:jammy-20211029

ARG DEBIAN_FRONTEND=noninteractive

RUN \
 apt-get update \
 && apt-get install -y -q curl gnupg \
 && curl -sSL 'http://p80.pool.sks-keyservers.net/pks/lookup?op=get&search=0x8AA7AF1F1091A5FD' | apt-key add -  \
 && echo 'deb [arch=amd64] http://repo.sawtooth.me/ubuntu/chime/stable bionic universe' >> /etc/apt/sources.list \
 && apt-get update \
 && apt-get install -y -q \
    apt-transport-https \
    build-essential \
    ca-certificates \
    python3-sawtooth-sdk \
    python3-protobuf \
    python3-pandas \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

EXPOSE 4004/tcp

WORKDIR /project/demo/demo-processor
ENV PATH "$PATH:/project/demo/demo-processor"

CMD bash -c './demo_tp'
