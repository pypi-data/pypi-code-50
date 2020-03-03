import pkg_resources
import logging
from queue import Queue
from .general_middleware import GeneralMiddleware
from .sql_middleware import SQLMiddleware
from .time_middleware import TimeMiddleware
from ..thread import MoonroofThread

log = logging.getLogger('moonroof')

MAX_QUEUE_SIZE=10000
MAX_BATCH_SIZE=100

class MoonroofMiddleware(object):

    def __init__(self, get_response):
        self.queue = Queue(MAX_QUEUE_SIZE)
        self.thread = MoonroofThread(queue=self.queue, max_batch_size=MAX_BATCH_SIZE)
        self.middlewares = [TimeMiddleware(), GeneralMiddleware(), SQLMiddleware()]
        self.get_response = get_response
        self.thread.start()

    def __call__(self, request):
        try:
            [middleware.before(request) for middleware in self.middlewares]
        except:
            log.error('Middleware failed before response: {0}'.format(err))
        response = self.get_response(request)
        try:
            data = {middleware.key(): middleware.value(request, response) for middleware in self.middlewares}
            version = pkg_resources.get_distribution('moonroof').version
            log.debug('version {}'.format(version))
            data['version'] = version
            endpoint_details = {'method': request.method}
            if request.resolver_match:
                endpoint_details = {
                    **endpoint_details,
                    'route': request.resolver_match.route,
                    'url_name': request.resolver_match.url_name,
                    'view_name': request.resolver_match.view_name
                }
            self.queue.put({
                'endpoint': request.get_full_path(),
                'endpoint_details': endpoint_details,
                **data
            })
        except err:
            log.error('Middleware failed after response: {0}'.format(err))
        return response

    # def process_view(self, request, view_func, view_args, view_kwargs):
    #     log.debug('Processing View', request.resolver_match.route, request.method, request.resolver_match.url_name, request.resolver_match.view_name)

