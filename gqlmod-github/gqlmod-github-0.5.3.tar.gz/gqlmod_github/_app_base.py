import time
import jwcrypto.jwt
import jwcrypto.jwk


class GithubBaseApp:
    # Lifespan of generated tokens
    LIFESPAN = 10 * 60  # 10min, documented maxmimum

    _token = None
    _expiration = None

    def __init__(self, app_id, pem_data):
        self.app_id = app_id
        self.key = jwcrypto.jwk.JWK.from_pem(pem_data)

    @property
    def token(self):
        """
        Returns the JWT-based App Token for calling GitHub as an application.

        This transparently manages expiration, so call directly for every use.
        (Do not cache.)

        This is per https://developer.github.com/apps/building-github-apps/authenticating-with-github-apps/
        """
        now = time.time()
        if self._token is None or self._expiration <= now:
            self._expiration = now + self.LIFESPAN
            jwt = jwcrypto.jwt.JWT(
                header={
                    "alg": "RS256",  # Hard coded
                },
                claims={
                    "iat": int(now),
                    "exp": int(self._expiration),
                    "iss": self.app_id,
                },
            )
            jwt.make_signed_token(self.key)
            self._token = jwt.serialize()

        return self._token
