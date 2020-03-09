import json
import jwt
import calendar
from datetime import datetime
from oauth2client.client import Credentials
from . import credentials


class AccessToken(Credentials):
    def __init__(self, crd):
        self.valid = True
        self.data = json.loads(crd.to_json())

    def get(self, key="access_token"):
        return self.data[key]

    def is_expired(self):
        try:
            payload = jwt.decode(self.data["access_token"], verify=False)
        except jwt.ExpiredSignatureError:
            return True

        now = calendar.timegm(datetime.utcnow().utctimetuple())
        expired = payload["exp"] < now
        return expired


def get_access_token(ctx, refresh=None):
    return AccessToken(credentials.get_credentials(ctx, refresh))
