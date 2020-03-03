from flask import request
from ...constants import responses
from ...constants.enums import HttpCode
from ..utils import token_decode
from .user import set_current_user
from ..repository import UserRepository, WhitelistTokenRepository


def _response_unauthorized(message: str = None) -> (dict, int):
    """Crea una respuesta de "unauthorized"

    Args:
        message (str): Default None

    Returns:
        body (dict)
        http_code (int)
    """
    return dict(
        message=message if message else responses.UNAUTHORIZED
    ), HttpCode.UNAUTHORIZED.value


def required(role: str = None):
    """Decorador para validar token jwt.
    Si role es diferente de None, verifica tambien el role

    Args:
        role (str)

    Returns:
        body (dict)
        http_code (int|None)
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            authorization = request.headers.get('Authorization')
            if not authorization:
                # header sin "Authorization"
                return _response_unauthorized()

            auth_type, token = authorization.split(' ')
            if auth_type != 'Bearer':
                # Tipo de "Authorization" no valido
                return _response_unauthorized()

            payload = token_decode(token)
            if payload.error:
                # Error de token
                return _response_unauthorized(payload.error)

            in_whitelist = WhitelistTokenRepository.find_one(token=token)
            if not in_whitelist:
                # El token no esta en la lista blanca
                return _response_unauthorized()

            user = UserRepository.find(payload.user_id)
            if not user:
                # Usuario no encontrado
                return _response_unauthorized()

            if role and role != user.role.name:
                # Role incorrecto
                return _response_unauthorized()

            set_current_user(user)

            return func(*args, **kwargs)
        return wrapper
    return decorator
