
class RequestTools():
    """ """

    def get_auth_from_request(self, request):
        """Estract auth_data from request object"""
        try:
            auth_data = request.auth.decode()
        except Exception as e:
            print(e)
            auth_data = ''

        return auth_data
