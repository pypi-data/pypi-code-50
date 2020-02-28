import os
import logging

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler, ThrottledDTPHandler
from pyftpdlib.servers import FTPServer

from ifile.storage import api as storage_api
from ifile import setting as conf
from ifile.exception import (
    FtpFileError
)

logger = logging.getLogger(__name__)


class CustomFTPHandler(FTPHandler):
    def on_file_received(self, file):
        _, filename = os.path.split(file)
        files = storage_api.Files()

        try:
            with open(file, "rb") as fp:
                binary_data = fp.read()
                files.add(filename, binary_data)
        except Exception as e:
            raise FtpFileError(f"save ftp file {filename} error. {str(e)}")

        os.remove(file)


class Service(object):
    def __init__(self, name):
        self.name = name
        self.host = conf.FTP_ALLOW_HOST
        self.port = conf.FTP_PORT
        self.authorizer = DummyAuthorizer()
        self.dtp_handler = ThrottledDTPHandler
        self.ftp_handler = CustomFTPHandler

        self.ftp_home = self.init_ftp_home()
        self.init_users()
        self.init_handler()

    def init_ftp_home(self):
        ftp_home = os.path.join(conf.APP_HOME, '.ftp')
        if not os.path.exists(ftp_home):
            os.makedirs(ftp_home)

        return ftp_home

    def init_handler(self):
        self.ftp_handler.authorizer = self.authorizer
        self.ftp_handler.passive_ports = conf.FTP_PASSIVE_PORTS

        self.dtp_handler.read_limit = conf.FTP_MAX_DOWNLOAD
        self.dtp_handler.write_limit = conf.FTP_MAX_UPLOAD

    def init_users(self):
        self.authorizer.add_user(
            conf.FTP_USER, conf.FTP_PASSWORD, self.ftp_home,
            perm='elradfmw')

    def init_server(self):
        server = FTPServer((self.host, self.port), self.ftp_handler)
        server.max_cons = conf.FTP_MAX_CONS
        server.max_cons_per_ip = conf.FTP_MAX_CONS_PER_IP

        return server

    def start(self):
        server = self.init_server()
        logger.info(f"{self.name} service running in {self.host}:{self.port} .")

        server.serve_forever()

    def stop(self):
        self.server.close()

    def add_anonymous(self, path):
        self.authorizer.add_anonymous(path)


if __name__ == "__main__":
    service = Service("ftp")
    service.start()
