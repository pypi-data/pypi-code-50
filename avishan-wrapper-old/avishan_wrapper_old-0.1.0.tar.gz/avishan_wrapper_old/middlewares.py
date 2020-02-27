from . import thread_storage, current_request


class AvishanThreadStorage:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        current_request['request'] = request
        current_request['user'] = None
        current_request['user_group'] = None
        current_request['status_code'] = 200
        current_request['response'] = {}
        current_request['execution_time'] = -1
        current_request['exception'] = None
        current_request['traceback'] = None

        from avishan.exceptions import AvishanException
        from django.http import JsonResponse

        response = self.get_response(request)
        if response.status_code == 567:

            if not isinstance(current_request['exception'], AvishanException):
                AvishanException(current_request['exception'])
            return JsonResponse(current_request['response'], status=current_request['status_code'])

        if hasattr(thread_storage, 'current_request'):
            del thread_storage.current_request

        return response