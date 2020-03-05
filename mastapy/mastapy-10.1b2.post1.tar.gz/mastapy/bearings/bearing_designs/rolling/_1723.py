'''_1723.py

BearingProtectionDetailsModifier
'''


from mastapy.bearings.bearing_designs.rolling import _1724
from mastapy._internal import constructor, conversion
from mastapy import _1
from mastapy._internal.python_net import python_net_import

_BEARING_PROTECTION_DETAILS_MODIFIER = python_net_import('SMT.MastaAPI.Bearings.BearingDesigns.Rolling', 'BearingProtectionDetailsModifier')


__docformat__ = 'restructuredtext en'
__all__ = ('BearingProtectionDetailsModifier',)


class BearingProtectionDetailsModifier(_1.APIBase):
    '''BearingProtectionDetailsModifier

    This is a mastapy class.
    '''

    TYPE = _BEARING_PROTECTION_DETAILS_MODIFIER

    __hash__ = None

    def __init__(self, instance_to_wrap: 'BearingProtectionDetailsModifier.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def current_protection_level(self) -> '_1724.BearingProtectionLevel':
        '''BearingProtectionLevel: 'CurrentProtectionLevel' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_enum(self.wrapped.CurrentProtectionLevel)
        return constructor.new(_1724.BearingProtectionLevel)(value) if value else None

    @property
    def new_protection_level(self) -> '_1724.BearingProtectionLevel':
        '''BearingProtectionLevel: 'NewProtectionLevel' is the original name of this property.'''

        value = conversion.pn_to_mp_enum(self.wrapped.NewProtectionLevel)
        return constructor.new(_1724.BearingProtectionLevel)(value) if value else None

    @new_protection_level.setter
    def new_protection_level(self, value: '_1724.BearingProtectionLevel'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.NewProtectionLevel = value

    @property
    def current_password(self) -> 'str':
        '''str: 'CurrentPassword' is the original name of this property.'''

        return self.wrapped.CurrentPassword

    @current_password.setter
    def current_password(self, value: 'str'):
        self.wrapped.CurrentPassword = str(value) if value else None

    @property
    def new_password(self) -> 'str':
        '''str: 'NewPassword' is the original name of this property.'''

        return self.wrapped.NewPassword

    @new_password.setter
    def new_password(self, value: 'str'):
        self.wrapped.NewPassword = str(value) if value else None

    @property
    def confirm_new_password(self) -> 'str':
        '''str: 'ConfirmNewPassword' is the original name of this property.'''

        return self.wrapped.ConfirmNewPassword

    @confirm_new_password.setter
    def confirm_new_password(self, value: 'str'):
        self.wrapped.ConfirmNewPassword = str(value) if value else None
