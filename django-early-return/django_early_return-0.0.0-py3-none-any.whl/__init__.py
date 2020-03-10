class EarlyReturn(Exception):
    '''
    Exception which views may raise, when using EarlyReturnMiddleware, to short-circuit view processing
    '''
    def __init__(self, response):
        self.response = response

class EarlyReturnMiddleware:
    '''
    Middleware which lets views/view decorators raise EarlyReturn to short-circuit processing
    '''
    def __init__(self, get_response):
        self.get_response = get_response
    def __call__(self, request):
        return self.get_response(request)
    def process_exception(self, request, exception):
        if isinstance(exception, EarlyReturn):
            return exception.response
