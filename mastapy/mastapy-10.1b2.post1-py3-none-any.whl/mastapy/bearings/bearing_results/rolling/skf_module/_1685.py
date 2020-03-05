'''_1685.py

SKFCredentials
'''


from typing import Callable

from mastapy._internal import constructor
from mastapy import _1
from mastapy._internal.python_net import python_net_import

_SKF_CREDENTIALS = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling.SkfModule', 'SKFCredentials')


__docformat__ = 'restructuredtext en'
__all__ = ('SKFCredentials',)


class SKFCredentials(_1.APIBase):
    '''SKFCredentials

    This is a mastapy class.
    '''

    TYPE = _SKF_CREDENTIALS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SKFCredentials.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def email_address(self) -> 'str':
        '''str: 'EmailAddress' is the original name of this property.'''

        return self.wrapped.EmailAddress

    @email_address.setter
    def email_address(self, value: 'str'):
        self.wrapped.EmailAddress = str(value) if value else None

    @property
    def password(self) -> 'str':
        '''str: 'Password' is the original name of this property.'''

        return self.wrapped.Password

    @password.setter
    def password(self, value: 'str'):
        self.wrapped.Password = str(value) if value else None

    @property
    def create_skf_account(self) -> 'Callable[[], None]':
        '''Callable[[], None]: 'CreateSKFAccount' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.CreateSKFAccount

    @property
    def skf_terms_of_use(self) -> 'Callable[[], None]':
        '''Callable[[], None]: 'SKFTermsOfUse' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.SKFTermsOfUse

    @property
    def skf_privacy_notice(self) -> 'Callable[[], None]':
        '''Callable[[], None]: 'SKFPrivacyNotice' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.SKFPrivacyNotice

    @property
    def read_accept_terms_of_use(self) -> 'bool':
        '''bool: 'ReadAcceptTermsOfUse' is the original name of this property.'''

        return self.wrapped.ReadAcceptTermsOfUse

    @read_accept_terms_of_use.setter
    def read_accept_terms_of_use(self, value: 'bool'):
        self.wrapped.ReadAcceptTermsOfUse = bool(value) if value else False

    @property
    def authenticate(self) -> 'Callable[[], None]':
        '''Callable[[], None]: 'Authenticate' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.Authenticate

    @property
    def authentication_state(self) -> 'str':
        '''str: 'AuthenticationState' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.AuthenticationState

    @property
    def error(self) -> 'str':
        '''str: 'Error' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.Error
