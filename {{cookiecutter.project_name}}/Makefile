#!make
repo ?= "{{cookiecutter.prefer_docker_registry}}"
version ?= "staging"
platform ?= "linux/amd64,linux/arm64"
listen_port ?= "{{cookiecutter.local_dev_port}}"
dev_env_file ?= "src/api/{{cookiecutter.api_name}}/settings/.env"
ui_dist_dir ?= "src/ui/dist/"
compose_mysql_password ?= "{{cookiecutter.local_dev_db_password}}"
with_pull ?= "0"

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

run-api:
	if [ ! -f ${dev_env_file} ]; \
		then \
			mv "src/api/{{cookiecutter.api_name}}/settings/env.example" ${dev_env_file}; \
	fi

	if [ ! -e ${ui_dist_dir} ]; \
		then \
			cd src/ui && npm i && npm run build; \
	fi

	export DJANGO_SETTINGS_MODULE="{{cookiecutter.api_name}}.settings.overlays.dev" && \
	cd src/api && poetry run python manage.py migrate && poetry run python manage.py runserver 0.0.0.0:${listen_port}

run-ui:
	cd src/ui && npm run dev

run:
	mkdir -p .services/

	if [ ! -f ${dev_env_file} ]; \
		then \
			mv "src/api/{{cookiecutter.api_name}}/settings/env.example" ${dev_env_file}; \
	fi

	if [ "$(with_pull)" == "1" ]; \
		then \
			docker pull ${repo}/{{cookiecutter.project_name}}:${version}; \
	fi

	STORAGE_ROOT=.services/ MYSQL_ROOT_PASSWORD=x${compose_mysql_password} REPO=${repo} TAG=${version} PORT=${listen_port}  \
	docker-compose --env-file ${dev_env_file} -f docker-compose.yaml up -d

stop:
	STORAGE_ROOT=.services/ MYSQL_ROOT_PASSWORD=${compose_mysql_password} REPO=${repo} TAG=${version} PORT=${listen_port} \
	docker-compose --env-file ${dev_env_file} -f docker-compose.yaml down

start: build run

startx: buildx run