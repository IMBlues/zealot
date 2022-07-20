FROM node:{{cookiecutter.node_version}}-stretch-slim AS StaticBuilding
ENV NPM_VERSION {{cookiecutter.npm_version}}

# install requirements & build
COPY src/ui /
WORKDIR /

RUN npm config set registry {{cookiecutter.prefer_npm_registry}}
RUN npm i
RUN npm run build

FROM python:{{cookiecutter.python_version}}-slim-buster AS SaaSBuilding
USER root

RUN rm /etc/apt/sources.list && \
    echo "deb {{cookiecutter.prefer_debian_registry}} buster main contrib non-free" >> /etc/apt/sources.list && \
    echo "deb {{cookiecutter.prefer_debian_registry}} buster-updates main contrib non-free" >> /etc/apt/sources.list && \
    echo "deb-src {{cookiecutter.prefer_debian_registry}} buster main contrib non-free" >> /etc/apt/sources.list && \
    echo "deb-src {{cookiecutter.prefer_debian_registry}} buster-updates main contrib non-free" >> /etc/apt/sources.list

RUN mkdir ~/.pip &&  printf '[global]\nindex-url = {{cookiecutter.prefer_pypi}}' > ~/.pip/pip.conf

RUN apt-get update && apt-get install -y gcc

ENV LC_ALL=C.UTF-8 \
    LANG=C.UTF-8

RUN pip install --upgrade setuptools pip
RUN pip install poetry==1.1.13

WORKDIR /app
COPY src/api/pyproject.toml /app

RUN poetry config virtualenvs.create false && poetry install --no-dev

COPY src/api/manage.py /app
COPY src/api/{{cookiecutter.api_name}}/wsgi.py /app
COPY src/api/{{cookiecutter.api_name}} /app/{{cookiecutter.api_name}}
COPY src/api/bin/start.sh /app
COPY --from=StaticBuilding /dist/ /app/{{cookiecutter.api_name}}/dist/

CMD ["bash", "/app/start.sh"]