import grpc

from hellogrpc.hellogrpc_pb2 import *
from hellogrpc.hellogrpc_pb2_grpc import *

def Client():
    creds = grpc.ssl_channel_credentials()
    channel = grpc.secure_channel('hello.rpc.stackmachine.com:443', creds)
    return GreeterStub(channel)
