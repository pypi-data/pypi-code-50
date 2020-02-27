import stomp
import ssl
class SampleListener(stomp.ConnectionListener):
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
        print(self.headers)
        print(type(msg))
        self.message_received = True

    def on_error(self, headers, body):
        print('received an error "%s"' % body)

def sendFileToMQ(host,port,queue,user,password,filepath,headers,properties):
    with open(filepath, 'rb') as temp_f:
        data = temp_f.read()
        data=data.hex()
        sendMessageToMQ(host,port,queue,user,password,headers,properties,data)

def openMQConnection(host,port,user,password):
    conn = stomp.Connection(host_and_ports=[(host, port)])
    conn.set_ssl(ssl_version=ssl.PROTOCOL_TLS)
    conn.connect(login=user, passcode=password)
    return conn


def sendMessageToMQ(host,port,queue,user,password,headers,properties,body):
    conn = openMQConnection(host,str(port),user,password)
    conn.send(destination=queue, body=body,headers=headers,**properties)
    conn.disconnect()

def getMessageFromMQ(conn,queue,headers):
    listener = SampleListener()
    conn.set_listener('SampleListener', listener)
    conn.subscribe(destination=queue, id="1", ack="client", headers=headers)
    while (not listener.message_received):
        pass
    return listener.msg_list[0],listener.headers

def getFileFromMQ(host,port,queue,user,password,localbody,localheader):
    conn = openMQConnection(host,port,user,password)
    h = {}
    h['activemq.prefetchSize']=1
    h['content-type'] = 'application/octet-stream'
    getMessageFromMQ(conn,queue,h)
    body,headers = getMessageFromMQ(conn,queue,headers=h)
    byte_body = bytes.fromhex(body)
    conn.ack(id=headers['message-id'],subscription=headers['subscription'])
    with open(localbody, 'wb') as f:
        f.write(byte_body)
    with open(localheader, 'w') as f:
        f.write(localheader)
    conn.disconnect()