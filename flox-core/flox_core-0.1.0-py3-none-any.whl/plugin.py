import abc
from typing import Dict

from pkg_resources import iter_entry_points


class Plugin(abc.ABC):
    """
    Plugin definition class. Only mandatory method is configuration.
    If you would like to inject to action you should implement handle_{action} method which will return list
    of the stages
    """

    @abc.abstractmethod
    def configuration(self):
        """
        Return Plugin Configuration definition
        :return: floxcore.config.Configuration
        """

    def add_commands(self, cli):
        """
        Add commands to given cli instance
        """

    def support(self, even_name: str):
        return hasattr(self, f"handle_{even_name}")

    def handle(self, even_name: str, *args, **kwargs):
        return getattr(self, f"handle_{even_name}")(*args, **kwargs)


class Manager:
    def __init__(self):
        self.plugins = {}

        for entry in iter_entry_points("flox.plugin"):
            self.plugins[entry.name] = entry.load()()

    def get(self, name: str) -> Plugin:
        return self.plugins.get(name)

    def all(self):
        return self.plugins

    def handlers(self, name: str) -> Dict[str, Plugin]:
        """
        Return plugins which are able to handle given event
        :param name:
        :return:
        """
        return {k: v for k, v in self.plugins.items() if v.support(name)}


def add_commands(self, cli):
    for plugin in filter(lambda x: hasattr(x, "add_commands"), self.plugins.values()):
        plugin.add_commands(cli)
