'''_1622.py

LoadedRollingBearingRaceResults
'''


from mastapy._internal import constructor
from mastapy import _1
from mastapy._internal.python_net import python_net_import

_LOADED_ROLLING_BEARING_RACE_RESULTS = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling', 'LoadedRollingBearingRaceResults')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedRollingBearingRaceResults',)


class LoadedRollingBearingRaceResults(_1.APIBase):
    '''LoadedRollingBearingRaceResults

    This is a mastapy class.
    '''

    TYPE = _LOADED_ROLLING_BEARING_RACE_RESULTS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'LoadedRollingBearingRaceResults.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def contact_radius_in_rolling_direction(self) -> 'float':
        '''float: 'ContactRadiusInRollingDirection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.ContactRadiusInRollingDirection

    @property
    def minimum_lubricating_film_thickness(self) -> 'float':
        '''float: 'MinimumLubricatingFilmThickness' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.MinimumLubricatingFilmThickness

    @property
    def name(self) -> 'str':
        '''str: 'Name' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.Name
