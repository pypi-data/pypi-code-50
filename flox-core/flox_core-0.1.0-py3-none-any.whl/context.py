from os import getcwd
from os.path import realpath, join, basename, isfile, abspath, isdir, pardir

import click

from floxcore import plugin
from floxcore.secrets import Manager


def locate_project_root(test, dirs=(".git",), default=None):
    prev, test = None, abspath(test)

    while prev != test:
        if any(isdir(join(test, d)) for d in dirs):
            return test
        prev, test = test, abspath(join(test, pardir))

    return default


class Flox:
    CONFIG_FILE_NAME = "config.yml"

    def __init__(self):
        self.cwd = getcwd()
        self.working_dir = realpath(locate_project_root(self.cwd) or self.cwd)
        self.profile = self._profile()
        from floxcore.config import load_settings
        self.settings = load_settings(self)
        self.secrets = Manager()
        self.plugins = plugin.Manager()

    @property
    def environment_file(self):
        return join(self.local_config_dir, "environment")

    @property
    def local_config_dir(self):
        return join(self.working_dir, ".flox")

    @property
    def config_file(self):
        return join(self.local_config_dir, Flox.CONFIG_FILE_NAME)

    @property
    def prompt(self):
        return Prompt(self)

    @property
    def name(self):
        return basename(self.working_dir)

    def _profile(self):
        if not isfile(self.environment_file):
            return "local"

        return open(self.environment_file).read().strip()


class Prompt:
    def __init__(self, flox: Flox) -> None:
        self.flox = flox

    @staticmethod
    def colourize(name):
        if name in ["prod", "production", "live"]:
            return click.style(name, fg="red")
        elif name in ["uat", "preprod", "test"]:
            return click.style(name, fg="yellow")
        elif name in ["staging", "integration"]:
            return click.style(name, fg="green")
        else:
            return name

    def __repr__(self):
        return "{name}@{profile}> ".format(name=self.flox.name, profile=Prompt.colourize(self.flox.profile))
