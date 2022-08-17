# Zealot - 偏执的 DRF 项目生成器
Zealot 是一个面向 [DRF 框架](https://www.django-rest-framework.org/) 的项目生成器。

正如项目名描述，与其他通用型的生成器不同的是，它对某些依赖的选择是更偏执的，针对一些特定场景有着更好的规范定义作用。

该项目以 [Cookiecutter](https://github.com/cookiecutter/cookiecutter) 为基础，特此感谢相关社区 ❤️ 。

## 特性
- 基于 [django-environ](https://github.com/joke2k/django-environ) 实现，满足[十二法则](https://12factor.net/) 的 settings 实现
- 前后端大仓开发，默认附带 [VueJS](https://vuejs.org/) 示例项目
- 支持 [Docker](https://www.docker.com/) 镜像一键构建（包括前端！）
- 支持 [Gunicorn](https://gunicorn.org/) wsgi 项目启动最佳实践
- 支持通过 [Docker Compose](https://docs.docker.com/compose/) 构建全套运行环境
- 支持基于 [PEP-621](https://peps.python.org/pep-0621/) 的全工具链 *(mypy\isort\flake8\black)* 配置方案
- 代码规范类 [pre-commit](https://pre-commit.com/) 整合
- 支持 API 自动化文档，**建议阅读[指引](example/zealot_example/docs/how_to_develop_api.md)，了解更多**

## 快速开始

安装 `cookiecutter`（已安装可跳过）
```shell
pip install cookiecutter
```

生成新的项目
```shell
cookiecutter gh:IMBlues/zealot
```
我们支持较多的配置，可以自由选择想使用的模块，具体使用方法请参考 [Zealot 配置指南](docs/how_to_configure_zealot.md)。

项目生成后，可以通过项目根路径下的 `README.md` 查看详情，也可以通过 [示例项目](example/zealot_example/README.md) 来了解更多。

## 参与开发

Zealot 的开发和大多数 cookiecutter 项目一样简单，可以参考 [Zealot 开发指南](docs/how_to_develop_zealot.md) 了解更多。


## 协议

基于 MIT 协议，详情请参考 [LICENSE](LICENSE)。
