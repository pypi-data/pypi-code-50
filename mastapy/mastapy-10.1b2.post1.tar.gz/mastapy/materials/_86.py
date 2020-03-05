'''_86.py

SNCurve
'''


from typing import List

from mastapy._internal import constructor, conversion
from mastapy.materials import _87
from mastapy import _1
from mastapy._internal.python_net import python_net_import

_SN_CURVE = python_net_import('SMT.MastaAPI.Materials', 'SNCurve')


__docformat__ = 'restructuredtext en'
__all__ = ('SNCurve',)


class SNCurve(_1.APIBase):
    '''SNCurve

    This is a mastapy class.
    '''

    TYPE = _SN_CURVE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SNCurve.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def maximum_cycles_for_static_stress(self) -> 'float':
        '''float: 'MaximumCyclesForStaticStress' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.MaximumCyclesForStaticStress

    @property
    def cycles_for_infinite_life(self) -> 'float':
        '''float: 'CyclesForInfiniteLife' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.CyclesForInfiniteLife

    @property
    def fatigue_limit_for_infinite_life(self) -> 'float':
        '''float: 'FatigueLimitForInfiniteLife' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.FatigueLimitForInfiniteLife

    @property
    def stress_for_first_cycle_failure(self) -> 'float':
        '''float: 'StressForFirstCycleFailure' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.StressForFirstCycleFailure

    @property
    def points(self) -> 'List[_87.SNCurvePoint]':
        '''List[SNCurvePoint]: 'Points' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Points, constructor.new(_87.SNCurvePoint))
        return value
