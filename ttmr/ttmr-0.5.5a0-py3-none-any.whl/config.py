import os
from pathlib import Path
from types import SimpleNamespace
import pendulum
import tomlkit
from appdirs import AppDirs


def assert_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def get_appdir():
    appdirs = AppDirs("ttmr", "mgemmill")
    user_data_dir = appdirs.user_data_dir
    assert_dir(user_data_dir)
    return user_data_dir


def get_config():
    cfg = SimpleNamespace()

    cfg.appdirs = appdirs = AppDirs("ttmr", "mgemmill")
    cfg.user_data_dir = app_dir = appdirs.user_data_dir
    cfg.user_cache_dir = cache_dir = Path(appdirs.user_cache_dir)

    assert_dir(app_dir)
    assert_dir(cache_dir)

    cfg.config_path = Path(app_dir, "ttmr.cfg").resolve()

    cfg.data = data = tomlkit.parse(cfg.config_path.read_text())
    cfg.db_path = Path(app_dir, data["ttmr"]["db"])
    cfg.timezone = timezone = data["ttmr"].get("timezone", "America/Vancouver")

    today = pendulum.today(timezone)
    hour, minute = [int(s) for s in data["ttmr"].get("start_time", "07:00").split(":")]

    cfg.day_start_time = pendulum.datetime(
        year=today.year, month=today.month, day=today.day, hour=hour, minute=minute
    )

    return cfg
