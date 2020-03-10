import json
import django.conf as conf
from django.contrib.auth import get_user_model
from social_django.utils import load_strategy, load_backend
import social_django.utils as utils

from drf_social.models import AuthProvider, Providers

UserModel = get_user_model()


def extract_scopes(scopes):
    try:
        scopes = json.loads(scopes)
        return scopes
    except json.JSONDecodeError:
        raise ValueError("Invalid extras were provided, must be json encoded")


AUTH_MAPPING = {
    Providers.Google: {
        "value": "GOOGLE_OAUTH2",
        "backend": 'social_core.backends.google.GoogleOAuth2',
        "name": "google-oauth2"
    },
    Providers.Facebook: {
        "value": "FACEBOOK",
        "backend": 'social_core.backends.facebook.FacebookOAuth2',
        "name": "facebook"
    },
    Providers.Instagram:
        {
            "value": "INSTAGRAM",
            "backend": "social_core.backends.instagram.InstagramOAuth2",
            "name": "instagram"
        }
}


def load_providers():
    all_auth = AuthProvider.objects.all()
    for auth in all_auth:
        value = str(AUTH_MAPPING[auth.provider]['value']).upper()
        setattr(conf.settings, f"SOCIAL_AUTH_{value}_KEY", auth.client_id)
        setattr(conf.settings, f"SOCIAL_AUTH_{value}_SECRET", auth.client_secret)
        setattr(conf.settings, f"SOCIAL_AUTH_{value}_SCOPE", extract_scopes(auth.scopes))
        backends = [*conf.settings.AUTHENTICATION_BACKENDS, AUTH_MAPPING[auth.provider]['backend']]
        setattr(conf.settings, "AUTHENTICATION_BACKENDS", backends)
        setattr(utils, "BACKENDS", backends)


def do_login(request, payload):
    strategy = load_strategy(request)
    backend = load_backend(strategy, AUTH_MAPPING[payload["provider"]]['name'], '/')
    user = backend.do_auth(payload['access_token'])
    return user

