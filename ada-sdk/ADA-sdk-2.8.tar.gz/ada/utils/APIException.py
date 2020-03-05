class APIException(Exception):
    def __init__(self, message):
        super(APIException, self).__init__(message)
