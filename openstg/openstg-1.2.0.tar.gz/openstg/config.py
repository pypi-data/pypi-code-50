import os

from flask import Flask, g
from api import GisceStg
from backend.pool import Pool
from osconf import config_from_environment
from SqliteCounter import SqliteCounter


class AppSetup(object):

    def __init__(self):
        self.api = GisceStg(prefix='/api')
        self.pool = Pool()

    def create_app(self, **config):
        """
        Create a gisce_stg app
        :param config:
        :return: gisce_stg app
        """
        app = Flask(__name__, static_folder=None)

        if 'SQLITE_DB' in os.environ:
            app.config['SQLITE_DB'] = os.environ['SQLITE_DB']

        app.config.update(config)

        self.configure_api(app)
        self.configure_counter(app)
        self.configure_backend(app)

        return app

    def configure_api(self, app):
        """
        Configure different API endpoints
        :param app: Flask application
        :return:
        """
        from api import resources
        for resource in resources:
            self.api.add_resource(*resource)

        self.api.init_app(app)

    def configure_counter(self, app):
        """
        Configure SqliteCounter counter
        :param app:
        :return:
        """
        app.counter = SqliteCounter(app.config['SQLITE_DB'])
        return app

    def setup_backend_conn(self):
        try:
            client = self.pool.connect(**config_from_environment('PEEK'))
            g.backend_cnx = client
        except Exception:
            pass

    def configure_backend(self, app):
        app.before_request(self.setup_backend_conn)

