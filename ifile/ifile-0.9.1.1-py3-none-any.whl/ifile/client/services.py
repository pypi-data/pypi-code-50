import os
import sys
import time
import base64
import logging
from concurrent import futures
from threading import Event

import grpc
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler, ThrottledDTPHandler
from pyftpdlib.servers import FTPServer

from ifile import setting as conf
from ifile.utils import gen_uuid, get_md5, gen_data_path
from ifile.client.rpc import client_pb2, client_pb2_grpc
from ifile.storage import api as storage_api
from ifile.client import Clients
from ifile.client.heartbeat import Receiver

logger = logging.getLogger(__name__)


class IFileClientServicer(client_pb2_grpc.IFileClientServicer):
    def HeartBeat(self, request, context):
        receiver = Receiver()
        is_active = receiver.activate_heart(request.hostname, request.ip)

        params = {"active": is_active}
        return client_pb2.BeatResponse(**params)


class RpcService(object):
    def __init__(self, name):
        self.name = name
        self.host = conf.GRPC_ALLOW_HOST
        self.port = conf.MASTER_GRPC_PORT

        self._is_stop = Event()

    def start(self):
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        client_pb2_grpc.add_IFileClientServicer_to_server(
            IFileClientServicer(), self.server)
        addr = f"{self.host}:{self.port}"
        self.server.add_insecure_port(addr)
        self.server.start()
        logger.info(f"{self.name} service running in {addr}.")

        try:
            while not self._is_stop.is_set():
                time.sleep(1)
        except KeyboardInterrupt:
            self.stop()
            logger.info("Goobye!")

    def stop(self):
        self._is_stop.set()


class CustomFTPHandler(FTPHandler):
    def ftp_STOR(self, file, mode='w'):
        _, filename = os.path.split(file)
        file_uuid = gen_uuid()
        data_path = gen_data_path()
        file_path = os.path.join(data_path, file_uuid)

        super().ftp_STOR(file_path, mode=mode)

        md5 = get_md5(file_path)
        logger.info(f"the md5 is {md5} of {file_path}.")

        files = storage_api.Files()
        logger.info(f"adding file {filename} info to db. uuid is {file_uuid}.")
        files.add_from_ftp(filename, file_uuid, md5)


class FtpService(object):
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
        logger.info(f"{self.name} service running in {self.host}:{self.port}.")

        server.serve_forever()

    def stop(self):
        self.server.close()

    def add_anonymous(self, path):
        self.authorizer.add_anonymous(path)
