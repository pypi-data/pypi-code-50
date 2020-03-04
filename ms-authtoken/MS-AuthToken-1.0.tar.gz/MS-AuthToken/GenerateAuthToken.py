import requests
import json

class AuthTokenGenerator():
    def GenerateAuthTokenCustomConfig(self, config):
        """
        Generate Microsoft authentication token for graph api and SharePoint rest api.
        """

        # username = request.data.get('username')
        # password = request.data.get('password')

        ## Sample config to send
        # config = {
        #     'grant_type': 'password',
        #     'client_id': settings.AZURE_CLIENT_ID,
        #     'client_secret': settings.AZURE_APP_SECRET,
        #     'userName': username,
        #     'password': password,
        #     'scope': settings.AZURE_AUTH_SCOPES,
        #     'TenantID': settings.AZURE_TENANT
        # }

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'SdkVersion': 'postman-graph/v1.0'
        }
        _url = "https://login.microsoftonline.com/{0}/oauth2/v2.0/token".format(config.TenantID)
        _body = config
        _response = requests.post(_url, headers=headers, data=_body)
        if 'access_token' in _response.json():
            access_token = _response.json()['access_token']
            return access_token
        else:
            return _response.json()
