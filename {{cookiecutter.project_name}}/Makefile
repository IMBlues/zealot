#!make
repo ?= "{{cookiecutter.prefer_docker_registry}}"
version ?= "staging"
platform ?= "linux/amd64,linux/arm64"
listen_port ?= "{{cookiecutter.local_dev_port}}"
dev_env_file ?= "src/api/{{cookiecutter.api_name}}/settings/.env"

build:
	docker build .  -t ${repo}/{{cookiecutter.project_name}}:${version}

push:
	docker push ${repo}/{{cookiecutter.project_name}}:${version}

buildx:
	docker buildx build . --platform ${platform} -t ${repo}/{{cookiecutter.project_name}}:${version} --push

migrate:
	export DJANGO_SETTINGS_MODULE="{{cookiecutter.api_name}}.settings.overlays.dev" && \
	cd src/api && poetry run python manage.py migrate

test:
	cd src/api && pytest --disable-pytest-warnings --reuse-db

run-backend:
	export DJANGO_SETTINGS_MODULE="{{cookiecutter.api_name}}.settings.overlays.dev" && \
	cd src/api && poetry run python manage.py runserver 0.0.0.0:${listen_port}

run-frontend:
	cd src/front && npm run dev

run:
	mkdir -p .services/
	# docker pull ${repo}/{{cookiecutter.project_name}}:${version}

	STORAGE_ROOT=.services/ MYSQL_ROOT_PASSWORD=123456 REPO=${repo} TAG=${version} PORT=${listen_port}  \
	docker-compose --env-file ${dev_env_file} -f docker-compose.yaml up -d

stop:
	STORAGE_ROOT=.services/ MYSQL_ROOT_PASSWORD=123456 REPO=${repo} TAG=${version} PORT=${listen_port} \
	docker-compose --env-file ${dev_env_file} -f docker-compose.yaml down

start: build run

startx: buildx run