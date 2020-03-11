import logging
import os

# from django.conf import settings
from django.shortcuts import redirect, reverse
from django.http import HttpResponse
from django.template import loader
from django import forms
from django.contrib.auth import logout as django_logout

from rest_framework import status

from allauth.account import views as allauth_account_views
from allauth.socialaccount import views as allauth_socialaccount_views

from .permissions import is_staff, is_authenticated
from .utils import set_cookie, invalidate_cookie, set_session_key, get_session_key
from .mixins import WebpackBuiltTemplateViewMixin
from . import app_settings

logger = logging.getLogger('django_sso_app.core')

CURRENT_DIR = os.getcwd()


# allauth views

class LoginView(allauth_account_views.LoginView, WebpackBuiltTemplateViewMixin):

    def get(self, request, *args, **kwargs):
        logger.info('Getting login')

        if is_authenticated(request.user):
            return redirect(reverse('profile'))

        try:
            return super(LoginView, self).get(request, *args, **kwargs)

        except:
            logger.exception('Error getting login')
            raise

    def post(self, request, *args, **kwargs):
        logger.info('Logging in')

        if is_authenticated(request.user):
            return redirect(reverse('profile'))

        try:
            set_session_key(request, '__django_sso_app__device__fingerprint', request.POST.get('fingerprint', None))

            response = super(LoginView, self).post(request, *args, **kwargs)

        except:
            logger.exception('Error logging in')
            raise

        else:
            if is_authenticated(request.user):
                if not is_staff(request.user):
                    token = get_session_key(request, '__django_sso_app__jwt_token')
                    set_cookie(response, app_settings.JWT_COOKIE_NAME, token, None)

            return response


class LogoutView(allauth_account_views.LogoutView, WebpackBuiltTemplateViewMixin):
    def get(self, request, *args, **kwargs):
        logger.info('Getting logout')

        if request.user and request.user.is_anonymous:
            return redirect(reverse('account_login'))

        try:
            return super(LogoutView, self).get(request, *args, **kwargs)

        except:
            logger.exception('Error getting logout')
            raise

    def post(self, request, *args, **kwargs):
        logger.info('Logging out')

        if request.user and request.user.is_anonymous:
            return redirect(reverse('account_login'))

        try:
            response = super(LogoutView, self).post(request, *args, **kwargs)

        except Exception as e:
            logger.exception('Error logging out')
            raise
        else:
            invalidate_cookie(response, app_settings.JWT_COOKIE_NAME)

            return response


class SignupView(allauth_account_views.SignupView, WebpackBuiltTemplateViewMixin):
    def get(self, request,  *args, **kwargs):
        logger.info('Getting signup')

        if is_authenticated(request.user):
            return redirect(reverse('account_login'))

        try:
            return super(SignupView, self).get(request, *args, **kwargs)

        except:
            logger.exception('Error getting signup')
            raise

    def post(self, request, *args, **kwargs):
        logger.info('Signing up')

        if is_authenticated(request.user):
            return redirect(reverse('account_login'))

        try:
            response = super(SignupView, self).post(request, *args, **kwargs)

        except forms.ValidationError as e:
            logger.info('Signup ValidationError: {}'.format(e))
            return self.form_invalid(self.get_form())

        except:
            logger.exception('Error signin up')
            raise

        else:
            if is_authenticated(request.user):
                logger.debug('disable SignupView login')
                django_logout(request)

        return response


class ConfirmEmailView(allauth_account_views.ConfirmEmailView):
    def get(self, request, *args, **kwargs):
        logger.info('Getting confirm email')

        try:
            return super(ConfirmEmailView, self).get(request, *args, **kwargs)

        except:
            logger.exception('Error get confirm email')
            raise

    def post(self, request, *args, **kwargs):
        logger.info('Confirming email')

        try:
            return super(ConfirmEmailView, self).post(request, *args, **kwargs)

        except:
            logger.exception('Error confirming email')
            raise


class EmailView(allauth_account_views.EmailView):
    def get(self, *args, **kwargs):
        logger.info('Getting email')

        try:
            return super(EmailView, self).get(*args, **kwargs)

        except:
            logger.exception('Error getting email')
            raise

    def post(self, *args, **kwargs):
        logger.info('Email')

        try:
            return super(EmailView, self).post(*args, **kwargs)

        except:
            logger.exception('Error email')
            raise


