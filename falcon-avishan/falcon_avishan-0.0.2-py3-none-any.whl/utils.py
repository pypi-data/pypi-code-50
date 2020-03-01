import datetime
import decimal

import falcon
from falcon.request import Request
from falcon.response import Response


class AvishanRequest:
    req: Request = None
    data: dict = {}
    params: dict = {}

    def __init__(self, req: Request):
        self.req = req
        data = {}
        if 'request' in req.context.keys():
            data = req.context['request']
        self.data = data
        self.params = req.params


class AvishanResponse:
    res: Response = None
    data: dict = {}
    status_code = falcon.HTTP_200

    def __init__(self, res: Response, data: dict = None):
        if data is None:
            data = {}
        self.res = res
        self.data = data


def json_serializer(obj):
    if isinstance(obj, datetime.datetime):
        return str(obj)
    elif isinstance(obj, decimal.Decimal):
        return str(obj)
    raise TypeError('Cannot serialize {!r} (type {})'.format(obj, type(obj)))


def all_subclasses(cls):
    return set(cls.__subclasses__()).union(
        [s for c in cls.__subclasses__() for s in all_subclasses(c)])
