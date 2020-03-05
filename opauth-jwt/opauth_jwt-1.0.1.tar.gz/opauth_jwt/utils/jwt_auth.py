import jwt
from .decorators import exceptionHandler
from ..settings import auth_settings


def jwt_get_secret_key(payload=None):
    return payload.get("secret", "")


@exceptionHandler(result={})
def jwt_decode_handler(token):
    options = {
        'verify_exp': True,
    }
    unverified_payload = jwt.decode(token, None, False)
    secret_key = jwt_get_secret_key(unverified_payload)
    return jwt.decode(
        token,
        key=secret_key,
        verify=True,
        options=options,
        leeway=auth_settings.JWT_LEEWAY,
        audience=auth_settings.JWT_AUDIENCE,
        issuer=auth_settings.JWT_ISSUER,
        algorithms=[auth_settings.JWT_ALGORITHM]
    )
