'''_1686.py

SKFModuleResults
'''


from mastapy.bearings.bearing_results.rolling.skf_module import (
    _1681, _1688, _1669, _1677,
    _1667, _1687, _1670, _1671,
    _1673
)
from mastapy._internal import constructor
from mastapy import _1
from mastapy._internal.python_net import python_net_import

_SKF_MODULE_RESULTS = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling.SkfModule', 'SKFModuleResults')


__docformat__ = 'restructuredtext en'
__all__ = ('SKFModuleResults',)


class SKFModuleResults(_1.APIBase):
    '''SKFModuleResults

    This is a mastapy class.
    '''

    TYPE = _SKF_MODULE_RESULTS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SKFModuleResults.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def minimum_load(self) -> '_1681.MinimumLoad':
        '''MinimumLoad: 'MinimumLoad' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1681.MinimumLoad)(self.wrapped.MinimumLoad) if self.wrapped.MinimumLoad else None

    @property
    def viscosities(self) -> '_1688.Viscosities':
        '''Viscosities: 'Viscosities' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1688.Viscosities)(self.wrapped.Viscosities) if self.wrapped.Viscosities else None

    @property
    def bearing_loads(self) -> '_1669.BearingLoads':
        '''BearingLoads: 'BearingLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1669.BearingLoads)(self.wrapped.BearingLoads) if self.wrapped.BearingLoads else None

    @property
    def grease_life_and_relubrication_interval(self) -> '_1677.GreaseLifeAndRelubricationInterval':
        '''GreaseLifeAndRelubricationInterval: 'GreaseLifeAndRelubricationInterval' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1677.GreaseLifeAndRelubricationInterval)(self.wrapped.GreaseLifeAndRelubricationInterval) if self.wrapped.GreaseLifeAndRelubricationInterval else None

    @property
    def adjusted_speed(self) -> '_1667.AdjustedSpeed':
        '''AdjustedSpeed: 'AdjustedSpeed' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1667.AdjustedSpeed)(self.wrapped.AdjustedSpeed) if self.wrapped.AdjustedSpeed else None

    @property
    def static_safety_factors(self) -> '_1687.StaticSafetyFactors':
        '''StaticSafetyFactors: 'StaticSafetyFactors' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1687.StaticSafetyFactors)(self.wrapped.StaticSafetyFactors) if self.wrapped.StaticSafetyFactors else None

    @property
    def bearing_rating_life(self) -> '_1670.BearingRatingLife':
        '''BearingRatingLife: 'BearingRatingLife' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1670.BearingRatingLife)(self.wrapped.BearingRatingLife) if self.wrapped.BearingRatingLife else None

    @property
    def frequencies(self) -> '_1671.Frequencies':
        '''Frequencies: 'Frequencies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1671.Frequencies)(self.wrapped.Frequencies) if self.wrapped.Frequencies else None

    @property
    def friction(self) -> '_1673.Friction':
        '''Friction: 'Friction' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1673.Friction)(self.wrapped.Friction) if self.wrapped.Friction else None
