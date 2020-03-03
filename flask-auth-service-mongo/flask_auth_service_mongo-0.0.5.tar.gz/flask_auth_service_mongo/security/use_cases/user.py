import datetime
from ...constants import responses
from ...constants.enums import HttpCode
from flask_auth_service_mongo.utils.use_case import Response, UseCaseInterface
from flask_auth_service_mongo.utils.validator import Validator
from flask_auth_service_mongo import config
from ..utils import password_match, token_generate, password_hash
from ..models import User, Role, WhitelistToken
from ..repository import UserRepository, WhitelistTokenRepository


class LoginResponse(Response):
    """Respuesta para los casos de uso login

    Attributes:
        token (str)
        http_code (int)
        message (str)
        errors (list)
    """
    def __init__(self, token: str = None, *args, **kwargs):
        self.token = token

        super(LoginResponse, self).__init__(*args, **kwargs)


class Login(UseCaseInterface):

    def handle(self, role: str, request: dict) -> LoginResponse:
        """
        Args:
            role (str)
            request (dict)

        Returns:
            security.use_cases.LoginResponse:
        """
        self.__token_enable = config.WHITE_LIST_TOKEN
        self._role = role
        self._request = request

        valid, errors = self.__request_is_valid()
        if not valid:
            return LoginResponse(
                message=responses.BAD_REQUEST,
                http_code=HttpCode.BAD_REQUEST,
                errors=errors
            )

        self._username = self._request['username'].lower()
        self._user = UserRepository.find_one(username=self._username)
        if not self.__credential_conditions():
            return LoginResponse(
                message=responses.BAD_CREDENTIALS,
                http_code=HttpCode.BAD_REQUEST
            )
        if self.__token_enable:
            return LoginResponse(
                message=responses.OK,
                token=self.__new_token()
            )
        else:
            return LoginResponse(
                message=responses.OK,
            )

    def __new_token(self) -> str:
        """Crea un token y lo registra en WhitelistToken

        Returns:
            str: token
        """
        token = token_generate(self._user)

        WhitelistToken(
            token=token,
            created_at=datetime.datetime.now()
        ).save()

        return token

    def __credential_conditions(self) -> tuple:
        """Condiciones para verificar credenciales.
        Usuario, contraseña y role

        Returns:
            (tuple)
        """
        return (
            self._user and
            self._user.role.name == self._role and
            password_match(self._request['password'], self._user.password)
        )

    def __request_is_valid(self) -> (bool, dict):
        """El request debe cumplir con la estructura,
        no debe tener key adicionales

        Returns:
            bool: Si es válido o no.
            dict: Diccionario con mensajes de errores.
                Solo si no es válido.
        """

        rules = {
            "username": {
                "type": "string",
                "required": True,
                "no_spaces": True
            },
            "password": {
                "type": "string",
                "required": True,
                "no_spaces": True
            }
        }
        v = Validator(rules)
        valid = v.validate(self._request, rules)
        if not valid:
            return False, v.errors
        return True, None


class Logout(UseCaseInterface):

    def handle(self, token: str) -> Response:
        """
        Args:
            token (str)

        Returns:
            response (utils.use_case.Response)
        """
        self.__token = token
        self.__delete_token()

        return Response(
            message=responses.OK
        )

    def __delete_token(self) -> None:
        """Borra el token de la WhitelistToken"""
        token = WhitelistTokenRepository.find_one(
            token=self.__token
        )
        if token:
            token.delete()


class SaveUserResponse(Response):
    """Respuesta para los casos de uso new y update user

    Attributes:
        user (security.models.User)
        http_code (int)
        message (str)
        errors (list)
    """
    def __init__(self, user: User = None, *args, **kwargs):
        self.user = user

        super(SaveUserResponse, self).__init__(*args, **kwargs)


