from django.contrib.auth import get_user_model, login
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.backends import ModelBackend
import logging
from django.conf import settings as django_settings
from django.utils.six import text_type
from django.contrib.auth import get_user_model
from django.utils.encoding import smart_text

from .settings import auth_settings
from .utils.jwt_auth import jwt_decode_handler
logger = logging.getLogger(__name__)

User = get_user_model()


class OpAuthJwtBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):

        auth = request.META.get('HTTP_AUTHORIZATION', b'')
        if isinstance(auth, text_type):
            auth = auth.encode(auth_settings.HTTP_HEADER_ENCODING)
        if not auth:
            return None
        auth = auth.split()
        if len(auth) != 2 and smart_text(auth[0].lower()) != auth_settings.JWT_AUTH_HEADER_PREFIX:
            return None

        playload: dict = jwt_decode_handler(auth[1])
        username = playload.get(auth_settings.USERNAME_FIELD, None)
        if not username:
            return None

        user = User.objects.filter(username=username).first()
        if not user.is_authenticated:
            return None
        return user