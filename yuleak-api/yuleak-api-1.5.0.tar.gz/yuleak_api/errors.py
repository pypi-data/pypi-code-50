class YuleakAPIError(Exception):
    def __init__(self, json_error):
        error = json_error.get('error')
        if error is not None:
            Exception.__init__(self, '{0} [{1}]'.format(error.get('message'), error.get('code')))
        else:
            Exception.__init__(self, json_error.get('message', 'Unkwown error.'))
