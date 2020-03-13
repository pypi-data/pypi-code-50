#!/usr/local/bin/python
import argparse
import json
import logging
import socket
import sys
import ssl
import threading
import websocket

try:
    import SocketServer
except:
    import socketserver as SocketServer

from thundradebugclient.constants import *

try:
    import thread
except ImportError:
    import _thread as thread


logger = logging.getLogger('debug_client')
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
logger.addHandler(handler)

def handle_error_message(ws, error):
    if hasattr(error, 'status_code'):
        logger.error("{} (Session name = {})".format(
            BROKER_WS_HTTP_ERR_CODE_TO_MSG.get(error.status_code, "Broker connection got error: {}".format(error)),
            ws.session_name
            )
        )
    else:
        logger.error("Broker connection got error: {}".format(error))

def handle_close_message(ws, code, message):
    if code == FUNCTION_TIMEOUT_CLOSE_CODE:
        logger.error("Function timed out. (Session name = {})".format(ws.session_name,))

    logger.info("Connection closed for session: "+ ws.session_name)

def on_open(ws):
    def run(debugger_socket):
        try:
            ws.running = True
            ws.send(ws.data_on_first_read, opcode=OPCODE_BINARY)
            while ws.running:
                buf = debugger_socket.recv(4096)
                logger.debug("Received message from debugger: {} (Session name = {})".format(buf, ws.session_name))
                if len(buf) == 0:
                    ws.running = False
                elif ws.running:
                    ws.send(buf, opcode=OPCODE_BINARY)
        except IOError:
            logger.debug("Connection closed. (Session name = {})".format(ws.session_name,))
        except Exception as e:
            logger.debug("Error while listening from debugger socket: {}  (Session name = {})".format(e, ws.session_name))

        try:
            ws.close()
        except:
            pass

    thread.start_new_thread(run, (ws.debugger_socket,))

def on_message(ws, message):
    if isinstance(message, str):
        message = message.encode()

    logger.debug("Received message from broker: {} (Session name = {})".format(message, ws.session_name))
    ws.debugger_socket.send(message)

def on_error(ws, error):
    handle_error_message(ws, error)
    ws.running = False

def on_close(ws, code, message):
    handle_close_message(ws, code, message)
    ws.running = False

def handle_managed_req(data, headers):
    try:
        if isinstance(data, bytes):
            data = data.decode()
        if data.startswith("GET /json"):
            headers.append("x-thundra-session-temp: true")
    except:
        pass

class ThundraRequestHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        logger.info("Debugger connected from: {} (Session name = {})".format(self.server.server_address[1], self.server.session_name))
        logger.debug("Debugger connected to {}".format(self.client_address[1]))
        try:
            buf = self.request.recv(4096)
            if len(buf) == 0:
                return
            
            headers = [
                    "{}: {}".format(BROKER_HANDSHAKE_HEADERS.get("AUTH_TOKEN"), self.server.auth),
                    "{}: {}".format(BROKER_HANDSHAKE_HEADERS.get("SESSION_NAME"), self.server.session_name),
                    "{}: {}".format(BROKER_HANDSHAKE_HEADERS.get("PROTOCOL_VER"), PROTOCOL_VER)
                    ]

            handle_managed_req(buf, headers)
            ws = websocket.WebSocketApp("wss://{}:{}".format(self.server.broker_host, self.server.broker_port),
                header=headers,
                    on_message=on_message,
                    on_close=on_close,
                    on_error=on_error
                )
            ws.debugger_socket = self.request
            ws.session_name = self.server.session_name
            ws.data_on_first_read = buf
            ws.on_open = on_open
            ws.run_forever(sockopt=((socket.IPPROTO_TCP, socket.TCP_NODELAY, 1),))

        except Exception as e:
            logger.error("Exception occured:"+ e)
        try:
            ws.close()
        except: pass
        
        logger.debug("End debugger connection to {}".format(self.client_address[1]))


class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass


