from requests import HTTPError
from rest_framework.exceptions import NotAuthenticated
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from social_core.exceptions import SocialAuthBaseException

from drf_social.models import AuthProvider
from drf_social.utils import do_login
from drf_social.serializers import SocialInputSerializer, JWTResponseSerializer


class SocialLoginView(GenericAPIView):
    permission_classes = []
    authentication_classes = []
    serializer_class = SocialInputSerializer
    response_serializer = JWTResponseSerializer

    def post(self, *args, **kwargs):
        token_serializer = self.get_serializer_class()(data=self.request.data)
        token_serializer.is_valid(raise_exception=True)
        try:
            AuthProvider.objects.get(client_id=token_serializer.validated_data['client_id'],
                                     provider=token_serializer.validated_data["provider"])
        except AuthProvider.DoesNotExist:
            return Response(status=404, data={
                "details": "client_id is wrong"
            })
        try:
            user = do_login(self.request, token_serializer.validated_data)
        except (SocialAuthBaseException, HTTPError) as e:
            raise NotAuthenticated(e)
        if user is None:
            raise NotAuthenticated("Invalid Social Token")

        serializer_class = self.response_serializer
        if not hasattr(serializer_class,  "get_token"):
            raise TypeError("serializer class must implement get_token method")

        token = serializer_class.get_token(user)
        token_response = {
            "refresh": str(token),
            "access": str(token.access_token)
        }
        response_serializer = serializer_class(data=token_response)
        response_serializer.is_valid(raise_exception=True)
        return Response(response_serializer.validated_data)
