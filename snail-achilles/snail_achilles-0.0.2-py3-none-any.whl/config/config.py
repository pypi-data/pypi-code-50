import os
import sys
import yaml


class ImproperlyConfigured(Exception):
    """Server is somehow improperly configured"""

    pass


CONFIG_PATH = "./config/config.yaml"
# 从配置文件更新
if os.path.exists(CONFIG_PATH):
    with open(CONFIG_PATH, "r") as f:
        config_dict = yaml.load(f.read(), Loader=yaml.FullLoader)
else:
    sys.stderr.write(f"请确认配置文件{CONFIG_PATH}是否存在!! 配置文件信息请见 README.MD#Configuration\n")
    exit(0)


def _get_config(field, default=None):
    if field in config_dict.keys():
        return config_dict[field]
    else:
        if default is None:
            raise ImproperlyConfigured(f"缺失必须的配置信息 {field}")
        else:
            sys.stderr.write(f"缺失配置信息{field}，现使用默认值{default}.\n")
            return default


# 数据库
POSTGRES_HOST = _get_config("POSTGRES_HOST", "127.0.0.1")
POSTGRES_PORT = _get_config("POSTGRES_PORT", 5432)
POSTGRES_DATABASE = _get_config("POSTGRES_DATABASE", "achilles")
POSTGRES_USERNAME = _get_config("POSTGRES_USERNAME", "postgres")
POSTGRES_PASSWORD = _get_config("POSTGRES_PASSWORD", "snail123")

# 文件oss
STATIC_OSS_URL = _get_config("STATIC_OSS_URL", "/algorithm/static/")
STATIC_OSS_ROOT = _get_config("STATIC_OSS_ROOT", "algorithm/static")
MEDIA_OSS_URL = _get_config("MEDIA_OSS_URL", "/algorithm/media/")
MEDIA_OSS_ROOT = _get_config("MEDIA_OSS_ROOT", "algorithm/media")
OSS_ACCESS_KEY_ID = _get_config("OSS_ACCESS_KEY_ID", "W9kszZirPgV2dsY8")
OSS_ACCESS_KEY_SECRET = _get_config("OSS_ACCESS_KEY_SECRET", "I7xGiBHmFY7LGgzVkdoSMQoiPZ0V8d")
OSS_BUCKET_NAME = _get_config("OSS_BUCKET_NAME", "litibaba")
OSS_ENDPOINT = _get_config("OSS_ENDPOINT", "https://oss-cn-beijing.aliyuncs.com")
BUCKET_ACL_TYPE = _get_config("BUCKET_ACL_TYPE", "public-read")
OSS_EXPIRE_TIME = _get_config("OSS_EXPIRE_TIME", 600)
