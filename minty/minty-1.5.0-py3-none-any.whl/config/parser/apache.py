from .base import ConfigParserBase
from apacheconfig import make_loader


class ApacheConfigParser(ConfigParserBase):
    __slots__ = ["content"]

    def parse(self, content: str) -> dict:
        """Return a dict with the parsed config.

        :return: Parsed configuration
        :rtype: dict
        """
        content = super().parse(content)

        if content == "":
            raise ValueError("Cannot parse empty configuration")

        # statsd configuration needs to be loaded before it can be used,
        # so we can't measure the loading easily
        with make_loader() as loader:
            config = loader.loads(content)

        if "statsd" in config:
            self.statsd.get_counter().increment("parse")

        return config
