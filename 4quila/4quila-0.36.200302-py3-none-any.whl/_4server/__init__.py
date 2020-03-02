# import _4quila
import json
import os
import inspect
from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application
from tornado.websocket import WebSocketHandler
from _4helper import _4ssert


class _WebSocketHandler(WebSocketHandler):
    async def open(self, *args, **kwargs):
        print(f"open {args} {kwargs}")

    async def on_close(self):
        print("close")

    async def on_message(self, message):
        print(f"handling {message}")
        self.write_message(f"got {message}")


class _Handler(RequestHandler):
    SUPPORTED_METHODS = ["GET", "POST"]

    def initialize(self, routes):
        self.routes = routes #pylint: disable=attribute-defined-outside-init

    async def get(self):
        await self.handle()

    async def post(self):
        await self.handle()

    async def handle(self):
        match_handler = None
        max_match_length = 0
        for path, handler in self.routes.items():
            if self.request.path.startswith(path):
                match_length = len(path)
                if match_length > max_match_length:
                    max_match_length = match_length
                    match_handler = handler

        if match_handler is None:
            self.set_status(404)
            self.finish()
            return

        func_name = "handle_%s" % self.request.path[max_match_length:]
        func = getattr(match_handler, func_name, None)
        if func is None:
            self.set_status(404)
            self.finish()
            return

        if self.request.arguments:
            request = dict(
                (i, j[0].decode()) for i, j in self.request.arguments.items()
            )
        else:
            request = json.loads(self.request.body or "{}")

        request = dict((i, str(j)) for i, j in request.items())

        func_parameters = inspect.signature(func).parameters
        for key, value in (
            ("headers", self.request.headers),
            ("body", self.request.body),
        ):
            _4ssert(key not in request)
            if key in func_parameters:
                request[key] = value

        response = await func(**request)

        if isinstance(response, dict):
            self.write(json.dumps(response))
        else:
            self.write(response)
        self.finish()


def start(settings):
    ip = settings.pop("ip", "127.0.0.1")
    port = int(settings.pop("port"))

    Application(
        [
            (r"/websocket", _WebSocketHandler),
            (r".*", _Handler, {"routes": settings.pop("routes", {})}),
        ],
        static_path=os.path.join(os.getcwd(), "static"),
    ).listen(port, address=ip)

    IOLoop.current().start()
