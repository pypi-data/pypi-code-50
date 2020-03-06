from oidcmsg.oauth2.device_authorization import AuthorizationResponse
from oidcmsg.oauth2.device_authorization import AuthorizationRequest

from oidcendpoint.endpoint import Endpoint


class AuthorizationEndpoint(Endpoint):
    request_cls = AuthorizationRequest
    response_cls = AuthorizationResponse
    request_format = "urlencoded"
    response_format = "json"
    response_placement = "body"
    endpoint_name = "device_authorization_endpoint"
    name = "device_authorization"

    def process_request(self, request=None, **kwargs):
        pass