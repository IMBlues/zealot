# 如何开发 Zealot

## 查阅 cookiecutter 文档

我们并未在 cookiecutter 上做更多的扩展，开发新的内容时请直接参照 [cookiecutter 文档](https://cookiecutter.readthedocs.io/) 。

## 本地修改后查看效果

```shell
make test
```

在创建项目之后会尝试运行 `make run-api`，首次运行会尝试安装依赖。

## 生成示例项目
```shell
make generate
```
将会在 `example/` 目录下生成示例项目，可以查看具体效果。