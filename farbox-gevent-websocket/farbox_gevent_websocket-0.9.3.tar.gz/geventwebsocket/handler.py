import base64
import hashlib
import warnings
import struct, re, socket

from gevent.pywsgi import WSGIHandler
from .websocket import WebSocket, Stream
from .logging import create_logger


def get_key_value(key_value):
    key_number = int(re.sub("\\D", "", key_value))
    spaces = re.subn(" ", "", key_value)[1]
    if key_number % spaces != 0:
        return None
    return key_number / spaces

def get_challenge(environ):
    key1 = environ.get('HTTP_SEC_WEBSOCKET_KEY1')
    key2 = environ.get('HTTP_SEC_WEBSOCKET_KEY2')
    rfile = environ['wsgi.input'].rfile
    if key1 and key2 and rfile:
        part1 = get_key_value(key1)
        part2 = get_key_value(key2)
        # This request should have 8 bytes of data in the body
        key3 = rfile.read(8)
        challenge = ""
        challenge += struct.pack("!I", part1)
        challenge += struct.pack("!I", part2)
        challenge += key3
        challenge = hashlib.md5(challenge).digest()
        return challenge


class Client(object):
    def __init__(self, address, ws):
        self.address = address
        self.ws = ws


class WebSocketHandler(WSGIHandler):
    """
    Automatically upgrades the connection to a websocket.

    To prevent the WebSocketHandler to call the underlying WSGI application,
    but only setup the WebSocket negotiations, do:

      mywebsockethandler.prevent_wsgi_call = True

    before calling run_application().  This is useful if you want to do more
    things before calling the app, and want to off-load the WebSocket
    negotiations to this library.  Socket.IO needs this for example, to send
    the 'ack' before yielding the control to your WSGI app.
    """

    SUPPORTED_VERSIONS = ('13', '8', '7')
    GUID = "258EAFA5-E914-47DA-95CA-C5AB0DC85B11"

    def run_websocket(self):
        """
        Called when a websocket has been created successfully.
        """

        if getattr(self, 'prevent_wsgi_call', False):
            return

        # In case WebSocketServer is not used
        if not hasattr(self.server, 'clients'):
            self.server.clients = {}

        # Since we're now a websocket connection, we don't care what the
        # application actually responds with for the http response

        # hepo
        # the self.server.clients will be usefule if you want to re-store them to identifya client
        # but if you use nginx to proxy it, all the client_address if from unix socket, you can't get the ip and port
        # so you can't make this job done, so supports the special headers!
        if not self.client_address and 'HTTP_X_REAL_IP' in self.environ and 'HTTP_X_REAL_PORT' in self.environ:
            try:
                self.client_address = (self.environ['HTTP_X_REAL_IP'], int(self.environ['HTTP_X_REAL_PORT']))
            except:
                pass

        try:
            self.server.clients[self.client_address] = Client(
                self.client_address, self.websocket)
            self.application(self.environ, lambda s, h: [])
        finally:
            del self.server.clients[self.client_address]
            if not self.websocket.closed:
                self.websocket.close()
            self.environ.update({
                'wsgi.websocket': None
            })
            self.websocket = None

    def run_application(self):
        if (hasattr(self.server, 'pre_start_hook')
                and self.server.pre_start_hook):
            self.logger.debug("Calling pre-start hook")
            if self.server.pre_start_hook(self):
                return super(WebSocketHandler, self).run_application()

        self.logger.debug("Initializing WebSocket")
        self.result = self.upgrade_websocket()

        if hasattr(self, 'websocket'):
            if self.status and not self.headers_sent:
                try:
                    self.write('')
                except socket.error: # maybe a broken pipe that closed by client side
                    return

            self.run_websocket()
        else:
            if self.status:
                # A status was set, likely an error so just send the response
                if not self.result:
                    self.result = []

                self.process_result()
                return

            # This handler did not handle the request, so defer it to the
            # underlying application object
            return super(WebSocketHandler, self).run_application()

    def handle_error(self, type, value, tb):
        if type == socket.error and getattr(value, 'strerror', '') in ['Broken pipe']:
            # broken pipe by client, so ignore
            return
        else:
            return WSGIHandler.handle_error(self, type, value, tb)

    def upgrade_websocket(self):
        """
        Attempt to upgrade the current environ into a websocket enabled
        connection. If successful, the environ dict with be updated with two
        new entries, `wsgi.websocket` and `wsgi.websocket_version`.

        :returns: Whether the upgrade was successful.
        """

        # Some basic sanity checks first

        self.logger.debug("Validating WebSocket request")

        if self.environ.get('REQUEST_METHOD', '') != 'GET':
            # This is not a websocket request, so we must not handle it
            self.logger.debug('Can only upgrade connection if using GET method.')
            return

        upgrade = self.environ.get('HTTP_UPGRADE', '').lower()

        if upgrade == 'websocket':
            connection = self.environ.get('HTTP_CONNECTION', '').lower()

            if 'upgrade' not in connection:
                # This is not a websocket request, so we must not handle it
                self.logger.warning("Client didn't ask for a connection "
                                    "upgrade")
                return
        else:
            # This is not a websocket request, so we must not handle it
            return

        if self.request_version != 'HTTP/1.1':
            self.start_response('402 Bad Request', [])
            self.logger.warning("Bad server protocol in headers")

            return ['Bad protocol version']

        if self.environ.get('HTTP_SEC_WEBSOCKET_VERSION'):
            return self.upgrade_connection()
        # old websocket @Hepo
        elif 'HTTP_SEC_WEBSOCKET_KEY1' in self.environ and 'HTTP_SEC_WEBSOCKET_KEY2' in self.environ:
            return self.upgrade_connection()
        else:
            self.logger.warning("No protocol defined")
            self.start_response('426 Upgrade Required', [
                ('Sec-WebSocket-Version', ', '.join(self.SUPPORTED_VERSIONS))])

            return ['No Websocket protocol version defined']

    def upgrade_connection(self):
        """
        Validate and 'upgrade' the HTTP request to a WebSocket request.

        If an upgrade succeeded then then handler will have `start_response`
        with a status of `101`, the environ will also be updated with
        `wsgi.websocket` and `wsgi.websocket_version` keys.

        :param environ: The WSGI environ dict.
        :param start_response: The callable used to start the response.
        :param stream: File like object that will be read from/written to by
            the underlying WebSocket object, if created.
        :return: The WSGI response iterator is something went awry.
        """

        if "HTTP_SEC_WEBSOCKET_KEY1" in self.environ and "HTTP_SEC_WEBSOCKET_KEY2" in self.environ:
            challenge = get_challenge(self.environ)
            if not challenge:
                return ['not supported']
            self.websocket = WebSocket(self.environ, Stream(self), self)
            self.environ.update({
                'wsgi.websocket_version': self.environ.get("HTTP_SEC_WEBSOCKET_VERSION", 'default'),
                'wsgi.websocket': self.websocket
            })
            headers = [
                ("Upgrade", "WebSocket"),
                ("Connection", "Upgrade"),
                ("Sec-WebSocket-Origin", self.websocket.origin),
                ("Sec-WebSocket-Protocol", self.websocket.protocol or 'draft'),
                ("Sec-WebSocket-Location", "ws://" + self.environ.get('HTTP_HOST') + self.websocket.path),
            ]
            self.logger.debug("WebSocket request accepted, switching protocols")
            self.start_response("101 Switching Protocols", headers)
            self.write(challenge)
            return



        self.logger.debug("Attempting to upgrade connection")

        version = self.environ.get("HTTP_SEC_WEBSOCKET_VERSION")

        if version not in self.SUPPORTED_VERSIONS:
            msg = "Unsupported WebSocket Version: {0}".format(version)

            self.logger.warning(msg)
            self.start_response('400 Bad Request', [
                ('Sec-WebSocket-Version', ', '.join(self.SUPPORTED_VERSIONS))
            ])

            return [msg]

        key = self.environ.get("HTTP_SEC_WEBSOCKET_KEY", '').strip()

        if not key:
            # 5.2.1 (3)
            msg = "Sec-WebSocket-Key header is missing/empty"

            self.logger.warning(msg)
            self.start_response('400 Bad Request', [])

            return [msg]

        try:
            key_len = len(base64.b64decode(key))
        except TypeError:
            msg = "Invalid key: {0}".format(key)

            self.logger.warning(msg)
            self.start_response('400 Bad Request', [])

            return [msg]

        if key_len != 16:
            # 5.2.1 (3)
            msg = "Invalid key: {0}".format(key)

            self.logger.warning(msg)
            self.start_response('400 Bad Request', [])

            return [msg]

        # Check for WebSocket Protocols
        requested_protocols = self.environ.get(
            'HTTP_SEC_WEBSOCKET_PROTOCOL', '')
        protocol = None

        if hasattr(self.application, 'app_protocol'):
            allowed_protocol = self.application.app_protocol(
                self.environ['PATH_INFO'])

            if allowed_protocol and allowed_protocol in requested_protocols:
                protocol = allowed_protocol
                self.logger.debug("Protocol allowed: {0}".format(protocol))

        self.websocket = WebSocket(self.environ, Stream(self), self)
        self.environ.update({
            'wsgi.websocket_version': version,
            'wsgi.websocket': self.websocket
        })

        headers = [
            ("Upgrade", "websocket"),
            ("Connection", "Upgrade"),
            ("Sec-WebSocket-Accept", base64.b64encode(
                hashlib.sha1(key + self.GUID).digest())),
        ]

        if protocol:
            headers.append(("Sec-WebSocket-Protocol", protocol))

        self.logger.debug("WebSocket request accepted, switching protocols")
        self.start_response("101 Switching Protocols", headers)

    @property
    def logger(self):
        if not hasattr(self.server, 'logger'):
            self.server.logger = create_logger(__name__)

        return self.server.logger

    def log_request(self):
        if '101' not in self.status:
            self.logger.info(self.format_request())

    @property
    def active_client(self):
        return self.server.clients[self.client_address]

    def start_response(self, status, headers, exc_info=None):
        """
        Called when the handler is ready to send a response back to the remote
        endpoint. A websocket connection may have not been created.
        """
        writer = super(WebSocketHandler, self).start_response(
            status, headers, exc_info=exc_info)

        self._prepare_response()

        return writer

    def _prepare_response(self):
        """
        Sets up the ``pywsgi.Handler`` to work with a websocket response.

        This is used by other projects that need to support WebSocket
        connections as part of a larger effort.
        """
        assert not self.headers_sent

        if not self.environ.get('wsgi.websocket'):
            # a WebSocket connection is not established, do nothing
            return

        # So that `finalize_headers` doesn't write a Content-Length header
        self.provided_content_length = False

        # The websocket is now controlling the response
        self.response_use_chunked = False

        # Once the request is over, the connection must be closed
        self.close_connection = True

        # Prevents the Date header from being written
        self.provided_date = True
