#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sanic.request import Request
from sanic.websocket import WebSocketCommonProtocol


class WebSocketConnection:
    def __init__(self, request: Request, connection: WebSocketCommonProtocol):
        connection.keepalive_ping_task.cancel()
        self.conn = connection
        self.request = request
        self.headers = request.headers
        self.send = connection.send
        self.recv = connection.recv
        self.close = connection.close
