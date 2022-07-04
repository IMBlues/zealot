FROM node:12.16.3-stretch-slim AS StaticBuilding
ENV NPM_VERSION 6.14.4

# install requirements & build
COPY src/front /
WORKDIR /

RUN npm config set registry https://mirrors.tencent.com/npm/
RUN npm i
RUN npm run build

FROM python:~3.10-slim-buster AS SaaSBuilding
USER root

RUN rm /etc/apt/sources.list && \
    echo "deb https://mirrors.cloud.tencent.com/debian buster main contrib non-free" >> /etc/apt/sources.list && \
    echo "deb https://mirrors.cloud.tencent.com/debian buster-updates main contrib non-free" >> /etc/apt/sources.list && \
    echo "deb-src https://mirrors.cloud.tencent.com/debian buster main contrib non-free" >> /etc/apt/sources.list && \
    echo "deb-src https://mirrors.cloud.tencent.com/debian buster-updates main contrib non-free" >> /etc/apt/sources.list

RUN mkdir ~/.pip &&  printf '[global]\nindex-url = https://mirrors.tencent.com/pypi/simple/' > ~/.pip/pip.conf

RUN apt-get update && apt-get install -y gcc

ENV LC_ALL=C.UTF-8 \
    LANG=C.UTF-8

RUN pip install --upgrade setuptools pip
RUN pip install poetry==1.1.13

WORKDIR /app
COPY src/api/pyproject.toml /app
COPY src/api/poetry.lock /app

RUN poetry config virtualenvs.create false && poetry install --no-dev

COPY src/api/manage.py /app
COPY src/api/zealot/wsgi.py /app
COPY src/api/zealot /app/zealot
COPY src/api/bin/start.sh /app
COPY --from=StaticBuilding /dist/ /app/zealot/dist/

CMD ["bash", "/app/start.sh"]