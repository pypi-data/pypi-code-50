import requests
import json

class AuthTokenGenerator():
    def GenerateAuthTokenCustomConfig(self, config):
        """
        Generate Microsoft authentication token for graph api and SharePoint rest api.

        Sample config to pass:
        
        config = {
            'grant_type': 'password',
            'client_id': YOUR_CLIENT_ID,
            'client_secret': YOUR_APP_SECRET,
            'userName': YOUR_USERNAME,
            'password': YOUR_PASSWORD,
            'scope': SCOPES,  ## For Graph api use: openid https://graph.microsoft.com/.default For sharepoint rest api use: openid https://your_tenant.sharepoint.com/.default
            'TenantID': YOUR_TENANT_ID
        }

        """

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



    def GenerateAuthTokenSharepoint(self, client_id, client_secret, userName, password, TenantID, tenantName):
        """
        Generate authentication token for SharePoint rest api.
        """

        config = {
            'grant_type': 'password',
            'client_id': client_id,
            'client_secret': client_secret,
            'userName': userName,
            'password': password,
            'scope': 'openid https://{0}.sharepoint.com/.default'.format(tenantName), 
            'TenantID': TenantID
        }


        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'SdkVersion': 'postman-graph/v1.0'
        }
        _url = "https://login.microsoftonline.com/{0}/oauth2/v2.0/token".format(TenantID)
        _body = config
        _response = requests.post(_url, headers=headers, data=_body)
        if 'access_token' in _response.json():
            access_token = _response.json()['access_token']
            return access_token
        else:
            return _response.json()



    def GenerateAuthTokenGraphApi(self, client_id, client_secret, userName, password, TenantID, tenantName):
        """
        Generate authentication token for MS Graph api.
        """

        config = {
            'grant_type': 'password',
            'client_id': client_id,
            'client_secret': client_secret,
            'userName': userName,
            'password': password,
            'scope': 'openid https://graph.microsoft.com/.default',
            'TenantID': TenantID
        }


        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'SdkVersion': 'postman-graph/v1.0'
        }
        _url = "https://login.microsoftonline.com/{0}/oauth2/v2.0/token".format(TenantID)
        _body = config
        _response = requests.post(_url, headers=headers, data=_body)
        if 'access_token' in _response.json():
            access_token = _response.json()['access_token']
            return access_token
        else:
            return _response.json()
