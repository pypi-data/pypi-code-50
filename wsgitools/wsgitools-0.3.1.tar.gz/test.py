#!/usr/bin/env python

import base64
import unittest
import doctest
import re
import wsgiref.validate
import io
from hashlib import md5
import sys

from wsgitools.internal import bytes2str, str2bytes

class Request(object):
    def __init__(self, case):
        """
        @type case: unittest.TestCase
        """
        self.testcase = case
        self.environ = dict(
            REQUEST_METHOD="GET",
            SERVER_NAME="localhost",
            SERVER_PORT="80",
            SCRIPT_NAME="",
            PATH_INFO="",
            QUERY_STRING="")
        self.environ.update({
            "wsgi.version": (1, 0),
            "wsgi.input": io.BytesIO(),
            "wsgi.errors": sys.stderr,
            "wsgi.url_scheme": "http",
            "wsgi.multithread": False,
            "wsgi.multiprocess": False,
            "wsgi.run_once": False})

    def setenv(self, key, value):
        """
        @type key: str
        @type value: str
        @returns: self
        """
        self.environ[key] = value
        return self

    def setmethod(self, request_method):
        """
        @type request_method: str
        @returns: self
        """
        return self.setenv("REQUEST_METHOD", request_method)

    def setheader(self, name, value):
        """
        @type name: str
        @type value: str
        @returns: self
        """
        return self.setenv("HTTP_" + name.upper().replace('-', '_'), value)

    def copy(self):
        req = Request(self.testcase)
        req.environ = dict(self.environ)
        return req

    def __call__(self, app):
        app = wsgiref.validate.validator(app)
        res = Result(self.testcase)
        def write(data):
            res.writtendata.append(data)
        def start_response(status, headers, exc_info=None):
            res.statusdata = status
            res.headersdata = headers
            return write
        iterator = app(self.environ, start_response)
        res.returneddata = list(iterator)
        if hasattr(iterator, "close"):
            iterator.close()
        return res

class Result(object):
    def __init__(self, case):
        """
        @type case: unittest.TestCase
        """
        self.testcase = case
        self.statusdata = None
        self.headersdata = None
        self.writtendata = []
        self.returneddata = None

    def status(self, check):
        """
        @type check: int or str
        """
        if isinstance(check, int):
            status = int(self.statusdata.split()[0])
            self.testcase.assertEqual(check, status)
        else:
            self.testcase.assertEqual(check, self.statusdata)

    def getheader(self, name):
        """
        @type name: str
        @raises KeyError:
        """
        for key, value in self.headersdata:
            if key == name:
                return value
        raise KeyError

    def header(self, name, check):
        """
        @type name: str
        @type check: str or (str -> bool)
        """
        found = False
        for key, value in self.headersdata:
            if key == name:
                found = True
                if isinstance(check, str):
                    self.testcase.assertEqual(check, value)
                else:
                    self.testcase.assertTrue(check(value))
        if not found:
            self.testcase.fail("header %s not found" % name)

    def get_data(self):
        return b"".join(self.writtendata) + b"".join(self.returneddata)

from wsgitools import applications

class StaticContentTest(unittest.TestCase):
    def setUp(self):
        self.app = applications.StaticContent(
            "200 Found", [("Content-Type", "text/plain")], b"nothing")
        self.req = Request(self)

    def testGet(self):
        res = self.req(self.app)
        res.status("200 Found")
        res.header("Content-length", "7")

    def testHead(self):
        req = self.req.copy()
        req.setmethod("HEAD")
        res = req(self.app)
        res.status(200)
        res.header("Content-length", "7")

class StaticFileTest(unittest.TestCase):
    def setUp(self):
        self.app = applications.StaticFile(io.BytesIO(b"success"), "200 Found",
                                           [("Content-Type", "text/plain")])
        self.req = Request(self)

    def testGet(self):
        res = self.req(self.app)
        res.status("200 Found")
        res.header("Content-length", "7")

    def testHead(self):
        req = self.req.copy()
        req.setmethod("HEAD")
        res = req(self.app)
        res.status(200)
        res.header("Content-length", "7")

from wsgitools import digest

