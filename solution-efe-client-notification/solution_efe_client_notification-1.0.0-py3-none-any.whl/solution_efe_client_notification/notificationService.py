import socket
import json
from solution_efe_config import configConstants

CLIENT_NOTIFICATION=configConstants.CLIENTS['notification']

def notificationServiceSendPushByToken(data):
    try:
        event = { 'event':'notification-service-send-push-by-token' , 'data': data }
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((CLIENT_NOTIFICATION['host'], CLIENT_NOTIFICATION['port']))
            sock.sendall(bytes(json.dumps(event) + "\n", "utf-8"))
            received = str(sock.recv(1024), "utf-8")
        response=json.loads(received)
        return response
    except Exception as e:
        return { 'code': 500, 'status': False, 'data': str(e) }
