from ...constants import responses
from ...constants.enums import HttpCode
from flask_auth_service_mongo.utils.use_case import Response, UseCaseInterface
from flask_auth_service_mongo.utils.validator import Validator
from ..models import Role


class SaveRoleResponse(Response):
    """Respuesta para los casos de uso new y update role

    Attributes:
        role (security.models.Role)
        http_code (int)
        message (str)
        errors (list)
    """
    def __init__(self, role: Role = None, *args, **kwargs):
        self.role = role

        super(SaveRoleResponse, self).__init__(*args, **kwargs)


class NewRole(UseCaseInterface):
    """Caso de uso: Crear un Role"""

    def handle(self, request: dict) -> SaveRoleResponse:
        """
        Args:
            request (dict): {'name': 'roleName', 'permissions': {'a':'b'}}

        Returns:
            (SaveRoleResponse)
        """
        self._request = request

        valid, errors = self.__request_is_valid()
        if not valid:
            return SaveRoleResponse(
                message=responses.BAD_REQUEST,
                http_code=HttpCode.BAD_REQUEST,
                errors=str(errors)
            )
        if self._find_role():
            return SaveRoleResponse(
                message=responses.EXISTING_RESOURCE,
                http_code=HttpCode.BAD_REQUEST
            )

        role = self._create_role()
        return SaveRoleResponse(
            message=responses.CREATED,
            http_code=HttpCode.CREATED,
            role=role
        )

    def _create_role(self) -> Role:
        """Crea un Role con los datos del self._request

        Returns:
            (role.models.Role)
        """
        role = Role(**self._request)
        role.save()

        return role

    def _find_role(self) -> Role:
        """Busca un role con el mismo nombre

        Returns:
            (security.models.Role|None)
        """
        return Role.objects(
            name=self._request['name']
        ).first()

    def __request_is_valid(self) -> (bool, dict):
        """ El request debe cumplir con la estructura,
        no debe tener keys adicionales

        Returns:
            bool: Si es válido o no.
            dict: Diccionario con mensajes de errores
        """
        rules = {
            'name': {
                'type': 'string',
                'required': True
            },
            'permissions': {
                'type': 'dict'
            }
        }

        v = Validator(rules)
        valid = v.validate(self._request, rules)
        if not valid:
            return False, v.errors
        return True, None
