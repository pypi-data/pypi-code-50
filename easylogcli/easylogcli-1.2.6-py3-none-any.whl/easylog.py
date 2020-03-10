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
import time
import sys

from easylogcli import util


class EasyLog:

    def __init__(self, name, host, port, absolute_path):
        self.name = name
        self.host = host
        self.port = port
        self.absolute_path = absolute_path

        self.pool = concurrent.futures.ThreadPoolExecutor(max_workers=os.cpu_count())

        self.server_address = (self.host, self.port)

        self.__connect()

        self.message_log = """
absolute_path:{absolute_path}
content:{content}
is_close:{is_close}
----------
"""
        self.content = '[{hostname} {IP}] INFO - {datetime} - ({filename}:{lineno}) - {message}'

    def __connect(self):
        """
        连接服务端. 若首次连接失败, 则重试 3 次, 每次间隔 60 秒钟.
        """
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect(self.server_address)
            print('连接服务端成功')
        except:
            i = 0
            while i < 3:
                time.sleep(60)
                try:
                    self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    self.sock.connect(self.server_address)
                except:
                    # raise
                    i += 1
                    continue

                # 重连成功
                break

            if i >= 3:
                print('重连服务端失败')
                # 直接结束客户端进程
                sys.exit()
            else:
                print('重连服务端成功')

    def __send(self, message=None, is_close=0, filename=None, lineno=None):
        """
        发送日志
        :param message: 用户指定的日志内容
        :param is_close: 标记消息体是否用于关闭连接, 1 是关闭, 0 是不关闭, 默认值是 0
        :param filename: 源码文件名
        :param lineno: 源码行号
        :return:
        """
        # 发送
        try:
            hostname, IP = util.get_hostname_IP()
            datetime = util.get_datetime()
            content = self.content.format(hostname=hostname, IP=IP, datetime=datetime, filename=filename, lineno=lineno,
                                          message=message)
            message_log = self.message_log.format(absolute_path=self.absolute_path, content=content, is_close=is_close)

            self.sock.sendall(message_log.encode('utf8'))
        except Exception:
            # TODO: 添加发送失败报警
            pass
            raise

    def send(self, message=None):
        """
        异步发送日志
        :param message: 用户指定的日志内容
        :return:
        """
        # 去除 '\n'
        message = message.replace('\n', '')

        caller = getframeinfo(stack()[1][0])
        self.__send(message=message, is_close=0, filename=caller.filename, lineno=caller.lineno)
        # self.pool.submit(self.__send, message=message, is_close=0, filename=caller.filename, lineno=caller.lineno)

    def close(self):
        """
        关闭连接与服务端之间的连接
        :return:
        """
        self.__send(is_close=1)


def test():
    client = EasyLog(name='log-server', host='127.0.0.1', port=10000, absolute_path='/Users/tiger/develop/tmp')

    for _ in range(999999):
        client.send(message='下载图片成功')

    import time

    # time.sleep(60)
    time.sleep(10)

    for _ in range(10):
        client.send(message='下载图片成功')
    time.sleep(35)
    print('done.')

    client.close()
    time.sleep(1)


if __name__ == '__main__':
    test()
