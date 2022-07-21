# zealot_example 项目开发指引

## 项目架构释义

### 项目分层



### 目录释义
```bash
zealot_example
├── ...
├── docs                                  # 项目文档目录
│   └── ...
└── src                                   # 项目源码目录
    ├── ...
    ├── api                               # 后台 API 模块
    │   ├── ...
    │   ├── bin
    |         | ...           
    │   └── zealot     # Django 项目根目录 
    │       ├── common                    # 项目通用工具目录
    │       ├── settings                  # 项目配置目录
    │       │   ├── ...
    │       │   ├── django.py
    │       │   ├── utils.py
    │       │   └── overlays              # 环境配置目录
    │       │       ├── ...
    │       │       ├── dev.py
    │       │       └── prod.py
    │       └── ...
    └── ui                             # 前端项目模块
        └── package.json  
```

## 如何在本地开启服务

### 方式一：拉起进程

```shell
# 首次运行需要运行 poetry install 安装依赖
make run-api
```

```shell
# 首次运行需要运行 npm i 安装依赖
make run-ui
```

### 方式二：本地构建镜像并拉起容器

Linux or Intel Mac
```shell
# 构建镜像，前端 + 后端
# 当本地代码更新后，需要再次构建
make build

# 将镜像更新到远端仓库
make push
```

M1 Mac Series
```bash
# arm64 机器需要额外安装 buildx
# 需要注意，此时会包括 build & push 两个操作
make buildx
```

镜像就绪后，本地运行容器
```bash
# 拉起容器，首次启动会尝试拉取镜像，等待时间稍长
make run

# 构建并拉起，
# 启动后会在项目路径下创建 .services 路径，其中会包括 mysql 存储文件
make start
```

本地 `localhost:8001` 即可访问系统。

或者 `localhost:8001/swagger/` 访问 API 文档。

如果本地不再需要该服务，可以删除容器：
```shell
make stop
```
剩余的镜像请通过 docker 命令手动删除。

## 如何持续开发

项目生成后，你可以按照自己的喜好随意改造代码，但这里我们偏执地推荐一些开发模式：
- [如何管理 Django settings](how_to_manage_django_settings.md)
- [如何做数据库 Migrate](how_to_migrate.md)
- [如何开发 API](how_to_develop_api.md)
- [如何打印日志](how_to_logging.md)

