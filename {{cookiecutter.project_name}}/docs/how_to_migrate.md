# 数据库 Migrate
你可以有多种方式执行数据库 migrate。

## 本地开发
```bash
make migrate
```

## 线上运行
可以设置环境变量 `RUN_MIGRATE=1`，启动脚本会在拉起进程时执行 migrate， 但是需要注意当线上多副本运行时，变更可能会产生竞争问题。