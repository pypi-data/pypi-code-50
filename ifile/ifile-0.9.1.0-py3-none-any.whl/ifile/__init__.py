import os
import logging
from logging.config import dictConfig

from flask import Flask

from ifile import setting as config
from ifile.db.base import DataBase
from ifile.services import Services

if config.SENTRY_ENABLE:
    import sentry_sdk
    from sentry_sdk.integrations.logging import LoggingIntegration

    sentry_logging = LoggingIntegration(
        level=logging.INFO,
        event_level=logging.ERROR
    )
    sentry_sdk.init(
        dsn=config.SENTRY_DSN,
        integrations=[sentry_logging]
    )


database = DataBase()
services = Services()


def create_app():
    app = Flask(__name__)

    app.config.from_object(config)

    database.init_app(app)

    from ifile.api import blueprint
    app.register_blueprint(blueprint, url_prefix='/api')

    return app


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

        logger = logging.getLogger(__name__)
        logger.info(f"{self.name} service running in {self.host}:{self.port}.")
        app.run(
            host=self.host,
            port=self.port,
            debug=self._is_debug
        )

    def stop(self):
        pass
