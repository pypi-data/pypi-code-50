import functools
import json
from itertools import chain
from urllib.parse import parse_qs

from .request import RequestQueryParams
from .response import HttpMethodNotAllowed, HttpError, HttpResponse


def with_response_support(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            res = func(*args, **kwargs)
            if res.status:
                return res
            yield from res
        except HttpError as err:
            return err.as_response()

    return wrapper


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


def parse_request_input(request, content_type=None):
    content_type = content_type or request.content_type
    content = request.input.read(int(request.environ['CONTENT_LENGTH']))

    if content_type.startswith('application/x-www-form-urlencoded'):
        try:
            return RequestQueryParams(parse_qs(content))
        except Exception:
            raise ValueError()
    elif content_type.startswith('application/json'):
        try:
            return json.loads(content)
        except Exception:
            raise ValueError()
    elif content_type.startswith('multipart/form-data'):
        raise NotImplemented('multipart/form-data content type is not supported')
    else:
        raise ValueError('Unknown request content type')
