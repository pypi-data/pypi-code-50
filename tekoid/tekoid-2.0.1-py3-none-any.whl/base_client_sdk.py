from .client import Client

DEFAULT_SCOPE = ["openid", "profile"]
DEFAULT_BASE_URI = "https://oauth.develop.tekoapis.net"
DEFAULT_AUTHORIZE_PATH = "/oauth/authorize"
DEFAULT_TOKEN_PATH = "/oauth/token"
DEFAULT_REFRESH_TOKEN_PATH = "/oauth/token"
DEFAULT_REVOKE_TOKEN_PATH = "/oauth/revoke"
DEFAULT_JWKS_PATH = "/.well-known/jwks.json"
DEFAULT_USERINFO_PATH = "/userinfo"


class BaseClientSDK(object):
    def __init__(self, client_id, client_secret, **kwargs):
        self.client_id = client_id
        self.client_secret = client_secret
        self.scope = kwargs.get("scope", DEFAULT_SCOPE)
        self.base_uri = kwargs.get("base_uri", DEFAULT_BASE_URI)
        self.authorize_uri = self.base_uri + \
            kwargs.get("authorize_path", DEFAULT_AUTHORIZE_PATH)
        self.token_uri = self.base_uri + \
            kwargs.get("token_path", DEFAULT_TOKEN_PATH)
        self.refresh_token_uri = self.base_uri + \
            kwargs.get("refresh_token_path", DEFAULT_REFRESH_TOKEN_PATH)
        self.revoke_token_uri = self.base_uri + \
            kwargs.get("revoke_token_path", DEFAULT_REVOKE_TOKEN_PATH)
        self.jwks_uri = self.base_uri + \
            kwargs.get("jwks_path", DEFAULT_JWKS_PATH)
        self.userinfo_uri = self.base_uri + \
            kwargs.get("userinfo_path", DEFAULT_USERINFO_PATH)
        self.client = Client(verify_ssl=kwargs.get("verify_ssl") or True)

    def get_full_user_info(self, access_token):
        headers = {
            "Authorization": f"Bearer {access_token}"
        }
        res = self.client.get(self.userinfo_uri, headers=headers)
        return res.json(), res.status_code

    def is_public_client(self):
        return not bool(self.client_secret)
