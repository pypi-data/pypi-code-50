import logging
import os

from django.utils.decorators import method_decorator
from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout as django_logout
# from django.http import HttpResponseRedirect

from rest_framework import status, serializers
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from allauth.account import views as allauth_account_views
from allauth.account.models import EmailAddress
from allauth.account.views import INTERNAL_RESET_URL_KEY, INTERNAL_RESET_SESSION_KEY
from allauth.account.forms import UserTokenForm
from allauth.utils import get_request_param

from ..apps.users.serializers import SuccessfullLoginResponseSerializer, SuccessfullLogoutResponseSerializer
from ..apps.passepartout.utils import get_passepartout_login_redirect_url
from ..permissions import is_staff, is_authenticated
from .. import app_settings
from .serializers import LoginSerializer, SignupSerializer, PasswordResetSerializer, PasswordResetFromKeySerializer
from ..utils import invalidate_cookie, set_cookie, set_session_key, get_session_key, is_test_user
from .utils import get_request_messages_string, get_error_response_data


sensitive_post_parameters_m = method_decorator(
    sensitive_post_parameters('password', 'password1', 'password2'))

logger = logging.getLogger('django_sso_app.core.api')

CURRENT_DIR = os.getcwd()
SUCCESS_STATUS_CODES = (status.HTTP_200_OK, status.HTTP_201_CREATED, status.HTTP_302_FOUND)


class FormWrapperViewMixin(GenericAPIView):
    http_method_names = ['get', 'post', 'head', 'options']

    _initial = {}

    def get_initial(self):
        """Return the initial data to use for forms on this view."""
        return self._initial.copy()

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(FormWrapperViewMixin, self).dispatch(request, *args, **kwargs)


# allauth views

class LoginView(FormWrapperViewMixin, allauth_account_views.LoginView):
    """
    Login
    """
    permission_classes = (AllowAny, )
    serializer_class = LoginSerializer
    http_method_names = ['post', 'head', 'options']
    response_data_errors = ['Login error.']

    def get_form_kwargs(self, **kwargs):
        kwargs = super(LoginView, self).get_form_kwargs(**kwargs)

        kwargs['data'] ={
            'login': self.request.data.get('login', None),
            'password': self.request.data.get('password', None),
            'fingerprint': self.request.data.get('fingerprint', None),
        }

        return kwargs

    def get_response(self):
        request = self.request
        data = {
            'user': request.user,
            'token': get_session_key(request, '__django_sso_app__jwt_token'),
            'redirect_url': get_passepartout_login_redirect_url(request),
        }
        serializer = SuccessfullLoginResponseSerializer(instance=data,
                                                        context={'request': self.request})

        response = Response(serializer.data, status=status.HTTP_200_OK)

        return response

    def form_valid(self, form):
        logger.debug('Valid login API form')
        return super(LoginView, self).form_valid(form)

    def form_invalid(self, form):
        errors = getattr(form, '__django_sso_app__login_errors', self.response_data_errors)
        logger.info('Invalid login API form "{}"'.format(errors))

        self.response_data_errors = errors

        return super(LoginView, self).form_invalid(form)

    def post(self, request, *args, **kwargs):
        logger.info('API logging in')
        if is_authenticated(request.user):
            return Response(status=status.HTTP_400_BAD_REQUEST)

        try:
            set_session_key(request, '__django_sso_app__device__fingerprint', request.data.get('fingerprint', None))

            _response = super(LoginView, self).post(request, *args, **kwargs)
            _status_code = _response.status_code

            logger.debug('allauth response ({})'.format(_response.__dict__))

            if _status_code not in SUCCESS_STATUS_CODES:
                logger.debug('allauth failed response')

        except:
            logger.exception('API Error logging in')
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        else:
            if is_authenticated(request.user):
                logger.debug('valid login')

                response = self.get_response()

                if not is_staff(request.user):
                    token = get_session_key(request, '__django_sso_app__jwt_token')
                    set_cookie(response, app_settings.JWT_COOKIE_NAME, token, None)

            else:
                logger.info('invalid login')

                try:
                    response_data = get_error_response_data(_response)

                except:
                    logger.exception('login error')
                    response_data = ', '.join(self.response_data_errors)

                response = Response(response_data, status.HTTP_400_BAD_REQUEST)

            return response


class LogoutView(FormWrapperViewMixin, allauth_account_views.LogoutView):
    """
    Logout
    """
    permission_classes = (IsAuthenticated, )
    serializer_class = serializers.Serializer

    def get_response(self):
        request = self.request
        redirect_url = get_request_param(request, 'next')
        data = {
            'redirect_url': redirect_url 
        }
        serializer = SuccessfullLogoutResponseSerializer(instance=data,
                                                         context={'request': self.request})

        # response = HttpResponseRedirect(redirect_url)
        response = Response(serializer.data, status=status.HTTP_200_OK)

        return response

    def get(self, request, *args, **kwargs):
        logger.info('API Getting logout')
        if request.user and request.user.is_anonymous:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        try:
            return super(LogoutView, self).get(request, *args, **kwargs)

        except:
            logger.exception('API Error getting logout')
            raise

    def post(self, request, *args, **kwargs):
        logger.info('API Logging out')
        if request.user and request.user.is_anonymous:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        try:
            _response = super(LogoutView, self).post(request, *args, **kwargs)
            status_code = _response.status_code
            if status_code not in SUCCESS_STATUS_CODES:
                logger.info('status_code error "{}"'.format(status_code))

        except:
            logger.exception('API Error logging out')
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        else:
            response = self.get_response()

            invalidate_cookie(response, app_settings.JWT_COOKIE_NAME)

            return response


