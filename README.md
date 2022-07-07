# Zealot - 偏执的 DRF 项目生成器
Zealot 是一个面向 [DRF 框架](https://www.django-rest-framework.org/)的生成器。

正如项目名描述，与其他通用型的生成器不同的是，它对某些依赖的选择是更偏执的，针对一些特定场景有着更好的规范定义作用。

该项目以 [Cookiecutter](https://github.com/cookiecutter/cookiecutter) 为基础，特此感谢相关社区 ❤️ 。

## 特性
- 支持前后端大仓开发
- 可以轻松开启 [API 编写最佳方案](docs/why_choose_yasg.md)
- 天然支持容器镜像构建（包括前端！）
- 支持通过 Docker Compose 构建全套运行环境


## 快速开始

生成新的项目
```shell
cookiecutter gh:IMBlues/zealot -o PROJECT-PATH-YOU-WANT/
```
我们支持较多的配置，可以自由选择想使用的模块，具体使用方法请参考 [Zealot 使用指南](docs/how_to_use_zealot.md)。

项目生成后，可以通过 `PROJECT-PATH-YOU-WANT/README.md` 查看项目详情，也可以通过 [示例项目](example/zealot_example/README.md) 来了解更多。


## 协议

基于 MIT 协议，详情请参考 [LICENSE](LICENSE)。
