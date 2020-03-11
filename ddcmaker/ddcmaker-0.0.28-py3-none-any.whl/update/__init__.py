import os

from ddcmaker.update.configure import get_conf
from ddcmaker.update.file import create_dir, download_file, unzip_file
from ddcmaker.update.configure import read_conf, get_conf, ConfigDamage, Config


def upgrade():
    print("本版本暂不支持手动更新")


def repair():
    print("本版本暂无手动修复功能")


def update_feature():
    """负责更新feature"""
    conf = get_conf()
    for feature in conf.features:
        file_path = download_file(feature.url, feature.temp_dir)
        unzip_file(file_path.as_posix(), feature.temp_dir)
    print("更新成功，请重启")


def update_ddcmaker():
    """负责更新ddcmaker"""
    conf = get_conf()
    for origin in conf.origins:
        try:
            os.system(f'pip install -i {origin.url} --upgrade ddcmaker')
            print("更新成功")
            break
        except Exception:
            pass
