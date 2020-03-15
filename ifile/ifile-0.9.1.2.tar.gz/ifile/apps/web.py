import logging
import multiprocessing

import gunicorn.app.base

from ifile import create_app
from ifile import setting as config

logger = logging.getLogger(__name__)


class StandaloneApplication(gunicorn.app.base.BaseApplication):

    def __init__(self, app, options=None):
        self.options = options or {}
        self.application = app
        super().__init__()

    def load_config(self):
        config = {key: value for key, value in self.options.items()
                  if key in self.cfg.settings and value is not None}
        for key, value in config.items():
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application


class WebService(object):
    def __init__(
        self,
        name,
        is_debug=False,
        host='0.0.0.0',
        port=8000
    ):
        self.name = name

        self._is_debug = is_debug
        self.host = host
        self.port = port

    def start(self):
        app = create_app()

        if self._is_debug:
            logger.info(f"{self.name} service running "
                        f"in {self.host}:{self.port}.")
            app.run(
                host=self.host,
                port=self.port,
                debug=self._is_debug
            )
        else:
            options = dict(config.GUNICORN_CONF)
            if options.get("workers", None) is None:
                options["workers"] = (multiprocessing.cpu_count() * 2) + 1
            StandaloneApplication(app, options).run()

    def stop(self):
        pass
