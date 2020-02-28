import grpc
import time
import base64
import sys
import socket
import logging
from concurrent import futures
from threading import Thread, Event

from grpcapi import file_pb2, file_pb2_grpc

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime)s] [%(process)d - %(threadName)s'
            ' - %(thread)d] %(message)s',)

logger = logging.getLogger(__name__)

_SERVER_HOST = "[::]:50051"


def gen_hostname():
    name = socket.gethostname()
    return name


def gen_host_ip():
    name = gen_hostname()
    ip = socket.gethostbyname(name)
    return ip


def activate():
    with grpc.insecure_channel(_SERVER_HOST) as channel:
        stub = file_pb2_grpc.IFileClientStub(channel)
        response = stub.HeartBeat(
            file_pb2.Beat(ip=gen_host_ip(), hostname=gen_hostname()))
        return response.active


class Service(object):
    def __init__(self, name):
        self.name = name
        self._is_stop = Event()

    def start(self):
        while not self._is_stop.is_set():
            try:
                is_active = activate()
            except Exception:
                print("rpc connect error.")
                continue
            finally:
                time.sleep(5)

            print(is_active)

    def stop(self):
        self._is_stop.set()


class IFileClientServicer(file_pb2_grpc.IFileClientServicer):
    def HeartBeat(self, request, context):
        # TODO request process
        logger.info(f"{request.ip} {request.hostname}")

        params = {
            "active": True
        }

        return file_pb2.BeatResponse(**params)

    def GetFile(self, request, context):
        logger.info(f"{request.file}")
        params = {
            "is_ok": True
        }
        return file_pb2.GetFileResponse(**params)


class GrpcService(object):
    def __init__(self, name):
        self.name = name
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        file_pb2_grpc.add_IFileClientServicer_to_server(
            IFileClientServicer(), self.server)
        self.server.add_insecure_port(_SERVER_HOST)

        self._is_stop = Event()

    def start(self):
        self.server.start()

        try:
            while not self._is_stop.is_set():
                time.sleep(1)
        except KeyboardInterrupt:
            self.stop()
            logger.info("Goobye!")

    def stop(self):
        self._is_stop.set()


def run():
    service = Service("beat")
    gservice = GrpcService("file")

    t1 = Thread(target=service.start, name=service.name)
    t1.start()
    logger.info(f"service {service.name} started.")

    t2 = Thread(target=gservice.start, name=gservice.name)
    t2.start()
    logger.info(f"service {gservice.name} started.")

    try:
        time.sleep(1)
    except KeyboardInterrupt:
        service.stop()
        print("\nGoobye.")


if __name__ == "__main__":
    # read_file("./DSC00102.jpg")

    run()
