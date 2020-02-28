import logging

import grpc

from ifile import setting as conf
from ifile.rpc import file_pb2, file_pb2_grpc

logger = logging.getLogger(__name__)


def get_file(host, file):
    address = f"{host}:{conf.CLIENT_GRPC_PORT}"
    logger.info(f"get file from host [{address}]")

    with grpc.insecure_channel(address) as channel:
        stub = file_pb2_grpc.IFileClientStub(channel)
        response = stub.GetFile(
            file_pb2.GetFileRequest(file=file))
        return response.is_ok
