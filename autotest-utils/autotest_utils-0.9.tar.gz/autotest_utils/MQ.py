import ssl
import stomp
import json

class MQStomp(stomp.Connection):
    class Listener(stomp.ConnectionListener):
        message_received = False
        headers = {}
        msg_list = []

        def __init__(self):
            self.msg_list = []
            self.headers = {}
            self.message_received = False

        def on_message(self, headers, msg):
            self.msg_list.append(msg)
            self.headers = {k: v for k, v in headers.items()}
            self.message_received = True

        def on_error(self, headers, body):
            print('received an error "%s"' % body)
    def __init__(self, host, port,ssl_version=ssl.PROTOCOL_TLS):
        super().__init__(host_and_ports=[(host, port)],ssl_version=ssl_version)

    def sendFile(self,queue,filepath,headers,properties):
        with open(filepath, 'rb') as temp_f:
            data = temp_f.read()
            data=data.hex()
            self.send(destination=queue, body=data,headers=headers,**properties)

    def open(self,user,password):
        self.connect(login=user, passcode=password)

    def getMessage(self,queue,headers):
        listener = self.Listener()
        self.set_listener('Listener', listener)
        self.subscribe(destination=queue, id="1", ack="client", headers=headers)
        while (not listener.message_received):
            pass
        self.ack(id=listener.headers['message-id'], subscription=listener.headers['subscription'])
        return listener.msg_list[0],listener.headers

    def getBinaryFile(self,queue,localbody,localheader):
        h = {}
        h['activemq.prefetchSize']=1
        h['content-type'] = 'application/octet-stream'
        self.getMessage(queue,h)
        body,headers = self.getMessage(queue,headers=h)
        try:
            byte_body = bytes.fromhex(body)
            with open(localbody, 'wb') as f:
                f.write(byte_body)
        except Exception:
            byte_body = body
            with open(localbody, 'w') as f:
                f.write(byte_body)
        with open(localheader, 'w') as f:
            f.write(json.dumps(headers))
        self.disconnect()