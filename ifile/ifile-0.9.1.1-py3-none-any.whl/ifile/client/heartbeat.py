import sys
import time
import base64
import logging
from concurrent import futures
from threading import Event

import grpc

from ifile import setting as conf
from ifile.client.rpc import client_pb2, client_pb2_grpc
from ifile.storage import api as storage_api
from ifile.client import Clients
from ifile.exception import (
    HeartBeatError
)

logger = logging.getLogger(__name__)


class Receiver(object):
    def activate_heart(self, hostname, ip):
        logger.debug(
            f"the request from client. "
            f"hostname: {hostname}, ip: {ip}")

        clients = Clients()

        try:
            clients.activate_client(hostname, ip)
        except Exception as e:
            logger.exception(f"hearbeat error. {str(e)}")
            return False
        return True
