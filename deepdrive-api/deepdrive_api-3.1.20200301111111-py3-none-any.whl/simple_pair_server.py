import zmq
import random
import sys
import time

port = "5557"
context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.bind("tcp://*:%s" % port)

while True:
    # socket.send(b'A')
    msg = socket.recv()
    print(msg)
    socket.send_json({'a': 1})
    time.sleep(1)