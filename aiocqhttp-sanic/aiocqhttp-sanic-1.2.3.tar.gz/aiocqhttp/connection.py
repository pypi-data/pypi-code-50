#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import Union

from sanic.request import Request
from sanic.websocket import WebSocketCommonProtocol as conn


class WebSocketConnection(conn):
    def __init__(self, request: Request, connection: conn):
        self.conn = connection
        self.request = request
        self.headers = request.headers
        self.send = connection.send
        self.recv = connection.recv
        self.close = connection.close
