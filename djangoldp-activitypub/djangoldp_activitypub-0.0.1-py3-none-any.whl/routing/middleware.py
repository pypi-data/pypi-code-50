##
# A simple middleware component that lets you use a single Django
# instance to serve multiple versions of your app, chosen by the client
# using the HTTP Accept header.
# In your settings.py, map a value you're looking for in the Accept header
# to a urls.py file.
# HTTP_HEADER_ROUTING_MIDDLEWARE_URLCONF_MAP = {
#     'application/activity+json': 'djangoldp-activitypub.routing.urls'
# }
##

from builtins import object

from django.conf import settings
from django.utils.deprecation import MiddlewareMixin


class HTTPHeaderRoutingMiddleware(MiddlewareMixin, object):

    def process_request(self, request):
        if request.method == 'GET':
            try:
                for content_type in settings.HTTP_HEADER_ROUTING_MIDDLEWARE_URLCONF_MAP:
                    if request.META['HTTP_ACCEPT'].find(content_type) != -1 :
                        request.urlconf = settings.HTTP_HEADER_ROUTING_MIDDLEWARE_URLCONF_MAP[content_type]
            except KeyError:
                pass  # use default urlconf (settings.ROOT_URLCONF)
        elif hasattr(request, 'content_type'):
            try:
                for content_type in settings.HTTP_HEADER_ROUTING_MIDDLEWARE_URLCONF_MAP:
                    if request.content_type == content_type:
                        request.urlconf = settings.HTTP_HEADER_ROUTING_MIDDLEWARE_URLCONF_MAP[content_type]
            except KeyError:
                pass  # use default urlconf (settings.ROOT_URLCONF)

    def process_response(self, request, response):
        return response
