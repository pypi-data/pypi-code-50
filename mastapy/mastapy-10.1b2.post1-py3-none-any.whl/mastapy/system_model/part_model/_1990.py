'''_1990.py

PointLoad
'''


from mastapy.math_utility.measured_vectors import _1105
from mastapy.utility.units_and_measurements.measurements import _1191
from mastapy._internal import constructor
from mastapy.system_model.part_model import _1997
from mastapy._internal.python_net import python_net_import

_POINT_LOAD = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'PointLoad')


__docformat__ = 'restructuredtext en'
__all__ = ('PointLoad',)


class PointLoad(_1997.VirtualComponent):
    '''PointLoad

    This is a mastapy class.
    '''

    TYPE = _POINT_LOAD

    __hash__ = None

    def __init__(self, instance_to_wrap: 'PointLoad.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def offset(self) -> '_1105.TwoDVectorPolar[_1191.LengthShort]':
        '''TwoDVectorPolar[LengthShort]: 'Offset' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1105.TwoDVectorPolar)[_1191.LengthShort](self.wrapped.Offset) if self.wrapped.Offset else None
