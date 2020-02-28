
import base64
from apitracker_agent.conf.constants import EVENT
from apitracker_agent.instrumentation.packages.base import AbstractInstrumentedModule
from apitracker_agent.context import execution_context
from uuid import uuid4
import time
# Python 2 and 3: alternative 4
try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse


class RequestsInstrumentation(AbstractInstrumentedModule):
    name = "urllib3"

    instrument_list = [
        ("requests.sessions", "Session.send"),
    ]

    def call(self, module, method, wrapped, instance, args, kwargs):
        request = args[0]
        # record request received at first thing
        request_received_at = int(round(time.time() * 1000000000))

        parsed_url = urlparse(request.url)
        host_name = parsed_url.hostname

        client = execution_context.get_client()
        if client is None or host_name not in client.config.api_ids:
            return wrapped(*args, **kwargs)

        api_id = client.config.api_ids[host_name]

        # call actual code
        response = wrapped(*args, **kwargs)

        # calculate latency & queue up event
        response_received_at = int(round(time.time() * 1000000000))
        request.headers['Host'] = host_name
        if client is not None:
            client.queue(EVENT, {
                "eventId": uuid4(),
                "apiId": api_id,
                "request": {
                    "method": request.method,
                    "path": request.path_url,
                    "headers": dict(request.headers),
                    "body": request.body,
                    "query": "",
                    "receivedAt": request_received_at
                },
                "response": {
                    "headers": dict(response.headers),
                    "statusCode": response.status_code,
                    "body": base64.b64encode(response.content),
                    "receivedAt": response_received_at
                }
            })
        return response
