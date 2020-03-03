from urllib.parse import parse_qs


class Request:
    def __init__(self, environ):
        self.environ = environ

        self._headers = None
        self._get = None

    @property
    def method(self):
        return self.environ['REQUEST_METHOD']

    @property
    def content_type(self):
        return self.environ['CONTENT_TYPE']

    @property
    def host(self):
        return self.environ['HTTP_HOST']

    @property
    def referrer(self):
        return self.environ['HTTP_REFERER']

    @property
    def user_agent(self):
        return self.environ['HTTP_USER_AGENT']

    @property
    def path(self):
        return self.environ['PATH_INFO']

    @property
    def query_string(self):
        return self.environ['QUERY_STRING']

    @property
    def get(self):
        if self._get is None:
            self._get = RequestQueryParams(parse_qs(self.environ['QUERY_STRING']))

        return self._get

    @property
    def input(self):
        return self.environ['wsgi.input']


class RequestQueryParams:
    def __init__(self, params):
        self._params = params

    def get(self, param, default=None):
        v = self.getlist(param)
        if v is None:
            return default
        return v[0]

    def getlist(self, param, default=None):
        return self._params.get(param, default)
