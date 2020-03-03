from collections import namedtuple

http_status_codes = {
    200: '200 OK',
    201: '201 Created',
    202: '202 Accepted',
    204: '204 No Content',
    205: '205 Reset Content',
    206: '206 Partial Content',

    301: '301 Moved Permanently',
    302: '302 Found',
    304: '304 Not Modified',

    400: '400 Bad Request',
    401: '401 Unauthorized',
    403: '403 Forbidden',
    404: '404 Not Found',
    405: '405 Method Not Allowed',

    500: '500 Internal Server Error',
    502: '502 Bad Gateway',
    503: '503 Service Temporary Unavailable',
}

HttpResponse = namedtuple('HttpResponse', ('status', 'headers', 'content'))


class HttpError(RuntimeError):
    def __init__(self, status, content, content_type):
        super().__init__()
        self.status = status
        self.extra_headers = []
        self.content_type = content_type
        self.content = content

    def as_response(self):
        resp = response(self.content, self.status, self.content_type)
        resp.headers.extend(self.extra_headers)
        return resp


class HttpBadRequest(HttpError):
    def __init__(self, content=b'', content_type=None):
        super().__init__(400, content, content_type)


class HttpForbidden(HttpError):
    def __init__(self, content=b'', content_type=None):
        super().__init__(403, content, content_type)


class HttpNotFound(HttpError):
    def __init__(self, content=b'', content_type=None):
        super().__init__(404, content, content_type)


class HttpInternalServerError(HttpError):
    def __init__(self, content=b'', content_type=None):
        super().__init__(500, content, content_type)


class HttpMethodNotAllowed(HttpError):
    def __init__(self, allowed_methods, content=b'', content_type=None):
        super().__init__(405, content, content_type)
        self.allowed_methods = allowed_methods

    def as_response(self):
        resp = super().as_response()
        resp.headers.insert(0, ('Allow', ', '.join(self.allowed_methods)))
        return resp


def response(content, status=200, content_type=None):
    resp = HttpResponse(
        http_status_codes.get(status) or str(status),
        [],
        content
    )
    if content_type is not None:
        resp.headers.append(
            ('Content-Type', str(content_type))
        )

    return resp


def redirect(location, permanent=False):
    return HttpResponse(http_status_codes[301 if permanent else 302], [
        ('Location', location),
    ], (b'',), )


def send_response(resp, start_response):
    start_response(resp.status, resp.headers)

    if isinstance(resp.content, (str, bytes, bytearray)):
        yield resp.content
    else:
        yield from resp.content
