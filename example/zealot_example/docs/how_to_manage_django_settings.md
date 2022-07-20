# Django Settings 设计

当前我们将 Django 分成两层：
- 通用配置层 zealot/settings/*.py
- 环境层 zealot/settings/overlays/*.py

前者存放通用项目配置，可以按照具体场景来划分不同的文件。
后者则是针对不同部署环境，将本地开发、预发布、正式等环境的不同变量区分开，单向依赖通用项目配置

## 通过环境变量解耦
当存在不同环境需要不同的配置时，更推荐使用环境变量来实现数据与结构的解耦。
可以参看 [get_db_config 方法](../src/api/zealot/settings/utils.py)