class AuthDigestMiddlewareTest(unittest.TestCase):
    def setUp(self):
        self.staticapp = applications.StaticContent(
            "200 Found", [("Content-Type", "text/plain")], b"success")
        token_gen = digest.AuthTokenGenerator("foo", lambda _: "baz")
        self.app = digest.AuthDigestMiddleware(
            wsgiref.validate.validator(self.staticapp), token_gen)
        self.req = Request(self)

    def test401(self):
        res = self.req(self.app)
        res.status(401)
        res.header("WWW-Authenticate", lambda _: True)

    def test401garbage(self):
        req = self.req.copy()
        req.setheader('Authorization', 'Garbage')
        res = req(self.app)
        res.status(401)
        res.header("WWW-Authenticate", lambda _: True)

    def test401digestgarbage(self):
        req = self.req.copy()
        req.setheader('Authorization', 'Digest ","')
        res = req(self.app)
        res.status(401)
        res.header("WWW-Authenticate", lambda _: True)

    def doauth(self, password="baz", status=200):
        res = self.req(self.app)
        nonce = next(iter(filter(lambda x: x.startswith("nonce="),
                                 res.getheader("WWW-Authenticate").split())))
        nonce = nonce.split('"')[1]
        req = self.req.copy()
        token = md5(str2bytes("bar:foo:%s" % password)).hexdigest()
        other = md5(str2bytes("GET:")).hexdigest()
        resp = md5(str2bytes("%s:%s:%s" % (token, nonce, other))).hexdigest()
        req.setheader('Authorization', 'Digest algorithm=md5,nonce="%s",' \
                      'uri=,username=bar,response="%s"' % (nonce, resp))
        res = req(self.app)
        res.status(status)

    def test200(self):
        self.doauth()

    def test401authfail(self):
        self.doauth(password="spam", status=401)

    def testqopauth(self):
        res = self.req(self.app)
        nonce = next(iter(filter(lambda x: x.startswith("nonce="),
                                 res.getheader("WWW-Authenticate").split())))
        nonce = nonce.split('"')[1]
        req = self.req.copy()
        token = md5(str2bytes("bar:foo:baz")).hexdigest()
        other = md5(str2bytes("GET:")).hexdigest()
        resp = "%s:%s:1:qux:auth:%s" % (token, nonce, other)
        resp = md5(str2bytes(resp)).hexdigest()
        req.setheader('Authorization', 'Digest algorithm=md5,nonce="%s",' \
                      'uri=,username=bar,response="%s",qop=auth,nc=1,' \
                      'cnonce=qux' % (nonce, resp))
        res = req(self.app)
        res.status(200)

from wsgitools import middlewares

def writing_application(environ, start_response):
    write = start_response("404 Not found", [("Content-Type", "text/plain")])
    write = start_response("200 Ok", [("Content-Type", "text/plain")])
    write(b"first")
    yield b""
    yield b"second"

def write_only_application(environ, start_response):
    write = start_response("200 Ok", [("Content-Type", "text/plain")])
    write(b"first")
    write(b"second")
    yield b""

class NoWriteCallableMiddlewareTest(unittest.TestCase):
    def testWrite(self):
        app = middlewares.NoWriteCallableMiddleware(writing_application)
        res = Request(self)(app)
        self.assertEqual(res.writtendata, [])
        self.assertEqual(b"".join(res.returneddata), b"firstsecond")

    def testWriteOnly(self):
        app = middlewares.NoWriteCallableMiddleware(write_only_application)
        res = Request(self)(app)
        self.assertEqual(res.writtendata, [])
        self.assertEqual(b"".join(res.returneddata), b"firstsecond")

class StupidIO(object):
    """file-like without tell method, so StaticFile is not able to
    determine the content-length."""
    def __init__(self, content):
        self.content = content
        self.position = 0

    def seek(self, pos):
        assert pos == 0
        self.position = 0

    def read(self, length):
        oldpos = self.position
        self.position += length
        return self.content[oldpos:self.position]

class ContentLengthMiddlewareTest(unittest.TestCase):
    def customSetUp(self, maxstore=10):
        self.staticapp = applications.StaticFile(StupidIO(b"success"),
                "200 Found", [("Content-Type", "text/plain")])
        self.app = middlewares.ContentLengthMiddleware(self.staticapp,
                                                       maxstore=maxstore)
        self.req = Request(self)

    def testWithout(self):
        self.customSetUp()
        res = self.req(self.staticapp)
        res.status("200 Found")
        try:
            res.getheader("Content-length")
            self.fail("Content-length header found, test is useless")
        except KeyError:
            pass

    def testGet(self):
        self.customSetUp()
        res = self.req(self.app)
        res.status("200 Found")
        res.header("Content-length", "7")

    def testInfiniteMaxstore(self):
        self.customSetUp(maxstore=())
        res = self.req(self.app)
        res.status("200 Found")
        res.header("Content-length", "7")

