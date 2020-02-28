#  BSD 3-Clause License
#
#  Copyright (c) 2019, Elasticsearch BV
#  All rights reserved.
#
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are met:
#
#  * Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
#
#  * Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
#  * Neither the name of the copyright holder nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
#  AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
#  IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
#  DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
#  FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
#  DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
#  SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
#  CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
#  OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
#  OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
import base64

from apitracker_agent.conf import constants
from apitracker_agent.conf.constants import EVENT
from apitracker_agent.instrumentation.packages.base import AbstractInstrumentedModule
from apitracker_agent.utils import default_ports
from apitracker_agent.context import execution_context
from uuid import uuid4
import time


class Urllib3Instrumentation(AbstractInstrumentedModule):
    name = "urllib3"

    instrument_list = [
        ("urllib3.connectionpool", "HTTPConnectionPool.urlopen"),
        # packages that vendor or vendored urllib3 in the past
        ("requests.packages.urllib3.connectionpool", "HTTPConnectionPool.urlopen"),
        ("botocore.vendored.requests.packages.urllib3.connectionpool", "HTTPConnectionPool.urlopen"),
    ]

    def call(self, module, method, wrapped, instance, args, kwargs):
        host = instance.host
        if host.endswith('apitracker.com'):
            return wrapped(*args, **kwargs)

        if "method" in kwargs:
            method = kwargs["method"]
        else:
            method = args[0]

        if "body" in kwargs:
            body = kwargs["body"]
        else:
            body = args[1]
        if body is not None:
            try:
                body.decode()
                body = base64.b64encode(body)
            except:
                body = base64.b64encode(body.encode('utf-8'))

        headers = None
        if "headers" in kwargs:
            headers = kwargs["headers"]
            if headers is None:
                headers = {}
                kwargs["headers"] = headers

        host = instance.host

        if instance.port != default_ports.get(instance.scheme):
            host += ":" + str(instance.port)

        if "url" in kwargs:
            url = kwargs["url"]
        else:
            url = args[1]

        # TODO: reconstruct URL more faithfully, e.g. include port
        request_received_at = int(round(time.time() * 1000000000))
        response = wrapped(*args, **kwargs)
        response_received_at = int(round(time.time() * 1000000000))
        client = execution_context.get_client()
        headers["Host"] = host
        if client is not None:
            client.queue(EVENT, {
                "eventId": uuid4(),
                "apiId": "6349ca11-e387-4eea-a790-496d2eecbed7",
                "request": {
                    "method": method,
                    "path": url,
                    "headers": dict(headers),
                    "body": body,
                    "query": "",
                    "receivedAt": request_received_at
                },
                "response": {
                    "headers": dict(response.headers),
                    "statusCode": response.status,
                    "body": base64.b64encode(response.data),
                    "receivedAt": response_received_at
                }
            })

        return response
