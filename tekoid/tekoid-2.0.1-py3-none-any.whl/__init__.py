from .code_client_sdk import CodeClientSDK
from .credentials_sdk import CredentialsClientSDK


class ClientSDK(object):
    """ this object is used to get, refresh token, user info from oauth server"""

    def __init__(self, client_id, client_secret, redirect_uri, **kwargs):
        """ constructor

        :param client_id: the app's client id
        :type client_id : str

        :param client_secret: the app's client secret
        :type client_secret : str


        :param redirect_uri: redirect uri will callback from oauth server
        :type redirect_uri : str


        :param scope: scope used to fetch user info.
        :type scope : array of string


        :param base_uri: base uri of oauth server
        :type base_uri : str


        :param authorize_path: authorize path of oauth server
        :type authorize_path : str


        :param token_path: token path of oauth server
        :type token_path : str


        :param refresh_token_path: path to refresh token path of oauth server
        :type refresh_token_path : str


        :param revoke_token_path: path to revoke token of oauth server
        :type revoke_token_path : str


        :param jwks_path: path to get jwks of oauth server
        :type jwks_path : str


        :param userinfo_path: path to get user info of oauth server
        :type userinfo_path : str
        """

        self.code = CodeClientSDK(
            client_id, client_secret, redirect_uri, **kwargs)

        self.credentials = CredentialsClientSDK(
            client_id, client_secret, **kwargs)
