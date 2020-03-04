import os

from kisters.water.rest_client.auth import OpenIDConnect, TemporaryAccess


def test_openid_connect():
    client_id = os.environ["CLIENT_ID"]
    client_secret = os.environ["CLIENT_SECRET"]
    auth = OpenIDConnect(client_id, client_secret)
    access_token = auth.get_access_token()
    assert access_token
    assert isinstance(access_token, str)


def test_temporary_access():
    client_id = os.environ["CLIENT_ID"]
    client_secret = os.environ["CLIENT_SECRET"]
    auth = OpenIDConnect(client_id, client_secret)
    access_token = auth.get_access_token()
    assert access_token
    assert isinstance(access_token, str)
    temp_auth = TemporaryAccess(access_token)
    assert access_token == temp_auth.get_access_token()

    # def test02_access_token_expiration(self):
    #     # Warning: this method accesses private vars for testing purposes
    #     # we pretend the token is expired to trigger a token refresh
    #     fake_expiration = datetime.utcnow()
    #     authentication._access_token_expiration = fake_expiration
    #     old_token = authentication._access_token
    #     authentication.get_access_token()
    #     self.assertNotEqual(fake_expiration, authentication._access_token_expiration)
    #     self.assertNotEqual(old_token, authentication._access_token)
