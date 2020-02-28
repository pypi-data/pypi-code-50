
import base64
from apitracker_agent.conf.constants import EVENT
from apitracker_agent.instrumentation.packages.base import AbstractInstrumentedModule
from urllib.parse import urlparse
from apitracker_agent.context import execution_context
from uuid import uuid4
import time


class RequestsInstrumentation(AbstractInstrumentedModule):
    name = "urllib3"

    instrument_list = [
        ("requests.sessions", "Session.send"),
    ]

    def call(self, module, method, wrapped, instance, args, kwargs):
        request = args[0]
        request_received_at = int(round(time.time() * 1000000000))

        response = wrapped(*args, **kwargs)
        response_received_at = int(round(time.time() * 1000000000))
        client = execution_context.get_client()
        parsed_url = urlparse(request.url)
        request.headers['Host'] = parsed_url.hostname
        if client is not None:
            client.queue(EVENT, {
                "eventId": uuid4(),
                "apiId": "6349ca11-e387-4eea-a790-496d2eecbed7",
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
