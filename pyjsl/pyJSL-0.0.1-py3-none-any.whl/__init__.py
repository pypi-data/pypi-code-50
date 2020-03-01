# Released by 2runo

from simple_websocket_server import WebSocketServer, WebSocket
import time
import json
from RSAhandler import *


class JSLhandshaker():
    def __init__(self, self2):
        self.memory = {}  # 특정 세션에 필요한 것을 저장하고 기억하는 변수 (ex: AESkey, JSL 사용 여부)
        self.logging = print  # print 대신 사용할 함수 (예를 들어 로깅이 필요한 경우)
        self.debug = True
        self.self2 = self2
        if not self.debug:
            self.logging = lambda *x: x

    def handle(self):
        msg = self.self2.data

        mem = self.memory[self.self2.address]
        rsa = mem['rsa']
        aes = mem['aes']
        try:
            _ = mem['step'], mem['use_jsl']
        except Exception:
            self.not_use_jsl()
            mem = self.memory[self.self2.address]

        if mem['step'] is None and not mem['use_jsl']:
            # jsl 사용하지 않는 경우
            return msg

        if mem['step'] == 0:  # 1. jsl 사용 여부 응답 + 공식키 전송
            if msg == "4":
                # jsl 사용한다고 응답
                self.handle_step0(rsa, aes)
                return None
            else:
                # jsl 사용 안 한다고 응답
                self.not_use_jsl()
                return msg
        elif mem['step'] == 1:  # 2. AES 키 전달받음
            self.handle_step1(msg, rsa)
            return None
        elif mem['step'] == 2:  # 3. 이제부터 보안 통신(JSL 통신) 시작
            return self.handle_step2(msg, aes)

    def handle_step0(self, rsa, aes):
        # jsl 사용한다고 응답
        self.memory[self.self2.address]['step'] = 1
        self.memory[self.self2.address]['use_jsl'] = True
        encrypted = self.encrypt(rsa.public_key, "handle() -> step 0")
        self.self2.send_message(encrypted)  # 공식키 전송 (AES 암호화)

    def handle_step1(self, msg, rsa):
        # AES 키 전달받음
        try:
            j = json.loads(rsa.decrypt(msg))
        except Exception as err:
            self.error_logging("decrypt error", "handle() -> step 1", [msg, err])
            self.not_use_jsl()
            return msg
        if j == "[Decrypt Error : Invalid Cryptogram]":
            self.error_logging("invalid cryptogram", "handle() -> step 1", [msg])
            self.not_use_jsl()
            return msg
        self.memory[self.self2.address]['aes'].key = j['i2']  # 'i2'='key'
        self.memory[self.self2.address]['aes'].iv = j['i']  # 'i'='iv'
        self.memory[self.self2.address]['step'] = 2

    def handle_step2(self, msg, aes):
        # 이제부터 보안 통신(JSL 통신) 시작
        try:
            msg = aes.decrypt(msg.encode())
        except Exception as err:
            self.error_logging("decrypt error", "handle() -> step 2", [msg, err])
            self.not_use_jsl()
        if msg == "[Decrypt Error : Invalid Cryptogram]":
            self.error_logging("invalid cryptogram", "handle() -> step 2", [msg])
            self.not_use_jsl()
        return msg

    def send(self, msg):
        if self.memory[self.self2.address]['use_jsl']:
            # jsl 사용하면 암호화 후 전송
            encrypted = self.encrypt(msg, "send() -> 'use_jsl'")
            self.self2.send_message(encrypted)
        else:
            # jsl 안 쓰면 그냥 전송
            self.self2.send_message(msg)

    def encrypt(self, msg, location="encrypt()"):
        # aes 암호화
        try:
            return self.memory[self.self2.address]['aes'].encrypt(msg)
        except Exception as err:
            self.error_logging("encrypt error", location, [err])
            return msg

    def not_use_jsl(self):
        # jsl을 사용하지 않는다고 설정
        self.memory[self.self2.address]['step'] = None
        self.memory[self.self2.address]['use_jsl'] = False

    def connected(self):
        self.self2.send_message(str(round(time.time(), 3)))  # jsl 사용 여부 확인 메시지 전송

        self.memory[self.self2.address] = {}
        self.memory[self.self2.address]['step'] = 0
        self.memory[self.self2.address]['use_jsl'] = False  # jsl 사용 여부 (초깃값은 '사용 안 함')
        self.memory[self.self2.address]['rsa'] = RSAcipher()
        self.memory[self.self2.address]['aes'] = AEScipher()

    def handle_close(self):
        # 연결이 종료됐을 경우 (세션이 종료됐을 경우) 해당 memory를 삭제한다. (더 이상 필요가 없으므로)
        del self.memory[self.self2.address]

    def is_use_jsl(self):
        return self.memory[self.self2.address]['use_jsl']

    def error_logging(self, msg_type, location, args=[]):
        # 오류 상황에 맞는 알맞은 로그를 남긴다.
        # msg_type: 오류 상황  |  location: 오류 발생 위치  |  args: msg나 암호문 등 추가 정보 (오류 상황에 따라 요구되는 정보가 다 다름)
        if msg_type == "invalid cryptogram":
            self.logging("[%s] Rreceived digest is invalid! -> The server will consider the client not using JSL for this session." % location)
            self.logging("received digest:", args[0])
        elif msg_type == "decrypt error":
            self.logging("[%s] The error occurs during AES decrypting! -> The server will consider the client not using JSL for this session." % location)
            self.logging("received digest:", args[0])
            self.logging("error message:", args[1])
        elif msg_type == "encrypt error":
            self.logging("[%s] An error occurred during AES decrypting! -> Send a message as a plain text." % location)
            self.logging("error message:", args[0])


class JSLserver(WebSocket):
    def __init__(self, server, sock, address):
        super(JSLserver, self).__init__(server, sock, address)
        self.jsl = JSLhandshaker(self)

    def handle(self):
        back_use_jsl = self.jsl.memory[self.address]['use_jsl']
        back_step = self.jsl.memory[self.address]['step']
        msg = self.jsl.handle()
        if back_use_jsl != self.jsl.memory[self.address]['use_jsl']:
            self.onfail()
        step = self.jsl.memory[self.address]['step']
        if back_step != step and step == 2:
            self.onopen()
        if msg is not None:
            self.onmsg(msg)

    def connected(self):
        self.onconn()
        self.jsl.connected()

    def handle_close(self):
        self.onclose()
        self.jsl.handle_close()

    def send(self, msg):
        self.jsl.send(msg)

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


def serve(host, port, websocketclass):
    WebSocketServer(host, port, websocketclass).serve_forever()


if __name__ == "__main__":
    serve('', 1004, JSLserver)
