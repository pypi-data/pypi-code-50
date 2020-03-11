import logging

from django.contrib.auth import get_user_model

from allauth.account.adapter import get_adapter
from allauth.account.models import EmailAddress
from rest_framework import serializers

from ... import app_settings
from ...permissions import is_staff
from ...serializers import AbsoluteUrlSerializer
from ..profiles.serializers import ProfileSerializer

User = get_user_model()

logger = logging.getLogger('django_sso_app.core.apps.users')


class CheckUserExistenceSerializer(serializers.ModelSerializer):
    sso_id = serializers.SerializerMethodField(required=False)

    class Meta:
        model = User
        fields = ('sso_id',)
        read_only_fields = ('sso_id', )

    def get_sso_id(self, instance):
        return instance.sso_id


class UserRevisionSerializer(serializers.ModelSerializer):
    sso_id = serializers.SerializerMethodField(required=False)
    sso_rev = serializers.SerializerMethodField(required=False)

    class Meta:
        model = User
        read_only_fields = ('sso_id', 'sso_rev')
        fields = read_only_fields

    def get_sso_id(self, instance):
        return instance.sso_id

    def get_sso_rev(self, instance):
        return instance.sso_rev


class UserSerializer(AbsoluteUrlSerializer):
    sso_id = serializers.SerializerMethodField(required=False)
    sso_rev = serializers.SerializerMethodField(required=False)
    email_verified = serializers.SerializerMethodField(required=False)
    groups = serializers.SerializerMethodField(required=False)
    profile = ProfileSerializer(required=False, source='sso_app_profile')

    class Meta:
        model = User
        read_only_fields = (
            'url',
            'sso_id', 'sso_rev',
            'date_joined',
            'is_active', 'email_verified',
            'groups',
            'profile')
        fields = read_only_fields + app_settings.USER_FIELDS + ('password', )

    def get_sso_id(self, instance):
        return instance.sso_id

    def get_sso_rev(self, instance):
        return instance.sso_rev

    def get_email_verified(self, instance):
        if app_settings.BACKEND_ENABLED:
            try:
                email_address = instance.emailaddress_set.get(email=instance.email)
                return email_address.verified
            except:
                logger.info('{} has not verified email.'.format(instance))
                return False

        return True

    def get_groups(self, instance):
        groups = list(instance.groups.values_list('name', flat=True))

        return groups

    def to_representation(self, obj):
        # get the original representation
        ret = super(UserSerializer, self).to_representation(obj)
        request = self.context.get('request', None)

        if request is not None:
            # remove field if password if not asked
            with_pass = request.query_params.get('with_password',
                                                 not app_settings.BACKEND_HIDE_PASSWORD_FROM_USER_SERIALIZER)

            if not with_pass:
                ret.pop('password', None)
                ret['_partial'] = True

        # return the modified representation
        return ret

    def create(self, validated_data):
        request = self.context.get("request")
        requesting_user = request.user
        adapter = get_adapter(request)

        requesting_user_is_staff = is_staff(requesting_user)
        skip_confirmation = request.GET.get('skip_confirmation', None)
        must_confirm_email = True
        password_is_hashed = request.query_params.get('password_is_hashed', None)

        new_email = validated_data.get('email', None)

        if password_is_hashed:
            new_password = validated_data.pop('password', None)
        else:
            new_password = validated_data.get('password', None)
            self.validated_data.update(password1=new_password)
            self.validated_data.update(password2=new_password)

        assert (new_email is not None and new_password is not None)

        logger.info(
            'User "{}" wants to create new user "{}"'.format(requesting_user, validated_data))

        if requesting_user_is_staff and skip_confirmation is not None:
            must_confirm_email = False

        new_user = adapter.save_user(request, User(), self, True)

        created_email = EmailAddress.objects.add_email(request, new_user,
                                                       new_email,
                                                       confirm=must_confirm_email)

        logger.info(
            'A new EmailAddress for {0} has been created with id {1}'
            ''.format(
                new_email, created_email.id))

        if must_confirm_email:
            logger.info(
                '{0} must confirm email {1}'.format(new_user, new_email))
        else:
            logger.info(
                '{0} must NOT confirm email {1}'.format(new_user, new_email))
            adapter.confirm_email(request, created_email)

        if password_is_hashed:
            new_user.password = new_password

        new_user.save()

        return new_user

    def update(self, instance, validated_data):
        user = instance
        request = self.context.get("request")
        requesting_user = request.user
        adapter = get_adapter(request=request)

        requesting_user_is_staff = is_staff(requesting_user)
        skip_confirmation = request.GET.get('skip_confirmation', None)
        must_confirm_email = True
        if requesting_user_is_staff and skip_confirmation is not None:
            must_confirm_email = False
        password_is_hashed = request.query_params.get('password_is_hashed', None)

        new_email = validated_data.get('email', None)
        new_password = validated_data.get('password', None)

        logger.info(
            'User {0} wants to update user {1}: {2}'.format(requesting_user, user, validated_data))

        if (new_email is not None):

            if new_email == user.email:  # !! because of app shitty logic (
                # always sends all fields)
                logger.info('{0} is has same email'.format(user))

            else:
                logger.info(
                    '{0} is changing email for user {1}, email confirmation '
                    'is {2}'.format(
                        requesting_user, user, must_confirm_email))

                created_email = EmailAddress.objects.add_email(request, user,
                                                               new_email,
                                                               confirm=must_confirm_email)
                logger.info(
                    'A new EmailAddress for {0} has been created with id {1}'
                    ''.format(
                        new_email, created_email.id))

                if must_confirm_email:
                    if requesting_user_is_staff:
                        logger.info(
                            'Unconfirming all emails for {0} while email has been updated by staff user {1}'.format(
                                user,
                                requesting_user))

                        adapter.unconfirm_all_user_emails(user)

                    logger.info(
                        '{0} must confirm email {1}'.format(user, new_email))
                else:
                    adapter.confirm_email(None, created_email)

                setattr(user, '__django_sso_app__email_updated', True)

        if (new_password is not None):
            logger.info(
                '{} is changing password for user {}'.format(requesting_user,
                                                             user))

            if password_is_hashed:
                logger.info('password is hashed')
                user.password = new_password
            else:
                logger.info('password is plain')
                user.set_password(new_password)

            setattr(user, '__django_sso_app__password_updated', True)

        user.save()

        return user

    def get_cleaned_data(self):
        return self.validated_data

    @property
    def cleaned_data(self):
        return self.validated_data


class SuccessfullLoginResponseSerializer(serializers.Serializer):
    """
    Login success response serializer
    """
    token = serializers.CharField()
    user = UserSerializer()
    redirect_url = serializers.CharField(required=False)


class SuccessfullLogoutResponseSerializer(serializers.Serializer):
    """
    Logout success response serializer
    """
    redirect_url = serializers.CharField(required=False)
