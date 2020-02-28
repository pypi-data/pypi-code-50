import os
import sys
import logging
from configparser import ConfigParser

logger = logging.getLogger(__name__)


def get_app_home():
    """get application home path"""
    app_home = os.path.expanduser(
        os.path.expandvars(os.environ.get('IFILE_HOME', '~/ifile')))
    return app_home


def parser_config_file():
    """parser config file"""
    app_home = APP_HOME
    if not os.path.exists(app_home):
        print(f"The directory '{app_home}' was created.")
        os.makedirs(app_home)

    config_file = os.path.join(app_home, 'ifile.ini')

    if not os.path.exists(config_file):
        config_file = os.path.join(
            os.path.dirname(os.path.realpath(__file__)), 'default_config.ini')

    config = ConfigParser()
    config.read(config_file)

    return config


APP_HOME = get_app_home()

config = parser_config_file()
core = config["core"]
rpc = config["rpc"]
ftp = config["ftp"]

SECRET_KEY = os.urandom(16)
SQLALCHEMY_DATABASE_URI = core["database_uri"]
STORAGE_TYPE = core["storage_type"]

MASTER_GRPC_PORT = rpc["master_port"]
CLIENT_GRPC_PORT = rpc["client_port"]

FTP_ALLOW_HOST = ftp["allow_host"]
FTP_PORT = ftp["port"]
FTP_MAX_CONS = int(ftp["max_cons"])
FTP_MAX_CONS_PER_IP = int(ftp["max_cons_per_ip"])
FTP_USER = ftp["user"]
FTP_PASSWORD = ftp["password"]
FTP_MAX_DOWNLOAD = int(ftp["max_download"])
FTP_MAX_UPLOAD = int(ftp["max_upload"])

ports = ftp["passive_ports"].split(',')
FTP_PASSIVE_PORTS = range(int(ports[0]), int(ports[1]))

if STORAGE_TYPE == "disk":
    disk = config["disk"]
    DATA_PATH = disk.get("data_path", None)
elif STORAGE_TYPE == "mongodb":
    mongodb = config["mongodb"]
    MONGO_URI = mongodb.get("uri", "mongodb://localhost:27017/ifile")

BEAT_TASKS = [
    "ifile.scheduler"
]
