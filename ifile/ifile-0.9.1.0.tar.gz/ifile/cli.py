import os
import sys
import logging
from logging.config import dictConfig
from shutil import copyfile
from functools import wraps

import click

from ifile import create_app, setting as conf, WebService
from ifile.db.sqlalchemy.session import get_engine
from ifile.db.sqlalchemy.models import metadata
from ifile.storage import api as storage_api
from ifile.client import RpcService, FtpService
from ifile.apps.beat import BeatService
from ifile.services import Services

logger = logging.getLogger(__name__)


def with_app_context(func):
    @wraps(func)
    def inner(*args, **kwargs):
        app = create_app()
        app.app_context().push()

        return func(*args, **kwargs)
    return inner


@click.group()
def cli():
    """iFile command line tools"""
    app_home = conf.APP_HOME
    os.chdir(app_home)


@click.group()
def db():
    """database manage tools"""


@click.group()
def run():
    """run service. web,rpc,ftp"""
    dictConfig(conf.LOGGING_CONFIG)


@click.group()
def dev():
    """development tools."""


@cli.command()
def init():
    """init application."""
    app_home = conf.APP_HOME
    config_file = os.path.join(app_home, 'ifile.ini')
    if not os.path.exists(config_file):
        default_config = os.path.join(
            os.path.dirname(__file__), 'default_config.ini')

        print(f"The config file '{config_file}' was created.")
        copyfile(default_config, config_file)

    supervisord_config = os.path.join(app_home, 'supervisord.conf')
    if not os.path.exists(supervisord_config):
        default_supervisord_config = os.path.join(
            os.path.dirname(__file__), 'default_supervisord.conf')

        print(f"The config file '{supervisord_config}' was created.")
        copyfile(default_supervisord_config, supervisord_config)

    logger_dir = os.path.join(app_home, 'log')
    if not os.path.exists(logger_dir):
        os.makedirs(logger_dir)

    runner_dir = os.path.join(app_home, 'run')
    if not os.path.exists(runner_dir):
        os.makedirs(runner_dir)

    print(f"Init completed! app_home is '{app_home}'.")


@run.command()
@click.option("--debug/--no-debug", default=False, help="debug model.")
@click.option("--host", "-h", default='0.0.0.0', help="host address.")
@click.option("--port", "-p", default=8000, help="server port.")
def web(debug, host, port):
    """run service."""
    web_service = WebService("web", host=host, port=port, is_debug=debug)
    web_service.start()


@run.command()
def rpc():
    """rpc service."""
    rpc_service = RpcService("rpc")
    rpc_service.start()


@run.command()
def ftp():
    """ftp service."""
    ftp_service = FtpService("ftp")
    ftp_service.start()


@run.command()
def beat():
    """beat service."""
    beats_service = BeatService("beat")
    beats_service.start()


@run.command("all")
def run_all():
    """run all service."""
    services = Services()
    services.register('ftp')
    services.register('rpc')
    services.register('beat')

    services.start_all()


@cli.command()
def details():
    """show application details."""
    print("\n      **APPLICATION DETAILS**      \n")

    print(" ========Configs========")
    # from ifile import setting as config
    configs = [config for config in dir(conf) if config.isupper()]

    for config in configs:
        value = getattr(conf, config)
        print(f" * {config}: {value}")

    print(" =======================")


@db.command("init")
@with_app_context
def init_db():
    """init database, create tables."""
    engine = get_engine()
    metadata.create_all(engine)

    print("init database successful.")


@dev.command()
def clean_all():
    """clean all data!"""
    files = storage_api.Files()
    for file_id in files:
        _file = storage_api.File(file_id)
        _file.destroy()
        print(f"file {_file.uuid} deleted.")


cli.add_command(db)
cli.add_command(run)
cli.add_command(dev)


if __name__ == "__main__":
    beats_service = BeatService("beat")
    beats_service.start()
