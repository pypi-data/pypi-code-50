'''_1660.py

RingForceAndDisplacement
'''


from mastapy._internal import constructor
from mastapy.math_utility.measured_vectors import _1106
from mastapy.utility.units_and_measurements.measurements import (
    _1194, _1148, _1168, _1240
)
from mastapy import _1
from mastapy._internal.python_net import python_net_import

_RING_FORCE_AND_DISPLACEMENT = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling', 'RingForceAndDisplacement')


__docformat__ = 'restructuredtext en'
__all__ = ('RingForceAndDisplacement',)


class RingForceAndDisplacement(_1.APIBase):
    '''RingForceAndDisplacement

    This is a mastapy class.
    '''

    TYPE = _RING_FORCE_AND_DISPLACEMENT

    __hash__ = None

    def __init__(self, instance_to_wrap: 'RingForceAndDisplacement.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def name(self) -> 'str':
        '''str: 'Name' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.Name

    @property
    def displacement(self) -> '_1106.VectorWithLinearAndAngularComponents[_1194.LengthVeryShort, _1148.AngleSmall]':
        '''VectorWithLinearAndAngularComponents[LengthVeryShort, AngleSmall]: 'Displacement' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1106.VectorWithLinearAndAngularComponents)[_1194.LengthVeryShort, _1148.AngleSmall](self.wrapped.Displacement) if self.wrapped.Displacement else None

    @property
    def force(self) -> '_1106.VectorWithLinearAndAngularComponents[_1168.Force, _1240.Torque]':
        '''VectorWithLinearAndAngularComponents[Force, Torque]: 'Force' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1106.VectorWithLinearAndAngularComponents)[_1168.Force, _1240.Torque](self.wrapped.Force) if self.wrapped.Force else None
