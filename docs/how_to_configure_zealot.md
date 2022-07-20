# 如何使用 Zealot

## 配置详解

`cookiecutter.json` 配置详细说明

### project_name

项目名称，通常用来描述整个项目，内部可能包括多个功能模块。

### api_name

后段 API 模块名称，该模块在项目架构中扮演 `apiServer` 的角色。

### author

项目作者。将被适当地填入各种工具配置中。

### description

项目描述。将被适当地填入各种工具配置中。

### license

开源协议，当前仅支持 MIT。

### license_owner

协议作者。将被适当地填入协议描述中。

### license_header

文件协议头，将在被填入生成的源码文件开头。不需要时留空。

### python_version

API 模块使用的 Python 版本。

### django_version

API 模块中 [Django 框架](https://www.djangoproject.com/) 版本。

### drf_version

API 模块中 [DRF 框架](https://www.django-rest-framework.org/) 版本。

### mysql_version

API 模块中的 MySQL 版本，默认为 `8.x`。

### 【WIP】node_version

UI 模块 [Node](https://nodejs.org/) 版本。

### 【WIP】npm_version

UI 模块 [NPM](https://www.npmjs.com/) 版本。

### prefer_debian_registry

偏好的 `debain` 软件镜像源，用于容器镜像构建，具体地址请根据所处网络环境自行选择。

### prefer_pypi

偏好的 `pypi` 软件镜像源，用于容器镜像构建，具体地址请根据所处网络环境自行选择。

### prefer_docker_registry

偏好的 `docker` 镜像源，用于容器镜像构建，具体地址请根据所处网络环境自行选择。

### prefer_npm_registry

偏好的 `npm` 软件镜像源，用于容器镜像构建，具体地址请根据所处网络环境自行选择。

### local_dev_port

本地开发进程启动端口，默认为`8001`。

###【WIP】with_poetry_install

当项目生成后，是否顺带执行 `poetry install`，懒人必备。

###【WIP】with_build_image

当项目生成后，是否顺带构建镜像，懒人必备。

###【WIP】with_run_backend

当项目生成后，是否顺带将后端以进程形式运行，同时会做 `poetry install` 操作，懒人必备。

### with_watermark

`README.md` 中附带 [Zealot](https://github.com/IMBlues/zealot) 项目水印开关。
