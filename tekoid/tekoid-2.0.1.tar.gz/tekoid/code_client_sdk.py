import jwt
import json
import random
import string
import urllib
from urllib.parse import urlparse, parse_qs
from .base_client_sdk import BaseClientSDK
import base64
from hashlib import sha256
from .errors import StateInvalidException, NonceInvalidException


class CodeClientSDK(BaseClientSDK):
    def __init__(self, client_id, client_secret, redirect_uri, **kwargs):
        super().__init__(client_id, client_secret, **kwargs)

        self.redirect_uri = redirect_uri
        self.__get_public_keys()

    def __get_public_keys(self):
        jwks = self.client.get(self.jwks_uri).json()
        public_keys = {}
        for jwk in jwks.get('keys'):
            kid = jwk['kid']
            public_keys[kid] = jwt.algorithms.RSAAlgorithm.from_jwk(
                json.dumps(jwk))

        self.public_keys = public_keys

    def __random_string(self, len=50):
        pattern = ''.join(
            (string.ascii_uppercase, string.ascii_lowercase, string.digits))
        return ''.join(random.choice(pattern) for _ in range(len))

    def get_authorization_url(self):
        authorize_uri = self.authorize_uri
        state = self.__random_string()
        nonce = self.__random_string()

        query_dict = {
            "response_type": "code",
            "client_id": self.client_id,
            "redirect_uri": self.redirect_uri,
            "scope": ' '.join(self.scope),
            "state": state,
            "nonce": nonce
        }

        if self.is_public_client():
            code_verifier = self.__random_string()

            code_challenge = base64.urlsafe_b64encode(
                sha256(code_verifier.encode('utf-8')).digest()).decode('utf-8')
            code_challenge = code_challenge.replace('=', '')

            query_dict["code_challenge"] = code_challenge
            query_dict["code_challenge_method"] = "S256"

        query = urllib.parse.urlencode(query_dict)

        authorization_url = f'{authorize_uri}?{query}'

        if self.is_public_client():
            return authorization_url, state, nonce, code_verifier
        else:
            return authorization_url, state, nonce

    def get_token(self, url, state, nonce=None, code_verifier=None):
        params = parse_qs(urlparse(url).query)
        req_state = params['state'][0]
        code = params['code'][0]
        if (state != req_state):
            raise StateInvalidException()

        redirect_uri = self.redirect_uri

        body = {
            "redirect_uri": redirect_uri,
            "grant_type": "authorization_code",
            "code": code
        }

        if code_verifier is not None:
            body["code_verifier"] = code_verifier
            body["client_id"] = self.client_id
            res = self.client.post(self.token_uri,
                                   data=body)
        else:
            res = self.client.post(self.token_uri,
                                   data=body, auth=(self.client_id, self.client_secret))

        data = res.json()

        if "id_token" in data:
            id_token = data["id_token"]
            nonce_token = jwt.decode(id_token, verify=False, algorithms=[
                'RSA256']).get('nonce')

            if nonce != nonce_token:
                raise NonceInvalidException(f"invalid nonce = {nonce}")

        return res.json(), res.status_code

    def __decode_token(self, token):
        kid = jwt.get_unverified_header(token).get('kid')
        aud = jwt.decode(token, verify=False, algorithms=[
            'RSA256']).get('aud')

        if kid not in self.public_keys:
            self.__get_public_keys()

        pubkey = self.public_keys.get(kid)
        payload = jwt.decode(token, key=pubkey, algorithms=[
            "RS256"], audience=aud)

        return payload

    def get_user_info(self, token):
        return self.__decode_token(token)

    def refresh_token(self, refresh_token):
        body = {
            "grant_type": "refresh_token",
            "refresh_token": refresh_token,
            "scope": ' '.join(self.scope),
            "client_id": self.client_id
        }
        
        res = self.client.post(self.refresh_token_uri,
                               data=body, auth=(self.client_id, self.client_secret))

        return res.json(), res.status_code
