import abc
from dataclasses import dataclass
from os.path import join
from typing import Any, Tuple

import anyconfig
from box import Box

from floxcore.context import Flox
from floxcore.settings import CONFIG_DIRS


@dataclass
class ParamDefinition:
    name: str
    description: str
    boolean: bool = False
    multi: bool = False
    secret: bool = False
    default: Any = None
    value: Any = None


def load_settings(flox: Flox):
    """
    :param flox: floxcore.context.Flox
    """
    config = anyconfig.load(
        [
            join(CONFIG_DIRS.get("system"), "settings.toml"),
            join(CONFIG_DIRS.get("system"), f"/etc/flox/settings.{flox.profile}.toml"),
            join(CONFIG_DIRS.get("user"), "settings.toml"),
            join(CONFIG_DIRS.get("user"), f"settings.{flox.profile}.toml"),
            join(flox.working_dir, ".flox", "settings.toml"),
            join(flox.working_dir, ".flox", f"settings.{flox.profile}.toml"),
        ],
        ignore_missing=True,
        ac_parser="toml",
    )

    from pkg_resources import iter_entry_points

    for entrypoints in iter_entry_points("flox.plugin.config"):
        config = entrypoints.load()()

    return Box(config, default_box=True)


class Configuration(abc.ABC):
    def __init__(self, name):
        self.name = name

    @abc.abstractmethod
    def parameters(self) -> Tuple[ParamDefinition]:
        pass

    def secrets(self) -> Tuple[ParamDefinition]:
        return tuple()

    @abc.abstractmethod
    def schema(self):
        pass

    def load(self):
        pass

    def write(self, configuration):
        pass
