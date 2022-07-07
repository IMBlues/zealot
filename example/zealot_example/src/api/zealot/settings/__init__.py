import environ

env = environ.Env()

# 仅在开发环境下读取 .env 文件
if env.str("DJANGO_SETTINGS_MODULE").endswith("dev"):
    env.read_env()
