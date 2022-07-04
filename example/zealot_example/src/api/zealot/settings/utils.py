""""""
from . import env

formatters = {
    "verbose": {
        "format": "%(levelname)s [%(asctime)s] %(lineno)d %(funcName)s %(process)d %(thread)d %(message)s \n",
        "datefmt": "%Y-%m-%d %H:%M:%S",
    },
    "simple": {"format": "%(levelname)s %(message)s"},
}


def get_loggers(package_name: str, log_level: str) -> dict:
    return {
        "django": {
            "handlers": ["null"],
            "level": "INFO",
            "propagate": True,
        },
        "django.request": {
            "handlers": ["root"],
            "level": "ERROR",
            "propagate": True,
        },
        "django.db.backends": {
            "handlers": ["root"],
            "level": "INFO",
            "propagate": True,
        },
        "django.security": {
            "handlers": ["root"],
            "level": "INFO",
            "propagate": True,
        },
        package_name: {
            "handlers": ["root"],
            "level": log_level,
            "propagate": True,
        },
        "requests": {
            "handlers": ["root"],
            "level": log_level,
        },
    }


def get_stdout_logging(log_level: str, package_name: str, formatter: str = "verbose"):
    """get stdout logging config"""
    log_class = "logging.StreamHandler"

    return {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": formatters,
        "handlers": {
            "null": {"level": "DEBUG", "class": "logging.NullHandler"},
            "root": {
                "class": log_class,
                "formatter": formatter,
            },
            "component": {
                "class": log_class,
                "formatter": formatter,
            },
        },
        "loggers": get_loggers(package_name, log_level),
    }


def get_db_config(db_prefix: str = "DB") -> dict:
    """get mysql-like db config"""
    return {
        "default": {
            "ENGINE": "django.db.backends.mysql",
            "NAME": env.str(f"{db_prefix}_NAME"),
            "USER": env.str(f"{db_prefix}_USER"),
            "PASSWORD": env.str(f"{db_prefix}_PASSWORD"),
            "HOST": env.str(f"{db_prefix}_HOST"),
            "PORT": env.int(f"{db_prefix}_PORT"),
            "OPTIONS": {"charset": "utf8mb4"},
            "TEST": {"CHARSET": "utf8mb4", "COLLATION": "utf8mb4_general_ci"},
        },
    }