'''_1520.py

RollerBearingUserSpecifiedProfile
'''


from typing import Callable, List

from mastapy._internal import constructor, conversion
from mastapy.bearings.roller_bearing_profiles import (
    _1510, _1512, _1522, _1519
)
from mastapy._internal.python_net import python_net_import

_ROLLER_BEARING_USER_SPECIFIED_PROFILE = python_net_import('SMT.MastaAPI.Bearings.RollerBearingProfiles', 'RollerBearingUserSpecifiedProfile')


__docformat__ = 'restructuredtext en'
__all__ = ('RollerBearingUserSpecifiedProfile',)


class RollerBearingUserSpecifiedProfile(_1519.RollerBearingProfile):
    '''RollerBearingUserSpecifiedProfile

    This is a mastapy class.
    '''

    TYPE = _ROLLER_BEARING_USER_SPECIFIED_PROFILE
    __hash__ = None

    def __init__(self, instance_to_wrap: 'RollerBearingUserSpecifiedProfile.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def number_of_points(self) -> 'int':
        '''int: 'NumberOfPoints' is the original name of this property.'''

        return self.wrapped.NumberOfPoints

    @number_of_points.setter
    def number_of_points(self, value: 'int'):
        self.wrapped.NumberOfPoints = int(value) if value else 0

    @property
    def set_to_full_range(self) -> 'Callable[[], None]':
        '''Callable[[], None]: 'SetToFullRange' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.SetToFullRange

    @property
    def data_to_use(self) -> '_1510.ProfileDataToUse':
        '''ProfileDataToUse: 'DataToUse' is the original name of this property.'''

        value = conversion.pn_to_mp_enum(self.wrapped.DataToUse)
        return constructor.new(_1510.ProfileDataToUse)(value) if value else None

    @data_to_use.setter
    def data_to_use(self, value: '_1510.ProfileDataToUse'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.DataToUse = value

    @property
    def profile_to_fit(self) -> '_1512.ProfileToFit':
        '''ProfileToFit: 'ProfileToFit' is the original name of this property.'''

        value = conversion.pn_to_mp_enum(self.wrapped.ProfileToFit)
        return constructor.new(_1512.ProfileToFit)(value) if value else None

    @profile_to_fit.setter
    def profile_to_fit(self, value: '_1512.ProfileToFit'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.ProfileToFit = value

    @property
    def points(self) -> 'List[_1522.UserSpecifiedProfilePoint]':
        '''List[UserSpecifiedProfilePoint]: 'Points' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Points, constructor.new(_1522.UserSpecifiedProfilePoint))
        return value
