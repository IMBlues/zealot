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