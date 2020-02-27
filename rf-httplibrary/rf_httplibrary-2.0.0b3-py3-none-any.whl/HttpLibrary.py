# Copyright (C) 2019 Spiralworks Technologies Inc.

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN

import requests
import logging
import os

from requests_toolbelt import MultipartEncoder
from requests import Session, Response

from HttpLibrary.version import VERSION

LOGGER = logging.getLogger(__name__)


class HttpLibrary:
    u"""
        A test library for web services and rest ful api.

        == Table of contents ==

        - `Usage`
        - `Examples`
        - `Author`
        - `Developer Manual`
        - `Importing`
        - `Shortcuts`
        - `Keywords`

    = Usage =

    | =Settings= | =Value=         | =Parameter=          |
    | Library    | HttpLibrary     |                      |

    = Examples =

    |  =Setting=  |     =Value=    |
    | Library     | HttpLibrary    |

    | =Test Case= |     =Action=                  | =Argument=                 |    =Argument=            |
    | Example     | ${screenshotfile}             | Capture Page Screenshot    |                          |
    |             | New Http Session              |                            |                          |
    |             | Create Http Multipart Request | <url>                      |                          |
    |             | Add Http Request File         | file                       | ${screenshotfile}        |
    |             | Add Http Request Parameter    | <paramkey1>                | <paramvalue2>            |
    |             | Add Http Request Parameter    | <paramkey2>                | <paramvalue2>            |
    |             | Invoke Http Request           |                            |                          |
    |             | Http Raise For Status         |                            |                          |
    |             | Close Http Session            |                            |                          |


    | =Test Case= |     =Action=                  | =Argument=                 |    =Argument=            |
    | Example     | New Http Session              |                            |                          |
    |             | Create Http Get Request       | <url>                      |                          |
    |             | Add Http Request Parameter    | <paramkey1>                | <paramvalue2>            |
    |             | Add Http Request Parameter    | <paramkey2>                | <paramvalue2>            |
    |             | Invoke Http Request           |                            |                          |
    |             | Http Raise For Status         |                            |                          |
    |             | Close Http Session            |                            |                          |

    | =Test Case= |     =Action=                  | =Argument=                 |    =Argument=            |
    | Example     | New Http Session              |                            |                          |
    |             | Create Http Post Request      | <url>                      |                          |
    |             | Add Http Request Header       | <headerkey1>               | <headervalue1>           |
    |             | Add Http Request Header       | <headerkey1>               | <headervalue1>           |
    |             | Add Http Request Parameter    | <paramkey1>                | <paramvalue2>            |
    |             | Add Http Request Parameter    | <paramkey2>                | <paramvalue2>            |
    |             | Invoke Http Request           |                            |                          |
    |             | Http Raise For Status         |                            |                          |
    |             | Close Http Session            |                            |                          |


    = Author =

    Created: 11/06/2019

    Author: Shiela Buitizon | email:shiela.buitizon@mnltechnology.com

    Company: Spiralworks Technologies Inc.

    = Developer Manual =

        Compiling this pip package:
            - python setup.py bdist_wheel

        Uploading build to pip
            - python -m twine upload dist/*
    """

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_VERSION = VERSION

    def __init__(self):
        self.url = None
        self.session: Session = None
        self.params = []
        self.headers = {}
        self.status: int = None
        self.multipart = False
        self.request = None
        self.request_body = None
        self.response: Response = None

    def new_http_session(self):
        """
        Creates a new http session. Also closes previous session.

        Example:
        | New Http Session        |        |
        | Create Http Get Request | <url>  |
        | Invoke Http Request     |        |
        | Close Http Session      |        |
        """
        # make sure previous session is closed
        self.close_http_session()

        self.session = requests.session()
        self.params = []
        self.headers = {}
        self.status = None
        self.multipart = False
        self.request = None
        self.request_body = None
        self.response = None

    def create_new_session(self,
                           url,
                           headers={},
                           params=[],
                           cookies={},
                           files=None,
                           auth=None,
                           hooks=None,
                           timeout=None,
                           proxies=None,
                           verify=False,
                           ):
        """A Requests session.

        Provides cookie persistence, connection-pooling, and configuration.
        """
        if self._has_existing_session():
            self.close_http_session()
        self.session = requests.Session()

    def _has_existing_session(self):
        if self.session:
            return True

    def create_http_get_request(self, url=None):
        """
        Creates an Http Get Request.

        Example:
        | Create Http Get Request | <url> |
        """
        assert self.session, "No session created."
        self.request = getattr(self.session, 'get')
        self.url = url

    def create_http_post_request(self, url=None):
        """
        Creates an Http Post Request.

        Example:
        | Create Http Post Request | <url> |
        """
        assert self.session, "No session created."
        self.request = getattr(self.session, 'post')
        self.url = url

    def create_http_put_request(self, url=None):
        """
        Creates an Http Put Request.

        Example:
        | Create Http Put Request | <url> |
        """
        assert self.session, "No session created."
        self.request = getattr(self.session, 'put')
        self.url = url

    def create_http_delete_request(self, url=None):
        """
        Creates an Http Delete Request.

        Example:
        | Create Http Delete Request | <url> |
        """
        assert self.session, "No session created."
        self.request = getattr(self.session, 'delete')
        self.url = url

    def create_http_multipart_request(self, url=None):
        """
        Creates an Http Multipart Request.

        Example:
        | Create Http Multipart Request | <url> |
        """
        assert self.session, "No session created."
        self.multipart = True
        self.request = getattr(self.session, 'post')
        self.url = url

    def add_http_request_file(self, name, file, content_type='application/octet-stream', file_name=None):
        """
        Adds an HTTP Request File. This keyword is only allowed for multipart request

        Example:

        | ${screenshotfile}             | Capture Page Screenshot |                   |
        | New Http Session              |                         |                   |
        | Create Http Multipart Request | <url>                   |                   |
        | Add Http Request File         | file                    | ${screenshotfile} |
        | Add Http Request Parameter    | <paramkey1>             | <paramvalue2>     |
        | Add Http Request Parameter    | <paramkey2>             | <paramvalue2>     |
        | Invoke Http Request           |                         |                   |
        | Http Raise For Status         |                         |                   |
        | Close Http Session            |                         |                   |
        """
        assert self.multipart, "Only allowed for multipart request."
        assert os.path.isfile(file), "Not a valid file: " + str(file)

        if not file_name:
            path, file_name = os.path.split(file)

        LOGGER.info("filename: " + str(file_name))
        self.params.append((name, (file_name, open(file, 'rb'), content_type)))

    def add_http_request_parameter(self, name, value):
        """
        Adds an HTTP Request Parameter.

        Example:

        | Add HTTP Request Parameter | <paramkey> | <paramvalue> |
        """
        self.params.append((name, value))
        return self.params

    def update_request_parameter(self, params):
        """
        """
        self.params = params
        return self.params

    def add_http_request_header(self, name, value):
        """
        Adds HTTP Request Header.

        Example:

        | Add HTTP Request Header | Accept | application/json | # Indicates that json format is the acceptable media type for the response |
        """
        self.headers.update({name: value})
        return self.headers

    def update_request_header(self, **kwargs):
        """Takes in a dictionary as parameter, then adds it as a request header.
        """
        self.headers.update(kwargs)
        return self.headers

    def set_http_request_body(self, body):
        """
        Sets HTTP request body.

        Example:
        | New Http Session         |                |                  |                                                                            |
        | Create Http Post Request | <url>          |                  |                                                                            |
        | Add HTTP Request Header  | Accept         | application/json | # Indicates that json format is the acceptable media type for the response |
        | Set Http Request Body    | { json body }  |                  | # Accepts string, json, dictionary, etc depending on the Accept header set |
        | Invoke Http Request      |                |                  |                                                                            |
        | Close Http Session       |                |                  |                                                                            |
        """
        self.request_body = body

    def invoke_http_request(self):
        """
        Invokes Http Request

        Example:
        | New Http Session        |       |
        | Create Http Get Request | <url> |
        | Invoke Http Request     |       |
        | Close Http Session      |       |
        """
        assert self.session, "No session created."
        assert self.request, "No request created."

        data = self.params
        if self.multipart:
            m = MultipartEncoder(self.params)
            self.headers.update({'Content-Type': m.content_type})
            data = m
        elif self.request_body:
            data = self.request_body

        self._request_invoke(data)
        self.status = self.response.status_code

    def _request_invoke(self, data):
        LOGGER.info("url: " + self.url)
        LOGGER.info("method: " + self._get_method())
        LOGGER.info("headers: " + str(self.headers))
        LOGGER.info("params: " + str(self.params))

        if self._get_method() == 'get':
            self.response = self.request(self.url, params=data, headers=self.headers)
        else:
            self.response = self.request(self.url, data=data, headers=self.headers)

    def _get_method(self):
        return self.request.__name__

    def _close_file_params(self):
        if not self.params:
            return

        # make sure we close open files
        for param in self.params:
            value = param[1]
            if isinstance(value, tuple):
                value[1].close()

    def http_raise_for_status(self):
        """
        Raises stored :class:`HTTPError`, if one occurred.

        Example:
        | Raise For Status |
        """
        assert self.response is not None, "No request invoked."
        self.response.raise_for_status()

    def http_response_status_code_should_be_equal_to(self, status_code: int):
        """
        Asserts response status code value

        Example:
        | Http Response Status Code Should Be Equal |
        """
        assert self.status, "No request invoked."
        assert self.status == status_code, "Expecting response status code of " + str(status_code)

    def assert_response_status(self, statusCode):
        """
        """
        if self.status:
            assert str(self.response.status_code) == str(statusCode)

    def return_response_status(self):
        return self.response.status_code

    def get_http_response_string(self):
        """
        Returns http response string

        Example:
        | New Http Session        |                          |
        | Create Http Get Request | <url>                    |
        | Invoke Http Request     |                          |
        | ${responsetext}         | Get Http Response String |
        | Close Http Session      |                          |
        """
        assert self.response is not None, "No request invoked."
        return self.response.text

    def get_http_response_json(self):
        """
        Returns http response json

        Example:
        | New Http Session        |                        |
        | Create Http Get Request | <url>                  |
        | Invoke Http Request     |                        |
        | ${responsejson}         | Get Http Response Json |
        | Close Http Session      |                        |
        """
        assert self.response is not None, "No request invoked."
        return self.response.json()

    def _consume_response(self):
        self._close_file_params()

        if self.response is not None:
            self.response.close()

    def close_http_session(self):
        """
        Closes http session

        Example:
        | New Http Session        |       |
        | Create Http Get Request | <url> |
        | Invoke Http Request     |       |
        | Close Http Session      |       |
        """
        self._consume_response()

        if self.session:
            self.session.close()
