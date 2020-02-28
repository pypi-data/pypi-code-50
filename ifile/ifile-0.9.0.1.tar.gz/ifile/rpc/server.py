import sys
import time
import base64
import logging
from concurrent import futures
from threading import Event

import grpc

from ifile import setting as conf
from ifile.rpc import file_pb2, file_pb2_grpc
from ifile.storage import api as storage_api
from ifile.manage.client import Clients
from ifile.exception import (
    HeartBeatError
)

logger = logging.getLogger(__name__)


class IFileClientServicer(file_pb2_grpc.IFileClientServicer):
    def HeartBeat(self, request, context):
        logger.debug(
            f"the request from client. "
            f"hostname: {request.hostname}, ip: {request.ip}")

        clients = Clients()

        try:
            clients.activate_client(request.hostname, request.ip)
        except Exception as e:
            raise HeartBeatError(f"hearbeat error. {str(e)}")

        params = {"active": True}

        return file_pb2.BeatResponse(**params)


class Service(object):
    def __init__(self, name):
        self.name = name
        self.host = ""
        self.port = conf.MASTER_GRPC_PORT

        self._is_stop = Event()

    def start(self):
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        file_pb2_grpc.add_IFileClientServicer_to_server(
            IFileClientServicer(), self.server)
        addr = f":{self.port}"
        self.server.add_insecure_port(addr)
        self.server.start()
        logger.info(f"{self.name} service running in {self.host}:{self.port}.")

        try:
            while not self._is_stop.is_set():
                time.sleep(1)
        except KeyboardInterrupt:
            self.stop()
            logger.info("Goobye!")

    def stop(self):
        self._is_stop.set()