class CreateUser(UseCaseInterface):
    """Crea usuario"""

    def handle(self, request: dict) -> SaveUserResponse:
        """
        Args:
            request (dict): Ejemplo: {
                'role': 'role_name',
                'username': 'username',
                'password': 'pass',
                'password_confirmed': 'pass',
                'identifier': '123' (Optional)
                }
        Returns:
            SaveUserResponse:
        """
        self.__username_min_length = config.USERNAME_MIN_LENGTH
        self.__password_min_length = config.PASSWORD_MIN_LENGTH
        self._request = request

        valid, response = self._validate()
        if not valid:
            return response

        try:
            self._create_user()
            response = SaveUserResponse(
                message=responses.CREATED,
                http_code=HttpCode.CREATED,
                user=self._user
            )
        except Exception:
            response = SaveUserResponse(
                message=responses.INTERNAL_SERVER_ERROR,
                http_code=HttpCode.INTERNAL_SERVER_ERROR
            )

        return response

    def _validate(self) -> (bool, SaveUserResponse):
        """Validaciones

        Returns:
            is_valid (bool)
            response (SaveUserResponse|None): Solo si no es valido
        """
        valid, errors = self.__request_is_valid()
        if not valid:
            return False, SaveUserResponse(
                message=responses.BAD_REQUEST,
                http_code=HttpCode.BAD_REQUEST,
                errors=errors
            )
        self._username = self._request['username'].lower()

        if (self._request.get('password') !=
                self._request.get('password_confirmed')):
            return False, SaveUserResponse(
                message="Passwords don't match",
                http_code=HttpCode.NOT_ACCEPTABLE
            )

        self._find_role()
        if not self._role:
            return False, SaveUserResponse(
                message="Role does not exist",
                http_code=HttpCode.NOT_ACCEPTABLE
            )
        self._find_user()
        if self._user:
            return False, SaveUserResponse(
                message="Username already exists",
                http_code=HttpCode.NOT_ACCEPTABLE
            )

        return True, None

    def _create_user(self):
        """ Crea User """
        self._user = User(
            username=self._username,
            password=password_hash(self._request['password']),
            role=self._role
        )

        self._user.save()

    def _find_role(self):
        """Busca role"""
        self._role = Role.objects(
            name=self._request['role']
        ).first()

    def _find_user(self):
        """ Busca user """
        self._user = User.objects(
            username=self._username
        ).first()

    def __request_is_valid(self) -> (bool, dict):
        """ El request debe cumplir con la estructura,
        no debe tener keys adicionales

        Returns:
            (bool, dict): Si es válido o no;
                diccionario con mensajes de errores
        """
        rules = {
            "role": {
                "type": "string",
                "required": True,
            },
            "username": {
                "type": "string",
                "minlength": int(self.__username_min_length),
                "required": True,
                "no_spaces": True
            },
            "password": {
                "type": "string",
                "minlength": int(self.__password_min_length),
                "required": True,
                "no_spaces": True
            },
            "password_confirmed": {
                "type": "string",
                "required": True,
                "no_spaces": True
            }
        }

        v = Validator(rules)
        valid = v.validate(self._request, rules)
        if not valid:
            return False, v.errors

        return True, None


class EditUser(UseCaseInterface):
    """Editar usuario"""

    def handle(self, uuid: str, request: dict) -> SaveUserResponse:
        """
        Args:
            uuid (str)
            request (dict):{
                'password': 'pass',
                'password_confirmed': 'pass'
                }

        Returns:
            SaveUserResponse:
        """
        self.__password_min_lenght = config.PASSWORD_MIN_LENGTH
        self._id = uuid
        self._request = request
        self._user = None

        valid, response = self._validate()
        if not valid:
            return response

        self._find_user()
        if not self._user:
            return SaveUserResponse(
                message=responses.NOT_FOUND,
                http_code=HttpCode.NOT_FOUND
            )

        try:
            self._edit()
            response = SaveUserResponse(
                message=responses.OK,
                http_code=HttpCode.OK,
                user=self._user
            )
        except Exception:
            response = SaveUserResponse(
                message=responses.INTERNAL_SERVER_ERROR,
                http_code=HttpCode.INTERNAL_SERVER_ERROR
            )

        return response

    def _edit(self) -> None:
        """Edita el usuario con los datos del request"""
        self._user.password = password_hash(self._request['password'])
        self._user.save()

    def _validate(self) -> (bool, SaveUserResponse):
        """Validaciones

        Returns:
            bool:
            SaveUserResponse: Solo si no es válido.
        """
        valid, errors = self.__request_is_valid()
        if not valid:
            return False, SaveUserResponse(
                message=str(errors),
                http_code=HttpCode.BAD_REQUEST
            )
        if (self._request.get('password') !=
                self._request.get('password_confirmed')):
            return False, SaveUserResponse(
                message="Passwords don't match",
                http_code=HttpCode.NOT_ACCEPTABLE
            )

        return True, None

    def __request_is_valid(self) -> (bool, dict):
        """ El request debe cumplir con la estructura,
        no debe tener keys adicionales

        Returns:
            bool: Si es válido
            dict: Diccionario con mensajes de errores

        """
        rules = {
            "password": {
                "type": "string",
                "minlength": int(self.__password_min_lenght),
                "required": True,
                "no_spaces": True
            },
            "password_confirmed": {
                "type": "string",
                "required": True
            }
        }
        v = Validator(rules)
        valid = v.validate(self._request, rules)
        if not valid:
            return False, v.errors
        return True, None

    def _find_user(self):
        self._user = User.objects(
            id=self._id
        ).first()


class DeleteUser(UseCaseInterface):
    """Elimina usuario"""

    def handle(self, uuid: str) -> Response:
        """
        Args:
            uuid (str)
        Returns:
            Response:
        """
        user = User.objects(id=uuid).first()
        if not user:
            return Response(
                message=responses.NOT_FOUND,
                http_code=HttpCode.NOT_FOUND
            )

        try:
            user.delete()
            response = Response(
                message=responses.OK,
                http_code=HttpCode.OK
            )
        except Exception:
            response = Response(
                message=responses.INTERNAL_SERVER_ERROR,
                http_code=HttpCode.INTERNAL_SERVER_ERROR
            )

        return response
