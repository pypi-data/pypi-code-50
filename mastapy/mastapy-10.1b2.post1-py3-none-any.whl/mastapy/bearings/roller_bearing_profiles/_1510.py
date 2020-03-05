'''_1510.py

RollerBearingDinLundbergProfile
'''


from mastapy.bearings.roller_bearing_profiles import _1514
from mastapy._internal.python_net import python_net_import

_ROLLER_BEARING_DIN_LUNDBERG_PROFILE = python_net_import('SMT.MastaAPI.Bearings.RollerBearingProfiles', 'RollerBearingDinLundbergProfile')


__docformat__ = 'restructuredtext en'
__all__ = ('RollerBearingDinLundbergProfile',)


class RollerBearingDinLundbergProfile(_1514.RollerBearingProfile):
    '''RollerBearingDinLundbergProfile

    This is a mastapy class.
    '''

    TYPE = _ROLLER_BEARING_DIN_LUNDBERG_PROFILE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'RollerBearingDinLundbergProfile.TYPE'):
        super().__init__(instance_to_wrap)
