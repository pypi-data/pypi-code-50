import datetime
import bcrypt
import jwt
from flask_auth_service_mongo import config
from .models import User
from ..constants import responses


def password_hash(password: str) -> str:
    """
    Args:
        password (str)

    Returns:
        hashed (str)
    """
    password = password.encode()
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    return hashed.decode()


def password_match(password: str, hashed: str) -> bool:
    """
    Args:
        password (str)
        hashed (str)

    Returns:
        (bool)
    """
    password = password.encode()
    hashed = hashed.encode()
    return bcrypt.checkpw(password, hashed)


class Payload:
    """
    Attributes:
        error (str)
        user_id (str)
    """
    def __init__(
        self,
        error: str = None,
        user_id: str = None
    ):
        self.error = error
        self.user_id = user_id


def token_generate(user: User) -> str:
    """Genera un token jwt

    Args:
        user (security.models.User)

    Returns:
        (str)
    """
    expire = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    payload = {
        'exp': expire,
        'iat': datetime.datetime.utcnow(),
        'sub': str(user.id)
    }
    return jwt.encode(
        payload,
        config.SECRET_KEY,
        algorithm='HS256'
    ).decode()


def token_decode(token: str) -> Payload:
    """
    Args:
        token (str)

    Returns:
        (dict)
    """
    try:
        payload = jwt.decode(
            token,
            config.SECRET_KEY,
            algorithms=['HS256']
        )

        return Payload(
            user_id=payload['sub']
        )
    except jwt.ExpiredSignatureError:
        return Payload(responses.SIGNATURE_EXPIRED)
    except jwt.InvalidTokenError:
        return Payload(responses.INVALID_TOKEN)
    except Exception:
        return Payload(responses.INVALID_TOKEN)
