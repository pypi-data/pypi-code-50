import logging
# import inspect
# import warnings

from django.db import transaction
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import activate as activate_translation
from django.core.cache import cache
from django.contrib.auth import (authenticate,
                                 get_backends,
                                 login as django_login)
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from allauth.account.adapter import DefaultAccountAdapter
from allauth.account.models import EmailAddress
from allauth.account import app_settings as allauth_app_settings

from .utils import set_session_key, check_user_can_login
from .apps.devices.models import Device
from .apps.devices.utils import get_request_device
from .apps.services.models import Service, Subscription
from .apps.profiles.utils import get_or_create_user_profile, update_profile
from .apps.profiles.models import Profile
from .apps.passepartout.utils import get_passepartout_login_redirect_url
from .tokens.utils import get_request_jwt_fingerprint
from .permissions import is_authenticated, is_staff
from . import app_settings

logger = logging.getLogger('django_sso_app.core')


class AccountAdapter(DefaultAccountAdapter):
    def __init__(self, request=None):
        super(AccountAdapter, self).__init__(request)

        self.error_messages = DefaultAccountAdapter.error_messages
        self.error_messages['email_not_verified'] = _('We have sent an e-mail to you for verification. Follow the link provided to finalize the signup process. Please contact us if you do not receive it within a few minutes.')

    def is_open_for_signup(self, request):
        """
        Checks whether or not the site is open for signups.

        Next to simply returning True/False you can also intervene the
        regular flow by raising an ImmediateHttpResponse
        """
        return True

    def is_ajax(self, request):
        return super(AccountAdapter, self).is_ajax(request) or \
               request.META.get('CONTENT_TYPE', None) == 'application/json'

    def get_login_redirect_url(self, request):
        """
        Returns the default URL to redirect to after logging in.  Note
        that URLs passed explicitly (e.g. by passing along a `next`
        GET parameter) take precedence over the value returned here.
        """

        if request.path.startswith(reverse('account_signup')) or request.path.startswith(reverse('rest_signup')):
            logger.info('do not get redirect_url from signup')
            redirect_url = None
        else:
            redirect_url = get_passepartout_login_redirect_url(request)

            if redirect_url is None:
                redirect_url = super(AccountAdapter, self).get_login_redirect_url(request)

        return redirect_url

    def login(self, request, user):
        # HACK: This is not nice. The proper Django way is to use an
        # authentication backend
        logger.debug('adapter login')

        check_user_can_login(user)

        if not hasattr(user, 'backend'):
            from .backends import DjangoSsoAppLoginAuthenticationBackend
            backends = get_backends()
            backend = None
            for b in backends:
                if isinstance(b, DjangoSsoAppLoginAuthenticationBackend):
                    # prefer our own backend
                    backend = b
                    break
                elif not backend and hasattr(b, 'get_user'):
                    # Pick the first vald one
                    backend = b
            backend_path = '.'.join([backend.__module__,
                                     backend.__class__.__name__])
            user.backend = backend_path

        if request.path.startswith(reverse('account_signup')) or request.path.startswith(reverse('rest_signup')):
            logger.debug('do not login from signup')

        else:
            logger.debug('django loggin in')
            django_login(request, user)

            if is_authenticated(user) and not is_staff(user):
                setattr(request, 'user', user)
                set_session_key(request, '__django_sso_app__user_logged_in', True)


    def logout(self, request):
        logger.debug('adapter logout, user logged out, setting flags')
        # print(inspect.stack()[1].function)
        try:
            device = get_request_device(request)

        except Exception as e:
            logger.debug('no device on request because of "{}"'.format(e))

        else:
            logger.info('Deleting device "{}"'.format(device))
            device.delete()

        # allauth logout
        super(AccountAdapter, self).logout(request)

        if not is_authenticated(request.user):
            set_session_key(request, '__django_sso_app__user_logged_out', True)

    def authenticate(self, request, **credentials):
        logger.debug('adapter authenticate')
        #exceptions print(inspect.stack()[1].function)

        """Only authenticates, does not actually login. See `login`"""
        from .backends import DjangoSsoAppLoginAuthenticationBackend

        self.pre_authenticate(request, **credentials)
        DjangoSsoAppLoginAuthenticationBackend.unstash_authenticated_user()
        user = authenticate(request, **credentials)
        alt_user = DjangoSsoAppLoginAuthenticationBackend.unstash_authenticated_user()
        user = user or alt_user
        if user and allauth_app_settings.LOGIN_ATTEMPTS_LIMIT:
            cache_key = self._get_login_attempts_cache_key(
                request, **credentials)
            cache.delete(cache_key)
        else:
            self.authentication_failed(request, **credentials)

        if is_authenticated(user):
            logger.info('adapter authenticated "{}"'.format(user))
            _profile = get_or_create_user_profile(user, Profile)

        return user

    def update_user_profile(self, user, cleaned_data, commit=True):
        logger.debug('adapter update user profile')
        profile = update_profile(user.sso_app_profile, cleaned_data, commit)

        return profile

    @transaction.atomic
    def save_user(self, request, user, form, commit=True):
        """
        Saves a new User instance using information provided in the
        signup form.
        """
        # !atomic
        cleaned_data = form.cleaned_data
        email = cleaned_data.get('email', None)
        username = cleaned_data.get('username', None)
        logger.info(
            'Saving new user {0} with email {1} from form {2} with cleaned_data {3}'.format(
                username, email, form.__class__, cleaned_data))

        new_user = super(AccountAdapter, self).save_user(request, user, form, commit)

        self.update_user_profile(new_user, cleaned_data, commit)

        return new_user

    def render_mail(self, template_prefix, email, context):
        user = context.get('user')
        logger.info('render mail for "{}"'.format(user))
        user_language = user.sso_app_profile.language

        activate_translation(user_language)
        context.update({
            'EMAILS_DOMAIN': settings.EMAILS_DOMAIN,
            'EMAILS_SITE_NAME': settings.EMAILS_SITE_NAME
        })

        return super(AccountAdapter, self).render_mail(template_prefix, email, context)

    def get_email_confirmation_url(self, request, emailconfirmation):
        """Constructs the email confirmation (activation) url.
        Note that if you have architected your system such that email
        confirmations are sent outside of the request context request
        can be None here.
        """
        _url = reverse(
            "account_confirm_email",
            args=[emailconfirmation.key])

        email_confirmation_url = '{}://{}{}'.format(app_settings.HTTP_PROTOCOL,
                                                    settings.EMAILS_DOMAIN,
                                                    _url)

        return email_confirmation_url

    # pai

    def unconfirm_all_user_emails(self, user):
        return EmailAddress.objects.filter(user=user,
                                           verified=True).update(verified=False)

    def add_user_profile_device(self, user, fingerprint, user_agent=None):
        profile = user.sso_app_profile
        logger.info(
            'Adding User Device for profile "{}" with fingerprint "{}"'.format(profile,
                                                                               fingerprint))

        device = Device.objects.create(profile=profile, fingerprint=fingerprint)
        logger.debug('device "{}" created with key "{}" and fingerprint "{}"'.format(device,
                                                                                     device.apigw_jwt_key,
                                                                                     device.fingerprint))

        return device

    def remove_user_profile_device(self, device):
        logger.info('Removing Device {0}'.format(device.id))

        device.delete()

        return 1

    def remove_all_user_profile_devices(self, user):
        logger.info('Removing All Profile Devices for "{}"'.format(user))

        removed = 0
        for device in user.sso_app_profile.devices.all():
            removed += self.remove_user_profile_device(device)

        return removed

    def subscribe_user_profile_to_service(self, user, referrer, update_rev=False, commit=True):
        profile = user.sso_app_profile
        logger.info('Subscribinig "{}" to service "{}"'.format(profile, referrer))

        service = Service.objects.get(service_url=referrer)

        subscription, _subscription_created = \
            Subscription.objects.get_or_create(
                profile=profile, service=service)

        if _subscription_created:
            logger.info('Created service subscrption for "{}"'.format(profile))

            setattr(profile.user, '__django_sso_app__subscription_updated', True)

            if update_rev:
                profile.update_rev(commit)
        else:
            logger.info(
                'Profile "{}" can not subscribe "{}"'.format(profile, service))

        return _subscription_created

    def unsubscribe_user_profile_from_service(self, user, subscription, update_rev=False,
                                              commit=True):
        logger.info('Unubscribinig "{}" form service "{}"'.format(user.sso_app_profile,
                                                                  subscription.service))

        subscription.unsubscribed_at = timezone.now()
        subscription.save()

        if update_rev and commit:
            user.sso_app_profile.save()

        return True

    def get_request_profile_device(self, request):
        received_jwt = get_request_jwt_fingerprint(request)

        return Device.objects.filter(fingerprint=received_jwt).first()

    def delete_request_profile_device(self, request):
        profile = request.user.sso_app_profile
        logger.info('Deleting request profile device for "{}"'.format(profile))

        removing_device = self.get_request_profile_device(request)

        if removing_device is not None:
            logger.info('Removing logged out user profile device "{}" for "{}"'.format(removing_device, profile))
            self.remove_user_profile_device(removing_device)
        else:
            logger.warning('Can not find request device for profile "{}"'.format(profile))

    def completely_unsubscribe(self, user):
        profile = user.sso_app_profile
        logger.info('Completely unsubscribing Profile "{}"'.format(profile))

        profile.unsubscribed_at = timezone.now()
        profile.is_active = False
        user.is_active = False

        user.save()  # Profile update managed by user signal

        return True
