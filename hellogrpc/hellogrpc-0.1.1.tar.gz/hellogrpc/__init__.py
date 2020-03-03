import grpc

from hellogrpc.hellogrpc_pb2 import *
from hellogrpc.hellogrpc_pb2_grpc import *

def Client():
    with grpc.insecure_channel('localhost:50051') as channel:
        return GreeterStub(channel)
