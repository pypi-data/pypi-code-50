'''_689.py

ConicalMeshManufacturingConfig
'''


from mastapy.gears.manufacturing.bevel import _698, _691
from mastapy._internal import constructor
from mastapy._internal.python_net import python_net_import

_CONICAL_MESH_MANUFACTURING_CONFIG = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Bevel', 'ConicalMeshManufacturingConfig')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalMeshManufacturingConfig',)


class ConicalMeshManufacturingConfig(_691.ConicalMeshMicroGeometryConfigBase):
    '''ConicalMeshManufacturingConfig

    This is a mastapy class.
    '''

    TYPE = _CONICAL_MESH_MANUFACTURING_CONFIG

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConicalMeshManufacturingConfig.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def wheel_config(self) -> '_698.ConicalWheelManufacturingConfig':
        '''ConicalWheelManufacturingConfig: 'WheelConfig' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_698.ConicalWheelManufacturingConfig)(self.wrapped.WheelConfig) if self.wrapped.WheelConfig else None
