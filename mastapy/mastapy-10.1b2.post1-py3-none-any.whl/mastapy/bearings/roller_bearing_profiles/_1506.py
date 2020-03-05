'''_1506.py

ProfileSet
'''


from mastapy.bearings import _1478
from mastapy._internal import constructor, conversion
from mastapy.bearings.roller_bearing_profiles import (
    _1514, _1508, _1509, _1510,
    _1511, _1512, _1513, _1515
)
from mastapy._internal.cast_exception import CastException
from mastapy import _1
from mastapy._internal.python_net import python_net_import

_PROFILE_SET = python_net_import('SMT.MastaAPI.Bearings.RollerBearingProfiles', 'ProfileSet')


__docformat__ = 'restructuredtext en'
__all__ = ('ProfileSet',)


class ProfileSet(_1.APIBase):
    '''ProfileSet

    This is a mastapy class.
    '''

    TYPE = _PROFILE_SET

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ProfileSet.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def active_profile_type(self) -> '_1478.RollerBearingProfileTypes':
        '''RollerBearingProfileTypes: 'ActiveProfileType' is the original name of this property.'''

        value = conversion.pn_to_mp_enum(self.wrapped.ActiveProfileType)
        return constructor.new(_1478.RollerBearingProfileTypes)(value) if value else None

    @active_profile_type.setter
    def active_profile_type(self, value: '_1478.RollerBearingProfileTypes'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.ActiveProfileType = value

    @property
    def active_profile(self) -> '_1514.RollerBearingProfile':
        '''RollerBearingProfile: 'ActiveProfile' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1514.RollerBearingProfile)(self.wrapped.ActiveProfile) if self.wrapped.ActiveProfile else None

    @property
    def active_profile_of_type_roller_bearing_conical_profile(self) -> '_1508.RollerBearingConicalProfile':
        '''RollerBearingConicalProfile: 'ActiveProfile' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1508.RollerBearingConicalProfile.TYPE not in self.wrapped.ActiveProfile.__class__.__mro__:
            raise CastException('Failed to cast active_profile to RollerBearingConicalProfile. Expected: {}.'.format(self.wrapped.ActiveProfile.__class__.__qualname__))

        return constructor.new(_1508.RollerBearingConicalProfile)(self.wrapped.ActiveProfile) if self.wrapped.ActiveProfile else None

    @property
    def active_profile_of_type_roller_bearing_crowned_profile(self) -> '_1509.RollerBearingCrownedProfile':
        '''RollerBearingCrownedProfile: 'ActiveProfile' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1509.RollerBearingCrownedProfile.TYPE not in self.wrapped.ActiveProfile.__class__.__mro__:
            raise CastException('Failed to cast active_profile to RollerBearingCrownedProfile. Expected: {}.'.format(self.wrapped.ActiveProfile.__class__.__qualname__))

        return constructor.new(_1509.RollerBearingCrownedProfile)(self.wrapped.ActiveProfile) if self.wrapped.ActiveProfile else None

    @property
    def active_profile_of_type_roller_bearing_din_lundberg_profile(self) -> '_1510.RollerBearingDinLundbergProfile':
        '''RollerBearingDinLundbergProfile: 'ActiveProfile' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1510.RollerBearingDinLundbergProfile.TYPE not in self.wrapped.ActiveProfile.__class__.__mro__:
            raise CastException('Failed to cast active_profile to RollerBearingDinLundbergProfile. Expected: {}.'.format(self.wrapped.ActiveProfile.__class__.__qualname__))

        return constructor.new(_1510.RollerBearingDinLundbergProfile)(self.wrapped.ActiveProfile) if self.wrapped.ActiveProfile else None

    @property
    def active_profile_of_type_roller_bearing_flat_profile(self) -> '_1511.RollerBearingFlatProfile':
        '''RollerBearingFlatProfile: 'ActiveProfile' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1511.RollerBearingFlatProfile.TYPE not in self.wrapped.ActiveProfile.__class__.__mro__:
            raise CastException('Failed to cast active_profile to RollerBearingFlatProfile. Expected: {}.'.format(self.wrapped.ActiveProfile.__class__.__qualname__))

        return constructor.new(_1511.RollerBearingFlatProfile)(self.wrapped.ActiveProfile) if self.wrapped.ActiveProfile else None

    @property
    def active_profile_of_type_roller_bearing_johns_gohar_profile(self) -> '_1512.RollerBearingJohnsGoharProfile':
        '''RollerBearingJohnsGoharProfile: 'ActiveProfile' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1512.RollerBearingJohnsGoharProfile.TYPE not in self.wrapped.ActiveProfile.__class__.__mro__:
            raise CastException('Failed to cast active_profile to RollerBearingJohnsGoharProfile. Expected: {}.'.format(self.wrapped.ActiveProfile.__class__.__qualname__))

        return constructor.new(_1512.RollerBearingJohnsGoharProfile)(self.wrapped.ActiveProfile) if self.wrapped.ActiveProfile else None

    @property
    def active_profile_of_type_roller_bearing_lundberg_profile(self) -> '_1513.RollerBearingLundbergProfile':
        '''RollerBearingLundbergProfile: 'ActiveProfile' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1513.RollerBearingLundbergProfile.TYPE not in self.wrapped.ActiveProfile.__class__.__mro__:
            raise CastException('Failed to cast active_profile to RollerBearingLundbergProfile. Expected: {}.'.format(self.wrapped.ActiveProfile.__class__.__qualname__))

        return constructor.new(_1513.RollerBearingLundbergProfile)(self.wrapped.ActiveProfile) if self.wrapped.ActiveProfile else None

    @property
    def active_profile_of_type_roller_bearing_user_specified_profile(self) -> '_1515.RollerBearingUserSpecifiedProfile':
        '''RollerBearingUserSpecifiedProfile: 'ActiveProfile' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _1515.RollerBearingUserSpecifiedProfile.TYPE not in self.wrapped.ActiveProfile.__class__.__mro__:
            raise CastException('Failed to cast active_profile to RollerBearingUserSpecifiedProfile. Expected: {}.'.format(self.wrapped.ActiveProfile.__class__.__qualname__))

        return constructor.new(_1515.RollerBearingUserSpecifiedProfile)(self.wrapped.ActiveProfile) if self.wrapped.ActiveProfile else None
