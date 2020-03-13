from .base_client_sdk import BaseClientSDK
import base64


class CredentialsClientSDK(BaseClientSDK):
    def __init__(self, client_id, client_secret, **kwargs):
        super().__init__(client_id, client_secret, **kwargs)

    def get_token(self):
        body = {
            "grant_type": "client_credentials",
            "scope": ' '.join(self.scope)
        }
        res = self.client.post(self.token_uri,
                               auth=(self.client_id, self.client_secret), data=body)
        return res.json(), res.status_code
