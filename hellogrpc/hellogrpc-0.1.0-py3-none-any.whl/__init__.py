import hellogrpc_pb2
import hellogrpc_pb2_grpc

HelloRequest = hellogrpc_pb2.HelloRequest 
HelloReply = hellogrpc_pb2.HelloReply 

def Client():
    with grpc.insecure_channel('localhost:50051') as channel:
        return helloworld_pb2_grpc.GreeterStub(channel)
