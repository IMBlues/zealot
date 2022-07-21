#!make
repo ?= "mirrors.tencent.com"
version ?= "staging"
platform ?= "linux/amd64,linux/arm64"
listen_port ?= "8001"
dev_env_file ?= "src/api/zealot/settings/.env"
compose_mysql_password ?= "C0mp0sePassw0rd"

build:
	docker build .  -t ${repo}/zealot_example:${version}

push:
	docker push ${repo}/zealot_example:${version}

buildx:
	docker buildx build . --platform ${platform} -t ${repo}/zealot_example:${version} --push

migrate:
	export DJANGO_SETTINGS_MODULE="zealot.settings.overlays.dev" && \
	cd src/api && poetry run python manage.py migrate

test:
	cd src/api && pytest --disable-pytest-warnings --reuse-db

run-api:
	export DJANGO_SETTINGS_MODULE="zealot.settings.overlays.dev" && \
	cd src/api && poetry run python manage.py runserver 0.0.0.0:${listen_port}

run-ui:
	cd src/ui && npm run dev

run:
	mkdir -p .services/
	# docker pull ${repo}/zealot_example:${version}

	STORAGE_ROOT=.services/ MYSQL_ROOT_PASSWORD=x${compose_mysql_password} REPO=${repo} TAG=${version} PORT=${listen_port}  \
	docker-compose --env-file ${dev_env_file} -f docker-compose.yaml up -d

stop:
	STORAGE_ROOT=.services/ MYSQL_ROOT_PASSWORD=${compose_mysql_password} REPO=${repo} TAG=${version} PORT=${listen_port} \
	docker-compose --env-file ${dev_env_file} -f docker-compose.yaml down

start: build run

startx: buildx run