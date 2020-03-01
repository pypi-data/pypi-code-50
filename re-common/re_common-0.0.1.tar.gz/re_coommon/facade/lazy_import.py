# 延迟导入　主要是为了使用时不去安装多余的
from re_coommon.baselibrary import IniConfig


def get_TomlConfig():
    from re_coommon.baselibrary.readconfig.toml_config import TomlConfig
    return TomlConfig
