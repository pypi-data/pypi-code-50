# coding=utf-8
"""
author = jamon
"""

import asyncio
import requests
import struct
import ujson
import websockets

from obespoir.share.encodeutil import AesEncoder


class RpcProtocol(object):
    """消息协议，包含消息处理"""

    def __init__(self):
        self.handfrt = "iii"  # (int, int, int)  -> (message_length, command_id, version)
        self.head_len = struct.calcsize(self.handfrt)
        self.identifier = 0

        self.encode_ins = AesEncoder()
        self.version = 0

        self._buffer = b""    # 数据缓冲buffer
        self._head = None     # 消息头, list,   [message_length, command_id, version]
        self.transport = None
        super().__init__()

    def pack(self, data, command_id):
        """
        打包消息， 用於傳輸
        :param data:  傳輸數據
        :param command_id:  消息ID
        :return: bytes
        """
        # print(type(data))
        data = self.encode_ins.encode(data)
        # data = "%s" % data
        length = data.__len__() + self.head_len
        head = struct.pack(self.handfrt, length, command_id, self.version)
        # print("type=", type(head), type(data), [head], head[0])
        # print(struct.unpack(self.handfrt, head))
        return head + data


def test_http_web_proxy():
    """
    服务节点http接口测试
    :return:
    """
    url = "http://127.0.0.1:20001/"
    ret = requests.post(url, data=ujson.dumps({"token": "19778225bc81894d8a6465c93542c0",
                                               "phone": [1, 2], "content": "test"
                                               }))
    print("test_http_web_proxy:", ret.status_code, ret.text)


async def test_websocket_proxy():
    """
    用户websocket长连接测试：
    主要测试功能有：
    1. 服务端接收客户端websocket登录请求，并对之进行响应
    2. 客户端向服务端发送一条游戏内部消息，观察服务端最后一层节点service是否正确响应，并且将结果返回给客户端；

    测试时服务端配置：
        登录请求：消息ID为1000， 登录消息暂时配置在route类型节点处理
        游戏进入排位场: 消息ID 20000， 进入排位场消息暂时配置在service类型节点处理

    客户端测试代码流程：
    1. 先发送登录消息
    2. 接收服务端对登录消息的响应
    3. 再发送游戏进入排位场消息
    4. 接收服务端推送过来的对"进入排位场"的消息响应
    :return:
    """
    user_name = "jamon"
    passwd = "test"
    async with websockets.connect("ws://127.0.0.1:20000") as websocket:
        rpc = RpcProtocol()
        msg_login = rpc.pack(ujson.dumps({"name": user_name, "passwd": passwd}), 1000)
        await websocket.send(msg_login)
        print("success send_login message(ID:1000):", msg_login)

        recv_login_response = await websocket.recv()
        print("recv_login_response: ", recv_login_response)

        await asyncio.sleep(6)    # 方便测试观察，休眠一段时间

        user_id = 10
        msg_enter_rank_room = rpc.pack(ujson.dumps({"user_id": user_id}), 20000)
        await websocket.send(msg_enter_rank_room)
        print("success send_enter_rank message(ID:20000):", msg_enter_rank_room)
        recv_enter_response = await websocket.recv()
        print("recv_enter_response:", recv_enter_response)


if __name__ == "__main__":
    test_http_web_proxy()
    asyncio.get_event_loop().run_until_complete(test_websocket_proxy())