class SignupView(FormWrapperViewMixin, allauth_account_views.SignupView):
    """
    Signup
    """
    permission_classes = (AllowAny, )
    serializer_class = SignupSerializer
    http_method_names = ['head', 'post', 'options']

    def get_form_kwargs(self, **kwargs):
        kwargs = super(SignupView, self).get_form_kwargs(**kwargs)

        data = {}
        for field in app_settings.REQUIRED_USER_FIELDS + ('password1', 'password2', 'fingerprint', 'referrer'):
            data[field] = self.request.data.get(field, None)

        if app_settings.BACKEND_SIGNUP_MUST_FILL_PROFILE:
            for f in app_settings.PROFILE_FIELDS:
                data[f] = self.request.data.get(f, None)

        kwargs['data'] = data

        return kwargs

    def form_valid(self, form):
        # By assigning the User to a property on the view, we allow subclasses
        # of SignupView to access the newly created User instance

        logger.debug('Valid signup API form')
        return super(SignupView, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        logger.info('API Signing up')
        if is_authenticated(request.user):
            return Response(status=status.HTTP_400_BAD_REQUEST)

        try:
            _response = super(SignupView, self).post(request, *args, **kwargs)
            _status_code = _response.status_code
            logger.debug('allauth response ({})'.format(_status_code))

        except:
            logger.exception('API Error signin up')
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        else:
            if _status_code not in SUCCESS_STATUS_CODES:
                response_data = get_error_response_data(_response)

                response = Response(response_data, status.HTTP_400_BAD_REQUEST)
            else:
                response = Response(status=status.HTTP_201_CREATED)

            if is_authenticated(request.user):
                logger.debug('disable API SignupView login')
                django_logout(request)

            return response


class EmailView(FormWrapperViewMixin, allauth_account_views.EmailView):
    """
    Manage user email addresses
    """
    permission_classes = (IsAuthenticated, )
    serializer_class = serializers.Serializer
    http_method_names = ['get', 'head', 'options']

    def get(self, request, *args, **kwargs):
        logger.info('API Getting email')
        try:
            _response = super(EmailView, self).get(request, *args, **kwargs)

        except:
            logger.exception('API Error getting email')
            raise

        else:
            email_addresses = EmailAddress.objects.filter(user=request.user).count()

            return Response(email_addresses, status=status.HTTP_200_OK)


class PasswordResetView(FormWrapperViewMixin, allauth_account_views.PasswordResetView):
    """
    Reset user password
    """
    permission_classes = (AllowAny, )
    serializer_class = PasswordResetSerializer
    http_method_names = ['head', 'post', 'options']

    def get_form_kwargs(self, **kwargs):
        kwargs = super(PasswordResetView, self).get_form_kwargs(**kwargs)
        kwargs['data'] = {
            'email': self.request.data.get('email', None)
        }

        return kwargs

    def post(self, request, *args, **kwargs):
        logger.info('API Asking for password reset')
        try:
            _response = super(PasswordResetView, self).post(request, *args, **kwargs)
        except:
            logger.exception('API Error while asking password reset')
            raise
        else:
            return _response


class PasswordResetFromKeyView(FormWrapperViewMixin, allauth_account_views.PasswordResetFromKeyView):
    """
    Confirm user password reset
    """
    permission_classes = (AllowAny, )
    serializer_class = PasswordResetFromKeySerializer
    http_method_names = ['head', 'post', 'options']

    __django_sso_app__is_api_view = True

    def get_form_kwargs(self, **kwargs):
        self.key = self.kwargs['key']
        uidb36 = self.kwargs['uidb36']

        token_form = UserTokenForm(
            data={'uidb36': uidb36, 'key': self.key})
        if token_form.is_valid():
            self.reset_user = token_form.reset_user
        else:
            logger.error('key is not valid!')
            raise KeyError('key is not valid')

        kwargs = super(PasswordResetFromKeyView, self).get_form_kwargs(**kwargs)

        kwargs['data'] = {
            'password1': self.request.data.get('password1', None),
            'password2': self.request.data.get('password2', None)
        }

        return kwargs

    def post(self, request, uidb36, key, **kwargs):
        logger.info('Resetting password form key')
        try:
            set_session_key(request, INTERNAL_RESET_SESSION_KEY, key)

            _response = super(PasswordResetFromKeyView, self).post(request, uidb36, INTERNAL_RESET_URL_KEY, **kwargs)
        except:
            logger.exception('Error while resetting password form key')
            raise
        else:
            return _response
