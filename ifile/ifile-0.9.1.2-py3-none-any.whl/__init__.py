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
