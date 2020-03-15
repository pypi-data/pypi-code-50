from functools import update_wrapper
from pathlib import Path
import appdirs


__version__ = "0.1.0"


class reify(object):
    """
    Copy of pyramid's reify decorator coopted to
    force a Path object.

    """

    def __init__(self, wrapped):
        self.wrapped = wrapped
        update_wrapper(self, wrapped)

    def __get__(self, inst, objtype=None):
        #  if inst is None:  # pragma: noqa
        #      return self
        val = Path(self.wrapped(inst))
        setattr(inst, self.wrapped.__name__, val)
        return val


class Site:
    """
    Namespace object to hold all site directory paths.

    """

    def __init__(self, adw, name="site"):
        self._appdirs = adw
        self._name = name

    @reify
    def data_dir(self):
        return getattr(self._appdirs, f"{self._name}_data_dir")

    @reify
    def config_dir(self):
        return getattr(self._appdirs, f"{self._name}_config_dir")

    def assert_directories(self):
        """
        Create all directory Paths if they do no already exist.

        """
        for name, obj in self.__dict__.items():
            if not name.startswith("_") and name.endswith("_dir"):
                dirpath = getattr(self, name)
                dirpath.mkdir(parents=True, exist_ok=True)

    def to_string(self):
        """
        Visualize all default application directories.

        """
        return (
            f"{self._name} data dir:   {self.data_dir}\n"
            f"{self._name} config dir: {self.config_dir}\n"
        )


class User(Site):
    """
    Namespace object to hold all user directory paths.

    """

    def __init__(self, adw):
        super().__init__(adw, "user")

    @reify
    def data_dir(self):
        return getattr(self._appdirs, f"{self._name}_data_dir")

    @reify
    def cache_dir(self):
        return getattr(self._appdirs, f"{self._name}_cache_dir")

    @reify
    def log_dir(self):
        return getattr(self._appdirs, f"{self._name}_log_dir")

    @reify
    def config_dir(self):
        return getattr(self._appdirs, f"{self._name}_config_dir")

    @reify
    def state_dir(self):
        return getattr(self._appdirs, f"{self._name}_state_dir")

    def to_string(self):
        return (
            f"{self._name} data dir:   {self.data_dir}\n"
            f"{self._name} cache dir:  {self.cache_dir}\n"
            f"{self._name} log dir:    {self.log_dir}\n"
            f"{self._name} config dir: {self.config_dir}\n"
            f"{self._name} state dir:  {self.state_dir}\n"
        )


class AppDirs:
    """
    Convenience wrapper object to the appdirs library.

    """

    def __init__(self, appname, version=None, appauthor=None):
        self._appdirs = _appdirs = appdirs.AppDirs(
            appname, appauthor=appauthor, version=version
        )
        self.user = User(_appdirs)
        self.site = Site(_appdirs)
