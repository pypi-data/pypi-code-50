from rest_framework import serializers
from drf_social import models

try:
    from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
except ImportError:
    raise ImportError("must install rest_framework_simplejwt first")

class SocialInputSerializer(serializers.Serializer):
    access_token = serializers.CharField(max_length=500, required=True, allow_blank=False, allow_null=False)
    provider = serializers.ChoiceField(choices=[(p, p)for p in models.Providers], allow_null=False, allow_blank=False, required=True)
    client_id = serializers.CharField(max_length=100,allow_null=False, allow_blank=False, required=True)

class JWTResponseSerializer(serializers.Serializer):
    access = serializers.CharField(max_length=500)
    refresh = serializers.CharField(max_length=500)

    @classmethod
    def get_token(cls, user):
        return TokenObtainPairSerializer.get_token(user)