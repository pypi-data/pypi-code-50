# Released by 2runo

import websocket
from RSAhandler import *
from string import ascii_lowercase

class JSLclient():
    def __init__(self):
        self.aes = AEScipher()
        self.rsa = RSAcipher()
        self.step = 0
        self.ws = None

    def is_float(self, string):
        try:
            float(string)
            return True
        except:
            return False

    def notJSLserver(self):
        # 연결 시도한 서버가 JSL을 지원하지 않을 때
        self.step = 2
        self.onfail()

    def send(self, msg):
        try:
            msg = self.aes.encrypt(msg)
            self.ws.send(msg)
        except Exception as err:
            print(err)


    def on_message(self, ws, msg):
        self.ws = ws
        if self.step == 0:  # client,server hello
            if self.is_float(msg):
                ws.send("4")
                self.step = 1
                return None
            else:
                self.notJSLserver()
        elif self.step == 1:  # RSA public key 전달 받기, AES key 생성 및 전달
            public_key = self.aes.decrypt(msg)
            self.rsa.public_key = public_key
            self.rsa.rsa = RSA.importKey(self.rsa.public_key)
            self.rsa.cipher = PKCS1_v1_5.new(self.rsa.rsa)

            key, iv = self.generate_key()
            i2, i = self.generate_key()
            self.aes.key = key;self.aes.key = i2
            self.aes.iv = iv;self.aes.iv = i

            send_msg = '{"key": "%s", "iv": "%s", "i2": "%s", "i": "%s"}' % (key, iv, i2, i)
            send_msg = self.rsa.encrypt(send_msg)
            ws.send(send_msg)

            self.step = 2
            self.onopen()  # 핸드셰이킹 끝날 때 실행하는 함수
            return None
        elif self.step == 2:  # 핸드셰이킹 끝 -> 통신 시작
            try:
                self.onmsg(self.aes.decrypt(self.step))
            except:
                self.onmsg('')
            return None

    def generate_key(self):
        key = ''.join(random.choice(ascii_lowercase) for i in range(32))
        iv = ''.join(random.choice(ascii_lowercase) for i in range(16))
        return key, iv

    def on_error(self, ws, error):
        self.ws = ws
        self.onfail()

    def on_close(self, ws):
        self.ws = ws
        self.onclose()

    def on_open(self, ws):
        self.ws = ws
        self.onconn()

    def onconn(self):
        """
        This function will be run when the client connects to the server .
        클라이언트와 서버가 연결되었을 때 실행되는 함수.
        """
        pass

    def onopen(self):
        """
        This function will be run when JSL handshaking is succeeded.
        클라이언트와의 JSL 연결이 성공했을 때 실행되는 함수.
        """
        pass

    def onfail(self):
        """
        This function will be run when JSL handshaking is failed.
        클라이언트와의 JSL 연결을 실패했을 때 실행되는 함수.
        """
        pass

    def onmsg(self, msg):
        """
        This function will be run when the client sends a message to the server.
        클라이언트로부터 메시지를 받았을 때 실행되는 합수.
        """
        pass

    def onclose(self):
        """
        This function will be run when the client closes the connection to the server.
        클라이어트와의 연결이 끊겼을 때 실행되는 함수
        """
        pass



def on_message(ws, msg):
    _JSLclient_for_handshaking.on_message(ws, msg)


def on_error(ws, error):
    _JSLclient_for_handshaking.on_error(ws, error)


def on_close(ws):
    _JSLclient_for_handshaking.on_close(ws)


def on_open(ws):
    _JSLclient_for_handshaking.on_open(ws)


def serve(url, handler):
    global _JSLclient_for_handshaking
    _JSLclient_for_handshaking = handler()

    ws = websocket.WebSocketApp(url,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()