class PasswordChangeView(allauth_account_views.PasswordChangeView):
    def get(self, *args, **kwargs):
        logger.info('Getting password change')

        try:
            return super(PasswordChangeView, self).get(*args, **kwargs)

        except:
            logger.exception('Error getting password change')
            raise

    def post(self, *args, **kwargs):
        logger.info('Changing password')

        try:
            return super(PasswordChangeView, self).post(*args, **kwargs)

        except:
            logger.exception('Error changing password')
            raise


class PasswordSetView(allauth_account_views.PasswordSetView):
    def get(self, *args, **kwargs):
        logger.info('Getting password set')

        try:
            return super(PasswordSetView, self).get(*args, **kwargs)

        except:
            logger.exception('Error getting password set')
            raise

    def post(self, *args, **kwargs):
        logger.info('Setting password')

        try:
            return super(PasswordSetView, self).post(*args, **kwargs)

        except:
            logger.exception('Error setting password')
            raise


class PasswordResetView(allauth_account_views.PasswordResetView, WebpackBuiltTemplateViewMixin):
    def get(self, *args, **kwargs):
        logger.info('Getting ask password reset')

        try:
            return super(PasswordResetView, self).get(*args, **kwargs)

        except:
            logger.exception('Error getting ask password reset')
            raise

    def post(self, *args, **kwargs):
        logger.info('Asking for password reset')

        try:
            return super(PasswordResetView, self).post(*args, **kwargs)

        except:
            logger.exception('Error while asking password reset')
            raise


class PasswordResetDoneView(allauth_account_views.PasswordResetDoneView):
    def get(self, request, *args, **kwargs):
        logger.info('Getting password reset done')

        try:
           return super(PasswordResetDoneView, self).get(request, *args, **kwargs)

        except:
            logger.exception('Error getting password reset done')
            raise


class PasswordResetFromKeyView(allauth_account_views.PasswordResetFromKeyView, WebpackBuiltTemplateViewMixin):

    def dispatch(self, request, uidb36, key, **kwargs):
        _response = super(PasswordResetFromKeyView, self).dispatch(request, uidb36, key, **kwargs)
        _status_code = _response.status_code

        if app_settings.BACKEND_FRONTEND_APP_RESTONLY and _status_code == status.HTTP_302_FOUND:
            template_name = self.get_template_names()[0]
            logger.debug('Frontend is rest only, returning template "{}"'.format(template_name))
            template = loader.get_template(template_name)
            context = {}

            return HttpResponse(template.render(context, request))

        return _response

    def get(self, request, uidb36, key, **kwargs):
        logger.info('Getting password reset from key')

        try:
            return super(PasswordResetFromKeyView, self).get(request, uidb36, key, **kwargs)

        except:
            logger.exception('Error while getting password reset from key')
            raise

    def post(self, request, uidb36, key, **kwargs):
        logger.info('Resetting password form key')

        try:
            return super(PasswordResetFromKeyView, self).post(request, uidb36, key, **kwargs)

        except:
            logger.exception('Error while resetting password form key')
            raise


class PasswordResetFromKeyDoneView(allauth_account_views.PasswordResetFromKeyDoneView):
    def get(self, *args, **kwargs):
        logger.info('Getting password reset from key done')
        try:
            return super(PasswordResetFromKeyDoneView, self).get(*args,
                                                                 **kwargs)
        except:
            logger.exception('Error while getting password reset from key done')
            raise


class AccountInactiveView(allauth_account_views.AccountInactiveView):
    def get(self, *args, **kwargs):
        logger.info('Getting account inactive')

        try:
            return super(AccountInactiveView, self).get(*args, **kwargs)

        except:
            logger.exception('Error while getting account inactive')
            raise


class EmailVerificationSentView(allauth_account_views.EmailVerificationSentView, WebpackBuiltTemplateViewMixin):
    def get(self, *args, **kwargs):
        logger.info('Getting email verification sent')

        try:
            return super(EmailVerificationSentView, self).get(*args, **kwargs)

        except:
            logger.exception('Error getting verification sent')
            raise


# allauth socialaccount views
class SocialSignupView(allauth_socialaccount_views.SignupView):
    pass


class SocialLoginCancelledView(allauth_socialaccount_views.LoginCancelledView):
    pass


class SocialLoginErrorView(allauth_socialaccount_views.LoginErrorView):
    pass


class SocialConnectionsView(allauth_socialaccount_views.ConnectionsView):
    pass
