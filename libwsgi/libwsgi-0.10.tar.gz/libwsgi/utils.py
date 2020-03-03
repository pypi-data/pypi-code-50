import functools
from itertools import chain

from .request import Request
from .response import HttpMethodNotAllowed, HttpError, response, send_response, HttpResponse


def reqresp(func):
    @functools.wraps(func)
    def application(environ, start_response):
        req = Request(environ)

        error = None
        try:
            resp = func(req)
            if not resp.status:
                resp = response(b'', status=500)
        except HttpError as e:
            resp = e.as_response()
        except Exception as exc:
            resp = response(b'', status=500)
            error = exc

        yield from send_response(resp, start_response)

        if error:
            raise error

    return application


def streaming(handler):
    @functools.wraps(handler)
    def wrapper(request, *args, **kwargs):
        generator = handler(request, *args, **kwargs)

        resp = next(generator)
        return HttpResponse(
            status=resp.status,
            headers=resp.headers,
            content=chain((resp.content,), generator)
        )

    return wrapper


def allowed_http_methods(allowed_methods):
    def inner(handler):
        @functools.wraps(handler)
        def wrapper(request, *args, **kwargs):
            if request.method not in allowed_methods:
                raise HttpMethodNotAllowed(allowed_methods)

            return handler(request, *args, **kwargs)

        return wrapper

    return inner