class CachingMiddlewareTest(unittest.TestCase):
    def setUp(self):
        self.cached = middlewares.CachingMiddleware(self.app)
        self.accessed = dict()

    def app(self, environ, start_response):
        count = self.accessed.get(environ["SCRIPT_NAME"], 0) + 1
        self.accessed[environ["SCRIPT_NAME"]] = count
        headers = [("Content-Type", "text/plain")]
        if "maxage0" in environ["SCRIPT_NAME"]:
            headers.append(("Cache-Control", "max-age=0"))
        start_response("200 Found", headers)
        return [str2bytes("%d" % count)]

    def testCache(self):
        res = Request(self)(self.cached)
        res.status(200)
        self.assertEqual(res.get_data(), b"1")
        res = Request(self)(self.cached)
        res.status(200)
        self.assertEqual(res.get_data(), b"1")

    def testNoCache(self):
        res = Request(self)(self.cached)
        res.status(200)
        self.assertEqual(res.get_data(), b"1")
        res = Request(self).setheader(
                "Cache-Control", "max-age=0")(self.cached)
        res.status(200)
        self.assertEqual(res.get_data(), b"2")

class BasicAuthMiddlewareTest(unittest.TestCase):
    def setUp(self):
        self.staticapp = applications.StaticContent(
            "200 Found", [("Content-Type", "text/plain")], b"success")
        checkpw = middlewares.DictAuthChecker({"bar": "baz"})
        self.app = middlewares.BasicAuthMiddleware(
            wsgiref.validate.validator(self.staticapp), checkpw)
        self.req = Request(self)

    def test401(self):
        res = self.req(self.app)
        res.status(401)
        res.header("WWW-Authenticate", lambda _: True)

    def test401garbage(self):
        req = self.req.copy()
        req.setheader('Authorization', 'Garbage')
        res = req(self.app)
        res.status(401)
        res.header("WWW-Authenticate", lambda _: True)

    def test401basicgarbage(self):
        req = self.req.copy()
        req.setheader('Authorization', 'Basic ()')
        res = req(self.app)
        res.status(401)
        res.header("WWW-Authenticate", lambda _: True)

    def doauth(self, password="baz", status=200):
        req = self.req.copy()
        token = "bar:%s" % password
        token = bytes2str(base64.b64encode(str2bytes(token)))
        req.setheader('Authorization', 'Basic %s' % token)
        res = req(self.app)
        res.status(status)

    def test200(self):
        self.doauth()

    def test401authfail(self):
        self.doauth(password="spam", status=401)

from wsgitools import filters
import gzip

class RequestLogWSGIFilterTest(unittest.TestCase):
    def testSimple(self):
        app = applications.StaticContent("200 Found",
                [("Content-Type", "text/plain")], b"nothing")
        if isinstance("x", bytes):
            log = io.BytesIO()
        else:
            log = io.StringIO()
        logfilter = filters.RequestLogWSGIFilter.creator(log)
        app = filters.WSGIFilterMiddleware(app, logfilter)
        req = Request(self)
        req.environ["REMOTE_ADDR"] = "1.2.3.4"
        req.environ["PATH_INFO"] = "/"
        req.environ["HTTP_USER_AGENT"] = "wsgitools-test"
        res = req(app)
        logged = log.getvalue()
        self.assertTrue(re.match(r'^1\.2\.3\.4 - - \[[^]]+\] "GET /" '
                                 r'200 7 - "wsgitools-test"', logged))

class GzipWSGIFilterTest(unittest.TestCase):
    def testSimple(self):
        app = applications.StaticContent("200 Found",
                [("Content-Type", "text/plain")], b"nothing")
        app = filters.WSGIFilterMiddleware(app, filters.GzipWSGIFilter)
        req = Request(self)
        req.environ["HTTP_ACCEPT_ENCODING"] = "gzip"
        res = req(app)
        data = gzip.GzipFile(fileobj=io.BytesIO(res.get_data())).read()
        self.assertEqual(data, b"nothing")

def alltests(case):
    return unittest.TestLoader().loadTestsFromTestCase(case)

fullsuite = unittest.TestSuite()
fullsuite.addTest(doctest.DocTestSuite("wsgitools.digest"))
fullsuite.addTest(alltests(StaticContentTest))
fullsuite.addTest(alltests(StaticFileTest))
fullsuite.addTest(alltests(AuthDigestMiddlewareTest))
fullsuite.addTest(alltests(ContentLengthMiddlewareTest))
fullsuite.addTest(alltests(CachingMiddlewareTest))
fullsuite.addTest(alltests(BasicAuthMiddlewareTest))
fullsuite.addTest(alltests(NoWriteCallableMiddlewareTest))
fullsuite.addTest(alltests(RequestLogWSGIFilterTest))
fullsuite.addTest(alltests(GzipWSGIFilterTest))

if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    if "profile" in sys.argv:
        try:
            import cProfile as profile
        except ImportError:
            import profile
        prof = profile.Profile()
        prof.runcall(runner.run, fullsuite)
        prof.dump_stats("wsgitools.pstat")
    else:
        sys.exit(len(runner.run(fullsuite).failures))
