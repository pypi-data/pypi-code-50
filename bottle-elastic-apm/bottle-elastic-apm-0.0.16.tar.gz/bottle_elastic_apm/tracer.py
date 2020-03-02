from logging import NOTSET

import bottle
import elasticapm
from bottle import request, response
from elasticapm import setup_logging
from elasticapm.handlers.logging import LoggingHandler

from bottle_elastic_apm.utils import get_data_from_response, \
    get_data_from_request, trace_parent


class ELKApmPlugin:
    name = 'elastic_apm'
    api = 2

    def __init__(self, config=None, logging=False):
        self.logging = logging
        self.client = elasticapm.Client(
            framework_name=bottle.__name__,
            framework_version=bottle.__version__,
            config=config
        )

    def setup(self, _app):
        pass

    def apply(self, callback, _context):
        def wrapper(*args, **kwargs):
            self.client.begin_transaction('request',
                                          trace_parent=trace_parent())
            transaction_result = '2xx'
            try:
                res = callback(*args, **kwargs)
                transaction_result = self.set_response_information(response)
                return res
            except bottle.HTTPError as e:
                transaction_result = self.set_response_information(e)
                if transaction_result == '4xx':
                    self.client.capture_exception(context={
                        "request": get_data_from_request(request,
                                                         capture_body=self.client.config.capture_body in (
                                                             "errors", "all"),
                                                         capture_headers=self.client.config.capture_headers)
                    }, handled=True)
                raise e
            except Exception as error:
                transaction_result = '5xx'
                self.client.capture_exception(context={
                    "request": get_data_from_request(request,
                                                     capture_body=self.client.config.capture_body in (
                                                         "errors", "all"),
                                                     capture_headers=self.client.config.capture_headers)
                }, handled=False)
                raise error
            finally:
                transaction_name = self.set_request_information()
                self.client.end_transaction(transaction_name,
                                            transaction_result)

        return wrapper

    def set_request_information(self):
        submodule = request.script_name or ''
        transaction_name = f"{request.method} {submodule[:-1]}{request.route.rule}"
        elasticapm.set_context(
            lambda: get_data_from_request(request,
                                          capture_body=self.client.config.capture_body in (
                                              "transactions", "all"),
                                          capture_headers=self.client.config.capture_headers),
            "request")
        return transaction_name

    @staticmethod
    def set_response_information(local_response: bottle.BaseResponse):
        transaction_result = str(local_response.status_code)[0] + 'xx'
        elasticapm.set_context(
            lambda: get_data_from_response(local_response),
            "response")
        return transaction_result
