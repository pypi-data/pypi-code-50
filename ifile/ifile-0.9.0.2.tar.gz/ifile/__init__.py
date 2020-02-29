import logging

from flask import Flask

from ifile.db.base import DataBase
from ifile.services import Services

logger = logging.getLogger(__name__)
database = DataBase()
services = Services()


def create_app():
    app = Flask(__name__)

    from ifile import setting as config
    app.config.from_object(config)

    database.init_app(app)

    from ifile.api import blueprint
    app.register_blueprint(blueprint, url_prefix='/api')

    return app


class Service(object):
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

        logger.info(f"{self.name} service running in {self.host}:{self.port} .")
        app.run(
            host=self.host,
            port=self.port,
            debug=self._is_debug
        )

    def stop(self):
        pass
