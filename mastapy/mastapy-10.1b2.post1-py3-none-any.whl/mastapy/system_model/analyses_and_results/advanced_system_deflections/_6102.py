'''_6102.py

CylindricalMeshedGearAdvancedSystemDeflection
'''


from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _6099
from mastapy import _1
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_MESHED_GEAR_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections', 'CylindricalMeshedGearAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalMeshedGearAdvancedSystemDeflection',)


class CylindricalMeshedGearAdvancedSystemDeflection(_1.APIBase):
    '''CylindricalMeshedGearAdvancedSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _CYLINDRICAL_MESHED_GEAR_ADVANCED_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CylindricalMeshedGearAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)

    @property
    def mean_node_torque_in_meshes(self) -> 'float':
        '''float: 'MeanNodeTorqueInMeshes' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.MeanNodeTorqueInMeshes

    @property
    def cylindrical_gear_advanced_system_deflection(self) -> '_6099.CylindricalGearAdvancedSystemDeflection':
        '''CylindricalGearAdvancedSystemDeflection: 'CylindricalGearAdvancedSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6099.CylindricalGearAdvancedSystemDeflection)(self.wrapped.CylindricalGearAdvancedSystemDeflection) if self.wrapped.CylindricalGearAdvancedSystemDeflection else None

    @property
    def other_cylindrical_gear_advanced_system_deflection(self) -> '_6099.CylindricalGearAdvancedSystemDeflection':
        '''CylindricalGearAdvancedSystemDeflection: 'OtherCylindricalGearAdvancedSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6099.CylindricalGearAdvancedSystemDeflection)(self.wrapped.OtherCylindricalGearAdvancedSystemDeflection) if self.wrapped.OtherCylindricalGearAdvancedSystemDeflection else None
