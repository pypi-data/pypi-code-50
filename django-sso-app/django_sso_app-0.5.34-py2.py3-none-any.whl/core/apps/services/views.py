import logging

from allauth.account.adapter import get_adapter
from django.contrib.auth import get_user_model
from django.http import Http404
from rest_framework import mixins
from rest_framework import permissions
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Service, Subscription
from .serializers import SubscriptionSerializer, ServiceSerializer
from ...permissions import is_staff, is_authenticated
from ...tokens.utils import get_request_jwt, renew_response_jwt

logger = logging.getLogger('services')
User = get_user_model()


class ServiceApiViewSet(mixins.ListModelMixin,
                        mixins.RetrieveModelMixin,
                        viewsets.GenericViewSet):
    """
    Service API viewset
    """

    serializer_class = ServiceSerializer
    permission_classes = (permissions.AllowAny, )

    def get_queryset(self):
        return Service.objects.filter(is_public=True)

    def subscribe(self, request, pk, *args, **kwargs):
        logger.info('subscribing')

        requesting_user = request.user

        if not is_authenticated(requesting_user):
            return Response(status=status.HTTP_400_BAD_REQUEST)

        profile = requesting_user.sso_app_profile
        service = Service.objects.get(id=pk)
        adapter = get_adapter(request)

        if service is None:
            raise Http404

        if requesting_user.sso_app_profile.subscriptions.filter(service=service).count() > 0:
            return Response('Already subscribed.', status=status.HTTP_409_CONFLICT)

        subscription_created = adapter.subscribe_user_profile_to_service(requesting_user, service.service_url, update_rev=True)

        if subscription_created:
            response = Response('Successfully subscribed.', status=status.HTTP_201_CREATED)
        else:
            return Response('Subscription subscribe error.', status=status.HTTP_500_INTERNAL_SERVER_ERROR)


        received_jwt = get_request_jwt(request)
        from_browser_as_same_user = received_jwt is not None

        if from_browser_as_same_user:  # From browser as same user
            logger.info(
                'From browser as same user "{}"'.format(requesting_user))
            logger.info('updating JWT for {}'.format(requesting_user))

            renew_response_jwt(received_jwt, requesting_user, request, response)

        return response

    def unsubscribe(self, request, pk, *args, **kwargs):
        logger.info('unsubscribing')

        requesting_user = request.user

        if not is_authenticated(requesting_user):
            return Response(status=status.HTTP_400_BAD_REQUEST)

        profile = requesting_user.sso_app_profile
        service = Service.objects.get(id=pk)

        logger.info('"{}" unsubscribing from "{}"'.format(profile, service))

        if service is None:
            raise Http404

        subscriptions = profile.subscriptions.filter(service=service)

        if subscriptions.count() == 0:
            return Response('Not subscribed.', status=status.HTTP_400_BAD_REQUEST)

        else:
            subscription = subscriptions.first()
            adapter = get_adapter(request)

            subscription_disabled = adapter.unsubscribe_user_profile_from_service(requesting_user, subscription, update_rev=True)

            if subscription_disabled:
                response = Response('Successfully unsubscribed.', status=status.HTTP_200_OK)
            else:
                return Response('Subscription unsubscribe error.', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            received_jwt = get_request_jwt(request)
            from_browser_as_same_user = received_jwt is not None

            if from_browser_as_same_user:  # From browser as same user
                logger.info(
                    'From browser as same user "{}"'.format(requesting_user))
                logger.info('updating JWT for {}'.format(requesting_user))

                renew_response_jwt(received_jwt, requesting_user, request, response)

            return response


class SubscriptionApiViewSet(mixins.ListModelMixin,
                             mixins.RetrieveModelMixin,
                             viewsets.GenericViewSet):
    """
    Subscription API viewset
    """

    serializer_class = SubscriptionSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        requesting_user = self.request.user
        if is_authenticated(requesting_user):
            if is_staff(requesting_user):
                return Subscription.objects.all()
            else:
                return Subscription.objects.filter(profile=requesting_user.sso_app_profile)
        else:
            return Subscription.objects.none()
