# 消息体例子:
#
# absolute_path:/Users/tiger/develop/tmp/1.txt
# content:时间 2020-03-02 03:21:11.098307 下载图片成功
# ----------
#
# 消息体字段解析:
#
# - absolute_path: 日志保存路径
# - content:       日志内容
# - ----------:    分隔符
#
#
#
#
# 日志内容例子:
#
# [Tiger-3.local 127.0.0.1] INFO - 2020-03-05 19:47:52.912865 - (easylog.py:97) - 下载图片成功
#
# 日志内容格式解析:
#
# [主机名 IP] INFO - 日期时间 - (文件名:行数) - 日志内容
import socket
import json
import concurrent.futures
import os
from inspect import getframeinfo, stack

from easylogcli import util


class EasyLog:

    def __init__(self, name, host, port, absolute_path):
        self.name = name
        self.host = host
        self.port = port
        self.absolute_path = absolute_path

        self.pool = concurrent.futures.ThreadPoolExecutor(max_workers=os.cpu_count())

        self.server_address = (self.host, self.port)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        # self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
        self.__connect()

        self.message_log = """
absolute_path:{absolute_path}
content:{content}
is_close:{is_close}
----------
"""
        self.content = '[{hostname} {IP}] INFO - {datetime} - ({filename}:{lineno}) - {message}'

    def __connect(self):
        try:
            self.sock.connect(self.server_address)
        except:
            self.sock.close()
            raise

    def __send(self, message=None, is_close=0, filename=None, lineno=None):
        try:
            hostname, IP = util.get_hostname_IP()
            datetime = util.get_datetime()

            content = self.content.format(hostname=hostname, IP=IP, datetime=datetime, filename=filename, lineno=lineno,
                                          message=message)
            message_log = self.message_log.format(absolute_path=self.absolute_path, content=content, is_close=is_close)

            self.sock.send(message_log.encode('utf8'))
            self.sock.send(b'')
        except Exception:
            # 这里发送失败可能是因为: 服务器进程崩溃, 网络问题.
            # 这里可以尝试不做处理, 避免因为日志组件的异常导致对应服务的异常.
            # TODO: 添加发送失败报警
            pass
            # DEBUG
            raise

    def send(self, message=None):
        caller = getframeinfo(stack()[1][0])
        # DEBUG
        # self.__send(message=message, is_close=0, filename=caller.filename, lineno=caller.lineno)
        self.pool.submit(self.__send, message=message, is_close=0, filename=caller.filename, lineno=caller.lineno)

    def close(self):
        self.__send(is_close=1)


def test():
    client = EasyLog(name='log-server', host='127.0.0.1', port=10000, absolute_path='/Users/tiger/develop/tmp/1.txt')

    # for _ in range(999999):
    for _ in range(10):
        client.send(message='下载图片成功')

    import time

    # time.sleep(60)
    time.sleep(3)

    client.close()


if __name__ == '__main__':
    test()
